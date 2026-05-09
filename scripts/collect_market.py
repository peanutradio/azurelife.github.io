#!/usr/bin/env python3
"""
주식/크립토 시황 게시판 수집 스크립트
CoinGecko, 크립토 뉴스 RSS, YouTube API 데이터를 수집하여 Hugo 포스트 생성
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import feedparser
import requests
import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"


def load_config(path: Path = CONFIG_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# CoinGecko 수집
# ---------------------------------------------------------------------------

def fetch_coingecko_market(coin_ids: list[str], api_key: str | None = None) -> list[dict]:
    base = "https://pro-api.coingecko.com/api/v3" if api_key else "https://api.coingecko.com/api/v3"
    headers = {"x-cg-pro-api-key": api_key} if api_key else {}
    params = {
        "vs_currency": "usd",
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc",
        "per_page": len(coin_ids),
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "1h,24h,7d",
    }
    try:
        resp = requests.get(f"{base}/coins/markets", params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        log.error("CoinGecko 시세 수집 실패: %s", exc)
        return []


def fetch_coingecko_global(api_key: str | None = None) -> dict:
    base = "https://pro-api.coingecko.com/api/v3" if api_key else "https://api.coingecko.com/api/v3"
    headers = {"x-cg-pro-api-key": api_key} if api_key else {}
    try:
        resp = requests.get(f"{base}/global", headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json().get("data", {})
    except Exception as exc:
        log.error("CoinGecko 글로벌 수집 실패: %s", exc)
        return {}


def fetch_coingecko_trending(api_key: str | None = None) -> dict:
    base = "https://pro-api.coingecko.com/api/v3" if api_key else "https://api.coingecko.com/api/v3"
    headers = {"x-cg-pro-api-key": api_key} if api_key else {}
    try:
        resp = requests.get(f"{base}/search/trending", headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        log.error("CoinGecko 트렌딩 수집 실패: %s", exc)
        return {}


def fetch_fear_greed() -> dict:
    try:
        resp = requests.get("https://api.alternative.me/fng/?limit=1", timeout=15)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        if data:
            return {"value": data[0]["value"], "value_classification": data[0]["value_classification"]}
        return {}
    except Exception as exc:
        log.error("Fear & Greed 수집 실패: %s", exc)
        return {}


# ---------------------------------------------------------------------------
# 뉴스 RSS 수집
# ---------------------------------------------------------------------------

def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def fetch_news_rss(sources: list[dict], max_articles: int = 15) -> list[dict]:
    articles = []
    seen_urls = set()

    for src in sources:
        try:
            feed = feedparser.parse(src["url"])
            for entry in feed.entries[:10]:
                url = entry.get("link", "")
                if not url or url in seen_urls:
                    continue
                seen_urls.add(url)

                import time
                published = datetime.now(tz=timezone.utc)
                for attr in ("published_parsed", "updated_parsed"):
                    t = getattr(entry, attr, None)
                    if t:
                        try:
                            published = datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
                        except Exception:
                            pass
                        break

                summary = strip_html(entry.get("summary", ""))[:300]

                articles.append({
                    "title": entry.get("title", "").strip(),
                    "url": url,
                    "source": src["name"],
                    "published_at": published.isoformat(),
                    "summary": summary,
                })
        except Exception as exc:
            log.warning("뉴스 RSS 수집 실패 (%s): %s", src.get("name", "?"), exc)

    articles.sort(key=lambda a: a["published_at"], reverse=True)
    return articles[:max_articles]


# ---------------------------------------------------------------------------
# YouTube 수집
# ---------------------------------------------------------------------------

def fetch_youtube_channels(channels: list[dict], api_key: str | None = None) -> dict:
    if not api_key:
        log.warning("YOUTUBE_API_KEY 미설정 — YouTube 수집 건너뜀")
        return {}

    result = {}
    for ch in channels:
        try:
            params = {
                "part": "snippet",
                "channelId": ch["id"],
                "maxResults": ch.get("max_videos", 3),
                "order": "date",
                "type": "video",
                "key": api_key,
            }
            resp = requests.get(
                "https://www.googleapis.com/youtube/v3/search",
                params=params, timeout=30,
            )
            resp.raise_for_status()
            items = resp.json().get("items", [])
            videos = []
            for item in items:
                vid_id = item.get("id", {}).get("videoId", "")
                snippet = item.get("snippet", {})
                if vid_id:
                    videos.append({
                        "title": snippet.get("title", ""),
                        "url": f"https://www.youtube.com/watch?v={vid_id}",
                        "channel": snippet.get("channelTitle", ch["name"]),
                        "published_at": snippet.get("publishedAt", ""),
                    })
            if videos:
                result[ch["name"]] = videos
        except Exception as exc:
            log.warning("YouTube 수집 실패 (%s): %s", ch.get("name", "?"), exc)

    return result


# ---------------------------------------------------------------------------
# Hugo 포스트 생성
# ---------------------------------------------------------------------------

def build_market_post(
    market_data: list[dict],
    global_market: dict,
    trending: dict,
    fear_greed: dict,
    news: list[dict],
    youtube: dict,
    date: datetime,
) -> tuple[str, str]:
    """시황 데이터를 Hugo 포스트(front matter + body)로 변환"""
    date_str = date.strftime("%Y-%m-%d")
    date_iso = date.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    # 요약 생성
    btc = next((c for c in market_data if c.get("symbol", "").lower() == "btc"), {})
    btc_price = btc.get("current_price", 0)
    btc_change = btc.get("price_change_percentage_24h_in_currency", 0) or 0
    fg_val = fear_greed.get("value", "?")
    fg_class = fear_greed.get("value_classification", "?")
    description = f"BTC ${btc_price:,.0f} ({btc_change:+.1f}%) | Fear & Greed: {fg_val} ({fg_class})"

    tags = ["크립토", "비트코인", "시황"]
    if any(c.get("symbol", "").lower() == "eth" for c in market_data):
        tags.append("이더리움")

    # Front matter
    fm_data = {
        "title": f"크립토 데일리 시황 — {date_str}",
        "date": date_iso,
        "draft": False,
        "tags": tags,
        "categories": ["시황"],
        "description": description[:160],
    }
    front_matter = "---\n" + yaml.dump(fm_data, allow_unicode=True, default_flow_style=False) + "---\n"

    # Body
    sections = []

    # Fear & Greed
    if fear_greed:
        sections.append("## 시장 심리\n")
        sections.append(f"**Fear & Greed Index: {fg_val}** ({fg_class})\n")

    # 글로벌 마켓
    if global_market:
        total_mcap = global_market.get("total_market_cap", {}).get("usd", 0)
        btc_dom = global_market.get("market_cap_percentage", {}).get("btc", 0)
        mcap_change = global_market.get("market_cap_change_percentage_24h_usd", 0)
        sections.append("## 시장 개요\n")
        sections.append(
            f"- 총 시가총액: **${total_mcap / 1e12:.2f}T** ({mcap_change:+.1f}%)\n"
            f"- BTC 도미넌스: **{btc_dom:.1f}%**\n"
        )

    # 시세 테이블
    if market_data:
        sections.append("## 주요 코인 시세\n")
        sections.append("| 코인 | 가격 | 24h | 7d | 거래량(24h) |")
        sections.append("|------|------|-----|-----|------------|")
        for coin in market_data[:10]:
            name = coin.get("name", "")
            symbol = coin.get("symbol", "").upper()
            price = coin.get("current_price", 0)
            c24h = coin.get("price_change_percentage_24h_in_currency", 0) or 0
            c7d = coin.get("price_change_percentage_7d_in_currency", 0) or 0
            volume = coin.get("total_volume", 0)
            sections.append(
                f"| {name} ({symbol}) | ${price:,.2f} | "
                f"{c24h:+.1f}% | {c7d:+.1f}% | "
                f"${volume / 1e6:.0f}M |"
            )
        sections.append("")

    # 트렌딩
    trending_coins = trending.get("coins", [])
    if trending_coins:
        sections.append("## 트렌딩 코인\n")
        for i, item in enumerate(trending_coins[:7], 1):
            coin = item.get("item", {})
            sections.append(
                f"{i}. **{coin.get('name', '')}** ({coin.get('symbol', '')}) "
                f"— 마켓캡 순위 #{coin.get('market_cap_rank', '?')}"
            )
        sections.append("")

    # 뉴스
    if news:
        sections.append("## 주요 뉴스\n")
        for article in news[:10]:
            title = article["title"]
            url = article["url"]
            source = article["source"]
            sections.append(f"- [{title}]({url}) — *{source}*")
        sections.append("")

    # YouTube
    if youtube:
        sections.append("## 크립토 영상\n")
        for ch_name, videos in youtube.items():
            if videos:
                sections.append(f"### {ch_name}\n")
                for v in videos[:3]:
                    sections.append(f"- [{v['title']}]({v['url']})")
                sections.append("")

    body = "\n".join(sections)
    return front_matter, body


def write_market_post(content_dir: Path, date: datetime, front_matter: str, body: str) -> Path:
    date_str = date.strftime("%Y%m%d")
    slug = f"{date_str}-crypto-daily"
    post_dir = content_dir / slug
    post_dir.mkdir(parents=True, exist_ok=True)
    post_path = post_dir / "index.md"
    with open(post_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write("\n")
        f.write(body)
    log.info("시황 포스트 생성: %s", post_path)
    return post_path


def load_from_json(json_path: Path) -> dict:
    """blockchain-board 출력 JSON에서 데이터 로드"""
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="주식/크립토 시황 수집기")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="설정 파일 경로")
    parser.add_argument("--from-json", help="blockchain-board JSON 파일에서 로드 (API 호출 생략)")
    parser.add_argument("--dry-run", action="store_true", help="파일 저장 없이 결과만 출력")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    market_cfg = cfg.get("boards", {}).get("market", {})
    if not market_cfg:
        log.error("설정에 boards.market 항목이 없습니다.")
        sys.exit(1)

    content_base = SCRIPT_DIR / cfg["hugo_content_dir"]
    content_dir = content_base / market_cfg["content_path"]
    now = datetime.now(tz=timezone.utc)

    if args.from_json:
        log.info("JSON 파일에서 데이터 로드: %s", args.from_json)
        data = load_from_json(Path(args.from_json))
        market_data = data.get("market_data", [])
        global_market = data.get("global_market", {})
        trending = data.get("trending", {})
        fear_greed = data.get("fear_greed", {}).get("current", data.get("fear_greed", {}))
        news = data.get("news", [])
        youtube_data = data.get("youtube", {}).get("channel_videos", {})
    else:
        cg_key = os.environ.get("COINGECKO_API_KEY")
        yt_key = os.environ.get("YOUTUBE_API_KEY")
        coin_ids = market_cfg.get("coin_ids", [])
        news_sources = market_cfg.get("news_sources", [])
        yt_channels = market_cfg.get("youtube_channels", [])

        log.info("=== 시황 데이터 수집 시작 ===")
        market_data = fetch_coingecko_market(coin_ids, cg_key)
        log.info("CoinGecko 시세: %d개 코인", len(market_data))

        global_market = fetch_coingecko_global(cg_key)
        trending = fetch_coingecko_trending(cg_key)
        fear_greed = fetch_fear_greed()
        news = fetch_news_rss(news_sources, max_articles=15)
        log.info("뉴스: %d건", len(news))

        youtube_data = fetch_youtube_channels(yt_channels, yt_key)
        log.info("YouTube: %d개 채널", len(youtube_data))

    front_matter, body = build_market_post(
        market_data=market_data,
        global_market=global_market,
        trending=trending,
        fear_greed=fear_greed,
        news=news,
        youtube=youtube_data,
        date=now,
    )

    if args.dry_run:
        print(front_matter)
        print(body)
        return

    post_path = write_market_post(content_dir, now, front_matter, body)
    log.info("=== 완료: %s ===", post_path)
    print(post_path)


if __name__ == "__main__":
    main()

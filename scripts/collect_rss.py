#!/usr/bin/env python3
"""
RSS 수집 스크립트 - livehigh 블로그용
Hugo 마크다운 포스트 자동 생성
"""

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
import yaml
from slugify import slugify

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


def load_published_urls(path: Path) -> set:
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return set(data.get("urls", []))
    return set()


def save_published_urls(path: Path, urls: set) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"urls": sorted(urls)}, f, ensure_ascii=False, indent=2)


def fetch_feed(url: str, source_name: str) -> list[dict]:
    """피드를 가져와 항목 목록으로 반환"""
    try:
        log.info("피드 수집: %s (%s)", source_name, url)
        feed = feedparser.parse(url)
        if feed.bozo and not feed.entries:
            log.warning("피드 파싱 오류 (%s): %s", source_name, feed.bozo_exception)
            return []
        return feed.entries
    except Exception as exc:
        log.error("피드 수집 실패 (%s): %s", source_name, exc)
        return []


def entry_url(entry: dict) -> str:
    return entry.get("link") or entry.get("id") or ""


def entry_published(entry: dict) -> datetime:
    """published_parsed 또는 updated_parsed → datetime (UTC)"""
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None)
        if t:
            try:
                import time
                return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
            except Exception:
                pass
    return datetime.now(tz=timezone.utc)


def entry_content(entry: dict) -> str:
    """본문 텍스트 (HTML 태그 제거)"""
    content = ""
    if hasattr(entry, "content") and entry.content:
        content = entry.content[0].get("value", "")
    elif hasattr(entry, "summary"):
        content = entry.summary or ""
    return strip_html(content)


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def make_slug(title: str, published: datetime) -> str:
    date_prefix = published.strftime("%Y%m%d")
    slug = slugify(title, max_length=60, word_boundary=True)
    return f"{date_prefix}-{slug}"


def build_front_matter(
    title: str,
    published: datetime,
    source_name: str,
    original_url: str,
    tags: list[str],
    categories: list[str],
    description: str,
) -> str:
    data = {
        "title": title,
        "date": published.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
        "draft": False,
        "source": source_name,
        "original_url": original_url,
        "tags": tags,
        "categories": categories,
        "description": description[:160],
    }
    return "---\n" + yaml.dump(data, allow_unicode=True, default_flow_style=False) + "---\n"


def write_hugo_post(
    content_dir: Path,
    slug: str,
    front_matter: str,
    body: str,
    original_url: str,
) -> Path:
    post_dir = content_dir / slug
    post_dir.mkdir(parents=True, exist_ok=True)
    post_path = post_dir / "index.md"

    source_notice = f"\n\n---\n*원문: [{original_url}]({original_url})*\n"

    with open(post_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write("\n")
        f.write(body)
        f.write(source_notice)

    return post_path


# ---------------------------------------------------------------------------
# IT 소식 보드 (AI 70% / 기타 IT 30%)
# ---------------------------------------------------------------------------

def score_ai(entry: dict, ai_keywords: list[str]) -> int:
    """AI 관련성 점수 (키워드 매칭 수)"""
    text = " ".join([
        entry.get("title", ""),
        entry.get("summary", ""),
        strip_html(entry.get("content", [{}])[0].get("value", "") if hasattr(entry, "content") and entry.content else ""),
    ]).lower()
    return sum(1 for kw in ai_keywords if kw.lower() in text)


def collect_it_board(
    board_cfg: dict,
    content_base: Path,
    published_urls: set,
    max_posts: int,
) -> list[str]:
    """IT 소식 보드: AI 70% / 기타 IT 30% 비율로 수집"""
    ai_keywords = board_cfg.get("ai_keywords", [])
    ai_ratio = board_cfg.get("ai_ratio", 0.7)
    content_path = content_base / board_cfg["content_path"]

    # AI 소스에서 수집
    ai_entries = []
    for src in board_cfg["sources"].get("ai", []):
        for entry in fetch_feed(src["url"], src["name"]):
            url = entry_url(entry)
            if url and url not in published_urls:
                score = score_ai(entry, ai_keywords)
                ai_entries.append((score, entry, src["name"]))

    # 기타 소스에서 AI 비해당 항목 수집
    other_entries = []
    for src in board_cfg["sources"].get("other", []):
        for entry in fetch_feed(src["url"], src["name"]):
            url = entry_url(entry)
            if url and url not in published_urls:
                score = score_ai(entry, ai_keywords)
                if score == 0:  # AI 키워드 없는 항목만 기타로 분류
                    other_entries.append((score, entry, src["name"]))

    # 비율에 따라 할당
    n_ai = round(max_posts * ai_ratio)
    n_other = max_posts - n_ai

    ai_entries.sort(key=lambda x: x[0], reverse=True)
    selected = ai_entries[:n_ai] + other_entries[:n_other]

    return _write_entries(selected, content_path, published_urls, categories=["IT"])


def _write_entries(
    entries: list[tuple],
    content_path: Path,
    published_urls: set,
    categories: list[str],
) -> list[str]:
    written = []
    for _score, entry, source_name in entries:
        url = entry_url(entry)
        title = entry.get("title", "제목 없음").strip()
        published = entry_published(entry)
        body = entry_content(entry)
        tags = [t.term for t in entry.get("tags", [])] if hasattr(entry, "tags") else []
        description = body[:160] if body else title

        slug = make_slug(title, published)
        fm = build_front_matter(
            title=title,
            published=published,
            source_name=source_name,
            original_url=url,
            tags=tags,
            categories=categories,
            description=description,
        )
        post_path = write_hugo_post(content_path, slug, fm, body, url)
        published_urls.add(url)
        written.append(str(post_path))
        log.info("포스트 생성: %s", post_path)

    return written


# ---------------------------------------------------------------------------
# MS 게시판 (서브카테고리별)
# ---------------------------------------------------------------------------

def collect_ms_board(
    board_cfg: dict,
    content_base: Path,
    published_urls: set,
    max_posts: int,
) -> list[str]:
    written_all = []
    per_sub = max(1, max_posts // len(board_cfg.get("subcategories", {}) or {"_": None}))

    for sub_key, sub_cfg in board_cfg.get("subcategories", {}).items():
        content_path = content_base / sub_cfg["content_path"]
        sub_entries = []

        for src in sub_cfg.get("sources", []):
            for entry in fetch_feed(src["url"], src["name"]):
                url = entry_url(entry)
                if url and url not in published_urls:
                    sub_entries.append((0, entry, src["name"]))

        # 최신순 정렬
        sub_entries.sort(key=lambda x: entry_published(x[1]), reverse=True)
        selected = sub_entries[:per_sub]
        categories = ["MS", sub_cfg["name"]]
        written = _write_entries(selected, content_path, published_urls, categories)
        written_all.extend(written)

    return written_all


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="livehigh RSS 수집기")
    parser.add_argument("--config", default=str(CONFIG_PATH), help="설정 파일 경로")
    parser.add_argument(
        "--board",
        choices=["it", "ms", "all"],
        default="all",
        help="수집할 보드 (기본: all)",
    )
    parser.add_argument("--dry-run", action="store_true", help="파일 저장 없이 수집 결과만 출력")
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    content_base = SCRIPT_DIR / cfg["hugo_content_dir"]
    published_path = SCRIPT_DIR / cfg["published_urls_file"]

    published_urls = load_published_urls(published_path)
    log.info("기 발행 URL 수: %d", len(published_urls))

    written_all: list[str] = []
    boards_cfg = cfg.get("boards", {})

    run_boards = list(boards_cfg.keys()) if args.board == "all" else [args.board]

    for board_key in run_boards:
        if board_key not in boards_cfg:
            log.warning("알 수 없는 보드: %s", board_key)
            continue

        board_cfg = boards_cfg[board_key]
        max_posts = board_cfg.get("max_posts_per_run", cfg.get("max_posts_per_run", 10))
        log.info("=== 보드 수집 시작: %s (최대 %d개) ===", board_cfg["name"], max_posts)

        if args.dry_run:
            log.info("[dry-run] 실제 파일 저장 없이 실행")
            continue

        if board_key == "it":
            written = collect_it_board(board_cfg, content_base, published_urls, max_posts)
        elif board_key == "ms":
            written = collect_ms_board(board_cfg, content_base, published_urls, max_posts)
        else:
            log.warning("보드 '%s'에 대한 수집기가 없습니다.", board_key)
            written = []

        written_all.extend(written)

    if not args.dry_run:
        save_published_urls(published_path, published_urls)

    log.info("=== 완료: 총 %d개 포스트 생성 ===", len(written_all))
    for p in written_all:
        print(p)


if __name__ == "__main__":
    main()

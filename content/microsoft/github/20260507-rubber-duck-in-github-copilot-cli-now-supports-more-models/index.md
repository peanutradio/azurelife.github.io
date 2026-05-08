---
categories:
- MS
- GitHub
date: '2026-05-07T14:49:28+00:00'
description: Rubber Duck, the cross-family review agent in GitHub Copilot CLI, is
  now available using a Claude-powered critic agent when your session is using a GPT
  model. F
draft: false
original_url: https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models
source: GitHub Changelog
tags:
- Improvement
- copilot
title: Rubber Duck in GitHub Copilot CLI now supports more models
---

Rubber Duck, the cross-family review agent in GitHub Copilot CLI, is now available using a Claude-powered critic agent when your session is using a GPT model. For sessions using Claude as their orchestrator, we&rsquo;ve upgraded the GPT model used to seek a second opinion.
## What&rsquo;s new

Rubber Duck for GPT sessions: When you&rsquo;ve selected a GPT model as your orchestrator, and /experimental is enabled, Copilot will dispatch a Claude-powered Rubber Duck agent to provide a second opinion. The same second-opinion benefits (architectural catches, subtle bugs, and cross-file conflicts) now apply to GPT-driven sessions.
Stronger reviewer models for Claude sessions: Claude orchestrator sessions can now pair with GPT-5.5 as the Rubber Duck model for more effective second opinions.

To try it, run copilot and ensure /experimental on is toggled.
To learn more about how Rubber Duck combines model families to improve Copilot CLI&rsquo;s performance, read our recent blog post.

The post Rubber Duck in GitHub Copilot CLI now supports more models appeared first on The GitHub Blog.

---
*원문: [https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models](https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models)*

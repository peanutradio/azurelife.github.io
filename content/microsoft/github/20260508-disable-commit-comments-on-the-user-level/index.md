---
categories:
- MS
- GitHub
date: '2026-05-08T13:51:08+00:00'
description: You can now choose whether commit comments are enabled or disabled by
  default for repositories owned by your personal account. This makes it easier to
  manage co
draft: false
original_url: https://github.blog/changelog/2026-05-08-disable-commit-comments-on-the-user-level
source: GitHub Changelog
tags:
- Improvement
- collaboration tools
title: Disable commit comments on the user level
---

You can now choose whether commit comments are enabled or disabled by default for repositories owned by your personal account. This makes it easier to manage commit comment behavior across multiple personal repositories without updating them one by one.
In user-level repository settings, you&rsquo;ll find a new &ldquo;Commit comments&rdquo; section with two options:

Enabled by default
Disabled by default

When you choose a default, it applies to repositories owned by your personal account that don&rsquo;t already have an explicit repository-level setting. You can still override the default in an individual repository with Allow comments on individual commits.
Repositories that already have an explicit repository-level choice keep that setting, even if you change your user-level default later.
If a repository inherits Disabled by default:

The comment form is hidden on commit pages.
Inline diff comment entry points and inline thread replies are hidden.
Creating commit comments through the REST API and GraphQL API is blocked.
Existing commit comments remain viewable, editable, and deletable.

To leave feedback, join the discussion within GitHub Community.

The post Disable commit comments on the user level appeared first on The GitHub Blog.

---
*원문: [https://github.blog/changelog/2026-05-08-disable-commit-comments-on-the-user-level](https://github.blog/changelog/2026-05-08-disable-commit-comments-on-the-user-level)*

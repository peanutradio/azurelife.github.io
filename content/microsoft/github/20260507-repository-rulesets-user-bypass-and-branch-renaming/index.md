---
categories:
- MS
- GitHub
date: '2026-05-07T14:13:48+00:00'
description: 'GitHub repository rulesets now support two frequently requested features:
  adding individual users as bypass actors and renaming branches covered by organization'
draft: false
original_url: https://github.blog/changelog/2026-05-07-repository-rulesets-user-bypass-and-branch-renaming
source: GitHub Changelog
tags:
- Improvement
- platform governance
title: 'Repository rulesets: User bypass and branch renaming'
---

GitHub repository rulesets now support two frequently requested features: adding individual users as bypass actors and renaming branches covered by organization rulesets.
Add individual users as bypass actors

You can now add individual users as bypass actors on repository-level rulesets through the UI, REST API, and GraphQL. If you&rsquo;ve been creating dedicated teams or roles just to grant bypass access for a single person or service account, you can now skip that step and add accounts directly.
Rename branches covered by rulesets
Repository administrators can now rename a branch that&rsquo;s covered by an organization or enterprise ruleset, as long as the new branch name remains within the scope of every ruleset that applied to the original name. This removes the need to involve an organization or enterprise administrator for routine renames (e.g., migrating from master to main) when the rename doesn&rsquo;t change which rules apply.
Enterprise-level setting:

Organization-level setting:


The rename is allowed only when every organization-level and enterprise-level rule that applied to the original branch also applies to the new branch name.
If the new name would fall outside the scope of any applicable ruleset, the rename is blocked and an administrator at that level must perform it.
Organization and enterprise administrators can disable this capability in their settings.

To learn more, see the rulesets documentation.

The post Repository rulesets: User bypass and branch renaming appeared first on The GitHub Blog.

---
*원문: [https://github.blog/changelog/2026-05-07-repository-rulesets-user-bypass-and-branch-renaming](https://github.blog/changelog/2026-05-07-repository-rulesets-user-bypass-and-branch-renaming)*

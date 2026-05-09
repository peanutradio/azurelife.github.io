---
categories:
- MS
- GitHub
date: '2026-05-08T12:52:23+00:00'
description: When you delegate a task to Copilot cloud agent, it works in the background
  in its own development environment powered by GitHub Actions. You can pass secrets
  a
draft: false
original_url: https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent
source: GitHub Changelog
tags:
- Release
- copilot
title: More flexible secrets and variables for Copilot cloud agent
---

When you delegate a task to Copilot cloud agent, it works in the background in its own development environment powered by GitHub Actions. You can pass secrets and variables to the agent to give it access to private resources or to configure MCP servers.
Until now, these had to be configured one repository at a time, in a copilot environment under the repository&rsquo;s Actions settings. That made it painful to roll out shared configuration (e.g., an internal package registry token or a common MCP server) across many repositories.
Today, Copilot cloud agent gets its own dedicated &ldquo;Agents&rdquo; secrets and variables, sitting alongside the existing &ldquo;Actions&rdquo;, &ldquo;Codespaces&rdquo;, and &ldquo;Dependabot&rdquo; types. This means you can:

Configure secrets and variables at the organization level for the first time, and share them across any or all repositories in your organization.
Manage repository-level secrets and variables in a dedicated &ldquo;Agents&rdquo; section in your repository settings, separate from your Actions configuration.
Choose which repositories in an organization can access each secret or variable, just like with Actions.

This makes it much easier to configure Copilot cloud agent at scale, without having to duplicate configurations across every repository.
To learn more, see &ldquo;Configuring secrets and variables for Copilot cloud agent&rdquo; in the GitHub Docs.

The post More flexible secrets and variables for Copilot cloud agent appeared first on The GitHub Blog.

---
*원문: [https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent](https://github.blog/changelog/2026-05-08-more-flexible-secrets-and-variables-for-copilot-cloud-agent)*

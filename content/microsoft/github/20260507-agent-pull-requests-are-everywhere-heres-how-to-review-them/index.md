---
categories:
- MS
- GitHub
date: '2026-05-07T19:00:00+00:00'
description: 'You&rsquo;ve probably already approved one without realizing it. The
  tests passed. The code was clean. You merged it.




  But it was agent-generated&mdash;and th'
draft: false
original_url: https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/
source: GitHub Blog
tags:
- AI & ML
- Generative AI
- GitHub Copilot
- AI agents
- code review
- pull requests
- tech debt
title: Agent pull requests are everywhere. Here’s how to review them.
---

You&rsquo;ve probably already approved one without realizing it. The tests passed. The code was clean. You merged it.



But it was agent-generated&mdash;and that ease of approval is exactly the problem.



A January 2026 study, &ldquo;More Code, Less Reuse&rdquo;, found that agent-generated code introduces more redundancy and more technical debt per change than human-written code. The surface looks clean. The debt is quiet. And reviewers, according to the same research, actually feel better about approving it.



This isn&rsquo;t an argument to slow down. It&rsquo;s an argument to be intentional. There&rsquo;s a difference.



Agent pull requests are already saturating review bandwidth



The volume is already staggering. GitHub Copilot code review has processed over 60 million reviews, growing 10x in less than a year. More than one in five code reviews on GitHub now involve an agent. That&rsquo;s just the automated review pass. The pull request themselves are multiplying faster than reviewers can handle.



The traditional loop&mdash;request review, wait for code owner, merge&mdash;breaks down when one developer can kick off a dozen agent sessions before lunch. Throughput has scaled exponentially. Human review capacity hasn&rsquo;t. The gap is widening.



You&rsquo;re going to review agent pull requests. The question is whether you&rsquo;ll catch what matters when you do.



Who (or what) actually wrote this pull request



Before you look at a single line of diff, you need a model for what you&rsquo;re reviewing.



A coding agent is a productive, literal, pattern-following contributor with zero context about your incident history, your team&rsquo;s edge case lore, or the operational constraints that don&rsquo;t live in the repository. It will produce code that looks complete. But that &ldquo;looks complete&rdquo; failure mode is dangerous.



You&rsquo;re the one who carries that context. That&rsquo;s not a burden. It&rsquo;s the actual job. The part of review that doesn&rsquo;t get automated is judgment, and judgment requires context only you have.




One note for authors



If you&rsquo;re opening an agent-generated pull request, edit body before you request review. Agents love verbosity. They describe what&rsquo;s better explored through the code itself. Annotate the diff where context is helpful. And review it yourself before tagging others, not just to check correctness, but to signal that you&rsquo;ve validated the agent captured your intent.




Reviewing your own pull request isn&rsquo;t optional when agents are involved. It&rsquo;s basic respect for your reviewer&rsquo;s time.





Now, back to reviewers. The pull request lands in your queue. The author did their part. Here&rsquo;s what to watch for.



Red flags to watch for



1. CI gaming



Agents fail CI. When they do, they have an obvious path to get tests passing: remove the tests, skip the lint step, add || true to test commands. Some agents take it.



Any change that weakens CI is a blocker. Full stop. Before approving any agent pull request, check:




Did coverage thresholds change?



Were any tests removed, renamed, or marked as skipped?



Did the workflow stop running on forks or pull requests?



Are any CI steps now gated behind conditions they weren&rsquo;t before?




Yes, to any of those means you need an explicit justification before you continue.



2. Code reuse blindness



This is the highest-ROI thing you can do as a reviewer. Agents look for prior art. They&rsquo;ll find a pattern in the codebase and replicate it, often without checking whether a utility that already does the same thing exists somewhere else. The symptoms: new utility functions that duplicate existing ones with slightly different names, validation logic reimplemented in multiple places, middleware written from scratch that already lives in a shared module, helpers that are &ldquo;almost the same&rdquo; but with different names.



The agent&rsquo;s local context doesn&rsquo;t include the full picture of what exists across your repository. You do.



For every new helper or utility in an agent pull request, do a quick search. If you find an equivalent, don&rsquo;t leave a comment. Require consolidation before merge. The cost of leaving duplicated logic is that agents will find it as prior art and replicate it further.



&#128161;Pro tip: Require justification for adding new utilities in agent pull requests above a size threshold. This catches the duplication problem early.



3. Hallucinated correctness



The obvious hallucination (calling an API that doesn&rsquo;t exist, referencing a variable out of scope) gets caught in CI. The dangerous one is subtler: code that compiles, passes every test, and is wrong.



Off-by-one errors in pagination. Missing permission checks on a branch that&rsquo;s never hit in tests. Validation that short-circuits under an edge case the agent never considered. Wrong behavior under a race condition that only surfaces at scale.



Trace it, don&rsquo;t just scan it. Pick the most critical path in the diff. Follow it from input through every transform to output. Check boundary conditions (zero, max, empty), missing validation on external values, permission checks on every branch, and surprising conditional logic.



Require a new test that fails on the pre-change behavior. If the agent can&rsquo;t write a test that would have caught the bug it claims to fix, the fix is incomplete or the understanding is wrong.



4. Agentic ghosting



You leave a thorough review. You explain the issue, provide context, suggest a direction. The pull request goes quiet. Or the agent responds and misses the point entirely and runs in circles. You invest another round. Still nothing useful.



Larger pull requests with no structured plan correlate strongly with agent abandonment or misalignment. The larger and less scoped the pull request, the more likely you&rsquo;re going to sink review time into something that goes nowhere.



Before you invest deep review on a large agent pull request check the pull request history. Has it been responsive in previous rounds? Does it have a clear implementation plan, or did the agent just start writing code?



If there&rsquo;s no plan, request a breakdown before you write a single comment. Copy-paste version:



&ldquo;This pull request is too large for me to review without a clearer implementation plan. Can you break it into smaller scoped units, or add a summary of what each part does and why it&rsquo;s structured this way? Happy to review after that.&ldquo;



Firm, short, not personal. And it saves you an hour.



5. Untrusted input in workflows



Prompt injection in CI agents is real and underappreciated. Here&rsquo;s the pattern: an agent workflow reads content from a pull request body, an issue, or a commit message. That content gets interpolated into a prompt. The prompt goes to a model. The model output gets piped to a shell command. The whole thing runs with GITHUB_TOKEN permissions.



When you&rsquo;re reviewing any workflow that calls an LLM, these are blockers:




Is untrusted user input, pull requestbodies, issue bodies, commit messages, being interpolated into prompts without sanitization?



Is GITHUB_TOKEN write-scoped when it only needs read access?



Is model output being executed as shell commands without validation?



Are secrets accessible to the agent step or being printed to logs?




What to require before merge: least-privilege permissions in the workflow YAML (permissions: read-all is a reasonable default), sanitize and quote untrusted content before it touches a prompt, separate the &ldquo;analysis&rdquo; step from the &ldquo;execution&rdquo; step with a human approval gate for anything touching production, never eval model output.



Time&nbsp;Step&nbsp;What to do&nbsp;1&ndash;2 min&nbsp;Scan and classify&nbsp;Look at the file list and diff size. Narrow task (docs, CI,&nbsp;small change) or complex (multi-file, logic, performance, tests)? That classification sets your review depth for everything that follows.&nbsp;2&ndash;3 min&nbsp;Check CI changes first&nbsp;Before reading a single line of app code, look at anything touching .github/workflows, test configs, coverage settings, or build scripts. Flag anything that weakens CI. Stop sign&nbsp;check.&nbsp;3&ndash;5 min&nbsp;Scan for new utilities&nbsp;Search for new functions, helpers, or modules. For each one, do a quick repo search to check for duplicates. Flag anything that reinvents existing functionality.&nbsp;5&ndash;8 min&nbsp;Trace one critical path&nbsp;Pick the most important logic change.&nbsp;Trace it&nbsp;end-to-end: input &rarr; transforms &rarr; output. Check boundary conditions, permissions, unexpected&nbsp;branching. This is the step you&nbsp;can&rsquo;t&nbsp;skip.&nbsp;8&ndash;9 min&nbsp;Security boundaries&nbsp;If this&nbsp;PULL&nbsp;REQUEST touches&nbsp;any workflow that calls an LLM or handles untrusted input, run through the security checklist above.&nbsp;9&ndash;10 min&nbsp;Require evidence&nbsp;For any non-trivial logic change, require a test that&nbsp;fails on&nbsp;the pre-change behavior. No rollback plan for risky changes? Ask for one.&nbsp;



When to request a smaller pull request:




The diff touches more than five unrelated files



You can&rsquo;t describe the purpose of the pull request in one sentence



The agent has no implementation plan or the pull request body is empty



CI is failing and the only changes in the diff are to test files




Let Copilot review it first



Use automated review for what it&rsquo;s good at: catching the mechanical stuff before a human has to. Copilot code review flags style inconsistencies, obvious logic errors, missing error handling, and type mismatches. It handles the low-level scan. That frees you up for the judgment work, which is where your time actually matters.



Treat it as a prerequisite, not a replacement. Let Copilot run first. If it catches something obvious, let the author address it before you invest your review time.



You can tune this with custom instructions specific to your team: flag anything that modifies CI thresholds, surface new utilities for deduplication review, check that every external input is validated. The more specific your instructions, the more useful the automated pass.



&#128161; Pro tip: I recently experimented with codifying my own review checklist using the Copilot SDK. Instead of remembering to run the same security checks on every pull request, I built a workflow that takes my personal checklist&mdash;auth on admin endpoints, tests actually running, safe env variable handling&mdash;and runs it against the diff automatically. If it finds critical issues, it blocks the merge.



Judgment is the bottleneck, and that&rsquo;s fine



The surface area of code is growing. pull request volume is growing. The time you spend scanning boilerplate should shrink.



What doesn&rsquo;t shrink is the context you carry. The things you know about your system that aren&rsquo;t written down anywhere. That&rsquo;s what makes your review valuable, and it&rsquo;s the part that doesn&rsquo;t get automated.



Three takeaways:




Any CI weakening is a hard stop.



Let the agents scan first. You trace the critical path.



Red flag checklist as your default on complex agent pull requests.





Read the docs &gt;


The post Agent pull requests are everywhere. Here&#8217;s how to review them. appeared first on The GitHub Blog.

---
*원문: [https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)*

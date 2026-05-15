---
categories:
- MS
- GitHub
date: '2026-05-14T22:02:43+00:00'
description: 'In April, we experienced 10 incidents that resulted in degraded performance
  across GitHub services.




  To increase transparency, at the end of April, we release'
draft: false
original_url: https://github.blog/news-insights/company-news/github-availability-report-april-2026/
source: GitHub Blog
tags:
- Company news
- News & insights
- GitHub Availability Report
title: 'GitHub availability report: April 2026'
---

In April, we experienced 10 incidents that resulted in degraded performance across GitHub services.



To increase transparency, at the end of April, we released a blog post covering major incidents on April 23 and April 27. We have also taken steps to bring more detail to the GitHub status page.



Thank you for your patience as we work through near-term and long-term investments we’re making.



April 01 15:02 UTC (lasting 8 hours and 43 minutes)



On April 1, 2026, between 14:40 and 17:00 UTC, GitHub&#8217;s code search service was fully unavailable; 100% of search queries failed. Service was restored in a degraded state by 17:00 UTC with temporarily stale results, and fully recovered with current data by 23:45 UTC.



During the 2 hour and 20 minute period of full unavailability, 100% of code search requests failed. After initial recovery at 17:00 UTC, search returned results, but they did not reflect repository changes made after approximately 07:00 UTC that day. Full indexing caught up by 23:45 UTC.



During a routine infrastructure upgrade to the messaging system supporting code search, an automated change was applied too aggressively, causing a coordination failure between internal services. This halted search indexing, and search results began going stale. While the team worked to recover the messaging infrastructure, an unintended service deployment cleared internal routing state, escalating the staleness issue into a complete outage.



We restored the messaging infrastructure through a controlled restart, reestablishing coordination between services. We then reset the search index to a point in time before the disruption. No repository data was lost—the search index is a secondary index derived from Git repositories, which were completely unaffected. Once re-indexing completed, all search results reflected the current state of repositories.



We are adding more gradual upgrades with better health checks, so problems are caught before they cascade, deployment safeguards to prevent unintended changes during active incidents, faster recovery tooling to reduce time to restore service and better traffic isolation to prevent cascading impact from unexpected traffic spikes during outages.



April 01 16:06 UTC (lasting 4 minutes)



On April 1, 2026, between 15:34 UTC and 16:02 UTC, our audit log service lost connectivity to its backing data store due to a failed credential rotation. During this 28-minute window, audit log history was unavailable via both the API and web UI. This resulted in 5xx errors for 4,297 API actors and 127 github.com users. Additionally, events created during this window were delayed by up to 29 minutes in github.com and event streaming. No audit log events were lost; all audit log events were ultimately written and streamed successfully. Customers using GitHub Enterprise Cloud with data residency were not impacted by this incident.



We were alerted to the infrastructure failure at 15:40 UTC—six minutes after onset—and resolved the issue by recycling the affected environment, restoring full service by 16:02 UTC. As a result of the incident, we completed several follow-up actions to reduce the risk of recurrence and improve detection. The team updated and strengthened the credential rotation process to improve resiliency and help prevent similar failures in the future. In parallel, we enhanced our monitoring configuration, including making paging thresholds more sensitive to improve detection speed and operator visibility into similar issues going forward.



April 09 09:50 UTC (lasting 25 minutes) and 16:20 UTC (lasting 4 hours and 16 minutes)



On April 9, 2026, we had two incidents, between 09:05 UTC and 19:05 UTC and between 16:05 UTC and 20:36 UTC, where the Copilot coding agent service was degraded and users experienced significant delays starting new agent sessions. Approximately 84% of new agent session requests were delayed across four separate outage waves, with queue wait times peaking at 54 minutes compared to a normal baseline of 15–40 seconds. On average, the error rate was 83.9% and peaked at 97.5% of requests to the service. Approximately 22,700 workflow creations were delayed or failed during the incident.



This was due to a bug in our rate limiting logic that incorrectly applied a rate limit globally across all users, rather than scoping it to the individual installation that triggered the limit. A contributing factor was a surge in API traffic from a client update that increased requests to an internal endpoint by 3–4x, which accelerated rate limit exhaustion. The second similar incident was also caused due to an internal service exceeding API rate limits, compounded by a caching bug that persisted the rate-limited state beyond the actual rate limit window, causing recurring outage.



Our team detected the issue within 15 minutes and began investigating immediately. We mitigated the incident by disabling the faulty rate limit caching mechanism via feature flag and updating our service to use per-installation credentials for API calls, ensuring rate limits are correctly scoped to individual installations. Service was fully restored by 20:36 UTC. Jobs that were delayed during the incident were queued and processed once service resumed.



We have since added automated monitoring and alerting to detect this failure mode proactively, deployed fixes to reduce unnecessary API traffic through caching improvements, and are continuing work to further isolate rate limit scoping across client types to prevent similar issues in the future.



April 13 19:56 UTC (lasting 39 minutes)



On April 13, 2026, between 18:53 UTC and 20:30 UTC, the GitHub Pages service experienced elevated error rates. On average, the error rate was 10.58% and peaked at 12.77% of requests to the service, resulting in approximately 17.5 million failed requests returning HTTP 500 errors.



This incident was due to an automated DNS management tool erroneously deleting a DNS record for a GitHub Pages backend storage host after its upstream data source intermittently failed to return the record, causing the tool to treat it as stale and remove it. As cached copies of the record expired across our systems, GitHub Pages servers were no longer able to reach the affected storage host, resulting in errors for a portion of requests.



Once the issue was identified, our team quickly traced it to the missing DNS record and re-created it. Service returned to normal by 20:30 UTC, and the incident was fully resolved by 20:35 UTC. We recognize that detection took longer than we would have liked—approximately 53 minutes—due to the gradual nature of the error increase and a gap in our alerting for this type of failure.



We are making three key improvements to prevent similar issues in the future. We are implementing availability-zone-tolerant routing in the GitHub Pages frontend so that an unresolvable backend host triggers failover to healthy hosts rather than returning errors, adding safeguards to prevent automated deletion of DNS records owned by other systems, and improving logging and alerting for DNS resolution failures in the GitHub Pages serving path.



April 16 15:06 UTC (lasting 3 hours and 22 minutes)



On April 16, 2026, between 09:30 UTC and 17:15 UTC, users experienced failures when attempting to connect to GitHub Codespaces via the VS Code editor. During this time, approximately 40% of codespace start operations failed. Users connecting via SSH were not impacted.



The issue was caused by failures in an upstream service that prevented the VS Code Server from being retrieved during codespace startup. The impact was mitigated by implementing a workaround to use an alternative download path when the primary endpoint is degraded. In parallel, we coordinated with the upstream dependency team to address the root cause of the download failure.



We are improving our fallback mechanism to reduce the impact of similar upstream failures in the future and streamlining processes to accelerate deployment of similar changes in the future.



April 20 13:28 UTC (lasting 15 hours and 36 minutes)



On April 20, 2026, between 10:28 UTC and 15:04 UTC, GitHub experienced degraded service for code scanning default setup, code quality, and project boards. Repair of affected project boards additionally lasted until 05:04 UTC on April 21.



During this time, code scanning default setup and code quality analyses were not triggered on newly opened pull requests. Additionally, newly created issues were not appearing on project boards.



The cause was a serialization error that prevented proper triggering of code scanning, code quality analyses, and project board updates.



We identified the issue within ~40 minutes and mitigated the issue by deploying a fix, restoring event publishing for code scanning and code quality. For project boards, an additional code change was deployed to update event consumers, followed by a reindex of affected project items.



We are working to prevent recurrence by strengthening our schema validations and improving monitoring for drops in publishing on critical topics. In addition, we are auditing other parts of our system to ensure no similar limitations exist elsewhere.



April 22 15:35 UTC (lasting 3 hours and 43 minutes)



On April 22, 2026, between 15:16 UTC and 19:18 UTC, users experienced errors when interacting with Copilot Chat on github.com and Copilot Cloud Agent. During this time, users were unable to use Copilot Chat or Copilot Cloud Agent. Copilot Memory (in preview) was not available to Copilot agent sessions during this time.



The issue was caused by an infrastructure configuration change that resulted in connectivity issues with our databases. The team identified the cause and restored connectivity to the database. Copilot Chat and Cloud Agent for github.com were restored by 18:16 UTC. Remaining regional deployments were restored incrementally, with full resolution at 19:18 UTC.



We have taken steps to prevent similar infrastructure changes from causing these kinds of database operations in the future.



April 23 16:12 UTC (lasting 1 hour and 18 minutes)



On April 23, 2026, between 16:03 and 17:30 UTC, users experienced elevated error rates and degraded performance across GitHub Copilot, Webhooks, Git Operations, GitHub Actions, Migrations, and Deployments. Approximately 5–7% of overall traffic was affected during the 1 hour and 27 minute impact window. For Copilot, ~7% of AI model requests failed, ~10% of Copilot cloud agent sessions were affected, and ~9% of Copilot Insights dashboard requests returned errors. For Webhooks, ~0.35% of API requests returned errors at peak, with up to 10% of traffic experiencing elevated latency (>3 seconds). Git Operations averaged 1.25% errors over the incident duration, with a peak of 2.07%. GitHub Actions saw workflow run status updates experienced delays of up to ~8 seconds. For Migrations, 0.88% of active repository migrations failed, and 79% saw elevated durations. Deployments were temporarily blocked during the incident window.



Our DNS infrastructure in one datacenter entered a degraded state and began intermittently failing to resolve service addresses. This caused a cascading impact: services that depend on name resolution to communicate with internal APIs, external providers, and storage systems all experienced errors simultaneously.



The root cause was a recently introduced traffic-balancing mechanism that had been rolled out progressively to support our growth. Under a specific load pattern, this mechanism caused DNS resolvers to begin failing. Existing DNS caching provided partial protection. Services with recently cached entries continued operating normally, which is why overall impact was limited to approximately 5–7% of traffic rather than a complete outage.



After an initial configuration rollback did not resolve the issue, we restarted the affected DNS infrastructure. Services began recovering within minutes, and all returned to normal by 17:30 UTC. No data was lost; all repositories, databases, and workflow data were unaffected.



To prevent incidents like this in the future we are improving our DNS infrastructure resilience to prevent single-datacenter failures from cascading across services, implementing safer rollout and validation with a dedicated environment to test infrastructure changes against production-like traffic, investing in faster automated detection and recovery with self-healing mechanisms for DNS resolution failures and reducing blast radius by reviewing service dependencies on shared infrastructure components.



April 27 16:31 UTC (lasting 6 hours and 15 minutes)



On April 27, 2026, between 16:15 UTC and 22:46 UTC, GitHub search services experienced degraded connectivity due to saturation of the load balancing tier deployed in front of our search infrastructure. This resulted in intermittent failures for services relying on our search data including Issues, Pull Requests, Projects, Repositories, Actions, Package Registry and Dependabot Alerts. The impact was varied by search target, with services seeing up to 65% of searches timing out or returning an error between 16:15 UTC and 18:00 UTC.



We detected the drop in search results through our ongoing monitoring and declared an incident at 16:21 UTC. We tracked the incident as mitigated as of 21:33 UTC and monitored the systems until 22:46 UTC when we declared the incident resolved.



The saturation was caused by a large influx of anonymous distributed scraping traffic that was crafted to avoid our public API rate limits. This scraping traffic made up 30% of the day’s total search traffic, but it was concentrated within a four-hour period. The traffic originated from over 600,000 Unique IP addresses, with matching actor information in all requests. Our existing monitoring did not classify the increased scraping as a risk and this dimension of the incident was only discovered while working to mitigate.



To mitigate, we immediately focused on relieving pressure from the load balancers while simultaneously working on scaling the load balancing tier, blocking the anomalous traffic and applying tuning to the balancers to fully resolve the incident.



Looking ahead, we’ve not only scaled the load balancer tier, but applied optimizations to improve our connection handling and re-use to reduce the possibility that a saturation event like this can re-occur. We’ve also added new monitors and controls within the platform to allow us to restrict anonymous traffic to mitigate the impact to our registered users. We are continuing to strengthen our defenses against this type of large-scale automated abuse.







Follow our status page for real-time updates on status changes and post-incident recaps. To learn more about what we’re working on, check out the engineering section on the GitHub Blog.
The post GitHub availability report: April 2026 appeared first on The GitHub Blog.

---
*원문: [https://github.blog/news-insights/company-news/github-availability-report-april-2026/](https://github.blog/news-insights/company-news/github-availability-report-april-2026/)*

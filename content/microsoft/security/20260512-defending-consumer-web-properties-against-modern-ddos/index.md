---
categories:
- MS
- 보안
date: '2026-05-12T16:00:00+00:00'
description: If you own, create, or maintain online services and web portals, you’re
  probably aware of the dramatic upswing in DDoS attacks on your domains. AI has democrati
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/05/12/defending-consumer-web-properties-against-modern-ddos-attacks/
source: Microsoft Security Blog
tags:
- Azure
title: Defending consumer web properties against modern DDoS attacks
---

If you own, create, or maintain online services and web portals, you’re probably aware of the dramatic upswing in DDoS attacks on your domains. AI has democratized tooling not just for us but for threat actors as well. DDoS in this era has extended from simple bandwidth saturation to sophisticated, application-layer abuse. Defending against this activity now requires system-level design, beyond just the typical network-level filtering. As botnets continue to expand their footprint and evade identification, it is important for us to take a step back, assess the situation, and take a defense-in-depth approach to increase our resilience against this class of disruption.




Protect your cloud workloads with Azure Cloud Security




DDoS activity across Bing and other online services at Microsoft has seen a large uptick in the past five to six years. As reported in the Microsoft Digital Defense Report 2025, Microsoft now processes more than 100 trillion security signals, blocks approximately 4.5 million new malware attempts, analyzes 38 million identity risk detections, and screens 5 billion emails for malicious content each day. This helps illustrate both the breadth of modern attack surfaces and the automation cyberattackers can now wield at industrial scale. When we narrow in specifically on DDoS, an even clearer trend emerges: beginning in mid-March of 2024, Microsoft observed a rise in network DDoS attacks that eventually reached approximately 4,500 cyberattacks per day by June 2024. And this persistent volume was paired with a shift toward more stealthy application-layer techniques.



In my role as Vice President, Intelligent Conversation and Communications Cloud Platform at Microsoft, I focus on helping the Microsoft AI and Bing teams build systems that are safe, resilient, and worthy of user trust, even under the sustained pressure we’re receiving from today’s cyberattackers. Whether you are responsible for a single public website or a large portfolio of consumer-facing applications, defending against modern DDoS attacks means more than just absorbing traffic. It means building defense-in-depth robust enough that, even if some attack traffic gets through, your service stays usable for the people who rely on it.



The nature of modern DDoS attacks



Early DDoS attacks were largely about volume. Cyberattackers would flood a target with traffic in an attempt to saturate network capacity and force an outage. While volumetric attacks still happen, most large services now have baseline protections that make this approach less effective on its own.




Get always-on monitoring with Azure DDoS Protection




Modern DDoS attacks are more nuanced. They are often multi-vector, with a single campaign potentially including network-layer floods and application-layer abuse at the same time. Along with the exponential increase in the scale of these cyberattacks, they are also getting more tailored to stress specific applications and user flows. Application-layer attacks are gaining popularity because they are harder to distinguish from legitimate usage.



We also see threat actors utilizing a broader range of devices in botnets, including consumer Internet of Things (IoT) devices and misconfigured cloud workloads. In some cases, cyberattackers abuse legitimate cloud infrastructure to generate traffic that blends in with normal usage patterns. Edge systems, such as content delivery networks (CDNs) and front-door routing services, are increasingly targeted because they sit at the boundary between users and applications.



When attack traffic looks like normal user traffic, typical network-level blocklists aren’t very effective. You need sophisticated fingerprinting (starting with JA4), layered controls, and good operational visibility. This evolution is part of what makes defending against DDoS more than a networking problem. It is now a system design problem, an operational monitoring problem, and ultimately a trust problem.



A defense-in-depth framework



Even if you block 95% of malicious traffic, the remaining 5% can still be enough to take you down if it hits the right bottleneck. That’s why defense-in-depth matters.



A strong defensive posture starts with making abnormal traffic easier to spot and harder to exploit. Techniques like rate limiting, geo-fencing, and basic anomaly detection remain foundational. They are most effective when tuned to your specific traffic patterns. Cloud-native DDoS protection services play an important role here by absorbing large-scale attacks and surfacing telemetry that helps teams understand what is happening in real time. If you run on Azure, there are built-in options that can help when used as part of a broader design. Azure DDoS Protection is designed to mitigate network-layer cyberattacks and is intended to be used alongside application design best practices. At the edge, services like Azure Web Application Firewall (WAF) on Azure Front Door can provide centralized request inspection, managed rule sets, geo-filtering, and bot-related controls to reduce malicious traffic before it reaches your origins.



Microsoft publishes a range of Secure Future Initiative (SFI) guidance and engineering blogs that describe patterns we use internally to harden consumer services at scale, and if you’re looking to assess how robust your site’s current DDoS resilience posture is, here’s a simple tabular framework to work from:



StateAttributes and characteristicsReadiness posture (availability and latency)Risk profile (CISO perspective)Level 1: Exposed(Direct Origin/No CDN)•Architecture: Monolithic; Origin IP exposed through DNS A-records.•Detection: Manual log analysis post-incident; reactive alerts on server CPU spikes.•Mitigation: Null-routing by ISP (taking the site offline to save the network); manual firewall rules.•Key Signal: Immediate 503 errors during minor surges.Fragile/Volatile•Availability: Single point of failure. Zero resilience to volumetric or L7 attacks.•Latency: Highly variable; degrades linearly with traffic load.•Recovery: Hours to days (manual intervention required).Critical/Existential•Residual Risk: High. The organization accepts that any motivated attacker can cause total outage.•Financial Impact: Direct revenue loss proportional to downtime.•Reputation: Severe damage; loss of customer trust.Level 2: Basic Protection(Commodity CDN/ Volumetric Shield)•Architecture: Static assets cached at edge; Origin cloaked.•Detection: Threshold-based volumetric alerts (for example, more than 1 Gbps).•Mitigation: &#8220;Always-on&#8221; scrubbing for L3/L4 floods; basic geo-blocking.•Key Signal: Survival of SYN floods, but failure under HTTP floods.Defensive/Static•Availability: Resilient to network floods; vulnerable to application exhaustion.•Latency: Improved for static content; poor for dynamic attacks.•Recovery: Minutes (automated scrubbing activation).High/Managed•Residual Risk: Moderate-High. Application logic remains a soft target.•Blind Spot: Sophisticated bots bypass volumetric triggers.•Compliance: Meets basic continuity requirements but fails resilience stress tests.Level 3: Advanced Edge(Intelligent Filtering/WAF)•Architecture: Edge compute; Dynamic web application firewall (WAF); API Gateway enforcement.•Detection: Signature-based (JA3/JA4 fingerprinting); User-Agent analysis.•Mitigation: Rate limiting by fingerprint/behavior; CAPTCHA challenges.•Key Signal: High block rate of &#8220;bad&#8221; traffic with low false positives.Proactive/Robust•Availability: High availability for most attack vectors, including low-and-slow.•Latency: Consistent; edge mitigation prevents origin saturation.•Recovery: Seconds (automated policy enforcement).Medium/Controlled•Residual Risk: Medium. Shift to &#8220;sophisticated bot&#8221; risk (mimicking humans).•Focus: Quality of Service (QoS) and reducing false positives.•Investments: Shift from hardware to threat intelligence feeds.Level 4: Resilient Architecture(Graceful Degradation/Bulkheading)•Architecture: Circuit Breakers; Load Shedding logic; defense-in-depth.•Detection: Service-level health checks; Dependency failure monitoring; outlier detection; trust scores.•Mitigation: Challenges/CAPTCHAs; Service Degradation Automated feature toggling (for example, disable &#8220;Reviews&#8221; to save &#8220;Checkout&#8221;).•Key Signal: &#8220;Limited Impact to Availability&#8221; during massive events.Resilient/Adaptive•Availability: Core functions remain online; non-critical features degrade.•Latency: Controlled degradation; critical paths prioritized.•Recovery: Real-time (system self-stabilization).Low/Tolerable•Residual Risk: Low. Business accepts degraded functionality to preserve revenue.•Narrative: &#8220;We operated through the attack with minimal user impact.&#8221;•Risk Appetite: Aligned with business continuity tiers.Level 5: Autonomous Defense(AI-Powered/Predictive)•Architecture: Serverless edge logic; Multi-CDN failover; Chaos Engineering.•Detection: AI and machine learning predictive modeling; Zero-day pattern recognition.•Mitigation: Autonomous policy generation; Preemptive scaling.•Key Signal: Attack neutralized before human operator awareness.Antifragile/Optimized•Availability: Near 100% through multi-redundancy and predictive scaling.•Latency: Optimized dynamically based on threat level.•Recovery: Instantaneous/Pre-emptive.Minimal/Strategic•Residual Risk: Very low. Focus shifts to supply chain and novel vectors.•Posture: Continuous improvement through Red Teaming and Chaos experiments.•Leadership: Chief information security officer (CISO) drives industry intelligence sharing.




Read the latest SFI progress report




Planning for graceful degradation



One of the most common misconceptions about DDoS defense is that success means “no reduction in services.” In reality, even a partially successful attack can degrade performance enough to frustrate users or erode trust, without triggering a full outage. Graceful degradation is about maintaining core functionality even when systems are under stress. It means being deliberate about which user flows must remain available and which can be temporarily limited without causing disproportionate harm.



For example, our systems prioritize core scenarios over secondary features during extremely large cyberattacks. In practice, this can mean temporarily delaying nonessential personalization or shedding load from less critical features to preserve overall responsiveness. These decisions are made in advance and tested, not improvised during an incident. Here’s an example of how we might do that:




Prioritizing core user flows: We would focus on keeping core scenarios responsive. That might mean protecting one or two core scenarios while de-emphasizing secondary experiences.





Reducing expensive work first: Some parts of an experience are computationally heavier. Under attack pressure, those are candidates for temporary reduction, so the overall service stays usable.





Tiered experience under load: In extreme conditions, you can provide a better experience for users with higher trust signals while still offering an acceptable experience to everyone else. This is not about punishing lower trust users. It is about making sure your system can still serve legitimate demand when resources are constrained.





Clear user messaging: If you need to disable or simplify a feature temporarily, communicate it in a way that is honest and calm. You do not need to explain your internal architecture. You do need to be predictable.




Designing for resilience means assuming that individual components will fail or be stressed at some point. Systems that are built with that expectation tend to recover faster and maintain user trust more effectively than systems that aim for perfect uptime at all costs.



Get started improving your DDoS defense



If I could leave you with a single practical concept, it would be this: treat DDoS as a normal operating condition for internet-facing services. Build defense in depth. Assume some cyberattack traffic will get through. Design your service so it can degrade gracefully while protecting the user experiences that matter most.



Consumer trust is fragile and hard-earned. Developers and operators who think beyond raw availability, and who design for transparency, prioritization, and resilience, are better positioned to handle the realities of today’s cyberthreat landscape. Modern defensive strategies combine proactive controls, thoughtful architecture, and a clear understanding of what matters most to users.



For those interested in going deeper, I encourage you to explore the Secure Future Initiative resources and the other Office of the CISO blogs provided by my peers at Microsoft. Both of these resources frequently share practical patterns for building and operating resilient services at scale.




Explore the Microsoft Secure Future Initiative





	

	
		
			
				

MicrosoftDeputy CISOs



To hear more from Microsoft Deputy CISOs, check out the&nbsp;OCISO blog series:







To stay on top of important security industry updates, explore resources specifically designed for CISOs, and learn best practices for improving your organization’s security posture, join the&nbsp;Microsoft CISO Digest distribution list.

			
		
					
				
																				
			
			





To learn more about Microsoft Security solutions, visit our&nbsp;website.&nbsp;Bookmark the&nbsp;Security blog&nbsp;to keep up with our expert coverage on security matters. Also, follow us on LinkedIn (Microsoft Security) and X (@MSFTSecurity)&nbsp;for the latest news and updates on cybersecurity.&nbsp;&nbsp;
The post Defending consumer web properties against modern DDoS attacks appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/05/12/defending-consumer-web-properties-against-modern-ddos-attacks/](https://www.microsoft.com/en-us/security/blog/2026/05/12/defending-consumer-web-properties-against-modern-ddos-attacks/)*

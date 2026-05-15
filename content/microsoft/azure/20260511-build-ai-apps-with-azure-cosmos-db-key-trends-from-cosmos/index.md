---
categories:
- MS
- Azure
date: '2026-05-11T16:00:00+00:00'
description: 'Every year, Azure Cosmos DB Conf offers a window into how modern applications
  are built—not in theory, but in production at global scale.





  This year, the key'
draft: false
original_url: https://azure.microsoft.com/en-us/blog/build-ai-apps-with-azure-cosmos-db-key-trends-from-cosmos-conf-2026/
source: Azure Blog
tags:
- Databases
- Internet of things
title: 'Build AI apps with Azure Cosmos DB: Key trends from Cosmos Conf 2026'
---

Every year, Azure Cosmos DB Conf offers a window into how modern applications are built—not in theory, but in production at global scale.




This year, the key theme from Cosmos Conf was clear: AI is not just another workload. It is fundamentally reshaping how applications—and data platforms—are built. 




  In the opening keynote, VP of Azure Cosmos DB Kirill Gavrylyuk described three key shifts driving this transformation, and we saw them play out across every customer story at the event.





Discover how Azure Cosmos DB powers AI app development




The three AI shifts reshaping application architecture with Azure Cosmos DB



AI is making flexible, semi-structured data foundational




  AI applications don’t operate on rigid schemas. They operate on prompts, memory, and context, all of which are inherently semi-structured and evolving over time. 





  This fundamentally changes how databases must behave.





  Data platforms are no longer just systems of record—they are becoming systems of reasoning, where flexibility is critical to how applications learn, adapt, and generate outcomes.




AI is dramatically accelerating the pace of development




  AI, and especially coding agents, are changing how software is built.





  Developers are:





Iterating faster  



Shipping more frequently  



Scaling from zero to massive usage instantly  




As Kirill highlighted, developers can no longer be constrained by strict schemas. Flexibility isn’t just a convenience—it’s what enables teams to move at AI speed. Databases need to meet the demand with serverless form factor, instant and limitless scalability, advanced integrated caching, and provide agent-friendly interfaces. 



Semantic search is becoming a first-class query operator




  The third shift is just as important:





  AI applications require:





Vector search  



Full-text search  



Hybrid search  



Semantic ranking  




These are no longer “add-ons.” They are core to how modern applications function. 




  Across Cosmos DB Conf, we saw a clear pattern: teams are building applications where retrieval, reasoning, and real-time context are tightly integrated.




OpenAI: Flexibility at planet scale




  These shifts are most visible in what organizations like OpenAI are building.





  Speaking at Cosmos Conf, Jon Lee of OpenAI addressed how they are operating at massive scale—processing trillions of transactions and petabytes of data—reinforcing that what matters most is not just scale, but the ability to evolve quickly.





Watch how OpenAI approaches database design at scale





  As Jon shared, modern systems must be able to:





Scale instantly from zero to massive usage.  



Support schema-less design for rapid onboarding.  



Enable thousands of developers to iterate simultaneously.   




“The most important thing… is being able to scale from zero to millions of QPS, being able to scale from zero bytes to petabytes,” explained Jon, adding that speed and flexibility go together. 




We have thousands of developers that are actively building products… it’s really important to make it easy to onboard to databases really fast.




This is exactly the world Kirill described: AI systems demand flexible data models that evolve as fast as the applications themselves.



This highlights how Azure Cosmos DB supports dynamically evolving, large-scale AI workloads.



Vercel: The rise of serverless, AI-native applications




  If OpenAI shows what’s possible at scale, Vercel shows how the shape of applications is changing.





  As Guillermo Rauch, CEO of Vercel, explained, AI is dramatically expanding who can build software—from millions of developers to potentially billions of creators, many of whom are using agents to generate applications on demand. Kirill underscored this point in his keynote when he stated that more than half of Azure Cosmos DB customers are already using coding agents in their development workflows. 





Watch how Vercel approaches building AI‑powered applications





  According to Guillermo, this is driving a structural shift toward:





Serverless architectures  



Ephemeral applications  



Instant scaling from zero to viral  





  Data platforms must keep up. To support this pace, platforms need to provide:





Built-in best practices (data modeling, partitioning, and optimization).  



Intelligent guidance (agent skills and automation).  



Real-time feedback on performance and cost.





  Speaking on why he turned to Azure Cosmos DB, Guillermo said, “I wanted a system that gave me an economical thinking where the developer writes a query and they understand its cost.”




Developers need immediate feedback on the cost of their decisions, making efficiency a built-in design principle, not an afterthought.



This reflects a broader shift toward AI-native apps built on globally distributed, serverless data platforms like Azure Cosmos DB.



Walmart: Reliability and performance at scale




  While AI is transforming how applications are built, one thing hasn’t changed: Performance and reliability remain mission-critical.




As Kirill emphasized, AI does not remove the need for reliability, security, and performance. 




  In fact, it raises the bar. This was reinforced in sessions like Walmart’s, where Technical Fellow Sid Anand explained that large-scale applications must:





Deliver low-latency experiences globally.  



Remain available through regional failures.  



Maintain consistent performance at massive scale.  





Watch how Walmart approaches global e‑commerce at scale





  “We want people to be able to add to their cart and view cart no matter what is happening in a given cloud region…and we need all of these interactions to be low latency because any type of latency friction will cause a drop-off,” said Sid.




From gigabytes to petabytes, from hundreds to trillions of transactions, modern systems must operate seamlessly under unpredictable demand.



These requirements align with how Azure Cosmos DB is designed for global distribution and low latency at scale.



Cost efficiency becomes a core design principle




  A final takeaway from Cosmos Conf: as systems grow more complex, cost becomes just as important as scale.





  Across the keynote and sessions, we saw a clear shift:





Developers need cost visibility in real time.  



Architects need to design for efficiency upfront.  



Teams want to consolidate platforms and reduce complexity.  




This is where innovations like Azure DocumentDB come into focus. 



As highlighted in the keynote, Azure DocumentDB offers over 40% lower cost vs. alternatives, and enables high performance with simplified architecture. It also supports open-source, multi-cloud portability scenarios. The result is a broader choice for builders: 




Azure Cosmos DB → for global scale, serverless, five-nines reliability.



Azure DocumentDB → for cost efficiency, flexibility, open ecosystem.




Design and architecture examples that developers can start building now




  Beyond the keynote, there were a number of demo-driven sessions at Cosmos Conf across app architectures, repeatable patterns, and best practices for building and scaling AI-enabled solutions.




For example, Farah Abdou, a lead machine engineer at startup SmartServe, shared how her team rebuilt their architecture using Azure Cosmos DB as a unified “agent memory fabric.” By combining vector search for semantic caching, change feed for event-driven coordination, and optimistic concurrency for conflict prevention, they were able to reduce costs, enable sub-100ms agent handoffs, and eliminate state conflicts.



Another topic we get asked about a lot is how users protect and govern their AI applications. Pamela Fox, a Microsoft Principal Cloud Advocate, walked through how to build secure, multi-user AI systems using the Model Context Protocol (MCP). By authenticating users with Entra ID and storing per-user data in Azure Cosmos DB, she enabled role-based access with Microsoft Graph, and practical development workflows using tools like VS Code and GitHub Copilot.



From these hands-on patterns to large-scale production systems, the lesson was consistent: teams are designing for scale, efficiency, and real-world usage from day one.



Key takeaways&nbsp;




AI applications require flexible, schema-agnostic data models.&nbsp;



Serverless and instant scalability are becoming default expectations.&nbsp;



Semantic and vector search are now core to application design.&nbsp;



Cost visibility and efficiency must be designed upfront.&nbsp;




Building for what’s next




  We’re entering a new era of application development. Apps are becoming AI-native, globally distributed, and are continuously evolving.





  And success will depend on how well organizations align to these shifts.





  The most forward-thinking teams we heard from at Cosmos Conf are already doing this by:





Designing for flexibility.  



Building for speed, not just scale.  



Treating cost and performance as key concerns.  



Leveraging AI not just in apps, but in how apps are built.  





  This isn’t just a technology shift.





  It’s a shift in how we think about building software.




Explore Cosmos DB Conf on demand



If you missed Cosmos Conf 2026, you can explore all sessions on demand and hear directly from the teams building these systems in production today.




  The patterns shared this year are more than best practices, they’re a blueprint for what comes next.





	
					
							
		
		
			Start building AI apps with Azure Cosmos DB
			Design scalable, AI-native applications with a globally distributed database built for speed, flexibility, and real-time insights.
							
					
						Explore Azure Cosmos DB					
				
					
	





The post Build AI apps with Azure Cosmos DB: Key trends from Cosmos Conf 2026 appeared first on Microsoft Azure Blog.

---
*원문: [https://azure.microsoft.com/en-us/blog/build-ai-apps-with-azure-cosmos-db-key-trends-from-cosmos-conf-2026/](https://azure.microsoft.com/en-us/blog/build-ai-apps-with-azure-cosmos-db-key-trends-from-cosmos-conf-2026/)*

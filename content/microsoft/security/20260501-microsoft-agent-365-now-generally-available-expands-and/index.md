---
categories:
- MS
- 보안
date: '2026-05-01T15:00:00+00:00'
description: "Microsoft Agent 365\n\n\n\nNow generally available for commercial customers.\n\
  \n\n\n\nConnect with your Microsoft 365 expert\n\n\n\t\t\t\n\t\t\n\t\t\t\n\n\n\n\
  \n\nChoose&nbsp;an&nbsp;ecosys"
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/
source: Microsoft Security Blog
tags:
- Microsoft 365
- Microsoft Agent 365
title: Microsoft Agent 365, now generally available, expands capabilities and integrations
---

Microsoft Agent 365



Now generally available for commercial customers.




Connect with your Microsoft 365 expert


			
		
			





Choose&nbsp;an&nbsp;ecosystem&nbsp;partner&nbsp;for agent security and governance



AI agents aren’t coming—they’re already in your environment. They show up in places you expect&nbsp;(like Microsoft&nbsp;Copilot,&nbsp;Microsoft&nbsp;Teams,&nbsp;and&nbsp;Microsoft 365) and even more places as technology evolves&nbsp;(a local autonomous personal AI assistant or a new software as a service (SaaS) agent&nbsp;connected to your sensitive data.)



The&nbsp;problem&nbsp;isn’t that agents exist. It’s that they proliferate fast, span apps, endpoints and cloud, and often operate outside the&nbsp;visibility&nbsp;and control&nbsp;of the teams accountable for risk.&nbsp;When an agent can invoke tools,&nbsp;access data,&nbsp;and interact with other agents,&nbsp;any&nbsp;“helpful” workflow can turn into data&nbsp;oversharing, tool misuse,&nbsp;or over-privileged actions in seconds.&nbsp;And as agents become even easier to create and deploy, your attack&nbsp;surface grows with them.&nbsp;



That’s why end-to-end observability matters: you can’t govern what you can’t see, and you can’t secure what you don’t understand—especially when the number of agents is a moving target.&nbsp;



Microsoft Agent 365&nbsp;helps you&nbsp;take control&nbsp;of agent sprawl&nbsp;as&nbsp;your&nbsp;control plane to&nbsp;observe, govern, and&nbsp;secure agents&nbsp;and their interactions—including agents built with Microsoft AI and agents from our ecosystem partners—using the admin and security workflows your teams already run.&nbsp;




Agent 365—the control plane for agents




General availability starts today&nbsp;for Agent 365.



Additionally, we’re announcing the previews of&nbsp;new&nbsp;Agent 365&nbsp;capabilities and integrations to help you scale agent adoption with the right controls in&nbsp;place.&nbsp;




Observability, governance, and security&nbsp;for agents operating independently—Agent 365&nbsp;is expanding&nbsp;to cover agents&nbsp;that operate with their own credentials and permissions.



Discovery&nbsp;of agents and&nbsp;shadow AI,&nbsp;using&nbsp;capabilities of Microsoft Defender and Microsoft Intune&nbsp;for both local and cloud agents.



A&nbsp;secured, managed environment&nbsp;for agents to work&nbsp;in&nbsp;Windows 365&nbsp;for Agents.



Coverage for a wide ecosystem of SaaS agents,&nbsp;including&nbsp;agents innovated by&nbsp;software development companies (SDCs).



Support&nbsp;for evaluation, adoption, and usage&nbsp;from Microsoft and&nbsp;ecosystem partners worldwide.




Manage agents with a single control plane, regardless of how or where they work



As organizations move from pilot to adoption, AI agents are being deployed across increasingly diverse use cases. Some act with delegated access, working on behalf of users; others operate with their own credentials&nbsp;and permissions, participating&nbsp;in&nbsp;team workflows or&nbsp;operating behind the&nbsp;scenes.&nbsp;



With&nbsp;Agent 365,&nbsp;you&nbsp;can&nbsp;observe, govern, and secure AI agents&nbsp;whether they act on behalf of users with delegated access—for example,&nbsp;an agent that helps employees organize their inbox—or&nbsp;agents that&nbsp;operate with their own access and scope of work—such as&nbsp;an&nbsp;agent&nbsp;autonomously triaging support tickets.&nbsp;



Supported by Agent 365Agents working on behalf ofusers&nbsp;(delegated access)&nbsp;Generally available&nbsp;Agents&nbsp;operating&nbsp;behind the scenes&nbsp;(own access)&nbsp;Generally available&nbsp;Agents&nbsp;participating&nbsp;in team workflows&nbsp;(own access)&nbsp;Public Preview&nbsp;&nbsp;&nbsp;



Discover&nbsp;and manage&nbsp;local&nbsp;and cloud-hosted agents&nbsp;



Users are&nbsp;installing agents&nbsp;like&nbsp;OpenClaw and Claude Code&nbsp;on their devices and adopting SaaS agents&nbsp;built by&nbsp;developers&nbsp;on new and emerging platforms. Many of these local and cloud-hosted&nbsp;agents&nbsp;run unmanaged and outside of traditional governance,&nbsp;as they&nbsp;autonomously execute tasks, modify code, or access confidential information,&nbsp;creating a new&nbsp;wave&nbsp;of shadow&nbsp;AI.&nbsp;&nbsp;



To help organizations address accelerating&nbsp;agent sprawl and&nbsp;the rise of unmanaged agents, we’re&nbsp;introducing new&nbsp;capabilities as part of Agent 365, Microsoft Defender, and Intune so you can discover&nbsp;shadow agents, and apply appropriate controls,&nbsp;such as blocking unmanaged agents.&nbsp;



Discover and manage local agents



With Microsoft Defender&nbsp;and Intune, organizations&nbsp;will be able to&nbsp;discover and manage&nbsp;local AI agents running on&nbsp;Windows&nbsp;devices, starting with OpenClaw agents and&nbsp;expanding soon to&nbsp;other&nbsp;widely used agents like GitHub Copilot CLI and Claude Code.&nbsp;Customers enrolled in the Frontier program can see if OpenClaw agents are being used in the organization, which devices they are running on, and use Intune policies to block common ways that OpenClaw runs on the new Shadow AI page in Agent 365 in the Microsoft 365 admin center and in the Intune admin center. Through&nbsp;Agent 365 registry,&nbsp;the inventory of local agents will be available in&nbsp;Defender and Intune so IT, endpoint management, and&nbsp;security&nbsp;teams&nbsp;can&nbsp;get a&nbsp;consistent view of discovered&nbsp;local&nbsp;agents in their environment and&nbsp;take&nbsp;appropriate&nbsp;action.



			
				
			
		In the Microsoft 365 admin center,&nbsp;an&nbsp;IT&nbsp;professional can&nbsp;apply Intune policies to&nbsp;continuously detect managed devices and block the&nbsp;common&nbsp;methods of running&nbsp;OpenClaw&nbsp;on&nbsp;them.&nbsp;



Starting in June 2026, Microsoft Defender will also provide asset context mapping for each agent including the devices they run on,&nbsp;MCP servers configured for those agents, the identities associated with them, and the cloud resources those identities can reach. This will give security teams the context needed to assess exposure and potential blast radius.&nbsp;They&nbsp;can then investigate agent activity, such as file access and network behavior, using familiar endpoint data, and use those insights to identify misconfigurations and even define custom detections.



			
				
			
		Security teams can investigate local AI agent exposure in Microsoft Defender through a relationship map&nbsp;that&nbsp;shows&nbsp;where an agent runs, which MCP servers are configured for use, which identities are associated with it, and which cloud resources those identities can reach. Defender context such as resource criticality and sensitive-data exposure helps teams prioritize the agents and paths that matter most.&nbsp;



Beyond&nbsp;monitoring,&nbsp;organizations&nbsp;will be able to&nbsp;apply policy-based controls to set guardrails for what agents are allowed to do—helping&nbsp;protect&nbsp;both&nbsp;agents and organizations from compromise and&nbsp;misuse—with initial support delivered for OpenClaw through&nbsp;Intune.&nbsp;If&nbsp;a&nbsp;managed&nbsp;agent exhibits malicious behavior patterns,&nbsp;such as attempting to&nbsp;access&nbsp;or&nbsp;exfiltrate sensitive data,&nbsp;Defender&nbsp;will be able&nbsp;to&nbsp;block&nbsp;coding agents&nbsp;in&nbsp;runtime&nbsp;and&nbsp;generate&nbsp;alerts&nbsp;with&nbsp;rich&nbsp;incident context to support&nbsp;investigation and&nbsp;response.&nbsp;&nbsp;



Context mapping capabilities, policy-based controls,&nbsp;plus runtime blocking and alerts will be available&nbsp;in Agent 365 through&nbsp;Intune and&nbsp;Defender&nbsp;public preview in&nbsp;June 2026.&nbsp;



Visibility across clouds and AI-builder platforms  



As developers are rapidly building&nbsp;agents&nbsp;with Microsoft Foundry, AWS Bedrock, and&nbsp;Google&nbsp;Gemini Enterprise Agent Platform&nbsp;(formerly Google&nbsp;Vertex AI) and deploying cloud agents across multicloud and multi-platform environments, the agent sprawl challenge intensifies.&nbsp;To manage potential security risks or vulnerabilities before they become breaches, security and IT teams need visibility to&nbsp;which cloud agents are running, what models these agents are built on, and what resources they’re accessing.



Today, we are excited to announce the public preview of Agent 365 registry sync with AWS Bedrock and Google Cloud connections, enabling IT teams to automatically discover, inventory, and, soon, perform basic lifecycle governance—for example, start, stop, delete agents—across these platforms.




			
				
			
		Now in public preview,&nbsp;Microsoft 365&nbsp;admins&nbsp;can&nbsp;connect and sync&nbsp;the Agent 365 registry&nbsp;with Amazon Bedrock and Google&nbsp;Cloud&nbsp;for cross-platform observability and&nbsp;governance.&nbsp;



Manage a wide&nbsp;ecosystem&nbsp;of SaaS agents&nbsp;



Agent 365 works with&nbsp;prebuilt&nbsp;agents&nbsp;in&nbsp;Microsoft&nbsp;365 Copilot and Teams, agents built with Microsoft&nbsp;Copilot Studio or&nbsp;Microsoft&nbsp;Foundry for your organization,&nbsp;and agents built by software development companies partnered with Microsoft.



Delivering on our promise of control plane for the broad agent ecosystem, we’re excited&nbsp;to&nbsp;announce&nbsp;ecosystem partner agents&nbsp;fully configured to be managed by&nbsp;Agent 365, including Genspark, Zensai, Egnyte,&nbsp;and&nbsp;Zendesk, and agents built on agent&nbsp;factories, including Kasisto, Kore, and n8n. Organizations can observe, govern, and secure these agents&nbsp;in&nbsp;the Agent 365 control plane, with no integration work&nbsp;by&nbsp;IT or security teams.&nbsp;&nbsp;



Agent 365 software development company launch partners



			
				
			
		Agent 365 Software Development Company Launch Partners&nbsp;have built&nbsp;agents&nbsp;fully enabled to be managed by Agent 365.&nbsp;




Enterprises can easily build AI agents today, but scaling them with trust and governance is where most initiatives stall. With Kore.ai deeply integrated into Microsoft Agent 365, identity, security, and governance are built in from the start—empowering enterprises to move from pilots to AI at scale with confidence.
—–&nbsp;Raj Koneru, Chief Executive Officer of Kore.ai



The Agent 365 developer and ecosystem partners play a critical role in extending agents into line-of-business systems, building vertical and scenario-specific integrations, modernizing legacy automation into agent workflows, extending Copilot experiences with custom agents, and helping customers operationalize agent ecosystems at scale. These Agent 365 enabled agents are then observable, governable, and securable in the Agent 365 control plane, accelerating adoption for your organization.




Explore&nbsp;the&nbsp;Agent Showcase&nbsp;of ecosystem partner agents&nbsp;that work seamlessly with Agent 365.



Get started with Agent 365 development&nbsp;with guidance from Microsoft Learn.




Secure&nbsp;agents as they work&nbsp;in Windows&nbsp;365&nbsp;



While Agent 365 provides the control plane to observe, govern, and secure agent activity across the enterprise,&nbsp;Windows 365 for Agents—now available in public preview&nbsp;(in the United States only)—provides a secured, managed environment where agents can carry out that work. It introduces a new class of Cloud PCs purpose-built for agentic workloads&nbsp;and managed in Intune, allowing agents to run in policy-controlled environments, interact with applications, and operate with the same identity, security, and management controls already used for employees.



Now, with Agent 365, you can also observe and secure agents running on Windows 365 for Agents in Microsoft 365 admin center, understanding which agents are connected to the cloud-powered&nbsp;compute.&nbsp;Together, they enable organizations to move from visibility and governance of agents to confidently running them in production environments.&nbsp;




Read the blog about Windows 365 for Agents




Secure agents against&nbsp;internet&nbsp;threats with network controls&nbsp;&nbsp;



AI&nbsp;agents can&nbsp;operate&nbsp;much&nbsp;faster than&nbsp;human&nbsp;users. Without proper guardrails, they can&nbsp;connect to risky&nbsp;web&nbsp;destinations, interact with unsanctioned AI services, handle sensitive files&nbsp;unsafely, or&nbsp;be manipulated through&nbsp;malicious prompt-based&nbsp;attacks.&nbsp;These risks are harder to manage when security teams lack consistent visibility and controls for agent traffic to internet, SaaS, and AI services.&nbsp;



To&nbsp;give&nbsp;security teams a consistent way to inspect agent traffic at the network layer,&nbsp;in general availability today,&nbsp;Agent 365 extends&nbsp;Microsoft&nbsp;Entra network controls&nbsp;to Microsoft Copilot Studio agents&nbsp;and agents running on user endpoint devices,&nbsp;including&nbsp;local&nbsp;agents such as&nbsp;OpenClaw.&nbsp;These controls can help identify unsanctioned AI usage, restrict connections to&nbsp;only&nbsp;approved web destinations, filter risky file movement, and help block malicious prompt-based attacks&nbsp;before they lead to harmful actions.&nbsp;



Confidently scale and govern AI agents while maintaining security and control&nbsp;



Agent 365 extends&nbsp;even&nbsp;further beyond Microsoft platforms to&nbsp;discover, observe, govern, and secure&nbsp;local, SaaS,&nbsp;and cloud agents across&nbsp;your&nbsp;agentic AI ecosystem.&nbsp;Each&nbsp;of today’s&nbsp;announcements&nbsp;build&nbsp;upon&nbsp;Agent 365 capabilities we&nbsp;shared in March 2026&nbsp;as well as&nbsp;detailed feedback&nbsp;of customers using the Frontier program,&nbsp;developers&nbsp;integrating with the platform, and partners testing Agent 365&nbsp;capabilities.&nbsp;




With Agent 365, we can scale and govern AI agents with confidence, while maintaining enterprise grade security and control. Agent 365 enables organizations to move beyond experimentation, driving tangible business value and innovation through trusted AI adoption. By providing a robust and integrated platform, Agent 365 empowers teams to&nbsp;confidently embrace AI and accelerate transformation across the enterprise.
—Yuji Shono, Head&nbsp;of&nbsp;the Global AI Office,&nbsp;NTT&nbsp;DATA Group Corporation, a global infrastructure, networking, and IT services provider.



As organizations begin to adopt&nbsp;Agent 365&nbsp;at scale,&nbsp;we’ve collaborated with strategic partners to&nbsp;create&nbsp;targeted services&nbsp;to help customers&nbsp;onboard,&nbsp;tackle governance challenges and realize the platform’s full value.



			
				
			
		Featured&nbsp;Agent 365 launch partners, including&nbsp;Accenture,&nbsp;Bechtle, Capgemini, Insight, KPMG,&nbsp;Protiviti&nbsp;and&nbsp;Slalom,&nbsp;collaborated with&nbsp;Microsoft&nbsp;engineering teams&nbsp;to develop&nbsp;services for planning, adopting, and managing&nbsp;your agent&nbsp;control plane implementation. 



Partner services&nbsp;offered today include&nbsp;expertise&nbsp;and guidance for:&nbsp;




Inventory and ownership:&nbsp;What agents exist, who owns them, and where they run.



Least privilege:&nbsp;Right-sizing permissions and enforcing access guardrails without slowing delivery.



Compliance and data protection:&nbsp;Preventing oversharing and producing audit-ready evidence.



Threats and multi-platform estates:&nbsp;Understanding attack paths and governing across vendors and clouds.



Ongoing operations:&nbsp;Lifecycle management, monitoring, and continuous governance hygiene.&nbsp;




These&nbsp;valuable&nbsp;services&nbsp;are&nbsp;typically&nbsp;scoped&nbsp;as&nbsp;workshops and assessments (diagnose and roadmap),&nbsp;governance and enablement&nbsp;(stand up the control plane and guardrails),&nbsp;managed services&nbsp;(run and improve continuously), advisory and readiness&nbsp;(operating model and adoption readiness), and&nbsp;security and integration&nbsp;(harden posture and integrate third-party agents.)




Find a&nbsp;Microsoft&nbsp;Agent Security and Governance&nbsp;partner&nbsp;to&nbsp;assist with your Agent 365&nbsp;evaluation, deployment and adoption.&nbsp;Filter&nbsp;the directory&nbsp;by Offer: “Agent Security and Governance” and Country name.&nbsp;





Read the blog&nbsp;for Microsoft Partners




How to get started with Agent 365&nbsp;&nbsp;



Agent 365&nbsp;is&nbsp;now&nbsp;available&nbsp;in&nbsp;Microsoft 365 E7&nbsp;or&nbsp;standalone&nbsp;at&nbsp;USD15 per user per month.&nbsp;Each&nbsp;Agent 365&nbsp;license&nbsp;covers&nbsp;an&nbsp;individual who manages&nbsp;or sponsors agents, or uses&nbsp;agents to do work on their behalf, ensuring all agent activity is consistently governed across the organization&nbsp;in a way that’s predictable for&nbsp;scaled growth.&nbsp;&nbsp;




Read the blog about Microsoft 365 E7&nbsp;general availability




In addition to the&nbsp;expertise of&nbsp;your&nbsp;Microsoft 365 team&nbsp;and partners,&nbsp;Agent 365 resources&nbsp;to support your&nbsp;experience include:




The&nbsp;Agent 365 blog.



The adoption&nbsp;hub&nbsp;and&nbsp;getting started guide.



AI&nbsp;Skills Navigator&nbsp;for Agent 365.&nbsp;



Technical documentation&nbsp;on Microsoft Learn.




Plus, on Tuesday, May 12, 2026, a team of Agent 365 experts are hosting a&nbsp;live &#8220;Ask Microsoft Anything&#8221;&nbsp;to answer your questions about&nbsp;Agent 365—we hope you’ll join&nbsp;for the discussion.




	

	
		
			
				

Microsoft Agent 365



Now generally available for commercial customers.




Connect with your Microsoft 365 expert


			
		
			





Choose&nbsp;an&nbsp;ecosystem&nbsp;partner&nbsp;for agent security and governance
The post Microsoft Agent 365, now generally available, expands capabilities and integrations appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)*

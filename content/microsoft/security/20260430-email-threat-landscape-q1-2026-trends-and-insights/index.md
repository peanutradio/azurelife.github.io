---
categories:
- MS
- 보안
date: '2026-04-30T15:00:00+00:00'
description: "In this article\n\t\t\n\n\t\t\n\t\t\t\n\t\t\n\t\n\t\n\t\t\n\t\t\tTycoon2FA\
  \ disruption impactQR code phishing attacksCAPTCHA tacticsMalicious payloadsBusiness\
  \ email compromiseDefending a"
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/
source: Microsoft Security Blog
tags:
- Adversary-in-the-middle (AiTM)
- Credential theft
- Phishing
title: 'Email threat landscape: Q1 2026 trends and insights'
---

In this article
		

		
			
		
	
	
		
			Tycoon2FA disruption impactQR code phishing attacksCAPTCHA tacticsMalicious payloadsBusiness email compromiseDefending against email threatsMicrosoft Defender detections		
	
	




During the first quarter of 2026 (January-March), Microsoft Threat Intelligence detected approximately 8.3 billion email-based phishing threats, with monthly volumes declining slightly from 2.9 billion in January to 2.6 billion in March. By the end of the quarter, QR code phishing emerged as the fastest-growing attack vector, more than doubling over the period, while CAPTCHA-gated phishing evolved rapidly across payload types. Overall, 78% of email threats were link-based, while malicious payloads accounted for 19% of attacks in January—boosted by large HTML and ZIP campaigns—before settling at 13% in both February and March. Credential phishing remained the dominant objective behind malicious payloads throughout the quarter. This shift toward link-based delivery, combined with the payload trends, suggests that threat actors increasingly preferred hosted credential phishing infrastructure over locally-rendered payloads as the quarter progressed.




These trends reflect how threat actors continue to iterate on both scale and delivery techniques to improve effectiveness. At the same time, disruption efforts can meaningfully impact this activity. Following Microsoft’s Digital Crime Unit-led action against the Tycoon2FA phishing-as-a-service (PhaaS) platform in early March, associated email volume declined 15% over the remainder of the month, alongside a significant reduction in access to active phishing pages, limiting the platform’s immediate effectiveness. While Tycoon2FA has since adapted by shifting hosting providers and domain registration patterns, these changes reflect partial recovery rather than full restoration of previous capabilities. Alongside these shifts, business email compromise (BEC) activity remained prevalent, totaling approximately 10.7 million attacks in the quarter, largely driven by low-effort, generic outreach messages. At the same time, Microsoft Defender Research observed early indications of emerging techniques such as device code phishing—sometimes enabled by offerings like EvilTokens—which, while not yet at the scale of the trends discussed below, reflect continued innovation in credential theft methods.





	
		
			Tycoon2fa ecosystem 		
		
							
						Detect, investigate, and disrupt AiTM phishing							›
					
	





	
		
			AI-enabled phishing		
		
							
						Examine device code authentication attacks at scale							›
					
	




This blog provides a view of email threat activity across the first quarter of 2026, highlighting key trends in phishing techniques, payload delivery, and threat actor behavior observed by Microsoft Threat Intelligence. We examine shifts in QR code phishing, CAPTCHA evasion tactics, malicious payloads, and BEC activity, analyze how disruption efforts and infrastructure changes influenced threat actor operations, and provide recommendations and Microsoft Defender detections to help mitigate these threats. By bringing these trends together, this blog can help defenders understand how email-based attacks are evolving and where to focus detection, mitigation, and user protection strategies.



Tycoon2FA disruption impact



Since its emergence in August 2023,&nbsp;Tycoon2FA&nbsp;has rapidly become one of the most widespread PhaaS platforms, leveraging&nbsp;adversary-in-the-middle (AiTM) techniques&nbsp;to attempt to defeat non-phishing-resistant multifactor authentication (MFA) defenses. The group behind the PhaaS platform (tracked by Microsoft Threat Intelligence as&nbsp;Storm-1747) leases malicious infrastructure and sells phishing kits that impersonate various enterprise application sign-in pages and incorporate evasion tactics, such as fake CAPTCHA pages.



The quarter began with Tycoon2FA in a period of reduced activity. January volumes represented a 54% decline from December 2025, marking the second consecutive month of sharp decreases. While post-holiday seasonal effects may have contributed to this decrease in volume, some of the reduction might also have been the result of Microsoft’s Digital Crimes Unit disruption of RedVDS, a service used by many Tycoon2FA customers to distribute malicious email campaigns.




	
		
			Inside RedVDS		
		
							
						Investigate infrastructure, tooling, and attack chains							›
					
	




After surging 44% in February, phishing attacks pointing to Tycoon2FA fell 15% in March driven largely by the effects of a coordinated disruption operation. In early March 2026, Microsoft’s Digital Crimes Unit, in coordination with Europol and industry partners, took action to&nbsp;disrupt Tycoon2FA’s infrastructure and operations, significantly impairing the platform&#8217;s hosting capabilities. While Tycoon2FA-linked messages continued to circulate after the disruption, almost one-third of March&#8217;s total volume was concentrated in a three-day period early in the month; daily volumes for the remainder of March were notably lower than historical averages, and targets&#8217; ability to reach active phishing pages was substantially reduced.


Figure 1. Tycoon2FA monthly malicious messages volume (November 2025 &#8211; March 2026)



Tycoon2FA’s infrastructure composition evolved multiple times during the first three months of 2026. In January, Tycoon2FA domains started shifting toward newer generic top-level domains (TLDs) such as .DIGITAL, .BUSINESS, .CONTRACTORS, .CEO, and .COMPANY, moving away from previous commonly used TLDs or second-level domains like .SA.COM, .RU, and .ES. This trend became even more well-established in February. Following the March disruption, however, Microsoft Threat Intelligence observed a notable increase in Tycoon2FA domains with .RU registrations, with more than 41% of all Tycoon2FA domains using a .RU TLD since the last week of March.


Figure 2. Top TLDs and second-level domains (2LDs) associated with Tycoon2FA infrastructure (November 2025 &#8211; March 2026)



Additionally, toward the end of March, we saw Tycoon2FA moving away from Cloudflare as a hosting service and now hosts most of its domains across a variety of alternative platforms, suggesting the group is attempting to find replacement services that offer comparable anti-analysis protections.&nbsp;&nbsp;



QR code phishing attacks



In recent years,&nbsp;QR codes have rapidly emerged as a preferred tool&nbsp;among phishing threat actors seeking to bypass traditional email defenses. By embedding malicious URLs within image-based QR codes in the body of an email or within the contents of an attachment, threat actors attempt to exploit the limitations of text-based scanning engines and redirect victims to phishing sites on unmanaged mobile devices.



The most significant shift in Q1 2026 was the rapid escalation of QR code phishing, with attack volumes increasing from 7.6 million in January to 18.7 million in March, a 146% increase over the quarter. After an initial 35% decline in January (continuing a late-2025 downtrend), volumes reversed course dramatically, growing 59% in February and another 55% in March. By the end of the quarter, QR code phishing had reached its highest monthly volume in at least a year.


Figure 3. Trend of QR code phishing attacks by weekly volume (November 2025 &#8211; March 2026)



PDF attachments were the dominant delivery method throughout the quarter, growing from 65% of QR code attacks in January to 70% in March. While the overall volume of DOC/DOCX payloads containing malicious QR codes steadily increased each month, their share of overall delivery payloads decreased from 31% in January to 24% in March. A notable late-quarter development was the emergence of QR codes embedded directly in email bodies, which surged 336% in March. While still a small share of total volume (5%), this approach eliminates the need for an attachment altogether and highlights a shift in threat actor delivery methods that defenders should continue to monitor.



CAPTCHA tactics



Threat actors use CAPTCHA pages to delay detection and increase user interaction. These pages function as a visual decoy, giving the appearance of a legitimate security check while concealing a transition to malicious content. By forcing users to engage with the CAPTCHA before accessing the payload, threat actors reduce the likelihood of automated scanning tools identifying the threat and increase the chances of successful credential harvesting or malware delivery. Additionally, fake CAPTCHAs are used in&nbsp;ClickFix attacks&nbsp;to trick users into copying and executing malicious commands under the guise of human verification, allowing malware to bypass conventional security controls.



After declining in both January (-45%) and February (-8%), CAPTCHA-gated phishing volumes exploded in March, more than doubling (+125%) to 11.9 million attacks, the highest volume observed over the last year.


Figure 4. CAPTCHA-gated phishing volume (November 2025 &#8211; March 2026)



The most notable aspect of Q1 CAPTCHA trends was the rapid rotation of delivery methods, as threat actors appeared to actively experiment with which payload formats most effectively evade email defenses:




HTML attachments started the year as the most common method to deliver CAPTCHA-gated phishing (37% in January), but dropped 34% in February, hitting its lowest monthly volume since August 2025. Although their volume more than doubled in March, hitting an annual monthly high, HTML files were still only the second-most common delivery method to close the quarter.





SVG files, which had seen consecutive months of decreasing volumes, grew by 49% in February at the same time nearly every other delivery payload type decreased. Because of this, it was the most common delivery method for the month, which had not happened since November 2025. This one-month spike reversed itself in March, however, and the number of SVG files delivering CAPTCHA-gated phish fell by 57%, accounting for just 7% of delivery payloads.



PDF files saw a meteoric rise in volume during the first quarter of the year. After seeing steady month-over-month declines since July 2025, and hitting an annual monthly low point in January 2026, the number of PDF attachments leading to CAPTCHA-gated phishing sites more than quadrupled in March (+356%). Not only did it retake its spot as the most common delivery method for these attacks since last July, but it eclipsed its annual high by more than 37%.



DOC/DOCX files, which didn’t make up more than 9% of CAPTCHA-gated phishing payloads over the previous nine months, increased almost five times (+373%) in March to account for 15% of payloads.



Email-embedded URLs, which had once delivered more than half of CAPTCHA-gated phish at the end of August 2025, hit an eight-month low after falling 85% between December and February. While their volume nearly doubled in March, they remained well below late-2025 levels.



Figure 5. Monthly CAPTCHA-gated phishing volume by distribution method (Q1 2026)



Another notable shift in CAPTCHA-gated phishing attacks was the erosion of Tycoon2FA’s impact on the landscape. At the end of 2025, more than three-quarters of CAPTCHA-gated phishing sites were hosted on Tycoon2FA infrastructure. This share decreased significantly over the course of the first three months of 2026, falling to just 41% in March. This broadening of CAPTCHA-gated phishing sites being used by an increasing number of threat actors and phishing kits, combined with the overall surge in volume, indicates that this technique is becoming a more entrenched component of the phishing playbook rather than a specialty of a small number of tools.



Three-day campaign delivers CAPTCHA-gated phishing content using malicious SVG attachments



Between February 23 and February 25, 2026, a large, sustained campaign sent more than 1.2 million messages to users at more than 53,000 organizations in 23 countries. Messages in the campaign included a number of different themes, including an important 401K update, a credit hold warning, a question about a received payment, a payment request for a past due invoice, and a voice message notification.



Many of the messages contained a fake confidentiality disclaimer to enhance the credibility of the messages and provide a proactive excuse about why a recipient may have mistakenly received an email that may not be applicable to them.


Figure 6. Example fake confidentiality message used in February 23-25 phishing campaign



Attached to each message was an SVG file that was named to appropriately match the theme of the email. All the file names included a Base64-encoded version of the recipient’s email address. Example of file names used in the campaign include the following:




&lt;Recipient Email Domain&gt;_statements_inv_&lt;Base64-encoded Email Address&gt;.svg



401K_copy_&lt;Recipient Name&gt;_&lt;Base64-encoded Email Address&gt;_241.svg



Check_2408_Payment_Copy_&lt;Recipient First Name&gt;_&lt;Base64-encoded Email Address&gt;_241.svg



INV#_1709612175_&lt;Base64-encoded Email Address&gt;.svg



Listen_(&lt;Base64-encoded Email Address&gt;).svg



PLAY_AUDIO_MESSAGE__&lt;Recipient Name&gt;_&lt;Base64-encoded Email Address&gt;_241.svg




If an attached SVG file was opened, the user’s browser would open locally and fetch content from one of the three following hostnames:




bouleversement.niovapahrm[.]com



haematogenesis.hvishay[.]com



ubiquitarianism.drilto[.]com




Initially, the user would be shown a “security check” CAPTCHA. Once the CAPTCHA had been successfully completed, the user would then be shown a fake sign-in page used to compromise their account credentials.



Malicious payloads



Credential phishing tightened its grip on the malicious payload landscape across Q1, growing from 89% of all payload-based attacks in January to 95% in February before settling at 94% in March. These credential phishing payloads either linked users to phishing pages or locally loaded spoofed sign-in screens on a user’s device. Traditional malware delivery continued its long-term decline, representing just 5–6% of payloads by the end of the quarter.


Figure 7. Malicious payloads by file type (Q1 2026)



The most striking payload trend was the volatility across file types, driven by large campaigns that created dramatic week-to-week swings:




HTML attachments started Q1 as the leading file type (37% of payloads in January), fell to an annual low in February (-57%), then nearly tripled in March (+175%). This volatility was largely campaign-driven, with concentrated activity in the first half of January and the third week of March.



Malicious PDFs followed a steady upward trajectory, increasing 38% in February and another 50% in March to reach their highest monthly volume in over a year. By March, PDFs accounted for 29% of payloads, up from 19% in January.



ZIP/GZIP attachments were similarly volatile by nearly doubling in January (+94%), dropping 38% in February, then surging 79% in March. Threat actors commonly use ZIP files to circumvent Mark of the Web (MOTW) protections.



SVG files emerged briefly in February as a notable delivery method (with a 50% volume increase) before declining 32% in March, mirroring the pattern seen in CAPTCHA-gated phishing.



Figure 8. Daily malicious payload file type (Q1 2026)



Large-scale HTML phishing campaign hosts content on multiple PhaaS infrastructures



On March 17, 2026, Microsoft Threat Intelligence observed a massive phishing campaign that drove a significant surge in malicious HTML attachments during the month. The campaign involved more than 1.5 million confirmed malicious messages sent to over 179,000 organizations across 43 countries, accounting for approximately 7% of all malicious HTML attachments observed in March.



All messages in this campaign were likely sent using the same tool or service, which exhibited several distinct and highly consistent characteristics. Most notably, sender addresses across the campaign featured excessively long, keyword‑stuffed usernames that embedded URLs, tracking identifiers, and service references. These usernames were crafted to resemble legitimate transactional, billing, or document‑related notification senders. Examples of observed sender usernames include:




eReceipt_Payment_Alert_Noreply-/m939k6d7.r.us-west-2.awstrack.me/L0/%2F%2Fspectrumbusiness.net%2Fbilling%2F/2/010101989f2c1f29-ab5789bd-1426-4800-ae7d-877ea7f61d24-000000/LHnBIXX0VmCLVoXwNWtt23hGCdc=439/us02web.zoom.nl/j/81163775943?pwd=bLoo4JaWavsiTAuLWNoRsmbmALwjLB.1-qq8m2tzd



Center-=AAP1eU7NKykAABXNznVa8w___listenerId=AAP1eU7NKykAABXNznVa8w___aw_0_device.player_name=Chrome___aw_0_ivt.result=unknown___cbs=9901711___aw_0_azn.zposition=%5B%22undefined%22%5D___us_privacy=___aw_0_app.name=Second+Screen___externalClickUrl=otdk-takaki-h



DocExchange_Noreply-m939k6d7.r.us_west_2.awstrack.me/L0/%2F%2Fspectrumbusiness.net%2Fbilling%2F/2/010101989f2c1f29ab5789bd14264800ae7d877ea7f61d24000000/LHnBIXX0VmCLVoXwNWtt23hGCdc=439/us02web.zoom.nl/j/81163775943?pwd=bLoo4JaWavsiTAuLWNoRsmbmALwjLB.1-angie




The emails themselves contained little to no message body content. While subject lines varied, they consistently impersonated routine business and workflow notifications, including payment and remittance alerts (for example, Automated Clearing House (ACH), Electronic Funds Transfer (EFT), wire), invoice or aging statements, and e‑signature or document delivery requests. These subjects relied on urgency, approval language, and transactional framing to prompt recipients to review, sign, or access an attached document.



Each message included an HTML attachment with a file name aligned to the email’s theme. When opened, the HTML file launched locally on the recipient’s device and immediately redirected the user to an initial external staging page. This page performed basic screening and then redirected the user to a secondary landing page hosting the phishing content. On the final landing page, users were presented with a CAPTCHA challenge before being directed to a fraudulent sign‑in page designed to harvest account credentials.



Interestingly, although messages in this campaign shared common tooling, structure, and delivery characteristics, the infrastructure hosting the final phishing payload was linked to multiple different PhaaS providers. Most observed phishing endpoints were associated with Tycoon2FA, while additional activity was linked to Kratos (formerly Sneaky2FA) and EvilTokens infrastructure.



Business email compromise



Microsoft defines business email compromise (BEC) as a&nbsp;text-based attack targeting enterprise users that impersonates a trusted entity&nbsp;for the purpose of persuading a recipient into initiating a fraudulent financial transaction or sending the threat actor sensitive documents. These attacks fluctuated across Q1, totaling approximately 10.7 million attacks: rising 24% in January, dipping 8% in February, then surging 26% in March.


Figure 9. Monthly BEC attack volume (November 2025 &ndash; March 2026)



The composition of BEC attacks remained consistent throughout Q1. Generic outreach messages (like &#8220;Are you at your desk?&#8221;) accounted for 82–84% of initial contact emails each month, while explicit requests for specific financial transactions or documents represented just 9–10%. This pattern underscores that BEC operators overwhelmingly favor establishing a conversational rapport before making fraudulent requests, rather than leading with direct financial asks.



Within the smaller subset of explicit financial requests, two sub-categories showed notable movement. Payroll update requests grew 15% in February, reaching their highest volume in eight months, potentially reflecting tax season-related social engineering. Gift card requests fell 37% in February to their lowest level since July before rebounding sharply in March (+108%), though they still represented less than 3% of overall BEC messages. These fluctuations suggest that BEC operators adjust their specific financial pretexts seasonally while maintaining a consistent overall approach.


Figure 10. Initial&nbsp;BEC email content by type (Q1 2026)



Defending against email threats



Microsoft recommends the following mitigations to reduce the impact of this threat. 




Review the recommended settings&nbsp;for Exchange Online Protection and Microsoft Defender for Office 365 to ensure your organization has established essential defenses and knows how to monitor and respond to threat activity.



Invest in user awareness training and phishing simulations.&nbsp;Attack simulation training&nbsp;in Microsoft Defender for Office 365, which also includes simulating phishing messages in Microsoft Teams, is one approach to running realistic attack scenarios in your organization.



Enable Zero-hour auto purge (ZAP)&nbsp;in Defender for Office 365 to quarantine sent mail in response to newly acquired threat intelligence and retroactively neutralize malicious phishing, spam, or malware messages that have already been delivered to mailboxes.



Responders could also manually check for and purge unwanted emails containing URLs and/or Subject fields that are similar, but not identical, to those of known bad messages.&nbsp;Investigate malicious email that was delivered in Microsoft 365&nbsp;and use&nbsp;Threat Explorer&nbsp;to find and delete phishing emails.



Turn on&nbsp;Safe Links&nbsp;and&nbsp;Safe Attachments&nbsp;in Microsoft Defender for Office 365.



Enable&nbsp;network protection&nbsp;in Microsoft Defender for Endpoint.



Encourage users to use Microsoft Edge and other web browsers that support&nbsp;Microsoft Defender SmartScreen, which identifies and blocks malicious websites, including phishing sites, scam sites, and sites that host malware.



Enable password-less authentication methods (for example, Windows Hello, FIDO keys, or Microsoft&nbsp;Authenticator) for accounts that support password-less. For accounts that still require passwords, use authenticator apps like Microsoft Authenticator for MFA.&nbsp;Refer to this article&nbsp;for the different authentication methods and features.

Conditional access policies can also be scoped to&nbsp;strengthen privileged accounts with phishing resistant MFA.





Configure&nbsp;automatic attack disruption&nbsp;in Microsoft Defender XDR. Automatic attack disruption is designed to contain attacks in progress, limit the impact on an organization&#8217;s assets, and provide more time for security teams to remediate the attack fully.




Microsoft Defender detections



Microsoft Defender customers can refer to the list of applicable detections below. Microsoft Defender coordinates detection, prevention, investigation, and response across endpoints, identities, email, apps to provide integrated protection against attacks like the threat discussed in this blog.



Microsoft Defender for Endpoint



The following alert might indicate threat activity associated with this threat. The alert, however, can be triggered by unrelated threat activity.




Suspicious activity likely indicative of a connection to an adversary-in-the-middle (AiTM) phishing site




Microsoft Defender for Office 365



The following alerts might indicate threat activity associated with this threat. These alerts, however, can be triggered by unrelated threat activity.




A potentially malicious URL click was detected



A user clicked through to a potentially malicious URL



Suspicious email sending patterns detected



Email messages containing malicious URL removed after delivery



Email messages removed after delivery



Email reported by user as malware or phish




Microsoft Security Copilot



Microsoft Security Copilot is embedded in Microsoft Defender and provides security teams with AI-powered capabilities to summarize incidents, analyze files and scripts, summarize identities, use guided responses, and generate device summaries, hunting queries, and incident reports.



Customers can also deploy AI agents, including the following Microsoft Security Copilot agents, to perform security tasks efficiently:




Threat Intelligence Briefing agent



Phishing Triage agent



Threat Hunting agent



Dynamic Threat Detection agent




Security Copilot is also available as a standalone experience where customers can perform specific security-related tasks, such as incident investigation, user analysis, and vulnerability impact assessment. In addition, Security Copilot offers developer scenarios that allow customers to build, test, publish, and integrate AI agents and plugins to meet unique security needs.



Threat intelligence reports



Microsoft Defender XDR customers can use the following Threat Analytics reports in the Defender portal (requires license for at least one Defender XDR product) to get the most up-to-date information about the threat actor, malicious activity, and techniques discussed in this blog. These reports provide intelligence, protection information, and recommended actions to prevent, mitigate, or respond to associated threats found in customer environments.



Microsoft Defender XDR threat analytics




Activity Profile: Email threat landscape, March 2026



Activity Profile: Email threat landscape, February 2026



Activity Profile: Email threat landscape, January 2026



Tool Profile: Tycoon2FA



Actor Profile: Storm-1747



Technique Profile: QR code phishing



Technique Profile: ClickFix technique leverages clipboard to run malicious commands



Threat Overview Profile: Business Email Compromise



Threat Overview Profile: Adversary-in-the-middle credential phishing




Microsoft Security Copilot customers can also use the Microsoft Security Copilot integration in Microsoft Defender Threat Intelligence, either in the Security Copilot standalone portal or in the embedded experience in the Microsoft Defender portal to get more information about this threat actor.



Learn more



For the latest security research from the Microsoft Threat Intelligence community, check out the Microsoft Threat Intelligence Blog.



To get notified about new publications and to join discussions on social media, follow us on LinkedIn, X (formerly Twitter), and Bluesky.



To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the Microsoft Threat Intelligence podcast.
The post Email threat landscape: Q1 2026 trends and insights appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/](https://www.microsoft.com/en-us/security/blog/2026/04/30/email-threat-landscape-q1-2026-trends-and-insights/)*

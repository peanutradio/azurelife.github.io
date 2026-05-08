---
categories:
- MS
- 보안
date: '2026-04-29T16:00:00+00:00'
description: 'The Deputy CISO blog series is where&nbsp;Microsoft&nbsp;Deputy Chief
  Information Security Officers&nbsp;(CISOs) share their thoughts on what is most
  important '
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/04/29/8-best-practices-for-cisos-conducting-risk-reviews/
source: Microsoft Security Blog
tags: []
title: 8 best practices for CISOs conducting risk reviews
---

The Deputy CISO blog series is where&nbsp;Microsoft&nbsp;Deputy Chief Information Security Officers&nbsp;(CISOs) share their thoughts on what is most important in their respective domains. In this series, you will get practical advice, tactics to start (and stop) deploying, forward-looking commentary on where the industry is going, and more. In this blog, Rico Mariani, Deputy CISO for Microsoft Security Products, Research Infrastructure, and Engineering Systems shares some of his best practices and expertise in conducting risk reviews.



The&nbsp;nature of cyberthreats has never been static, but&nbsp;it’s&nbsp;hard to accurately convey the scale of&nbsp;their recent evolution and proliferation. As&nbsp;we’ve&nbsp;seen in many other arenas,&nbsp;AI has become&nbsp;a&nbsp;very&nbsp;powerful&nbsp;productivity tool for would-be cybercriminals. Between April&nbsp;2024 and April&nbsp;2025, Microsoft stopped&nbsp;$4 billion&nbsp;in fraud attempts.1&nbsp;And as of the&nbsp;writing of&nbsp;the&nbsp;Microsoft Digital Defense Report 2025, we&nbsp;are tracking&nbsp;100&nbsp;trillion security signals each day&nbsp;(a 40% increase since&nbsp;2023).2




Explore the Microsoft Secure Future Initiative




This is why I&nbsp;decided to&nbsp;write a blog&nbsp;about risk reviews. By asking the right questions, risk reviews help us transform the utility of our security data from primarily reactive remediation and response information into key insights helping to inform our proactive security stances. And embracing strong proactive security is something we can all do to mitigate our increased exposure to security threats.&nbsp;&nbsp;



Risk reviews are also a topic I’ve lent focus to during my first six months as Deputy CISO for Microsoft Security. It’s a very interesting role for me, as I’ve traditionally described myself as performance specialist and a systems specialist more than a security specialist. It’s not necessarily a distinction of skill set, but more one of mindset, and what I’d like to share with you is actually a bit of a synthesis of my inherent performance- and systems-first way of thinking and things I’ve brought into that practice after working with many of the other Microsoft Deputy CISOs over the last few months.



There are roughly eight points I want to bring up concerning risk reviews in this blog. Each point has the potential to help expose potential security vulnerabilities when brought up with security teams. Together, they represent a structured and approachable way to initiate necessary conversations and drive meaningful results:




Assets



Applications&nbsp;



Authentication&nbsp;



Authorization&nbsp;



Network isolation&nbsp;



Detections&nbsp;



Auditing&nbsp;



Things not to&nbsp;miss&nbsp;




Now, why did I choose to highlight these areas and not others? Generally, I find that looking at problems from the lens of risk management gives me a fresh perspective. When you very consistently ask specific questions around these areas, they often effectively start the conversation you want to have.



Just one last thing before we dive in: What I’m about to tell you is only approximately correct. There will be edge cases and exceptions, but generally I think you’ll find this information helpful.



1. Assets



The best place to start a review is identifying the assets that you need to protect. This will largely define the scope of the review. A good place to find those assets is, of course, on your architecture diagrams and your threat models. The assets we’re talking about could be storage (where perhaps you’re storing sensitive or otherwise important data) or they could be highly-privileged applications like command-and-control systems or something similar. This is, in short, the list of things that your cyberattacker wants to get to. 



2. Applications



In the next step, you identify your applications. These are, broadly speaking, the active part of your system. They are the outward-facing surfaces that customers will use and the set of microservices that support your interface. These systems could be providing any set of services that you might need—and herein lies the problem. It’s entirely normal for your applications to require access to your most important assets, but that means the applications themselves can become viable targets for a cyberattacker. So how do we make this situation better? At this point, it’s reasonable to start talking about possible controls. 



Read up on&nbsp;Zero Trust for&nbsp;source&nbsp;code&nbsp;access.



3. Good&nbsp;quality&nbsp;authentication 



The next thing you will want to inspect is the form of authentication that your system is using. The best systems are using tokens for authentication, and they are getting these tokens from standard token issuers like, for instance, Microsoft Entra. It’s sometimes viable to have your own token generation system, but remember that such systems tend to have bugs. Those bugs can be exploitable. And even lacking bugs, there could be, say, gaps or vulnerabilities in your token issuing system such that perhaps the tokens cannot be properly scoped. The tokens could also tend to be too long-lived, or difficult to be made fine-grained enough, or lack the capacity to allow for flowing user context from the request to the authorization system. Many such deficiencies are possible. 




Explore Microsoft Entra solutions




Even with a good quality token issuing system, you can easily find yourself in a situation where the tokens that you’re creating are too fungible, or too powerful, or both. Thinking back to the assets you’re trying to protect and the applications that you have, you can likely categorize some of the applications as having more “power,” if you will, than others. Sometimes we call these &#8220;highly privileged applications” because they have the capability to do something that is especially of interest to cyberattackers, like reading a lot of data, changing configuration, or anything like that. 



To best manage the privileges associated with these applications, it needs to be the case that the kinds of tokens that they use are as limited as possible. So, a particular token might authorize a capability for a certain customer, on behalf of a certain user, for a certain set of data—and nothing more than that. When privileges are very generic, like “I can do this operation for anyone, anywhere,” things become much more dangerous. So, here the idea is to make sure that the tokens that you’re getting are very specific to the intent that you have and that only the applications that need those tokens can get them, and, again, the tokens are as limited as possible. This goes a long way in reducing the possible damage that a cyberattacker could do if they found such a token errantly stored somewhere. 



A lot of the things we think about when we’re working with tokens and trying to limit them fall into the category of limiting what a&nbsp;cyberattacker&nbsp;can do if they get a foothold somewhere. This is the&nbsp;Zero Trust&nbsp;model,&nbsp;where you assume breach everywhere. &nbsp;




Strengthen security with a Zero Trust strategy




Additionally, it’s essential to use standard libraries to accurately authenticate with tokens, so that all the aspects and limitations of the token are certain to be honored. 



Learn&nbsp;about&nbsp;phishing-resistant multifactor authentication&nbsp;from the Microsoft Secure Future Initiative (SFI).&nbsp;



4. Good&nbsp;quality&nbsp;authorization &nbsp;



Good quality tokens are not going to help you if they’re enforced poorly (or not at all). And bugs can creep into code. Ad hoc authorization code can render the good authentication that you’ve done moot. 



Any time you can use declarative style patterns that help you verify tokens against incoming APIs and the data that the client is attempting to access with your API, you’ll find yourself in a better place. Simple, consistent authorization yields fewer bugs and therefore less risk. 



5. Network&nbsp;isolation 



In addition to having good quality tokens, it’s important to isolate the pieces of your environment to the maximum extent possible. Again, this is done because it’s prudent to assume that a cyberattacker has a foothold somewhere in your network. The questions are “where exactly can that foothold be,” and “once they have that foothold, where in my network can they get to?” If a threat actor can reach any part of your system from any other part of your system, this is obviously less good than if your most sensitive systems can be accessed from exactly one or two key places and nowhere else. When properly controlled, most footholds become useless to a cyberattacker—or at least only indirectly useful.  



Use&nbsp;service tags&nbsp;to create boundaries around your various assets such that applications are used by exactly those systems that are supposed to be using&nbsp;them&nbsp;and data is accessed by exactly those applications that are supposed to be accessing the data. This goes a long way to take many cyberthreats off the table. &nbsp;



Network isolation can happen at several levels in the network stack. Popularly, level 7 is used at the perimeter. Maybe this manifests as some kind of HTTP proxy, for example, or an HTTP routing gateway. However, protection is incomplete without additional work happening at level 3 within your network. You want to limit IP traffic to be going to exactly the places that you want it to go. You might use techniques like virtual LANs, or similar constructs like network security groups (NSGs) in Microsoft Azure. The idea is to limit connectivity to exactly what is necessary to do the job and not give the cyberattacker freedom to move around. 



With good network isolation comes the ability to log any&nbsp;attempts to gain access at the perimeter,&nbsp;and potentially even internally. Depending on what networking technology&nbsp;you’re&nbsp;using, all of this is great for hunting.&nbsp;We’ll&nbsp;talk about that in the next section. &nbsp;



Learn more about&nbsp;network isolation and other best practices from SFI.



6. Detections &nbsp;



It’s normal to think about&nbsp;monitoring for&nbsp;reliability. Systems need to stay within their operating parameters in the face of changes and external conditions. But it’s also important to think about detection from the perspective of your threat model. If you identify five or ten risks in your threat model that need controls, it’s useful to think about how you might detect if any of those things are actually happening in your environment. &nbsp;



In this context, one place to look is at the perimeter—by&nbsp;examining your incoming HTTP traffic, for instance. But you can also look anywhere in your environment where you&nbsp;predict&nbsp;that attacks might happen. You might look for badly formatted requests, or fuzzing, or evidence of DDoS attack—whatever is appropriate to the risks you have. The idea is that you want to be able to create alerts if you have evidence of a&nbsp;threat&nbsp;actor operating in your estate. &nbsp;



And, of course, security products can be very helpful here. &nbsp;



7. Auditing



We separate the notions of auditing from detection. Specifically, auditing is what I will call the pieces of data that you would use after a breach to determine the extent of the breach and the customers that were affected by it. In the event that you find a vulnerability without any evidence of threat actor exploitation, you’d want to go and check your auditing again to verify those claims. That way you can have evidence that whatever problem you found was not in fact exploited. If it was exploited, you’ll know to what extent, who was affected, and who needs to be notified. 



Some parts of your endpoint detection and response (EDR) stream will be very useful for auditing. Additional auditing information can come from the logs you create in your applications that record suitable information concerning recent activity. 



8. Things not to&nbsp;miss 



It’s important to think about all the applications and data that you have in your estate. For instance, it’s easy to overlook the backup data that you have stored. A cyberattacker might not be able to get access to your primary systems but might find that your backups are entirely unprotected and they can just read the backup.



Similarly, support systems often go overlooked. There are frequently important customer support scenarios that require access, and it’s easy to fall into the trap of not giving those systems the highest level of scrutiny. 



We should add systems that are under development and test systems to this problematic set. In both these cases, the code that’s running those systems is less trustworthy than normal production code. Development code, for instance, can be presumed to have more bugs than production code. Some of those bugs might be authorization bugs. And if there are authorization bugs, that buggy code might provide access to important assets. Therefore, your plans should include even greater scrutiny when it comes to these kinds of systems. 



Explore&nbsp;actionable patterns and practices from SFI.&nbsp;



In summary



If you&#8217;ve gotten as far as identifying all of your assets, all your applications, and then thinking about the access patterns and controls that you have between them—including authentication, authorization, network isolation, and the use of bug-resistant patterns—you&#8217;re in a pretty good place to write a risk summary that can guide your actions for many months. And we haven&#8217;t even touched on basic things like vulnerability management, security, bug management, and the usual software lifecycle things that are necessary to keep the system in good health. Combine all of the above and you should have a good-looking risk plan. 




	

	
		
			
				

MicrosoftDeputy CISOs



To hear more from Microsoft Deputy CISOs, check out the&nbsp;OCISO blog series:







To stay on top of important security industry updates, explore resources specifically designed for CISOs, and learn best practices for improving your organization’s security posture, join the&nbsp;Microsoft CISO Digest distribution list.

			
		
					
				
																				
			
			





To learn more about Microsoft Security solutions, visit our website. Bookmark the Security blog to keep up with our expert coverage on security matters. Also, follow us on LinkedIn (Microsoft Security) and&nbsp;X&nbsp;(@MSFTSecurity) for the latest news and updates on cybersecurity.&nbsp;







1Microsoft Cyber Signals Issue 9.&nbsp;



2Microsoft Digital Defense Report 2024.
The post 8 best practices for CISOs conducting risk reviews appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/04/29/8-best-practices-for-cisos-conducting-risk-reviews/](https://www.microsoft.com/en-us/security/blog/2026/04/29/8-best-practices-for-cisos-conducting-risk-reviews/)*

---
categories:
- MS
- 보안
date: '2026-05-07T16:00:00+00:00'
description: 'World Passkey Day is a chance to reflect on progress toward a shared
  goal: reducing our reliance on passwords and other phishable authentication methods
  by acce'
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/05/07/world-passkey-day-advancing-passwordless-authentication/
source: Microsoft Security Blog
tags: []
title: 'World Passkey Day: Advancing passwordless authentication'
---

World Passkey Day is a chance to reflect on progress toward a shared goal: reducing our reliance on passwords and other phishable authentication methods by accelerating passkey adoption. As cyberattacks become more automated and AI-powered, each account is only as secure as its weakest credential. Real progress requires more than adding stronger sign-in options—it requires removing phishable credentials and strengthening common attack paths like recovery flows. In partnership with the FIDO Alliance, Microsoft is committed to advancing passkey adoption through ongoing standards work, active participation in working groups, and other contributions to a passwordless future.




Explore Microsoft Entra identity and access solutions




Passwords remain a major source of risk; they’re difficult to manage and easy to steal. Along with weaker forms of multifactor authentication, they’re also highly vulnerable to phishing: AI-powered campaigns drive click-through rates as high as 54%.1 In response, Microsoft is expanding passkey adoption across our ecosystem. We’re reducing reliance on legacy authentication and strengthening account recovery so it won’t become a backdoor for cyberattackers.



&#8220;Instead of vulnerable secrets or potentially identifiable personal information, a passkey uses a private key stored safely on the user’s device. It only works on the website or app for which the user created it, and only if that same user unlocks it with their biometrics or PIN. This means passkey users can’t be tricked into signing in to a malicious lookalike website, and a passkey is unusable unless the user is present and consenting. These are some qualities that make passkeys a &#8216;phishing-resistant&#8217; form of authentication.&#8221;From Microsoft Digital Defense Report.



Passkey adoption continues to grow industry wide



Passkey adoption is accelerating: FIDO Alliance estimates 5 billion passkeys already in use worldwide.2 Across Microsoft’s consumer services, including OneDrive, Xbox, and Copilot, hundreds of millions of users sign in with passkeys every day.



There are many reasons to choose passkeys as the standard authentication method over passwords. Sign-in success rates are significantly higher than with passwords, and exposure to credential-based attacks is significantly lower.3 Organizations and individual users alike prefer the simpler, more secure sign-in experience passkeys offer.4



Inside Microsoft, we’ve eliminated weaker authentication methods and rolled out phishing-resistant authentication, covering 99.6% of users and devices in our environment.5 It’s made signing in a lot simpler: no codes to enter, no extra prompts to manage, just a straightforward experience for everyone.



Product updates across sign-in and recovery



Across Microsoft, we’ve been steadily building passkey support into every layer of the identity experience from consumer accounts to enterprise access with Microsoft Entra, and from device-based authentication like Windows Hello to Microsoft’s password manager. This work ensures people can create and use passkeys wherever they sign in, with a consistent, phishing-resistant experience across devices, apps, and environments.



To make passkeys more accessible, we’re expanding where and how people can use them:




Synced passkeys and passkey profiles in Microsoft Entra ID make it easier to scale passwordless sign-in across diverse environments. We’re expanding flexibility in cloud passkey management, including support for larger and more complex policies, and transitioning tenants to a unified passkey profile model. 



Entra passkeys on Windows make it simple for users to create and use device-bound passkeys directly on personal or unmanaged Windows devices using Windows Hello, and will be generally available in late May 2026.



Passkeys for Microsoft Entra External ID will be generally available late May 2026, so your customer-facing applications can offer a more seamless, consumer-grade sign-in experience.



Passkey-preferred authentication in Microsoft Entra ID&nbsp;(preview)&nbsp;detects registered methods and prompts the strongest one first. If a passkey is registered,&nbsp;that&#8217;s&nbsp;what the user sees—immediately.&nbsp;



On the consumer side, with Microsoft Password Manager, users can now save and sync passkeys&nbsp;across devices signed in with their Microsoft account, with support for iOS and Android rolling out soon through Microsoft Edge.&nbsp;




Account recovery also plays a critical role in maintaining the integrity of identity systems. Historically, it’s been vulnerable to cyberattackers who try to hijack the recovery process, for example by impersonating legitimate users and requesting new credentials. 



Microsoft Entra ID account recovery, generally available today, strengthens security for recovery flows by enabling users to regain access to their accounts through a robust identity verification process. Users can regain access after losing all authentication methods by using government-issued ID and biometric face checks. At general availability, we are expanding our identity verification ecosystem with two new partners—1Kosmos and CLEAR1—joining our existing partners Au10tix, IDEMIA, and TrueCredential. 



Removing phishable credentials from user accounts



Strengthening authentication is important, but reducing risk means eliminating phishable credentials entirely. Microsoft is continuing to phase out legacy methods and move users toward phishing-resistant authentication. Starting in January 2027, security questions will be removed as a password reset option in Microsoft Entra ID due to their susceptibility to guessing and social engineering.



The rationale is straightforward: improving strong methods while removing weak ones shrinks the attack surface. This is increasingly urgent as AI agents act on behalf of users. If an identity is compromised, cyberattackers can leverage those agents to access systems, execute workflows, and operate within existing permissions. Organizations need to address this risk quickly.



A more secure and usable future



Last year, Microsoft joined dozens of organizations in taking the Passkey Pledge, a commitment to accelerating the adoption of phishing-resistant authentication and to moving beyond passwords. Since then, we’ve seen meaningful progress, from hundreds of millions of better-protected consumer accounts to large-scale deployments across organizations like our own.



What once felt like a long-term shift is finally gaining real momentum: authentication is becoming simpler, safer, and passwordless.



For a more in-depth perspective on how cyberattackers try to bypass authentication through fallback methods and recovery flows—and how to address those gaps—read our companion post.



Getting started



Organizations that want to strengthen their identity security posture can enable passkeys for their users and extend policy protections across both sign-in and recovery scenarios.



Get started with a phishing-resistant passwordless authentication deployment in Microsoft Entra ID.



Individuals can create and use passkeys for their personal accounts for better security and convenience. 




Learn more about Microsoft Entra 




To learn more about Microsoft Security solutions, visit our&nbsp;website.&nbsp;Bookmark the&nbsp;Security blog&nbsp;to keep up with our expert coverage on security matters. Also, follow us on LinkedIn (Microsoft Security) and&nbsp;X&nbsp;(@MSFTSecurity)&nbsp;for the latest news and updates on cybersecurity.







1Microsoft Digital Defense Report 2025.



2FIDO Alliance reports mainstream global usage on World Passkey Day. FIDO Alliance, 2026.



3Synced passkeys and high assurance account recovery, Microsoft Entra blog. December 16, 2025.



4FIDO Alliance Champions Widespread Passkey Adoption and a Passwordless Future on World Passkey Day 2025, FIDO News Center. May 1, 2025.



5Microsoft Security and Future Initiative (SFI) Progress Report—November 2025.
The post World Passkey Day: Advancing passwordless authentication appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/05/07/world-passkey-day-advancing-passwordless-authentication/](https://www.microsoft.com/en-us/security/blog/2026/05/07/world-passkey-day-advancing-passwordless-authentication/)*

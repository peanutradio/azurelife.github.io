---
categories:
- MS
- GitHub
date: '2026-05-08T16:30:00+00:00'
description: Policymakers around the world are advancing age assurance proposals to
  protect children and teens online. Some approaches restrict minors&rsquo; access
  to certa
draft: false
original_url: https://github.blog/news-insights/policy-news-and-insights/why-age-assurance-laws-matter-for-developers/
source: GitHub Blog
tags:
- News & insights
- Policy
- maintainers
- open source
- policy
title: Why age assurance laws matter for developers
---

Policymakers around the world are advancing age assurance proposals to protect children and teens online. Some approaches restrict minors&rsquo; access to certain services or content, while others would require devices, operating systems, or app stores to collect age information and pass age signals to apps and websites. These proposals are driven by serious concerns, but without appropriate scoping, they risk imposing burdensome requirements on open source software and developer infrastructure services that do not present the same risks to minors as consumer-facing platforms. In this blog post, we&rsquo;ll provide an overview of what developers should know and how to engage.



The harms these laws aim to address are serious and deserve attention. Grooming for sexual purposes, exposure to violent content, and online bullying are just some of the risks young people are facing online. At the same time, participation in online communities, including open source software development, can be an important part of a young person&rsquo;s education and social life. When trying to strike a balance between freedom and protection, policymakers are not always aware of how their proposals could affect developers or how the open source ecosystem operates.



&ldquo;Age assurance&rdquo; refers to a range of approaches used to determine or estimate a user&rsquo;s age. It is sometimes used interchangeably with &ldquo;age verification,&rdquo; which typically refers to higher-confidence methods like photo ID matching or checks against financial or identity systems. Age assurance also includes self-attestation (where users report their age) and age estimation (where age is inferred from signals, facial scanning, or behavior). These approaches span a wide spectrum, with ongoing debate about tradeoffs between accuracy, privacy, security, interoperability, and accessibility. Proposals also vary in what age thresholds trigger restrictions, the services or content covered, how parental consent should factor in, and how access is limited. While we do not discuss each approach in detail here, we encourage readers to engage with the legislation, consider different technical and policy perspectives, and think about how to protect young people online while preserving access to the knowledge, learning opportunities, and creative potential the internet enables&mdash;including opportunities to learn to code and participate in the global open source ecosystem.



A poorly designed age assurance law could have significant unintended impacts for open source projects. For example, requirements that operating systems centrally collect and manage user data, or that restrict users from installing software outside of centralized app stores, would conflict with the decentralized, user-controlled norms of the open source ecosystem.



Another potential pitfall is placing age assurance requirements on &ldquo;publishers&rdquo; of operating systems, regardless of whether they are individuals or companies. Open source operating systems are frequently iterated on, reused, and redistributed by individual contributors and small communities, many of which have limited resources and small user bases. The diversity of the software ecosystem is worth preserving.



GitHub has engaged with governments on age&#8209;related online safety proposals for several years. In some cases, including Australia&rsquo;s Social Media Minimum Age legislation, we worked with policymakers to explain why open source code collaboration platforms should not be in scope. Similar exemptions appear elsewhere. France&rsquo;s current Social Media Minimum Age proposal, for example, includes the same exclusions for open source code collaboration sites and online encyclopedias that appear in the EU Copyright Directive.



Many policymakers recognize that access to the open source software development ecosystem delivers significant public benefits, including education, innovation, and security, and that the risks young people face from participating in open source development communities are materially different by comparison. At the same time, a growing number of laws are seeking to advance child safety goals at varying levels of the tech stack, including through operating systems and application distribution layers. This has raised new questions for developers about how these requirements apply in practice, and whether open source operating systems and developer infrastructure like GitHub could be impacted.



Legislation&nbsp;to&nbsp;know&nbsp;




California AB 1043 Digital Age Assurance Act and 2026 amending bill AB 1856: Requires operating system providers (in coordination with covered app stores) to collect self&#8209;declared age at account setup and transmit an age&#8209;range signal to applications via a real&#8209;time API.



Colorado SB 26-051 Age Attestation on Computing Devices: Requires operating systems and covered app stores to generate and share an age&#8209;bracket signal with applications via a real&#8209;time interface, with evolving definitions of &ldquo;covered application&rdquo; and &ldquo;covered application store&rdquo; shaping scope.



Illinois HB 4140 Digital Age Assurance Act: Applies to operating system providers and requires collection of age data and transmission of an age&#8209;category signal to developers via a real&#8209;time API, closely mirroring California&rsquo;s model.



New York S 8102/A 8893 Device&#8209;Level Age Assurance: Applies broadly to device manufacturers, operating systems, and app stores, requiring &ldquo;commercially reasonable&rdquo; age assurance (not just self&#8209;reporting) at device activation and transmission of a verified age signal to apps and websites.




This is just a selection&nbsp;of operating system and app store age assurance legislation in the United States.&nbsp;There have also been related but distinct laws&nbsp;focused on app stores&nbsp;passed in&nbsp;Texas (SB 2420),&nbsp;Louisiana (HB&nbsp;570),&nbsp;and&nbsp;Utah (SB 142).



These proposals are actively evolving. In Colorado, SB 26&#8209;051 recently had a committee hearing on April 23, 2026, as part of ongoing legislative consideration. The hearing reflected the complexity of balancing child safety, privacy, and feasibility, and included strong engagement from open source developers and organizations. Committee members also signaled that the intent is not to bring open source operating systems or developer infrastructure into scope, and the latest amended text clarified that software installed outside of app stores, including software downloaded from public repositories, is not in scope.



In Brazil, the Digital Statute for Children and Adolescents (Digital ECA), enforceable as of March 2026, applies broadly to digital services &ldquo;likely to be accessed by children and adolescents&rdquo; including operating systems, app stores, and platforms, and excludes essential internet functionalities such as open technical protocols and standards. Although the Brazilian National Data Protection Agency (ANPD) has not yet formally clarified whether or how the law applies to free and open source software, its regulatory agenda has initially prioritized &ldquo;app stores and proprietary operating systems,&rdquo; and recent draft guidance under public consultation indicates that systems based on collaborative models and free software should not be subject to the same obligations as proprietary services.



Despite this, legal uncertainty has already driven some open source projects to restrict access in Brazil, reflecting concerns about the feasibility of compliance for non-commercial, volunteer-driven ecosystems. While the law was primarily designed for commercial actors, key questions about scope remain unresolved, making it critical for open source developers to actively participate in the ongoing public consultation to ensure implementation reflects decentralized development models and avoids unintended restrictions on access and innovation.



What is an app store, really?



While much of the open source community&rsquo;s concern has focused on the risk that these proposals could present to open source operating systems, an equally important open question is how &ldquo;application store&rdquo; and &ldquo;application&rdquo; are defined. As drafted, some definitions of &ldquo;application store&rdquo; are broad enough to capture developer infrastructure&mdash;such as code collaboration platforms, package managers, and open source indexing services&mdash;simply because they allow users to access or download software.



Making software available for download is not the same as operating the kind of centralized, consumer-facing marketplace that most people would understand to be an app store. It is also important to define &ldquo;application&rdquo; precisely. Downloading software components like source code, libraries, frameworks, models, and utilities is fundamentally different from offering a standalone executable application through a consumer app marketplace. These components are upstream building blocks, not end&#8209;user products, and the services that host or index them do not control consumer distribution or presentation in the way traditional app stores do.



Recent amendments and discussions across jurisdictions suggest regulators intend to focus on consumer&#8209;facing distribution and services that control end&#8209;user access. Clear statutory distinctions are needed to ensure laws align with that intent. This reflects a familiar challenge in technology policymaking. Frameworks aimed at youth safety and age assurance are typically responding to risks associated with consumer-facing services that collect and monetize user data, distribute content at scale, and rely on engagement-driven systems to shape user behavior.



By contrast, platforms that support collaborative software development serve a fundamentally different function&mdash;they are built to help users create, share, and maintain code, not to attract mass audiences, amplify content, or drive passive or excessive consumption&mdash;resulting in a materially lower risk profile. Open source communities operating on services like GitHub are organized around shared technical goals and guided by norms of collaboration, reuse, and transparency, further underscoring why these developer-focused services should be distinguished from consumer-facing platforms in regulatory design.



Open source software is also a key driver of economic development and innovation and functions as critical digital infrastructure. Ensuring that policies accurately reflect how open source is built and maintained is essential to preserving these benefits. When policymakers engage directly with open source developers and civil society, they are often able to refine definitions, clarify scope, and better align laws with technical realities.



Uncertainty around compliance requirements can be challenging for open source developers, many of whom contribute on a voluntary basis. At the same time, there are positive examples of policymakers engaging with the open source community to strike a balanced approach. The EU Cyber Resilience Act, for example, was refined through an iterative process to get the balance right for open source. Across U.S. states, these bills continue to evolve and policymakers have shown a willingness to engage with the open source community and consider changes to align with regulatory intent and technical feasibility.



An opportunity for engagement&nbsp;



The window for constructive engagement remains open&mdash;and developer voices can make a meaningful difference.



Whether through contacting elected representatives in states considering these proposals like California, Colorado, Illinois, and New York, contributing to Brazil&rsquo;s Digital ECA public consultation, or engaging with organizations like the Open Source Initiative, or through foundations that steward projects that may be impacted like the FreeBSD Foundation and Debian, there are concrete ways for developers to share their perspectives&mdash;helping ensure these policies both support children&rsquo;s digital safety and reflect technical realities, align with regulatory intent, and avoid unintended harm to the open source ecosystem.



GitHub will continue working with policymakers and the open source community to support balanced approaches that protect young people while preserving open development. We encourage developers to stay informed, connect with open source policy organizations, and reach out to us with questions or concerns. We&rsquo;ll also continue this conversation with a Maintainer Month livestream on May 22 with panelists from the FreeBSD Foundation and the Open Source Initiative to discuss the broader issues raised by these proposals and how technology policy can be designed with open source in mind.

The post Why age assurance laws matter for developers appeared first on The GitHub Blog.

---
*원문: [https://github.blog/news-insights/policy-news-and-insights/why-age-assurance-laws-matter-for-developers/](https://github.blog/news-insights/policy-news-and-insights/why-age-assurance-laws-matter-for-developers/)*

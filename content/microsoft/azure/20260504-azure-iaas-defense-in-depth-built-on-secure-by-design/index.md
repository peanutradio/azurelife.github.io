---
categories:
- MS
- Azure
date: '2026-05-04T16:00:00+00:00'
description: "In this article\n\t\t\n\n\t\t\n\t\t\t\n\t\t\n\t\n\t\n\t\t\n\t\t\tDefense\
  \ in depth as a systemSecure by design: Engineering security into the platformHardware\
  \ and host-level trustVirtual"
draft: false
original_url: https://azure.microsoft.com/en-us/blog/azure-iaas-defense-in-depth-built-on-secure-by-design-principles/
source: Azure Blog
tags:
- Compute
- DevOps
- Hybrid + multicloud
- Identity
- Management and governance
- Networking
- Security
- Azure Built-In Security
- Azure IaaS
- Zero Trust
title: 'Azure IaaS: Defense in depth built on secure-by-design principles'
---

In this article
		

		
			
		
	
	
		
			Defense in depth as a systemSecure by design: Engineering security into the platformHardware and host-level trustVirtual machine-layer trustSecure by default: Protection enabled without frictionSecure defaults across networkingEncryption and data protection by defaultCompute protection defaultsSecure in operation: Continuous protection at runtimeMonitoring, detection, and signal correlationIdentity-centric control and least privilegeBringing defense in depth and SFI together Security as an ongoing platform commitment		
	
	




This blog post is the third part of a blog series called Azure IaaS which will share best practices and guidance to help you build a trusted infrastructure platform—from performance, resiliency, and security to scalability and cost efficiency.



​Security for cloud infrastructure is no longer defined by a single control, product, or boundary. Modern threats target identity, software supply chains, control planes, networks, and data simultaneously. Addressing this reality requires two things to work together: a layered defense-in-depth architecture and security principles that are enforced consistently across the platform.



In Azure Infrastructure as a Service (IaaS), security is built around these two reinforcing ideas. First, Azure implements defense in depth, applying multiple, independent layers of protection across compute, networking, storage, and operations so that no single control stands alone. Second, those protections are guided by Microsoft’s  Secure Future Initiative (SFI) principles: secure by design, secure by default, and secure in operation. Together, they define how Azure IaaS is engineered, configured, and operated at scale.




Explore Azure IaaS solutions




Defense in depth as a system



Defense in depth is not a checklist of features—it is a system-level security architecture. Each layer is designed with the assumption that another layer may fail, and that compromise at one point should not lead to platform-wide impact.



In Azure IaaS, defense in depth spans the full infrastructure stack:




Hardware and host integrity



Virtualized compute isolation



Network segmentation and traffic control



Data protection for storage



Continuous monitoring and response




These layers are intentionally independent. Hardware root-of-trust mechanisms validate host integrity before workloads ever start. Virtual machines (VM) run with strong isolation boundaries enforced by the hypervisor. Network controls limit lateral movement and restrict exposure. Storage services encrypt and protect data even if credentials are compromised. And telemetry and monitoring systems operate continuously, detecting and responding to anomalous behavior across the platform.



This layered approach ensures that Azure IaaS security does not rely on perimeter assumptions or a single “control plane defense,” but instead applies multiple mutually reinforcing controls that work together.




Build a stronger cloud infrastructure with Azure IaaS




Secure by design: Engineering security into the platform



“Secure by design” means security is architected into the platform from the beginning, not added after deployment. In Azure IaaS, this starts at the lowest layers of the stack.



Hardware and host-level trust



Azure servers are built with hardware roots of trust, measured boot, and secure firmware validation. Technologies such as Trusted Platform Modules (TPMs) and secure boot validate that host firmware, boot loaders, and operating systems have not been tampered with before the system joins the Azure fleet. These mechanisms reduce exposure to firmware-level and boot-chain attacks that traditional software-only defenses cannot address.



Azure also offloads critical infrastructure functions—such as storage, networking, and management operations—into dedicated, hardened components like Azure Boost, reducing the attack surface of the host operating system and improving isolation between customer workloads and platform services.



Virtual machine-layer trust



At the virtual machine layer, Azure enforces strong virtualization boundaries using a hardened hypervisor. Features like Trusted Launch for Azure VM combine secure boot, virtual TPMs, and integrity monitoring to protect VMs against low-level attacks such as bootkits and kernel rootkits.



For highly sensitive workloads,  Azure confidential computing extends defense in depth by using trusted execution environments (TEEs) backed by hardware-based memory encryption (such as AMD SEV‑SNP or Intel TDX). These technologies help ensure that data remains protected even while in use and inaccessible to the host or hypervisor.



Security here is not a bolt-on—it is a design property of how Azure compute infrastructure is built and operated.



Secure by default: Protection enabled without friction



Secure-by-default controls reduce risk by making the safest option the standard configuration, without requiring customers to assemble security from scratch.




Learn how to keep critical applications running with built-in resiliency at scale with Azure IaaS




Secure defaults across networking



In Azure IaaS, networking defaults are aligned with least-privilege and Zero Trust principles. Virtual networks are isolated by default. Inbound traffic to VM is blocked unless explicitly allowed. Network security groups (NSGs) enforce stateful filtering, while Azure Firewall provides centralized policy enforcement and traffic inspection when deployed.



Private connectivity options such as Azure Private Link and private endpoints allow services to be accessed without exposing them to the public internet. DDoS protection is automatically applied at the platform edge, helping protect workloads from volumetric attacks without additional configuration.



These defaults limit exposure by design, narrowing the attack surface before workload-specific rules are added.



Encryption and data protection by default



Azure IaaS storage services encrypt data at rest by default, using platform-managed keys, with options to use customer-managed keys via Azure Key Vault or Managed HSM. Disk encryption protects operating system and data disks for VM, and secure snapshots protect point-in-time copies of data.



Encryption in transit is enforced across Azure backbone networks, ensuring traffic between services within the platform is protected without requiring per-workload configuration.



Secure-by-default encryption ensures that data protections are always on, not optional.



Compute protection defaults



Signed and measured Azure host boot, secure host operating system (OS) hardening, host‑level monitoring and patching by Microsoft, and hypervisor-enforced isolation between tenants are all enabled by default and cannot be disabled by Azure tenants.



Trusted Launch is enabled by default for newly created Azure Gen2 VMs and VM scale sets, when using supported OS images, VM sizes, and deployment methods. Supported deployments methods include deployment via the Azure Portal, ARM templates, Bicep, Terraform, and Azure SDKs.



Secure in operation: Continuous protection at runtime



Security does not stop at deployment. The secure in operation principle focuses on maintaining protection continuously as threats evolve.



Monitoring, detection, and signal correlation



Azure integrates telemetry from compute, network, and storage layers into centralized monitoring systems such as Azure Monitor and Microsoft Defender for Cloud. These systems continuously analyze behavior to identify misconfigurations, detect threats, and surface actionable security recommendations.



For IaaS workloads, Defender for Cloud helps identify exposed management ports, missing disk encryption, and insecure network configurations, while also correlating threat signals across the environment.



Identity-centric control and least privilege



Operational security depends heavily on identity. Azure IaaS integrates with Microsoft Entra ID to enforce identity-based access controls, reduce standing privileges, and apply conditional access policies. Features like Just-In-Time (JIT) VM access limit administrative exposure by only opening management ports when needed and only for approved identities.



By minimizing persistent access and rotating privileges dynamically, Azure reduces the impact of credential compromise.



Bringing defense in depth and SFI together



Defense in depth provides the technical structure of Azure IaaS security. Secure by design, secure by default, and secure in operation provide the engineering and operational discipline that governs how those controls are built, deployed, and maintained.



Together, they ensure that Azure IaaS security is:




Layered: No single control is assumed to be sufficient.



Intrinsic: Security is part of the platform architecture, not an add-on.



Consistent: Defaults and policies reduce configuration drift.



Adaptive: Continuous monitoring and operational controls evolve with the threat landscape.




This combination allows Azure to protect IaaS workloads across compute, network, and storage while maintaining compatibility with diverse operating systems, workload types, and deployment models.



 Security as an ongoing platform commitment



Azure IaaS security is not defined by a static set of features. It is the result of ongoing engineering investment, guided by clear principles, and reinforced through layered technical controls.



Defense in depth ensures that failures are contained. Secure-by-design architecture reduces attack surfaces from the start. Secure-by-default configurations minimize exposure without adding friction. And secure-in-operation practices ensure the platform continues to adapt as threats evolve.



Together, these principles define how Azure IaaS delivers infrastructure security that is systematic, scalable, and aligned with modern threat realities.



To go deeper, explore the Azure IaaS Resource Center for tutorials, best practices, and guidance across compute, storage, and networking to help you design and operate resilient infrastructure with greater confidence.



Did you miss these posts in the Azure IaaS series?




Explore new resources for building a stronger, more efficient infrastructure



Keep critical applications running with built-in resiliency at scale








	
					
							
		
		
			Create a resilient infrastructure with Azure
			Visit the Azure IaaS Resource Center to start building a stronger, more efficient infrastructure today.
							
					
						Get started with Azure					
				
					
	




The post Azure IaaS: Defense in depth built on secure-by-design principles appeared first on Microsoft Azure Blog.

---
*원문: [https://azure.microsoft.com/en-us/blog/azure-iaas-defense-in-depth-built-on-secure-by-design-principles/](https://azure.microsoft.com/en-us/blog/azure-iaas-defense-in-depth-built-on-secure-by-design-principles/)*

---
categories:
- MS
- 보안
date: '2026-05-12T22:53:09+00:00'
description: "In this article\n\t\t\n\n\t\t\n\t\t\t\n\t\t\n\t\n\t\n\t\t\n\t\t\tCore\
  \ Idea: From TTPs to LogsApproaches for Synthetic Attack Log GenerationEvaluation DatasetsReferencesLearn\
  \ more\t\t\n\t\n\t\n"
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/05/12/accelerating-detection-engineering-using-ai-assisted-synthetic-attack-logs-generation/
source: Microsoft Security Blog
tags: []
title: Accelerating detection engineering using AI-assisted synthetic attack logs
  generation
---

In this article
		

		
			
		
	
	
		
			Core Idea: From TTPs to LogsApproaches for Synthetic Attack Log GenerationEvaluation DatasetsReferencesLearn more		
	
	




Logs and telemetry&nbsp;are&nbsp;the&nbsp;foundation&nbsp;of modern cybersecurity. They enable threat detection, incident response, forensic investigation, and&nbsp;compliance across endpoints, networks, and cloud environments. Yet, despite their importance, high‑quality security&nbsp;attack&nbsp;logs are notoriously difficult to&nbsp;collect,&nbsp;especially&nbsp;at scale.&nbsp;



Real‑world security&nbsp;telemetry is&nbsp;often composed of repeated benign activity occurring&nbsp;across&nbsp;environments&nbsp;and&nbsp;with&nbsp;very&nbsp;rare&nbsp;malicious activity.&nbsp;Gathering, labeling, and&nbsp;maintaining&nbsp;datasets with real attack logs is costly and operationally challenging. It requires not only labeling malicious activities, but also fully reconstructing attack scenarios.&nbsp;These challenges significantly slow&nbsp;detection engineering and limit&nbsp;the&nbsp;quality of both the rule-based detection&nbsp;authoring&nbsp;and&nbsp;anomaly-detection&nbsp;approaches.&nbsp;



In this post, we explore a different path:&nbsp;using&nbsp;AI&nbsp;to generate realistic, high‑fidelity synthetic security&nbsp;attack&nbsp;logs. By translating attacker behaviors,&nbsp;expressed as tactics, techniques, and procedures&nbsp;(TTPs)—directly into structured telemetry, we aim to accelerate detection development while preserving realism and security.&nbsp;



Why is this work important for&nbsp;Microsoft&nbsp;Defender customers?&nbsp;



For Microsoft Defender customers, this work is crucial because&nbsp;it directly addresses the challenge of obtaining high-quality, realistic security attack logs needed for effective threat detection and response. By&nbsp;leveraging&nbsp;AI-driven synthetic log generation, organizations can accelerate the development of detection rules&nbsp;and AI-based automation approaches,&nbsp;while&nbsp;ensuring&nbsp;privacy and reducing operational overhead. Synthetic logs enable customers to simulate a broader range of attack scenarios—including rare and emerging threats—without exposing sensitive data or relying on costly lab-based simulations.&nbsp;Ultimately, this&nbsp;approach enhances the agility and effectiveness of&nbsp;Microsoft Defender detection and response capabilities,&nbsp;helping customers stay ahead of evolving cyber threats.&nbsp;



Why Synthetic Security Logs&nbsp;in addition to&nbsp;Lab Simulations?&nbsp;



Synthetic data has been widely adopted in various fields as a privacy-conscious substitute for real data, and it offers even greater advantages in cybersecurity. It enables the creation of safe, shareable datasets that avoid exposure of sensitive customer information, allows simulation of rare or emerging attacks that are challenging to&nbsp;observe&nbsp;in real environments, accelerates the process of detection engineering and testing, and supports reproducible experiments for benchmarking and evaluation.&nbsp;



While synthetic logs are not a replacement for all lab-based validation, they can complement lab simulations by speeding up early-stage detection design, testing, and coverage expansion.&nbsp;Traditionally, generating realistic attack telemetry&nbsp;requires&nbsp;executing real attacks in controlled lab environments. While&nbsp;accurate, this approach is slow, labor‑intensive, and difficult to scale.&nbsp;It also limits agility for the security teams responsible for defending our systems and delays the rollout of new threat detections into production.&nbsp;This&nbsp;blog examines&nbsp;whether&nbsp;AI-assisted&nbsp;synthetic log generation&nbsp;can provide similar fidelity,&nbsp;without the operational overhead of lab‑based attack execution.&nbsp;



Core Idea: From TTPs to Logs



Attackers can abuse TTP through various actions that exploit different processes.&nbsp;At&nbsp;a high level,&nbsp;the&nbsp;proposed&nbsp;workflow&nbsp;consumes&nbsp;“TTP + Action”&nbsp;as input and produces&nbsp;structured security logs&nbsp;as output.&nbsp;



Input:&nbsp;High‑level&nbsp;attacker TTPs from&nbsp;the&nbsp;MITRE ATT&amp;CK&nbsp;framework&nbsp;[1], a widely used knowledge base of adversary tactics and techniques, and concrete attacker actions.&nbsp;See the example&nbsp;below.&nbsp;



Tactic&nbsp;Technique&nbsp;Action&nbsp;Stealth&nbsp;T1202 &#8211; Indirect Command Execution&nbsp;&nbsp;The attackers executed&nbsp;forfiles&nbsp;and obfuscated their actions using variable expansion of&nbsp;%PROGRAMFILES&nbsp;and hex characters (for example, 0x5d). They obfuscated the use of&nbsp;echo, open, read, find,&nbsp;and exec to extract file contents, then passed the output to a Python interpreter for execution.&nbsp;



Output:&nbsp;Realistic log entries with correctly populated fields such as&nbsp;&#8220;Command Line&#8221;, &#8220;Process Name&#8221;, &#8220;Parent Process Name&#8221;,&nbsp;and other relevant telemetry fields.&nbsp;



Goal: The goal is not to reproduce logs verbatim, but to generate&nbsp;realistic, semantically correct logs&nbsp;that&nbsp;would accurately&nbsp;trigger&nbsp;detections,&nbsp;mirroring real attacker behavior.&nbsp;



Approaches&nbsp;for&nbsp;Synthetic&nbsp;Attack&nbsp;Log Generation



We&nbsp;explore&nbsp;three increasingly sophisticated techniques for generating logs.&nbsp;




Prompt‑Engineered Generation:&nbsp;Our baseline approach uses a&nbsp;series of&nbsp;carefully designed&nbsp;expert‑crafted prompts.&nbsp;The&nbsp;workflow&nbsp;comprises&nbsp;a structured, multi‑stage dialogue:&nbsp;

Prompting: The model is given a detailed attack scenario and context.&nbsp;



Iterative Generation: Logs are generated across multiple turns to&nbsp;maintain&nbsp;coherence.&nbsp;



Evaluation: An independent&nbsp;large language model (LLM)-as-a-Judge&nbsp;assesses realism and consistency.&nbsp;






As depicted in&nbsp;the following image, the prompts explicitly instruct the model to reason like a cybersecurity researcher, leverage MITRE&nbsp;ATT&amp;CK knowledge, and produce coherent attack narratives.&nbsp;


Diagram that shows a three-stage AI agent pipeline: prompting for attack scenarios,iterative generation of logs, and LLM-as-a-Judge evaluation.




Agentic&nbsp;Workflow-based Generation:&nbsp;While the first approach works well in simpler cases, it struggles with complex, multi‑stage scenarios.&nbsp;To address these limitations, we introduced an&nbsp;agentic workflow&nbsp;using three specialized agents&nbsp;focused on different tasks:&nbsp;

Generator Agent: Produces&nbsp;an initial&nbsp;set of logs based on the input.&nbsp;



Evaluator Agent: Reviews logs and provides structured feedback.&nbsp;



Improver Agent: Suggests targeted refinements based on feedback.&nbsp;






As depicted in the image below, these agents collaborate in an iterative loop&nbsp;(generate, evaluate, improve),&nbsp;allowing the system to correct errors, fill gaps, and refine details over multiple turns.&nbsp;This collaborative process significantly improves log completeness and fidelity, especially for complex attack chains.&nbsp;


Diagram that shows a cyclical agentic workflow where generator, evaluator, and improveragents collaborate to produce synthetic telemetry logs.




Multi-Turn Reinforcement Learning with Verifiable Rewards:&nbsp;While the synthetic logs generated by the agentic workflow are often semantically correct,&nbsp;preserving key properties like parent‑child process relationships and event ordering,&nbsp;they still differ noticeably from real event logs, especially in process paths,&nbsp;command‑line arguments, service names and so on.&nbsp;This limits the usage of these logs to test detection efficacy;&nbsp;effective detection engineering&nbsp;requires&nbsp;reliably distinguishing&nbsp;benign&nbsp;activity&nbsp;from malicious behavior.&nbsp;&nbsp;To address this challenge,&nbsp;we&nbsp;conduct experiments using&nbsp;Reinforcement Learning with Verifiable Rewards (RLVR).&nbsp;Instead of rigid rewards used by the evaluator agent in the&nbsp;previous&nbsp;agentic workflow approach,&nbsp;we use&nbsp;partial&nbsp;rewards&nbsp;to learn the policies as follows:&nbsp;

We use an LLM‑as‑a‑Judge as follows to compare the synthesized data against ground‑truth logs.&nbsp;&nbsp;



The model&nbsp;only&nbsp;awards&nbsp;partial rewards based on semantic alignment&nbsp;and&nbsp;imposes a&nbsp;penalty&nbsp;if the&nbsp;generated string is&nbsp;not&nbsp;an&nbsp;exact&nbsp;match of the ground-truth logs, producing a more context-aware and flexible reward signal to guide the learning process.&nbsp;



The judge also produces reasoning, making&nbsp;evaluations&nbsp;transparent,&nbsp;and auditable.&nbsp;





Diagram that shows the LLM-as-a-Judge evaluation comparing generated logs to groundtruth, issuing rewards or penalties to drive policy updates.



While this direction of research shows a lot of promise, it is heavily dependent on the amount of labeled training data.&nbsp;To&nbsp;address this limitation, we applied&nbsp;data augmentations, including:&nbsp;




Paraphrasing attack narratives while preserving technical intent&nbsp;





Perturbing parameters (e.g., replacing executable names with plausible alternatives, re-ordering flags, etc.)&nbsp;




This allowed us to scale from hundreds to thousands of training examples.&nbsp;



Evaluation&nbsp;Datasets



To ensure our approach generalizes across environments and attack types, we evaluated it on three complementary datasets:&nbsp;




Goal‑Driven (GD) Campaigns: These are tightly scoped&nbsp;datasets produced by&nbsp;repeatable attack simulations&nbsp;conducted by our threat researchers.&nbsp;GDs are&nbsp;built around a specific&nbsp;security&nbsp;objective&nbsp;(e.g., detecting credential dumping on Windows servers). They provide clean ground truth and well‑defined attacker actions.&nbsp;We used a total of 10 different GD executions to evaluate our approaches.&nbsp;





Security Datasets Project:&nbsp;An open‑source initiative&nbsp;[2]&nbsp;that provides malicious and benign datasets from multiple platforms, enabling broader evaluation and generalizability across different environments.&nbsp;&nbsp;





ATLASv2 Dataset:&nbsp;The ATLASv2&nbsp;dataset&nbsp;[3]&nbsp;is&nbsp;comprised&nbsp;of&nbsp;Windows Security Auditing logs, Sysmon logs, Firefox logs, and&nbsp;Domain Name System (DNS)&nbsp;telemetry. These&nbsp;logs&nbsp;are&nbsp;generated&nbsp;across&nbsp;two Windows VMs&nbsp;by executing&nbsp;10&nbsp;multi‑stage attack scenarios and introducing&nbsp;realistic noise and cross‑host behaviors.&nbsp;We limited the evaluation of synthetic attack logs to&nbsp;malicious&nbsp;activity&nbsp;during the attack windows.&nbsp;




Note: The external datasets from the Security Datasets Project and ATLASv2 are used strictly for research and validation of our log generation methods. These datasets are not used in the development, training, or deployment of any commercial products.&nbsp;



Evaluation&nbsp;



Methodology:&nbsp;We evaluated&nbsp;the prompt engineering and agentic workflow approach&nbsp;on the three datasets&nbsp;across multiple reasoning and non‑reasoning models, using&nbsp;recall&nbsp;as our primary metric.&nbsp;Recall measures the model’s ability to generate&nbsp;semantically&nbsp;relevant log instances (true positives) expected for a given attack scenario.&nbsp;Our&nbsp;LLM‑as‑a‑Judge&nbsp;performs flexible matching, focusing on:&nbsp;




New process name&nbsp;





Parent process name&nbsp;





Command line semantics&nbsp;




For example, a synthetic log&nbsp;containing&nbsp;“forfiles.exe”&nbsp;can successfully match a ground‑truth entry with the full path&nbsp;“D:\Windows\System32\forfiles.exe”.&nbsp;



Key Results:&nbsp;The results&nbsp;in experimental evaluation&nbsp;demonstrate&nbsp;that prompt-only&nbsp;&nbsp;approaches&nbsp;establish a baseline but show inconsistent performance.&nbsp;The agentic workflows deliver dramatic recall improvements across all datasets.&nbsp;Reasoning models, combined with agentic refinement, achieve the highest fidelity.&nbsp;&nbsp;



Finally, our&nbsp;experiments&nbsp;training reinforcement learning&nbsp;approaches&nbsp;conclude&nbsp;that while it shows a significant promise, a&nbsp;substantial&nbsp;amount of labeled data will be&nbsp;required&nbsp;for the agent to learn effective policies to make the synthetic data identical to benign logs.&nbsp;



Table 1 and Table 2&nbsp;report&nbsp;the performance of the prompt-based and agentic workflow-based approaches, respectively.&nbsp;For reasoning&nbsp;models&nbsp;(o1, o3 and o3-mini), we report the recall values using&nbsp;a&nbsp;Medium&nbsp;reasoning effort.&nbsp;Overall, agentic collaboration&nbsp;emerges&nbsp;as the most effective technique for high‑quality synthetic attack logs generation.&nbsp;


Table 1: Recall values for prompt-based log generation.


Table 2: Recall values for agentic workflow-based log generation.



Across the evaluation datasets we used, AI‑driven synthetic log generation shows strong potential to produce semantically meaningful logs from TTPs and attacker actions. It can capture multi‑event sequences, preserve parent‑child process relationships, and generate realistic command lines. 



This capability can accelerate detection engineering by reducing dependence on costly lab setups and enabling rapid experimentation, without sacrificing realism or safety.&nbsp;Our early experiments with reinforcement learning with verifiable rewards also look&nbsp;promising and&nbsp;could improve verbatim alignment when sufficient training data is available.&nbsp;



References




MITRE ATT&amp;CK Framework:&nbsp;MITRE ATT&amp;CK®&nbsp;&nbsp;





Security Datasets:&nbsp;GitHub &#8211; OTRF/Security-Datasets: Re-play Security Events&nbsp;





ATLASv2: ATLAS Attack&nbsp;Engagements,&nbsp;Version 2:&nbsp;2401.01341&nbsp;




This research is provided by Microsoft Defender Security Research with contributions from Raghav Batta and  members of Microsoft Threat Intelligence.



Learn more



For the latest security research from the Microsoft Threat Intelligence community, check out the&nbsp;Microsoft Threat Intelligence Blog.



To get notified about new publications and to join discussions on social media, follow us on&nbsp;LinkedIn,&nbsp;X (formerly Twitter), and&nbsp;Bluesky.



To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the&nbsp;Microsoft Threat Intelligence podcast.



Review our documentation to learn more about our real-time protection capabilities and see how to enable them within your organization.  &nbsp;




Learn more about securing Copilot Studio agents with Microsoft Defender &nbsp;



Evaluate your AI readiness with our latest&nbsp;Zero Trust for AI workshop.



Learn more about Protect your agents in real-time during runtime (Preview)



Explore how to build and customize agents with Copilot Studio Agent Builder&nbsp;



Microsoft 365 Copilot AI security documentation&nbsp;



How Microsoft discovers and mitigates evolving attacks against AI guardrails&nbsp;

The post Accelerating detection engineering using AI-assisted synthetic attack logs generation appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/05/12/accelerating-detection-engineering-using-ai-assisted-synthetic-attack-logs-generation/](https://www.microsoft.com/en-us/security/blog/2026/05/12/accelerating-detection-engineering-using-ai-assisted-synthetic-attack-logs-generation/)*

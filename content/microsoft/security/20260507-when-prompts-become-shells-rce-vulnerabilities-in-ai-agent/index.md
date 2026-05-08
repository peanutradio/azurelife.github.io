---
categories:
- MS
- 보안
date: '2026-05-07T20:22:39+00:00'
description: "In this article\n\t\t\n\n\t\t\n\t\t\t\n\t\t\n\t\n\t\n\t\t\n\t\t\tA representative\
  \ case study: Semantic KernelCVE-2026-26030: In-Memory Vector StoreCVE-2026-25592:\
  \ Arbitrary file write t"
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/
source: Microsoft Security Blog
tags: []
title: 'When prompts become shells: RCE vulnerabilities in AI agent frameworks'
---

In this article
		

		
			
		
	
	
		
			A representative case study: Semantic KernelCVE-2026-26030: In-Memory Vector StoreCVE-2026-25592: Arbitrary file write through SessionsPythonPluginThe vulnerabilityAttack chain overviewDefending the agentic edgeNot bugs, but developed by designCTF challenge: Attack your own agentLearn more		
	
	




AI agents have fundamentally changed the threat model of AI model-based applications. By equipping these models with plugins (also called tools), your agents no longer just generate text; they now read files, search connected databases, run scripts, and perform other tasks to actively operate on your network.



Because of this, vulnerabilities in the AI layer are no longer just a content issue and are an execution risk. If an attacker can control the parameters passed into these plugins via prompt injection, the agent may be driven to perform actions beyond its intended use.



The AI model itself isn’t the issue as it’s behaving exactly as designed by parsing language into tool schemas. The vulnerability lies in how the framework and tools trust the parsed data.



To build powerful applications, developers rely heavily on frameworks like Semantic Kernel, LangChain, and CrewAI. These frameworks act as the operating system for AI agents, abstracting away complex model orchestration. But this convenience comes with a hidden cost: because these frameworks act as a ubiquitous foundational layer, a single vulnerability in how they map AI model outputs to system tools carries systemic risk.



As part of our mission to make AI systems more secure and eliminate new class of vulnerabilities, we’re launching a research series focused on identifying vulnerabilities in popular AI agent frameworks. Through responsible disclosure, we work with maintainers to ensure issues are addressed before sharing our findings with the community.



In this post, we share details on the vulnerabilities we discovered in Microsoft’s Semantic Kernel, along with the steps we took to address them and interactive way to try it yourself. Stay tuned for upcoming blogs where we’ll dive into similar vulnerabilities found in frameworks beyond the Microsoft ecosystem.



Background



We discovered a vulnerable path in Microsoft Semantic Kernel that could turn prompt injection into host-level remote code execution (RCE).



A single prompt was enough to launch calc.exe on the device running our AI agent, with no browser exploit, malicious attachment, or memory corruption bug needed. The agent simply did what it was designed to do: interpret natural language, choose a tool, and pass parameters into code.


Figure 1. Illustration of CVE-2026-26030 exploitation using a local model.



This scenario is the real security story behind modern AI agents. Once an AI model is wired to tools, prompt injection draws a thin line between being just a content security problem and becoming a code execution primitive. In this post in our research series on AI agent framework security,&nbsp;we show how two vulnerabilities in Semantic Kernel could allow attackers to cross that line, and what customers should do to assess exposure, patch affected agents, and investigate whether exploitation may already have occurred.



A representative case study: Semantic Kernel



Semantic Kernel is Microsoft’s open-source framework for building AI agents and integrating AI models into applications. With over 27,000 stars on GitHub, it provides essential abstractions for orchestrating AI models, managing plugins, and chaining workflows.



During our security research into the Semantic Kernel framework, we identified and disclosed two critical vulnerabilities: CVE-2026-25592 and CVE-2026-26030. These flaws, which have since been fixed, could allow an attacker to achieve unauthorized code execution by leveraging injection attacks specifically targeted at agents built within the framework.



In the following sections, we break down the mechanics of these vulnerabilities in detail and provide actionable guidance on how to harden your agents against similar exploitation.



CVE-2026-26030: In-Memory Vector Store



Exploitation of this vulnerability requires two conditions:




The attacker must have a prompt injection vector, allowing influence over the agent’s inputs



The targeted agent must have the Search Plugin backed by In-Memory Vector Store functionality using the default configuration




When both these two conditions are met, the vulnerability enables an attacker to achieve RCE from a prompt.



To demonstrate how this vulnerability could be exploited, we built a “hotel finder” agent&nbsp; using Semantic Kernel. First, we created an In Memory Vector collection to store the hotels’ data, then exposed a search_hotels(city=…) function to the kernel (agent) so that the AI model could invoke it through tool calling.


Figure 2. Semantic Kernel agent configured with In-Memory Vector collection.



When a user inputs, for example, “Find hotels in Paris,” the AI model calls the search plugin with city=&#8221;Paris&#8221;. The plugin then first runs a deterministic filter function to narrow down the dataset and computes vector similarity (embeddings).



With this understanding of how a Semantic Kernel agent performs the search, let’s dive deep into the vulnerability.



Issue 1: Unsafe string interpolation



The default filter function that we mentioned previously is implemented as a Python lambda expression executed using eval(). In our example, The default filter will result to new_filter = &#8220;lambda x: x.city == &#8216;Paris'&#8221;.


Figure 3. Default filtering function definition.



The vulnerability is that kwargs[param.name] is AI model-controlled and not sanitized. This acts as a classic injection sink. By closing the quote (&#8216;) and appending Python logic, an attacker could turn a simple data lookup into an executable payload:




Input:&nbsp;&#8216; or MALICIOUS_CODE or &#8216;



Result:&nbsp;lambda x: x.city == &#8221; or MALICIOUS_CODE or &#8221;




Issue 2: Avoidable blocklist



The framework developers anticipated this RCE risk&nbsp;and implemented a validator that parses the filter string into an Abstract Syntax Tree (AST) before execution.


Figure 4. Blocklist implementation.



Before running a user-provided filter code, the application runs a validation function designed to block unsafe operations. At a high level, the validation does the following:




It only allows lambda expressions. It rejects outright any attempt to pass full code blocks (such as import statements or class definitions).



It scans every element in the code for dangerous identifiers and attributes that could enable arbitrary code execution (for example, strings like eval, exec, open, __import__, and similar ones). If any of these identifiers appear, the code is rejected.



If the code passes both checks, it is executed in a restricted environment where Python&#8217;s built-in functions (like open and print) are deliberately removed. So even if something slips through, it shouldn&#8217;t have access to dangerous capabilities.




The resulting lambda is then used to filter records in the Vector Store.



While this approach is solid in theory, blocklists in dynamic languages like Python are inherently fragile because the language’s flexibility allows restricted operations to be reintroduced through alternate syntax, libraries, or runtime evaluation.



We found a way to bypass this blocklist implementation through a specially crafted exploit prompt.



Exploit



Our exploit prompt was designed to manipulate the agent into triggering a Search Plugin invocation with an input that ultimately leads to malicious code execution:


A Malicious prompt demanding execution of the search_hotels function with the malicious argument.



This prompt circumvented the agent to trigger the following function calling:


Invocation of the &ldquo;search hotels&rdquo; function with the malicious argument.



As result, the lambda function was formatted as the following and executed inside eval(). This payload escaped the template string, traversed Python’s class hierarchy to locate&nbsp;BuiltinImporter, and used it to dynamically load&nbsp;os&nbsp;and call&nbsp;system(). These steps bypassed the import blocklists to launch an arbitrary shell command (for example,&nbsp;calc.exe) while keeping the template syntax valid with a clean closing expression.



The filter function didn’t block the payload because of the following reasons:



1. Missing dangerous names



The payload used several attributes that weren’t in the blocklist:




__name__&nbsp; – Used to find&nbsp;BuiltinImporter&nbsp;by name



load_module&nbsp;– The method that imports modules



system&nbsp;– The method that executes shell commands



BuiltinImporter&nbsp;– The class itself




2. Structural check passes



The payload was wrapped inside a valid lambda expression. The check&nbsp;isinstance(tree.body, ast.Lambda)&nbsp;passed because the entire thing is in itself a lambda that just happens to contain malicious code in its body.



3. Empty&nbsp;__builtins__&nbsp;is irrelevantThe&nbsp;eval()&nbsp;call used&nbsp;{&#8220;__builtins__&#8221;: {}}&nbsp;to remove access to built-in functions. However, this protection was meaningless because the payload never used built-ins directly. Instead, it started with tuple(), which exists regardless of the builtins environment, and crawled through Python&#8217;s type system to reach dangerous functionality.



4. No&nbsp;ast.Subscript&nbsp;checkingWhile not used in this payload, it&#8217;s worth noting that the filter only checked&nbsp;ast.Name&nbsp;and&nbsp;ast.Attribute&nbsp;nodes. If the payload needed to use a blocked name, it could’ve accessed it using bracket notation (for example,&nbsp;obj[&#8216;__class__&#8217;]&nbsp;instead of&nbsp;obj.__class__), which creates an&nbsp;ast.Subscript&nbsp;node that the validation completely ignored.



Mitigation



After responsibly disclosing the vulnerability to MSRC, the Microsoft Semantic Kernel team implemented a comprehensive fix using four layers of protection to eliminate every escape primitive needed to turn a lambda filter into executable code:




AST node-type allowlist&nbsp;– Permits only safe constructs like comparisons, boolean logic, arithmetic, and literals.



Function call allowlist&nbsp;– Checks even allowed AST call nodes to ensure only safe functions can be invoked.



Dangerous attributes blocklist&nbsp;– Blocks class hierarchy traversal (for examples,&nbsp;__class__,&nbsp;__subclasses__).



Name node restriction – Allows only the lambda parameter (for example,&nbsp;x) as a bare identifier and rejects references to&nbsp;os,&nbsp;eval,&nbsp;type, and others.




How do I know if I am affected?



Your agent is vulnerable to CVE-2026-26030 if it meets all of the following conditions:




It uses the Python package semantic-kernel.



It’s running a framework version prior to 1.39.4.



It uses the In-Memory Vector Store and relies on its filter functionality (when acting as the backend for the Search Plugin using default configurations).




What to do if I am affected?



You don’t need to rewrite your agent. Upgrading the Python semantic-kernel dependency to version 1.39.4 or higher mitigates the risk.



What about the time that my agent was vulnerable?



While patching closes the bug, but it doesn’t answer the retrospective question defenders care about: whether their agent was exploited before they upgraded.



First, define the vulnerable window for each affected deployment: from the moment a vulnerable Semantic Kernel Python version was deployed until the moment version 1.39.4 or later was installed. Any investigation should focus on that time range.



Second, hunt for host-level post-exploitation signals during that vulnerable window. Because successful exploitation results in code execution on the host, the most useful evidence is in endpoint telemetry: suspicious child processes, outbound connections, or persistence artifacts created by the agent host process. We provide a set of practical advanced hunting queries for further investigation in a separate section of this blog.



If you find suspicious activity during that window, treat it as a potential host compromise. Review the affected host, rotate credentials and tokens accessible to the agent, and investigate what data or systems that host could reach.



CVE-2026-25592: Arbitrary file write through SessionsPythonPlugin



Before diving into the mechanics of this second vulnerability, here is what an agent sandbox escape looks like in practice: with a single prompt, an attacker could bypass a cloud-hosted sandbox, write a malicious payload directly to the host device’s Windows Startup folder, and achieve full RCE.



The container boundary



Semantic Kernel includes a built-in plugin called&nbsp;SessionsPythonPlugin&nbsp;that allows agents to safely execute Python code inside Azure Container Apps dynamic sessions, which are isolated cloud hosted sandboxes with their own filesystem.



The security model relies entirely on this boundary. Code runs in the isolated sandbox and cannot touch the host device where the agent process runs. To help move data in and out of the sandbox, the plugin uses helper functions like&nbsp;UploadFile&nbsp;and&nbsp;DownloadFile,&nbsp;which run on the host side to transfer files across this boundary.



The vulnerability



In the .NET software development kit (SDK), DownloadFileAsync was accidentally marked with a [KernelFunction] attribute, which officially advertised it to the AI model as a callable tool, complete with its parameter schema:






Because of this attribute, the localFilePath parameter, which dictates exactly where File.WriteAllBytes() saves data on the host device, was now entirely AI controlled. With no path validation, directory restriction, or sanitization in place, an attacker wouldn’t need a complex hypervisor exploit; they just needed to prompt the model to do it for them.



(Note: Arbitrary File Read. A similar vulnerability existed in reverse for the upload_file() function across both the Python and .NET SDKs. It accepted any local file path without validation, allowing prompt injections to exfiltrate sensitive host files, like SSH keys or credentials, directly into the sandbox).



Attack chain overview



By chaining two exposed tools, an attacker could turn standard function calling into a sandbox escape:






Step 1: Create the payload



An &nbsp;injected prompt instructs the agent to use the&nbsp;ExecuteCode&nbsp;tool to generate a malicious script inside the isolated container:



At this point, the payload is contained. It exists only in the sandbox and cannot execute on the host.



Step 2: Escape the sandbox



A second injected instruction tells the AI model to use the&nbsp;DownloadFileAsync&nbsp;tool to download the file to a dangerous location on the host:






The agent calls:






The agent fetches the script from the sandbox&#8217;s API and writes it directly to the host&#8217;s&nbsp;Windows\Start Menu\Programs\Startup&nbsp;folder.



Step 3: Execute the code



On the next user sign-in, the script runs, granting full host compromise.



This exploit illustrates the MITRE ATLAS technique AML.T0051 (LLM Prompt Injection) cascading into AML.T0016 (Obtain Capabilities).



 Exposing&nbsp;DownloadFileAsync&nbsp;provided a direct file write primitive on the host filesystem, effectively negating the container isolation.



The fix and how to defend



Semantic Kernel patched this vulnerability by removing the root cause of tool exposure and adding defense in depth:



Removed AI access – The&nbsp;[KernelFunction]&nbsp;attribute was removed, making the function invisible to the AI model. The AI agent can no longer invoke it, and prompt injection can no longer reach it:






This single change breaks the entire attack chain. The AI&nbsp;can now only be called directly by the developer&#8217;s intentional code.




Path validation – For developers calling the function programmatically, a&nbsp;ValidateLocalPathForDownload()&nbsp;method was added using path canonicalization (Path.GetFullPath()) and directory allowlist matching to ensure the target path falls within permitted directories:



Similar opt-in protections were applied to uploads.



How do I know if I am affected?



Your agent is vulnerable to CVE-2026-25592 if it uses a Semantic Kernel .NET SDK version older than&nbsp;1.71.0.



Defending the agentic edge



If you use Semantic Kernel,&nbsp;our primary recommendation is to upgrade immediately.&nbsp;You don’t need to rewrite your agent&#8217;s architecture; the security updates simply remove the AI model’s ability to trigger these functions autonomously.



More broadly, defending AI agents requires acknowledging that AI models aren’t security boundaries. Security teams must correlate signals across two layers: the&nbsp;AI model level&nbsp;(intent detection through meta prompts and content safety filters) and the&nbsp;host level&nbsp;(execution detection). If an attacker bypasses the AI model guardrails, traditional endpoint defense must be in place to detect anomalous behavior, such as an AI agent process suddenly spawning command lines or dropping scripts into Startup folders.



Not bugs, but developed by design



Untrusted data being used as input for high-risk operations isn’t&nbsp;entirely new. In the early days of web application security, such input was passed directly into SQL queries or filesystem APIs. Today, agents are doing something similar, in that they could map untrusted natural-language input to system tools.



The overarching lesson from both vulnerabilities is that both aren’t bugs in the AI model itself, but rather issues in agent architecture and tool design.&nbsp;We must make a clear distinction between model behavior and agent architecture. The AI model functions exactly as it was designed to: translate intent into structured tool calls.



When models are connected to system tools, prompt injection risks may extend beyond typical chatbot misuse and require additional safeguards. Instead, it becomes a direct path to concrete execution primitives like data exfiltration, arbitrary file writes, and RCE. For a deeper look at the runtime risks of tool-connected AI models, see Running OpenClaw safely: identity, isolation, and runtime risk.



As mentioned previously, your LLM is not a security boundary. The tools you expose define your attacker’s affected scope. Any tool parameter the model can influence must be treated as attacker-controlled input.



In the next blog in this series, we’ll expand beyond Semantic Kernel to explore structurally similar execution vulnerabilities that we found in other widely used third-party agent frameworks.







CTF challenge: Attack your own agent



If you want to see how prompt injections escalate into execution and to put your skills to the test, we&#8217;ve packaged the vulnerable hotel-finder agent that we described in this blog into an interactive, hands-on capture-the-flag (CTF) challenge.



This CTF challenge lets you step into the shoes of an attacker and try to exploit the CVE-2026-26030 vulnerability in a controlled environment. You need to craft a prompt injection that not only bypasses the agent’s natural language defenses but also smuggle a Python AST-traversal payload through the vulnerable eval() sink.



To see if you can manipulate the AI model into launching arbitrary code and popping calc.exe on the server, download the challenge, spin it up in a sandbox, and see if you can achieve RCE. Keep in mind that this challenge is for educational purposes only, and shouldn’t be run in production environments.






Reconnaissance:






Exploit (jailbreak and payload):






Note: Because the agent will running locally on your device, calc.exe will open on your desktop. In a real-world scenario, such an executable file will launch remotely on the server hosting the agent.



Download the CTF challenge: https://github.com/amiteliahu/AIAgentCTF/tree/main/CVE-2026-26030



Advanced hunting



The following advanced hunting queries lets you surface suspicious activities from Semantic Kernel agents.



Detect common RCE post-exploitation child processes from Semantic Kernel agent hosts



DeviceProcessEvents
| where Timestamp > ago(30d)
| where InitiatingProcessCommandLine matches regex @"(?i)semantic[\s_\-]?kernel"
    or InitiatingProcessFolderPath matches regex @"(?i)semantic[\s_\-]?kernel"
| where FileName in~ (
    "cmd.exe", "powershell.exe", "pwsh.exe", "bash.exe", "wsl.exe",
    "certutil.exe", "mshta.exe", "rundll32.exe", "regsvr32.exe",
    "wscript.exe", "cscript.exe", "bitsadmin.exe", "curl.exe",
    "wget.exe", "whoami.exe", "net.exe", "net1.exe", "nltest.exe",
    "klist.exe", "dsquery.exe", "nslookup.exe"
)
| project 
    Timestamp,
    DeviceName,
    AccountName,
    FileName,
    ProcessCommandLine,
    InitiatingProcessFileName,
    InitiatingProcessCommandLine,
    InitiatingProcessFolderPath
| sort by Timestamp desc



Detect .NET hosting Semantic Kernel that spawns suspicious children



DeviceProcessEvents
| where Timestamp > ago(30d)
| where InitiatingProcessFileName in~ ("dotnet.exe")
| where InitiatingProcessCommandLine matches regex @"(?i)(semantic[\s_\-]?kernel|SKAgent|kernel\.run)"
| where FileName in~ (
    "cmd.exe", "powershell.exe", "pwsh.exe", "bash.exe",
    "certutil.exe", "curl.exe", "whoami.exe", "net.exe"
)
| project 
    Timestamp,
    DeviceName,
    AccountName,
    FileName,
    ProcessCommandLine,
    InitiatingProcessFileName,
    InitiatingProcessCommandLine
| sort by Timestamp desc



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





The post When prompts become shells: RCE vulnerabilities in AI agent frameworks appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)*

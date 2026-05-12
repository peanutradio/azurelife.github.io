---
categories:
- MS
- GitHub
date: '2026-05-11T16:00:00+00:00'
description: 'Welcome back to GitHub for Beginners. So far, we&rsquo;ve discussed
  GitHub Issues and Projects, GitHub Actions, security, GitHub Pages, and Markdown.
  This time '
draft: false
original_url: https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-oss-contributions/
source: GitHub Blog
tags:
- Developer skills
- GitHub
- GitHub for beginners
- open source
title: 'GitHub for Beginners: Getting started with OSS contributions'
---

Welcome back to GitHub for Beginners. So far, we&rsquo;ve discussed GitHub Issues and Projects, GitHub Actions, security, GitHub Pages, and Markdown. This time we&rsquo;re going to talk about open source software and how to contribute to that community. By the end of this post, you&rsquo;ll know what open source is, how to find projects to work on, how to read an open source repository, as well as start making your first contributions. So let&rsquo;s get started!



As always, if you prefer to watch the video or want to reference it, we have all of our GitHub for Beginners episodes available on YouTube.



What is open source?



Open source software (OSS) refers to software that features freely available source code. In contrast with &ldquo;closed source software,&rdquo; OSS is publicly available for anyone to use and build upon. This means that all of the work, including the codebase and communication between users, is available for everyone to see.



If you&rsquo;re just getting started in the world of software development, browsing and contributing to open source projects is a great way to dip your toes into large, impactful projects used by countless users worldwide.



GitHub is the home for open source software, so let&rsquo;s look at how to find projects you can contribute to.



How to find OSS projects to work on



Contributing to an open source software project for the first time can be daunting&mdash;we&rsquo;ve all been there! The first step is to look for projects in a language that you know which are accepting new contributors. One of the ways you can do this is to ask GitHub Copilot Chat for help.




Navigate to github.com and select the Copilot icon to open a chat window.



In the bottom-left corner of the chat window, use the combo box to select Ask.



Enter a prompt like the following, but remember to update it for a language you&rsquo;re comfortable with.




I&rsquo;m looking for a list of open source projects written in TypeScript that are accepting new contributors. Search GitHub and narrow down the list to repositories that use the good first issue label and have over 100 stars on GitHub. 



Copilot will do some searching and return a list of projects you can explore filtered by the good first issue label. This label indicates that an issue is beginner friendly, and a great starting point for new contributors. This label is a great way to find issues in a project you can work on.



For example, let&rsquo;s say that you wanted to contribute to the vscode repository.




Navigate to the vscode repository.



At the top of the repository, select the Issues tab.



On the Issues page, click the Labels box to open the drop down menu.



In the text box on the drop down menu, start typing &ldquo;good&rdquo; until you see the option for good first issue.



Select the good first issue label.




The window will update and display a list of good first issues for you to work on. But before jumping in, you should read the contributor&rsquo;s guide in the project&rsquo;s repository. Most well-maintained open source projects will have one.



Understanding an open source project



As we just alluded to, most open source projects have a few things in common if they&rsquo;re well maintained. These are the following items:




A well-documented README with installation instructions.



A contributor&rsquo;s guide that explains how to contribute.



An open source license, so everyone knows the project is free to use.



At least 100 GitHub stars to show it&rsquo;s used in the community.



Active development so that you know a maintainer of the source code will be able to review your contributions.



A good first issue label to indicate its open to new contributors.




When you&rsquo;re looking for a project to contribute to, these are the things you should be looking for in a repository.



&#128161; For more documentation on finding a good open source project, go to gh.io/gfb-oss to learn more about finding good first issues.



Making an OSS contribution



Now let&rsquo;s look at an actual project and work on how you would submit your first issue. For this demo, take a look at the gitfolio repository. Using the bullet points above, we want to see if this would be a good project to work on.




The project does have a well-documented README file.



The project has a contributor&rsquo;s guide: CONTRIBUTING.md.



You can see the open source license: LICENSE.



It has several thousands of stars, so well over our 100 benchmark.



At the top of the file list, you can see the most recent check in which should be fairly recent. While writing this, the last check in was yesterday, indicating the project is being actively maintained.




Based on these points, as long as you are familiar with TypeScript, this is a good repository to contribute to. However, you don&rsquo;t need to be familiar with TypeScript to continue following along in the demo.



Now you want to create a fork of the repository. A fork is a copy of the repository that we can freely experiment on and make changes in without affecting the original project. We usually use forks for open source contributions. If you need a refresher on forking a repository, check out this previous GitHub for Beginners blog.




Navigate to the home page of the project if you are not already there.



At the top of the project, click the Fork button.



In the new window, leave yourself as the owner and make sure the &ldquo;Repository name&rdquo; is the same as the original repository (i.e., &ldquo;gitfolio&rdquo;).



At the bottom of the window, select Create fork.



In your forked copy of the repository, click README.md in the list of files.



Change the file by adding some text.



In the top-right, select Commit changes&hellip;



Make sure to select the option at the bottom for Create a new branch from this commit and start a pull request.



Select Propose changes.



On the following window, click the Create pull request button. This will let you create a pull request to the main repository from your branch with the changes.



At the top of the &ldquo;Open a pull request&rdquo; window, select compare across forks. This will show your fork&rsquo;s changes compared to the original repository.



If you were submitting an actual change to the repository&mdash;not just walking through a demo&mdash;this is where you would give your pull request a title and a description. You&rsquo;d also want to provide a link to the issue that you were solving in the description of the pull request.




At this point, you&rsquo;d be ready to submit your pull request by clicking the button at the bottom of the window. However, once you do that, it no longer becomes just a change in your fork and will be a requested update on the original repository. That&rsquo;s why it isn&rsquo;t included in the steps above. When you do submit your pull request, it will be available and ready for a maintainer to review and, hopefully, approve!



Once approved and merged, GitHub automatically applies the changes from your fork into the main branch of the original repository, the official source of truth for the codebase.



What&rsquo;s next?



Congratulations! You&rsquo;ve learned how to make your own contributions to open source software. I hope it inspires you to contribute to your favorite projects.



And if you&rsquo;re looking for more information, we have lots of documentation that can help. Here are a few links to get you stated:




Finding ways to contribute to open source on GitHub



Contributing to open source projects



Contributing to a project through forking




Happy coding!

The post GitHub for Beginners: Getting started with OSS contributions appeared first on The GitHub Blog.

---
*원문: [https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-oss-contributions/](https://github.blog/developer-skills/github/github-for-beginners-getting-started-with-oss-contributions/)*

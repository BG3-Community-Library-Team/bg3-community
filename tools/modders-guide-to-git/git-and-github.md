---
title: A Modder's Guide to Git
description: The Difference between Git and GitHub
published: true
date: 2024-04-23T22:34:06.928Z
tags: git, github, workspace, organization
editor: markdown
dateCreated: 2024-04-23T22:34:04.842Z
---

## The Difference between Git and GitHub
You may be wondering, "Git? GitHub? Isn't it all the same thing?" They go hand-in-hand, but are two separate things. Let's go over what these two tools are, and then we'll get into how to use them together.

### Git
Before we get into what Git is, let's look at the [official description](https://git-scm.com/) from their site:
> Git is a [free and open source](https://git-scm.com/about/free-and-open-source) distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Okay, truthfully, that's not especially descriptive for the average modder who hasn't worked with Git before. And for those of us that have worked with it, whether in our careers or in our hobbies, the knowledge of it really amounts to "This is what is used." At the end of the day, it's a Version Control System which keeps track of your changes based on snapshots of your existing code. It's primarily used via a Command-Line Interface - `Command Prompt` or `Power Shell` for Windows users, `Terminal` for Mac & Linux users. It's designed in a way that  makes it difficult to permanently lose data - as long as the repository exists, you have a way to retrieve different versions of your code, on and offline. 

The Workflow of using Git can be explained in three steps:

1. You modify files in your **Local Repository**.
2. Out of all the files you've modified, you add just the files you want to have stored as part of the snapshot of your codebase.
3. You perform a **commit**, storing a snapshot of your modified codebase into a database held within your Local Repository.

We'll go further into the bolded topics later in this guide.

### GitHub
Having repositories is great, but without a central online location to store your repositories, the benefits are limited - you can't access your repository from other devices, it's more difficult to show what you're doing if you need help, collaboration gets messy, as you have to rely on sharing your files via USB, Disc, Email, or some other file transfer method. None of these are ideal. 

Enter GitHub.

GitHub is essentially a Cloud Storage service, but instead of backing up valuable photos and videos, it's aimed specifically at Git Repositories. Using Git, you can **clone** an existing project, **push** your changes, and **pull** the changes made by others. You can even create your own projects. It's made to be as seamless as possible.

Now that we understand what Git and GitHub are, let's dive into how to use them together.

---

[<img align="left" src="https://img.shields.io/static/v1?label=Previous&message=Getting+Started&color=blue&style=for-the-badge">](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/wiki/A-Modder's-Guide-to-Git)  [<img align="right" src="https://img.shields.io/static/v1?label=Next&message=Working+with+Repositories&color=2ea44f&style=for-the-badge">](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/wiki/_Modders-Guide-to-Git:-Working-with-Repositories)
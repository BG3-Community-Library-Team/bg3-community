---
title: 3. Working with Repositories
description: Learn the basics of using Git
published: true
date: 2024-04-24T06:51:56.628Z
tags: git, github, workspace, organization
editor: markdown
dateCreated: 2024-04-24T05:25:29.333Z
---

# Working With Repositories
In this section, we'll guide you through the process of Creating, **Forking**, and **Cloning** Repositories. Some of these terms you might not understand just yet - that's okay. By the end of this section, it will be much more clear.

## What is a Repository?
To put it simply, a Repository, often shortened to "Repo," is a location in which your code managed by git is stored. When you tell Git to manage a specific folder, that folder becomes a Repository of the information held within it. Every change that you save to Git is stored locally, tracked, and easily-accessible to you at any time. But before we can make use of these benefits, we need to *tell* Git that we want to track our folder. So let's get started:

## Initializing a Repository from the Command Line
What we want to do right now is to create a folder, and then have it's contents be tracked by Git. So let's get started!

1. Navigate to your `Documents` folder
2. Create a new folder, name it `Git Guide`.
3. In your newly created folder, create another folder titled `Initializing a Git Repo`
4. Enter your new folder, and open your Command Line Interface:
   - Windows: Right click in the folder contents part of the window, and select `Git Bash here`
   - Mac/Linux: Control-click the folder in the path bar, and select `Open in Terminal`
5. Type in `git init`

You should see the following message:
> Initialized empty Git repository in FILEPATH HERE

If you have the OS option to show hidden files enabled, you will also see that there's a new `.git` folder in your folder

Congratulations, you've created your first Git Repository! It's a little bit empty right now, but soon we'll show you how to make use of it. First, let's look at another option: Cloning a Repo.

## Cloning
We've already created our own local repository, but what if we want to work with an existing Repo instead? This is where Github comes in. Follow [this link](https://github.com/BG3-Community-Library-Team/Sample-Template). It'll take you to the Community Library team's Sample Mod Template. 

If you'd like to take a moment to get familiar with the GitHub UI, click this button:



<div style="text-align:center">
  
[![Image](https://img.shields.io/badge/Check_Out-Getting_Familiar_with_GitHub-orange?style=for-the-badge)](/Tutorials/Tools/modders-guide-to-git/getting-familiar-with-github)
</div>

### Cloning The Repo
Now that we understand how to initialize a Repo, let's take a look at cloning a repo from GitHub. First, let's make sure we have git open:

1. In your file manager, navigate to the "Git Guide" folder we created earlier, and open Git here.
2. Switch to your web browser, and navigate to the Sample Template link from the beginning of this section.
3. Click on the Green `Code` button, and copy the URL-like line in the middle of the dropdown.
4. Switching back to Git, enter in `git clone`, followed by a space, and then the link you just copied, then hit Enter. It will look something like this:
```bash
git clone git@github.com:BG3-Community-Library-Team/BG3-Community-Library.git
```

The console will display some progress text, and you should have a new folder, "Sample-Template." Now, let's use the console to bring Git into the folder:
1. Type in Git `cd Sample-Template`, and hit Enter

You'll now see the that you're in a repo. Input `get branch` to see what branch you're on - it should respond with `* main`.

## Recap
By this point, we understand the difference between Git and GitHub. We've learned what Version Control is, and how Git's focus is to take and store snapshots of a codebase. We've familiarized ourselves with the GitHub UI, installed Git, learned how to create a Repository from Scratch, and learned how to clone down an existing Repository. Next, we'll cover topics relating to Branches: What a branch is, how to create a snapshot of your code, and switch away to a different Branch. How to upload and download from GitHub using Version Control.

---

[<img align="left" src="https://img.shields.io/badge/Previous-The_Difference_Between_Git_and_GitHub-blue?style=for-the-badge">](/Tutorials/Tools/modders-guide-to-git/git-and-github) [<img align="right" src="https://img.shields.io/static/v1?label=Next&message=Branch+Management&color=2ea44f&style=for-the-badge">](/Tutorials/Tools/modders-guide-to-git/branch-management)
 
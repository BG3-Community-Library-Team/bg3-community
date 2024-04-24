---
title: 4: Branch Management
description: Learn how to handle different states of a codebase using Git
published: true
date: 2024-04-24T05:33:46.992Z
tags: git, github, workspace, organization
editor: markdown
dateCreated: 2024-04-24T05:25:13.608Z
---

# Branch Management
Now that we've gotten our feet wet, let's find out how to perform some of the key actions related to Git. Throughout the article, I've bolded some terms that may be unfamiliar. This is where they come in. We're going to cover topics like **Branches**, **Pushing**, **Pulling**, **Committing**, and **Fetching**. Don't worry if you're not clear on these terms yet, by the end of this section, you'll have a better understanding of what they mean.

## What is a Branch?
From the beginning, we've talked about how Git takes a Snapshot of your codebase, and stores them in a local database. Branches are, effectively the place where these snapshots are stored. Any git repository can have countless branches, or it can have just one.

## Common Branch Actions
So what can you do with a branch? Well, when using Git, there are 6 actions you'll typically perform: **Checking Out**, **Adding**, **Committing**, **Pushing**, **Fetching**, & **Pulling**. In this section, we'll go over what the first three of these mean, and have you practice performing the action.

### Checking out
We now know that a branch is part of a database. So how do we retrieve it? Git has a simple command, `git checkout BRANCHNAME`. If you type this into the command line while in a Git Repository, it will check if a branch with a name matching the input Branch Name exists, and if so, change the state of your local Repository to match the state of the branch you've checked out.

Before we try this out, though, we need another branch. Our Sample-Template only has the one branch, `main`, so how can we test this out? Thankfully, the developers behind Git made this as easy as possible: In Git, checking out a branch covers both existing and non-existant branches. While `git checkout NAMEOFNONEXISTANTBRANCH` will give you an error, they added a flag to the command: `git checkout -b NEWBRANCHNAME`. The -b tells Git that you want to create a new branch based off of the current branch. So let's try this.

1. Open Git in your Sample-Template branch
2. Input `git checkout -b my-new-feature` and press Enter

You're now on your new branch! This is the point where, when working on a project, you would start working on a feature. Patience, though - we'll get to that soon enough. Let's say you wanted to make a different feature as well. We know that making a new branch bases the new branch-to-be off of the current one, so we don't want to be on our current Feature branch, otherwise things will get messy fast. Instead, let's navigate back to the `main` branch, and make a new branch from there:

1. Input `git checkout main` and press enter
2. Input `git checkout -b my-other-new-feature`

Now we've got three branches: The default `main` branch, our `my-new-feature` branch, and our other `my-other-new-feature` branch. And of course, you may be wondering, "Can I swap between my feature branches, or do I need to go back to `main` first? The answer is, you can switch to any existing branch from any other existing branch. Because we're not using `-b` to build a new branch, I can go to `my-new-feature` directly from `my-other-new-feature`, like so:

`git checkout my-new-feature`

Feel free to practice making more branches and swapping between them if you like, then we'll move on to Adding our changes to a branch.

### Adding & Committing
Now we want to add files to our branch. To do this, we'll need to understand how to do two things: Adding files and Committing changes. 

#### Git Status
Before I go into the idea behind these actions, I'm going to introduce you to a new command: `git status`. 

1. Input `git status` into your command line and press Enter

You'll be greeted with the following:
```bash
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

What we just did was check for the status of our current branch. If no files have been added, modified, or removed, this is the message we'll get. Let's take a look at what happens when we add a file.

1. Create a text file in our root `Sample-Template` folder, `Test.txt`.
2. Open it up and type a bunch of random characters (or let your cat step on your keyboard), then save the file.
3. In your command line, enter `git status`

This time, you'll see something like this:

![An image of the output of the git status command, showing a new Untracked Files section containing the Test Text file that was added in the above steps](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/git%20status%202.PNG)

Similar to what we had before, but we can see a new section, "Untracked  files," containing our brand new `Test.txt` file. So what's an Untracked File? Well, we know that Git tracks changes to our codebase in Branches, but what if we haven't submitted any changes to our Branch? Those changes won't be tracked by Git. Those files need to first be **Added**, and then **Committed**. But what if instead of making a new file, we changed one? 

1. Open up Readme.md using your preferred Text Editor/IDE
2. Make a change somewhere in the file - add text or delete a section.
3. In your command line, enter `git status`

Now you'll see this:

![An image of the output of the git status command, showing a new "Changes not staged for commit" section referencing Readme.md](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/git%20status%203.PNG)

Yet another new section has appeared in our status: Changes not staged for **commit**. Files in this section are files that Git is already tracking, but changes have been made to them. In short, Untracked files are files that Git can see, but are not stored in Git. Files with changes that aren't staged for commit *are* already stored in Git, but Git sees that they have been changed. So how do we go about getting our new file tracked, and our modifications stored?

### Git Add
In the prompts we see above after inputting `git status`, Git told us a useful piece of information: `use "git add <file>..." to update what will be committed`. `git add` is a fairly self-explanatory command, but let's take a look at how to use it. First, we'll add our changes to `Readme.md`:

1. In the command line, input `git add Readme.md`.
2. Input `git status` again.

We'll now see the "Changes not staged for commit" section has changed to "Changes to be committed". Readme.md is now green instead of Red. What happens if we do the same for "Test.txt", and input `git status` again?

![The output of the Git Status command, with all changes ready to be comitted](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/git%20status%204.PNG)

`Test.txt` is now inside the "Changes to be committed" section, and is also green.

At this point, let's checkout our `my-new-feature` branch if we aren't already on it - you'll notice that our changes are carrying over - `my-new-feature` is currently identical to our `main` branch, and so Git will let you do this. Typically, you'd want to do this before making any changes. If the branch already had changes, you may be faced with an error about files being overwritten instead, but right now, we don't need to worry about that. Our changes are currently staged for inclusion in git, but they're not in yet, are they? First, we need to perform a `git commit`.

### Git Commit
You've seen this word thrown around quite a bit earlier. Now you finally get to learn what it means: When we submit our changes to git, we're making a commit. This commit is the snapshot of our code mentioned throughout the guide as the core focus of Git. Whenever we want git to know about our changes, we use the command `git commit` after staging our files via `git add`. Now, this has been a massive amount of information to process, so feel free to take a minute to let yourself connect the dots between all these concepts. When you're ready, let's make a commit ourselves.

1. In the command line, input `git commit`

You'll be faced with this:

![The VIM interface shown when using the git commit command](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/git%20commit.PNG)

This is probably the most challenging part of using Git. The default command line text editor it uses is called `vim`. Vim is powerful, fully-featured, and the exact opposite of user friendly, so I'll walk you through what to do here:

<img align="right" alt="The VIM interface shown when using the git commit command, after following the above steps" src="https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/git%20commit%202.PNG">

1. Press the letter `i`.
2. Type in a short, descriptive name of your changes.
3. Hit enter twice.
4. Type in a list of descriptions of your changes, using hyphens(-) as bullet points.
5. Press the `Esc` key.
6. Hold the Shift key and press `Z` twice.

You'll see information in your command line about 2 files being changed, some insertions, maybe some deletion. Congratulations! Your changes are now stored in Git. While this guide won't go into much detail, if you wanted to make a new commit that, for example, deleted our `Test.txt` file, you would simply delete the file, use `git add Test.txt`, and then use `git commit`. Even though the file is being deleted, `git add` adds the change itself.

## Recap
In this section, you learned about branches in Git, how to change branches and create new ones. You also learned how to check the status of a branch, and add and commit new files and changed files to Git. In the next section, we'll look at Remote interactions - Fetching, Pulling, and Pushing.

---


[<img align="left" src="https://img.shields.io/badge/Previous-Working_With_repositories-blue?style=for-the-badge">](/tools/modders-guide-to-git) [<img align="right" src="https://img.shields.io/static/v1?label=Next&message=Remote+Branch+Management&color=2ea44f&style=for-the-badge">](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/wiki/_Modders-Guide-to-Git:-Remote-Branch-Management)

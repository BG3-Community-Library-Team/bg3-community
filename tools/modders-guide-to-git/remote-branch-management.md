---
title: 5. Remote Branch Management
description: Learn how to handle pushing your code to Github
published: true
date: 2024-04-24T05:36:11.097Z
tags: git, github, workspace, organization
editor: markdown
dateCreated: 2024-04-24T05:25:26.244Z
---

# Remote Branch Management
By this point, you've learned the basics of Git. You can manage a local Branch in your Repository, , make changes, and get them stored in Git. Now it's time to bridge your knowledge of GitHub with your knowledge of Managing Branches. Let's get started!

## Remote Actions
In this section, we'll cover the **Fetch**, **Pull**, and **Push** actions, as well as how to fork a mod.

### Forking
We'll start this part of the guide off by forking Sample-Template. Previously, we've cloned it down, and made our own branches, but now we need to figure out how to get things to and from GitHub. To start us off, we'll go to the [Sample-Template](https://github.com/BG3-Community-Library-Team/Sample-Template) GitHub Project, and fork it down.

1. On the Sample-Template GitHub page, hit the "Fork" button.
2. On the Form that appears, hit "Create Fork."

So, we've "Forked" the Sample-Template, but what does that even mean? You've probably heard the phrase, "A fork in the road." One path diverging into two. That's the idea between forking in Git. By forking the Sample-Template Repo, you've created our own Repository on GitHub, based on a specific branch of Sample-Template. You have the option to import future changes to the original Repository into your forked one, that won't happen by default - you are steering the wheel of this version.

Now, in your file manager, delete the Sample-Template folder you have, and in your Git Guide folder, clone down your Forked version of Sample-Template. Now you're ready for the next step: Fetching and Pulling. 

### SSH Keys
Did I say you were ready? Well, not quite. Git requires you to use SSH Keys, a kind of security protocol, when you want to work with remote Repositories. I won't go into this much, but if you don't add SSH keys, you won't be able to continue, so click on the image below to see a well-done video on setting those up:

[![Link to Git For Everybody's SSH Key Tutorial](http://img.youtube.com/vi/Z3ELWci34cM/0.jpg)](https://www.youtube.com/watch?v=Z3ELWci34cM "Git for Everybody: Creating and adding your SSH Key (Windows, Mac and Linux)")

### Fetching and Pulling 
Alright, *now* we're ready. In your GitHub repo (not your local cloned-down Repo), scroll over to the "Readme" section, and hit the pencil icon in the upper right to edit the ReadMe remotely. Like we did when we were learning about adding and committing files, make some random changes, and then click on the icon that says `Commit Changes`. A window will appear, asking you to ender an extended description - you can ignore this, and just click the `Commit Changes` button in the window.

Now that we've done this, we're in a tricky situation. The files in the Remote Repository are different than the ones in our Local Repository. Won't htis cause issues when I want to push? The short answer is: Yes, yes it will. But we can get around that with two steps: Fetching and Pulling.

1. Go to your command line in your local Repository
2. Enter `git fetch`

You'll see some information appear, informing your local Repository of changes having been made. The changes you made remotely are now tracked by Git, but if you check your ReadMe file, you'll notice the changes haven't been applied to your local Repository yet. `git fetch` is a command designed to fetch the information from a Remote Repository, and inform your Local Repository of any changes. Now for the next command:

1. Enter `git pull`

Now check out your ReadMe. The changes you made on GitHub are now present on your local Repository. `git pull` tells your Local Repository that you want your local Branch to match its counterpart on the Remote Repository. Overall, a simple concept. You'll want to do this regularly, if you're working collaboratively, as Git works best when your branches are up-to-date. Otherwise, you run the risk of conflicts.

Before we head to the next section, in your local Repository, make a new branch. Change some files, add or delete things, go wild. Finally add and commit your changes. 

### Git Push
So, you have your own local repository of your Forked branch. You've made some changes, and even committed them. Now you want to send them up to GitHub, so you can access them elsewhere, back them up, or easily show them to or collaborate with others. This is where Pushing comes in.

1. In your command line, enter `git push`

You'll likely get an issue here, something about setting upstreams. At this stage, git doesn't actually know where you're trying to push this branch. The remote repository only has the `main` branch, so it doesn't know about your new branch. Let's try this again, with what it requests us to use:

1. In your command line, enter `git push --set-upstream origin BRANCHNAME`

Now, let's break this down. 
- `git push`, of course, is the command we're trying to call. 
- `--set upstream` is a flag that tells Git, "I want to send this push to this branch on this remote repository." 
- `origin` is the default title of our remote repository. A local repository can push to multiple remote repositories, referred to as `remotes`. Right now, we're only concerned with our fork, which, since we've cloned from our fork, is `origin`, as far as Git is aware.
- `BRANCHNAME` must be defined, or Git still won't understand where to put this branch.

Now, navigate to your Fork on GitHub, and you'll see a banner saying that recent changes have been made. If you click on this, GitHub will give you the option of creating a Pull Request. If you instead select the branch selector, you'll see your branch there. Click on it, and you can confirm the changes you made have made their way to the remote repository.


## Recap
In this section, we learned how to Fork a Repo. We also learned how to add SSH keys to our GitHub account, and Fetch, Pull, and Push to and from our Remote Repository.

---

[<img align="left" src="https://img.shields.io/badge/Previous-Branch_Management-blue?style=for-the-badge">](/tools/modders-guide-to-git/branch-management)
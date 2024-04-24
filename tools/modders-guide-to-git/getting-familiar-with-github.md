---
title: A Modder's Guide to Git
description: Getting Familiar with Github
published: true
date: 2024-04-23T22:34:06.928Z
tags: git, github, workspace, organization
editor: markdown
dateCreated: 2024-04-23T22:34:04.842Z
---

## The GitHub UI
Let's take a minute to look at the GitHub UI. Feel free skip forward until the [Cloning The Repo](#cloning-the-repo) section if you want.

### The GitHub UI: Header
![GitHub UI: Header - Shows the Tab bar for GitHub, specifically the tabs titled "Code," "Issues," "Pull Requests," "Security," "Insights," and "Settings"](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/GitHub%20Header.PNG)

The first thing to pay attention to here is the Header. At the top of the screen, you'll see the author & name of the Repository, in this case, "BG3-Community-Library-Team" and "Sample-Template." Beneath that, we can see a few sections, `Code`, `Issues`, `Pull requests`, `Security`, `Insights`, and `Settings.` What are these tabs for?

- ***Code:*** This is the default section. It will show a section containing the code in your Repository, what **branches** are available, an "About" section, and the Readme file, if any.
- ***Issues:*** This tab will open up a new page, showcasing any issues or feature requests that may exist.
- ***Pull requests:*** Similarly to Issues, this opens up a new page, showcasing any **Pull Requests**, which are contributions to your mod, either from other modders, or from your own separate branches.
- ***Security:*** This page shows the security policies set for the Repository.
- ***Insights:*** This won't be important for most, but for data nerds, it'll be an interesting place to check out statistics about your Repository.
- ***Settings:*** This details the settings available for your Repository

---
### GitHub UI: Actions
![Image shows the Actions bar on GitHub, specifically the buttons titled "Edit Pins," "Watch," "Fork," and "Star."](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/GitHub%20Actions.PNG)

Here you'll see a few actions: `Watch`, `Fork`, and `Star`. The `Edit Pins` button appears only on your own uploaded Repositories.

- ***Edit Pins:*** This allows you to pin the Repository to your GitHub profile, either publicly or privately, to make it easier to access the Repo.
- ***Watch:*** Let's you keep an eye on the Repository, tracking updates on your GitHub homepage.
- ***Fork:*** This effectively duplicates the Repository under your account - useful when you want to use the Sample Template as a basis for your own mod, or if you want to contribute to another project. More on Forks in a bit.
- ***Star:*** Starring a Repository is kind of like bookmarking it, and shows support for the Repo.

---
### GitHub UI: Contents
![Image shows the Contents section of the Code tab on GitHub - specifically the Branch Selector, the "Go to file," "Add file," and "Code" buttons, and the Contents of the currently selected branch.](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/GitHub%20Contents.PNG)

The Contents section is the main part of the page you'll typically see. This has several components to it: The **Branch** Selector, a list of branches and tags, the `Go to file`, `Add File`, and `Code` buttons, a banner showing the latest **commit**, as well as the list of latest commits, and then a view of all the files within currently selected branch of the Repository.

- ***Branch Selector:*** We haven't discussed Branches directly yet, but we've seen the idea of them earlier in the article. As mentioned when talking about Version Control and Git, the idea is that you save snapshots of your code in a database to easily retrieve later. Branches themselves are snapshots of your code at a certain point. You can have multiple branches at a time, with different additions and subtractions your codebase as a whole. `main` is typically the default branch, and if other branches exist, you'll be able to see what the codebase looks like in those branches by selecting a different Branch from the selector

- ***Go to file:*** The Go to File button opens up a new page in your Repository, allowing you to search for specific files throughout the Repository and all its branches.

- ***Add file:*** This button gives you the option to create a brand new file, or upload files from your computer. Typically, you won't need or even want to use this, as Gitbash, which we installed earlier, is much easier to work with.

- ***Code:*** This green button opens up a dropdown, giving you the ability to **Clone** the repository(more on that in a minute), open with GitHub's Dekstop Application, or download it as a `.zip` file. Typically, you'll just use it to clone the repo or to get what's called the **remote**: that URL in the center of the dropdown. There's different sections for HTTPS, SSH, and GitHub CLI. For this guide's purposes, we'll stick with the SSH section.

- ***Commits:*** Beneath the section we just talked about it a header, displaying the username of the last person to make a chane, a description of what was changed, and a "# commits" link that will allow you to see the complete change history of the Branch.

- ***Contents:*** Finally, below the Commits header, you can see and navigate through all the files and folders in the repository, be they Code, Images, or even just Readmes.

---
### GitHub UI: Readme
![Image shows the ReadMe of the Sample-Template Project on GitHub](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/GitHub%20ReadMe.PNG)

Finally, we have the Readme. In any Repository, you'll often find a file called `Readme.MD` (Note: `MD` means `MarkDown`, a type of syntax that GitHub supports, which makes it easy to format text for display online). This section of the UI auto-loads the Readme file, so anyone can, at a glance, get an idea of how to use the project.

---
### GitHub UI: Sidebar
<img align="right" src="https://github.com/BG3-Community-Library-Team/BG3-Community-Library/blob/main/WikiRes/Git/img/GitHub%20Sidebar.PNG" alt="Image shows the sidebar of a GitHub Project">

The Sidebar shows useful details about the Repository - A link to a readme and the current license of the project, if any, a link to the list of commits for the project, the amount of stars, watches, and forks, and a link to the latest Release of the project. You may have noticed that many of these are easy to find across the rest of the UI, but they're all placed here for ease-of-use. Whether you're using GitHub for your own project, or viewing another person's project, this is one of the key areas to pay attention to.

The link to the latest release will bring you to a new page, with links to the  source code, as well as any attached files. There may also be a "Packages" section beneath Releases, but in the case of BG3 modding, this section will typically not be used.

---
<p align="center">

[<img src="https://img.shields.io/badge/Back_To-Working_with_Repositories-orange?style=for-the-badge">](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/wiki/_Modders-Guide-to-Git:-Working-with-Repositories)
</p>
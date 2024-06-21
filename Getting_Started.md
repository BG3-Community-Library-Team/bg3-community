---
title: Getting Started
description: If this is your first dive into modding BG3, this is a good place to start!
published: true
date: 2024-06-21T02:39:31.066Z
tags: 
editor: markdown
dateCreated: 2024-06-21T01:23:16.004Z
---

# Intro

Jumping into modding baulders gate 3 can be a daunting task, especially if you dont have any background doing such things. The reality though is that you can get started really quite easily. The key is getting started though. Its hard to know where to being and what you need. This page is designed to help you get started with modding baulders gate 3 from scratch.

# Starting Knowledge
This guide is intended to be able to be followed with no knowledge of baulders gate 3 modding, but you will need some basic computer skills such as making folders, making files, etc. Will maybe flesh this out more but assuming if you are undertaking the task of modding you probably have as least know knowledge of this and computers.

# Environment Setup
When working on your mod you will want to set up a good space to work in and keep things organized, ie an enviroment. Setting up an enviorment or project folder in the most simple terms would be to just make a folder that will house all the future mods you plan on making as well as getting the tools we will need readily available. I wont cover how to use the tools here, rather just how to get them setup. For usage see further below or their respective pages.

*Many of these tools get updated regularly. Make sure you are getting the most recent stable release. Note images and instructions may be from previous versions but should typically follow the same structure.

1. Create a folder on your desktop named bg3_mods (or anything you want, but I will be calling mine bg3_mods if you want to follow along). You could technically just make a folder of your mods name but if you intend to make more mods in the future it would be better to make this bg3_mods folder and place all mod folders in here for better organization.
2. Download visual studio code from https://code.visualstudio.com/download. You can use whatever code editor you want, but I will be using visual studio code when dealing with my files and showing examples below.
3. Download the bg3 mod manager from https://github.com/LaughingLeader/BG3ModManager/releases. As the name suggests, it will help you manage your mods 👍. The page includes install and setup instructions so I will not include them here, follow them there where they will be up to date.
4. Download the mod fixer from https://www.nexusmods.com/baldursgate3/mods/141. Character creation bugs out without this. Will explain how to use below, simply download for now and extract the .pak.
5. Download the bg3 modders multitool from https://github.com/ShinyHobo/BG3-Modders-Multitool/releases. This tool has alot of uses but we will cover them as we need them. Download and extract the files for now.
6. Download LSLIB and the export tool from https://github.com/Norbyte/lslib/releases. Like the multitool, many uses we will cover later. Download and extract the files for now.
7. We should have a few file explorer windows open now from extracting folders and creating them. Here they are and what to do with them:
   1. bg3-modders-multitool : Create a shortcut of the bg3-modders-multitool application and move it to bg3_mods folder. Then move the entire bg3-modders-multitool to bg3_mods.
   2. BG3ModManager_Latest : Create a shortcut of the BG3ModManager application and move it to bg3_mods folder. Then move the entire BG3ModManager_Latest to bg3_mods.
   3. ExportTool-v{whatever version number its on} : Go one directory deep by clicking on ExportTool-v{whatever version number its on}. Create a shortcut of the ConverterApp application and move it to bg3-mods folder. Take the entire folder you are currently in, ExportTool-v{whatever version number its on}, and move it to bg3-mods.
   4. bg3_mods : We are getting all the tools we need into on spot, this folder. It would be wise to add vscode into here as well but there are other better ways to access it which I cover below when we get into working with the tools.

*Again, it doesn't need to be like this, it's just how I work with it. If you understand file structures well, do what is comfortable to you.

Here is how they look before I moved everything around:
![268487717-6c8a580d-455a-4013-b6c2-e9c58ec55578.png](/tutorials/getting_started/268487717-6c8a580d-455a-4013-b6c2-e9c58ec55578.png)

With all the files/folders moved, the only folder we should need atm is bg3-mods. Here is what it looks like now:
![268488734-0c6119b4-2f0a-4b3b-a9e5-85ec7c9fd9b1.png](/tutorials/getting_started/268488734-0c6119b4-2f0a-4b3b-a9e5-85ec7c9fd9b1.png)

*<sub>This isnt that important but something I did to help speed things up. Use your quick access window on the windows file explorer. I pinned alot of my folders to the file explorer quick access window that I plan to open alot.</sub>


# Learn About/Prepare Your Tools
Hopefully you have everything set up correctly and you have a folder structure similar to the image shared above. Before we create the most simple/basic mod ever we still have a few things to learn such as the various tools you just downloaded. I will only cover the basics/essentials of these tools since reading their own documentation would be more useful. But for those looking to just get started, this would be a good place to refer to regarding the tools

## LSLIB/Converter App
LSLIB is critical when it comes to modding baulders gate. Created and still regularly updated by Norbyte, the export tool we downloaded in step 6 in enviorment setup is the most important thing you will need when getting started on your modding journey.






# Ignore this
Most people who are starting their modding journey have probably already installed mods before. On the off chance you have not, here is an important one to install which will while ensure that we have things set up right while learning how to install a mod. If you have not already, extract the mod fixer folder you downloaded from nexus. There should be a readme in there to explain what to do with the .pak in there but if not, open up your mods folder for bg3. You can find this folder by holding the windows key and pressing r. In the window that opens up, enter %LocalAppdata%\Larian Studios\Baldur's Gate 3\Mods which will take you to the mods folder. Drop the ModFixer.pak in. If you open up the mod manager you should see the mod fixer is in, at the bottom left. You may need to hit refresh.
---
title: Getting Started
description: If this is your first dive into modding BG3, this is a good place to start!
published: true
date: 2024-06-21T01:23:16.004Z
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
4. Download the mod fixer from https://www.nexusmods.com/baldursgate3/mods/141. Character creation bugs out without this.
   1. You need to get the mod fixer working with the mod manager. You can open the mod manager and drag the mod fixer to it or drop the mod fixer in the Mods folder for baulders gate 3 found in %APPDATA%
5. Download the bg3 modders multitool from https://github.com/ShinyHobo/BG3-Modders-Multitool/releases. This tool has alot of uses but we will cover them as we need them. Download and extract the files for now.
6. Download the export tool from https://github.com/Norbyte/lslib/releases. Like the multitool, many uses we will cover later. Download and extract the files for now.
7. We should have a few file explorer windows open now. Here they are and what to do with them:
   1. bg3-modders-multitool : Create a shortcut of the bg3-modders-multitool application and move it to bg3-mods folder. Then move the entire bg3-modders-multitool to bg3-mods.
   2. BG3ModManager_Latest : Create a shortcut of the BG3ModManager application and move it to bg3-mods folder. Then move the entire bg3-modders-multitool to bg3-mods.
   3. ExportTool-v{whatever version number its on} : Go one directory deep by clicking on ExportTool-v{whatever version number its on}. Create a shortcut of the ConverterApp application and move it to bg3-mods folder. Take the entire folder you are currently in, ExportTool-v{whatever version number its on}, and move it to bg3-mods.
   4. bg3-mods : Create a folder that has the name of your mod. As I mentioned above, the example we will be doing later will be for creating a class called Quickster, so I will be naming my folder Quickster.

*Again, it doesn't need to be like this, it's just how I work with it. If you understand file structures well, do what is comfortable to you.

Here is how they look before I moved everything around:
![img 1](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/6c8a580d-455a-4013-b6c2-e9c58ec55578)

With all the files/folders moved, the only folder we should need atm is bg3-mods. Here is what it looks like now:
![img 2](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/0c6119b4-2f0a-4b3b-a9e5-85ec7c9fd9b1)

We have one more thing to take care of (and a very useful but optional step too). Extract the mod fixer folder you downloaded from nexus. There should be a readme in there to explain what to do with the .pak in there but if not, open up your mods folder for bg3. You can find this folder by holding the windows key and pressing r. In the window that opens up, enter %LocalAppdata%\Larian Studios\Baldur's Gate 3\Mods which will take you to the mods folder. Drop the ModFixer.pak in. If you open up the mod manager you should see the mod fixer is in, at the bottom left. You may need to hit refresh.

This isnt that important but something I did to help speed things up. Use your quick access window on the windows file explorer. I pinned alot of my folders to the file explorer quick access window. If anything at least pin your Mods folder (where we placed ModFixer.pak) since everytime we make changes to our mod and pack it up again, we will need to drop off the pak in the mods folder, so pinning it helps speed up an action you may find yourself repeating alot. Think of that when it comes to pinning and setting up in general. The goal is make the process and fast and efficient as possible. We shouldnt be wasting our time running around looking for files, that time should be commited to crying about why your mod isnt working :)

Great, I think we are ready to go. Jump over to [class creation](https://github.com/ghostboats/bg3_modders_guide/wiki/Class-Creation) to start modding. Remember to check out file insights to understand what sort of options you have when messing around with your files. Good luck, you got this👍 

# Learn About/Prepare Your Tools
TODO
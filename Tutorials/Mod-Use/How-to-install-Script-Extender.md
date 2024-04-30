---
title: How to install Script Extender
description: 
published: false
date: 2024-04-30T11:01:34.949Z
tags: 
editor: markdown
dateCreated: 2024-04-30T09:59:44.829Z
---

# How to install Script Extender 

This is a guide that covers how to install Script Extender (SE for short) correctly, and from where. 
This guide will also cover well known information in the mod author communities, that many mod users may not know but should know about. 

## Why you should not download the Script Extender from Nexus: 
Do not download the SE from Nexus. This was not uploaded by Norbyte. It was uploaded by someone who had DP (Donation Points) turned on. Donation Points can be exhanged to real life money. 

The same goes for different configs such as "achivements enabler for script extender" settings on Nexus. These are native to SE and is turned on by default. 
For more information, see Norbyte's Script Extender readme: https://github.com/Norbyte/bg3se/blob/main/README.md

Some discord servers has taken an active stance and does not support the Script Extender on Nexus. BG3 Modding Community is one of them.

## 1: How to download Script Extender

There are two ways on how to download script extender. 

##### 1.1 First is the easy way if you are using BG3MM: 

(Screenshot)

As seen above screenshot, simply open BG3MM, then go up in the bar and press on "tools" and then press "Download and extract Script Extender". 

##### 1.2 Second way is the little harder, but still easy way if you are not using BG3MM but is on linux, or using Vortex. 

First you will need to download it from Github: https://github.com/Norbyte/bg3se/releases/tag/updater-20240329
Do not worry about the version on github. As it will be explained later in the guide, SE updates to the newest version when you launch the game.

When you open the page, scroll down and press the "BG3SE-Updater" as highlighted below. 
(Screenshot) 

When you have downloaded the zip file from Github, you will need to navigate to your bin folder.

If you do not know how to find your bin folder, here is a small quick guide: 

Open your steam library, or if you use GOG, you will need to do the equivalent. 
When you have opened the steam library, right click on BG3 and hover over "manage", and click on "Browse local files" as highlighted below. 

![steam.png](/tutorials/steam.png)

File explore will open your "root installation" folder. 

It should look something like this: 

![bg3_folder.png](/tutorials/bg3_folder.png)

> For GOG users, it may look a bit different. This is okay, and normal. 
{.is-info}

Now just open the bin folder, and then you extract the "DWrite.dll" into the bin folder, that is inside the zip folder you just downloaded. 

The DWrite.dll is essentially SE.

(Screenshot)

## 2. Install Script Extender

When you have downloaded SE, you have not installed it. 
SE installs on launch of the game to main menu. 
It also auto updates on launch of the game, when Norbyte pushes out an update for SE, so you do not need to worry about the version you download and you do not need to worry about updating the Script Extender. 

However, during patches you may need to wait a bit for the update and remove SE until it has been updated again. 
This page will be updated if that happens. 

You will know if you have been successful if you open the game to main menu, and look at the bottom left and see "Script Extender version x built on date x" as you can see at the below screenshot: 

(Screenshot) 

## 3. How to install the console 

Depending on if you are using BG3MM or not, there are a few ways to enable the console. 

##### 3.1 How to enable the console via BG3MM 


## But I do not want SE to auto update for me because xyz? 

It is generally not a good idea to roll back on a SE update or stop the updates for SE. Here is a few reasons why: 

When you stop the updates, you can very quickly get locked into one version only so when even you uninstall SE and reinstall it again, it cannot update. This causes issues if you update the game, and SE needs to update to be compatible with that game version. 

To fix this, you will need to follow this guide: (Link to guide on how to do a clean/fresh reinstall of SE) 

Some mods will end up not working, as they are getting updated and ends up needing a later version of SE than what you have. This is a huge risk you will have to keep in mind. 

## Compatibility issues

You may be surprised, but SE does have a few compatbility issues. 

1: Achievements enabler on Nexus. 
This is because SE by default has turned on achievements and those two will end up conflicting, and either SE or achievements enabler will end up being deactivated, and you may experience issues with getting achievements.
You may end up not being able to start the game if you have both. To fix this, delete achievements enabler. It should sort itself out. 

If it does not, and you use BG3MM, simply open BG3MM, go to "settings", then "preferences" as highlighted below: 

(Screenshot)

Then go into the tab "Script Extender" and check off "Enable achievements". 
It may be checked on already, 



 

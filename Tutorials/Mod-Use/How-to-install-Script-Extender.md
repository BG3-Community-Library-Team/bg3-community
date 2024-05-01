---
title: How to install Script Extender
description: 
published: true
date: 2024-05-01T01:50:27.954Z
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

![bg3mmse.png](/tutorials/bg3mmse.png)

As seen above screenshot, simply open BG3MM, then go up in the bar and press on "tools" and then press "Download and extract Script Extender". 
Continue to step 3 after this. 

##### 1.2 Second way is the little harder, but still easy way if you are not using BG3MM but instead uses linux, or using Vortex. 

First you will need to download it from Github: https://github.com/Norbyte/bg3se/releases/tag/updater-20240329
Do not worry about the version on github. As it will be explained later in the guide, SE updates to the newest version when you launch the game.

When you open the page, scroll down and press the "BG3SE-Updater" as highlighted below. 

![se.png](/tutorials/se.png)

> For Linux users, follow the guide on Norbyte's github page (link above) instead of this guide.
{.is-info}


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

So it goes from this: 

![movese.png](/tutorials/movese.png =x400)

To this:

![semoved.png](/tutorials/semoved.png)

## 2. Install Script Extender

When you have downloaded SE, you have not installed it. 
SE installs on launch of the game to main menu. 
It also auto updates on launch of the game, when Norbyte pushes out an update for SE, so you do not need to worry about the version you download and you do not need to worry about updating the Script Extender. 

However, during patches you may need to wait a bit for the update and remove SE until it has been updated again. 
This page will be updated if that happens. 

You will know if you have been successful if you open the game to main menu, and look at the bottom left and see "Script Extender version x built on date x" as you can see at the below screenshot: 

![mainmenuse.png](/tutorials/mainmenuse.png =x500)

For BG3MM to register you have installed Script Extender: Open game to main menu, close the game, and refresh in BG3MM. 

## 3. How to install the console 

Depending on if you are using BG3MM or not, there are a few ways to enable the console. 

##### 3.1. How to enable the console via BG3MM 

Open "Settings", then "Preferences" in BG3MM. 

![settings.png](/tutorials/settings.png)

Then click on the tab "Script Extender" and check off "Create Console". 

![createconsole.png](/tutorials/createconsole.png =x350)

##### 3.2. Create the ScriptExtenderSettings.json file yourself 

Best way to do this, is to go inside your bin folder then click "create new" and choose txt file: 

(The PC is in another language, however it will look the same but the words will be in your own language.)
![newtxt.png](/tutorials/newtxt.png =x450)

Now rename that txt as: `ScriptExtenderSettings.json` 
This means remove the last txt in the file (you may need to have show file extensions on. I will show below how to do it on windows 11, otherwise if you do not know how to do it in your system, there are tons of guides on google): 

![fileextension.png](/tutorials/fileextension.png =x470)

It should end up looking like this:

![jsonfile.png](/tutorials/jsonfile.png)

When you have done that, you will need to open up the json file (right click, open with NotePad, VSCode or any other program that can open json files. NotePad should natively be on your Windows PC)
You will need to paste this into the json file, and save it: 

{
  "CreateConsole": true
}

You should be able to use programs such as VSCode, NotePad++ or simply just notepad. I will show screenshots from both VSCode and Notepad to show how it may differ in looks but is still the same no matter which program you use: 

VSCode: 

![createconsolevscode.png](/tutorials/createconsolevscode.png)

NotePad: 

![notepadse.png](/tutorials/notepadse.png)


> Check this guide out on how to use the console and getting started with using Script Extender for mod creation: https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted
{.is-info}


## But I do not want SE to auto update for me because xyz? 

It is generally not a good idea to roll back on a SE update or stop the updates for SE. Here is a few reasons why: 

When you stop the updates, you can very quickly get locked into one version only so when even you uninstall SE and reinstall it again, it cannot update. This causes issues if you update the game, and SE needs to update to be compatible with that game version. 

To fix this, you will need to follow this guide: (Link to guide on how to do a clean/fresh reinstall of SE, to do)

Some mods will end up not working, as they are getting updated and ends up needing a later version of SE than what you have. This is a huge risk you will have to keep in mind. 

> If you are worried about not being up to date on BG3 and you want SE to stay on the latest version for the patch you are on; Do not worry, SE will only update if you also update the game. 
> So lets say BG3 updates, you did not update and Norbyte pushes out a new update for SE to make it compatible with the new update, then SE will stay on the version you are currently on as it detects you are not on the latest patch.
{.is-info}


## Compatibility issues

You may be surprised, but SE does have a few compatbility issues, mainly with Native Mod Loader mods (not Native Mod Loader itself). 

1: Achievements enabler on Nexus. 
This is because SE by default has turned on achievements and those two will end up conflicting, and either SE or achievements enabler will end up being deactivated, and you may experience issues with getting achievements.
You may end up not being able to start the game if you have both. To fix this, delete achievements enabler. It should sort itself out. 

If it does not, and you use BG3MM, simply open BG3MM, go to "settings", then "preferences" as highlighted below: 

![enableach.png](/tutorials/enableach.png =x400)

Then go into the tab "Script Extender" and check off "Enable achievements". 
It may be checked on already. If that is the case, simply just uncheck it and check it again. 

If you do not use BG3MM, you can go on Norbyte's Script Extender Readme and copy paste the command: 

{
  "EnableAchievements": true
}

Paste this into the ScriptExtenderSettings.json (look at the above, 3.2: how to create the ScriptExtenderSettings.json file for yourself.) 

2: Camera Tweaks 
Some have experienced issues with having SE and Camera Tweaks at the same time. 
Camera Tweaks have one temporary solution on their posts on Nexus: https://www.nexusmods.com/baldursgate3/mods/945?tab=posts

For some it may work, for some it does not. It seems to be a hit and miss, and both creators are trying to make it work together.

## I have heard Devel version will fix all my problems!!!! (No, it will not!) 

Fun fact, contrary to popular belief: Devel version is actually harmful to your game if you do not know how to use it, and will not fix your mod issues. 

First and foremost, what is the devel version? 
The Devel version is a branch of SE. However, think of it as early development branch of SE. Think of it as an earlier development than Alpha developments. This is because the devel version is the version where Norbyte tests functions, and develop functions that are going to be released in the next offical releases. 

This means the devel version is very expiremental and if you, as a user, is playing the game while using the devel version, and Norbyte is testing Virtual Textures but accidently breaking them in the process, you can experience crashes, bugs such as weird textures on your tavs, companion etc, console not responding, console flashing red, spam in the console, spam in the game, game not responding, game not starting, and many more. 

Most of the time, the devel version is a version behind the main release. For good reasons as this is a playground for testing. 

Norbyte even created a warning but unfortunately it does get suppressed by mods such as Improved UI: 

![sedevelwarning.png](/tutorials/sedevelwarning.png =x600)

You can check if you have the devel version by going into your bin folder and search for this file: 
`ScriptExtenderUpdaterConfig.json`

If you do have it, delete it. 

It should not be confused with the console json file which is named: `ScriptExtenderSettings.json`

> Devel version is for Norbyte and experienced mod authors only. Usually that is if a mod author is working on something using SE, and Norbyte personally tells the mod author "oh hey, this is on the devel version set to release in this update, so go on the devel version to use this function."
{.is-warning}

## Now that I have Script Extender, do I still need Mod Fixer? 

Yes you do. 
Mod fixer prevents durge harem instead of character creation. 
Mod fixer also prevents the issue of not being able to talk or interact with anything if you are in the middle of your playthrough. 

*"But I heard that Mod fixer has so many issues?"*
Yes but no. It is a complicated issue but Mod fixer is very essential but it is best used with SE. 

## Other relevant guides and credits:
Using the console and using Script Extender for mod creation: https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted

How to install BG3MM, mods and manual/loose file mods: 
Part 1: How to install BG3MM: https://wiki.bg3.community/Tutorials/Mod-Use/Installation-Of-BG3MM
Part 2: How to install pak files: https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-Install-Pak-Files
Part 3: How to install loose file mods: On to do 

How to do a fresh reinstall of SE: To do
How to install Native Mod Loader and Native Mod Loader mods (Camera Tweaks, WASD Movement etc.) To do 
How to install Unique Tav: To do 

Made by: Maze 
Credits: Satan, Norbyte, Kaz

 

---
title: VSCod(e/ium) Extension
description: an extension for VSCode and VSCodium by @khbsd and @ghostboats that has lots of helpful features for modders.
published: true
date: 2024-05-22T16:27:42.407Z
tags: vscode, vscodium, bg3-mod-helper, tool, tools, ghostboats, khbsd
editor: markdown
dateCreated: 2024-04-25T01:43:35.054Z
---

# BG3 Mod Helper - A VSCod(e/ium) Extension
Created by ghostboats and khbsd, this VSCode extension is designed to help mod authors speed up their mod creation workflows. The extension has multiple useful utilities that include but are not limited to:
- **Mod Packing/Unpacking**
- **UUID/Handle Generation**
- **UUID Mapping**
- **Handle Management**
- **LSX/XML/LOCA/ETC File Conversions**
- **Generate Mod Templates**
- **And More!**

While the extension is still receiving regular updates, it's at a stable point where it can be very useful to mod authors and save them a lot of time. It is built off the philosophy of being able to mod without having to tab out as often while requiring as few clicks as possible to get the job done. It has saved us a lot of time, and I hope it can do the same for you!

> **Goal:** The goal of this wiki is twofold: provide documentation for [mod authors](#mod-authors-guide) and [developers (coming soon)](#) who may wish to contribute/fork their own version.

## Table of Contents
1. [File Locations](#file-locations)
2. [Requirements](#requirements)
3. [Mod Authors Guide](#mod-authors-guide)
	1. [Limitations](#limitations)
	2. [Download Guide](#download-guide)
	3. [Getting Started](#getting-started)
	4. [Setup Extension Settings](#setup-extension-settings)
	5. [Features and Usage](#features-and-usage)

### File Locations 📂
- [Github (source code)](https://github.com/ghostboats/bg3_mod_helper)
- [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper)

### Requirements
- [Visual Studio Code](https://code.visualstudio.com/)
- [LSLib](https://github.com/Norbyte/lslib/releases)

> **Note:** Previous versions of the extension required direct use of `divine.exe`. This has since been replaced with [LSLib](https://github.com/Norbyte/lslib/releases). Make sure your path now points to the directory containing `lslib`. Likewise, previouse versions of the extension required python and some external modules (ImageMagick, PIL, etc). This has ll been removed and only the above is required

# Mod Authors Guide

## Limitations
Nothing is perfect, lets get the rough stuff out of the way before we start to possibly save you time incase this extension is not what you are looking for.
- Unable to work with multiple workspaces in one vscode window
- Unable to edit pngs/dds in vscode (can resize, convert, generate atlas texture, and apply backgrounds to transparent pngs though)
- Buggy when having other folders within your workspace
- Buggy when using multiple vscode windows (need to confirm)
- Possible lag due to folder/file size (need to confirm)
- No references to base game uuids/handles (coming soon?)

<sub>Being on this list doesnt guarentee that it will or will not be possible in the future. Just that it is unlikely</sub>

## Download Guide
There are several ways to download the extension, but below is the easiest method.
1. Open VS Code
2. Click on the `View` tab on the top ribbon
3. Click on `Extensions`
4. In the `Search Extensions in Marketplace` search box, enter `bg3`
5. Click `Install` on the correct extension (bg3_mod_helper)

![installextension-ezgif.com-optimize.gif](/tutorials/bg3-mod-helper/installextension-ezgif.com-optimize.gif)

> It is recommended that you restart vscode after installing. In fact, you should restart vscode everytime you change your workspace for ensurance.
{.is-warning}

## Getting Started
After installing the extension, you will most likely see a message like this:

![error_message_on_start.png](/tutorials/bg3-mod-helper/error_message_on_start.png)
or this:
![no_workspace_set.png](/tutorials/bg3-mod-helper/no_workspace_set.png)
in the bottom right of vscode, especially if this is your first time using the extension.

There are a few quick setup steps that the extension requires to be in a working state, namely adjusting the paths in the extension's settings. I cover that [below](#setup-extension-settings) but first lets properly get a workspace set up so you can utilize all the features of the extension. The extension is designed to launch right when you start vscode (once you have installed).

> While the extension doesnt do anything while sitting in the background, it is technically always on. This shouldnt hinder your other non modding projects but its just good practice to disable or delete the extension if you dont plan on using it anymore or not for a while.
{.is-info}


The key working with the extension is setting up a workspace. There are a few different ways to do it but here is the simplest and safest.

0) Optional but recommended you close all other vscode windows.
1) Open a new vscode window and make sure no previous workspace is open. Your explorer tab should have options like this picture. You will need to press `Open Folder`.
![blank_workspace.png](/tutorials/bg3-mod-helper/blank_workspace.png)
2) The extension is designed to have what would be the "Shared" folder as your mods workspace. So when you select `Open Folder`, you should select the folder that contains your Localization, Mods, and Public folder as your workspace folder. You should see the message below if you have opened up your workspace correctly (and have your settings set up which I cover in the section below)
![no_workspace_set.png](/tutorials/bg3-mod-helper/workspace_set.png)

> VSCODE QUICK TIP: In Windows, you can pin vscode to your taskbar and simply right click on it. This will give you the option to open previously opened workspaces right away or open an empty workspace. Also, it is possible to add an `Open with Code` option when right clicking a folder on your desktop (or anywhere) to instantly open and add a folder to vscode. Its useful to learn these methods should you swap between mod folders alot. More info and possible steps [here.](https://stackoverflow.com/questions/37306672/visual-studio-code-open-with-code-does-not-appear-after-right-clicking-a-folde)
{.is-info}

## Setup Extension Settings
As I mentioned, if it is your first time using the extension (or perhaps some error on loadup which could be other unrelated issues) you may see the image below when you install and open up vscode or a workspace.

![error_message_on_start.png](/tutorials/bg3-mod-helper/error_message_on_start.png)
or possibly this message instead:
![no_workspace_set.png](/tutorials/bg3-mod-helper/no_workspace_set.png)

Both error messages relate to settings, the first is suggesting the path your lslib in the settings may be off while the latter is suggesting something is wrong with your workspace, ie rootmodpath setting.

There are a few quick setup steps that the extension requires to be in a working state, namely adjusting the paths in the extension's settings. There are a few ways to get to these settings, with the following being the easiest:
1. Click on "File" in the top ribbon in VSCode
2. Click on "Preferences" > "Settings"
3. Search for `bg3` in the settings search bar

You should be seeing something like this (settings seem to move around):
![settings.png](/tutorials/bg3-mod-helper/settings.png)

Before we actually look at any of the settings we need to understand the difference between User settings and Workspace settings in vscode. In the picture above showing the settings, we can see an option for User and Workspace. User settings persist over vscode windows. Workspace settings are for that specific vscode window. This distinction is important because of how the extension handles paths for you. You will understand more as you go though each setting option below but understanding this distinction is important, especially for Root Mod Path.

Let's go through each settings option.
- **Auto Launch On Pack:** Toggle this setting to do exactly as the name implies. If you pack your mod with the extension while this is toggled, your game will launch upon packing (disabled at the momemnt, just hit launch game in data provider).
- **Excluded Files:** Enter in full paths to files that you wish to not have converted when the mod is packed. This is done to avoid creation of non essential files. These files wont affect your work but do clutter up your space so adding them to excluded can be valuable to avoid the clutter. The fastest way to add an item to the list is to simply right click on a file in your file tree in vscode and select the new menu option added by the extension which says "Add to Conversion Exclusion List". At the moment, the entered path is very specific. Ensure a lowercase drive letter and you use /. ie c:/Users/ghostboats/Desktop/Squire/Public/Squire/ClassDescriptions/ClassDescriptions.lsx 
<sub>Certain files/folders are automatically excluded, like meta.lsx</sub>
- **Hover: Enabled:** Toggle this to turn the uuid/handle hover information (users say it can be too much and obstruct the page, an alternative solution would be below)
- **Hover: Max Files:** Enter a number into the field to limit the amount of entries returns when looking for uuid/handles to display via hover, for visibility.
- **Hover: Show Path:** Not working and will probably be removed in future, dont worry about this. Probably leave it checked but it shouldnt do anything.
- **Launch Continue Game:** Toggle this do exactly as stated, launch the game with continue game flag so it will auto start your last save instead of waiting at the game menu.
- **Lslib Path:** Previously this setting was for supplying the path to divine.exe. The extension has since grown and can leverage lslib directly. You will need to supply the path to your lslib. Typically this will be something like this C:\Users\ghostboats\Desktop\ExportTool-v1.19.5\Packed.
- **Max Cache Size:** Integer value field. Caching is used to reduce lag and stop hover information from re-searching when hovering over already hovered uuids/handles which makes its position in the hover box shift around and hard to read. Typically you wont need to adjust this setting.
- **Mod Destination Path:** This field is for supplying the path to the Mods folder for baulder gate 3. When you pack your mod with the extension, it will get set to this folder so you want to point it straigh to the mods folder for the game. For most people this will typically be C:/Users/{username}/AppData/Local/Larian Studios/Baldur's Gate 3/Mods, just make sure to replace username with your actual name.
- **Root Mod Path:** This field is a bit unique. We actually do not want to touch this setting. When we open a folder in vscode, the extension will automatically populate this field with your current workspace folder. In User settings, it should be blank and you should not enter anything here. If you want to confirm your root mod was correctly auto set, change to the Workspace settings tab and take a look.
- **Game Install Location:** The path to your `Baulders Gate 3` folder (C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3). This is used to launch the game from vscode.

## Features and Usage
### 0. **The Data Provider**
While the extension has many other capabilities and shortcuts, the best way to access the features of the extension are to use the data provider. Im sure when you first installed the extension you noticed the little box on the far left (given you havent moved around your vscode ui). Clicking it opens up the data provider, which is a quick one stop shop for alot of (but not all) the main functionality of the extension.
![data_providerr.png](/tutorials/bg3-mod-helper/data_providerr.png)
I will cover most of what these do below but some information about the data provider in general:
- If you see a `>` before an option, such as Pack/Unpacking Tool, it means that button does multiple things. If you press the text of the button it will do its main action, typically open up some sort of webview to work with that tool/process. Your other option would be to hit the `>`, revealing a dropdown list of quick options you can do without access the more intensive main action.
- If you see `(in development)` next to an option, it is clearly in development. Expect issues with these and please dont reach out regarding errors when using. Its expected in development.

> -If you dont see the cardboard box, you dont have the extension installed correctly or something is corrupted.
> -If none of the options are available when you click the data provider (it will say something like nothing to display), something failed on load up of the extension. It could be a number of things but the firs thing to check would be the make sure all the paths you have provided in settings are correct and that you do have lslib downloaded.
{.is-warning}


### 1. **UUID/Handle Creation**
- Right-click on an open editor to open a right click menu and click "Generate UUID" or "Generate Handle" to generate a uuid or handle respectivly at that location.
-- If a UUID/handle is highlighted when generating a UUID/handle, it will replace the entry with whatever was generated.
-- Generate a UUID/Handle using the keystrokes `control+shift+U` and `control+shift+H`, respectively.
-- When handles are generated, if an XML file exists, it will add the newly created handle to the XML as well.
*<sub>Use the `Add Handles To All Locas` setting to apply the newly created handle to all your loca files should you have multiple. Otherwise you will be prompted to select which files to insert to</sub>

### 2. **File Conversions (lsx<>lsf, xml<>loca)**
- Open a custom webview tab where users can manage converting lsx, lsf, loca, xml, etc., files. by clicking on `Conversion Tool` in the data provider.
- Can also quick convert without the converter tab by clicking the dropdown arrow on `Conversion Tools` to display quick options regarding conversion such as `Convert all XML to LOCA` or `Convert all LSX to LSF`.
- Single file conversion via right-click menu from file tree.
- Auto-convert files when packing, including an exclusion list managed in the extension's settings.


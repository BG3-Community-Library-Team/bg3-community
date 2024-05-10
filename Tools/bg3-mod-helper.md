---
title: VSCod(e/ium) Extension
description: an extension for VSCode and VSCodium by @khbsd and @ghostboats that has lots of helpful features for modders.
published: true
date: 2024-05-10T19:50:36.778Z
tags: vscode, vscodium, bg3-mod-helper, tool, tools, ghostboats, khbsd
editor: markdown
dateCreated: 2024-04-25T01:43:35.054Z
---

# BG3 Mod Helper - A VSCod(e/ium) Extension
Created by ghostboats and khbsd, this VSCode extension is designed to help mod authors speed up their mod creation workflows. The extension has multiple useful utilities that include but are not limited to:
- **Mod Packing**
- **UUID/Handle Generation**
- **UUID Mapping**
- **LSX/XML/LOCA/ETC File Conversions**
- **Generate Mod Templates**
- **And More!**

While the extension is still receiving regular updates, it's at a stable point where it can be very useful to mod authors and save them a lot of time. It is built off the philosophy of being able to mod without having to tab out as often while requiring as few clicks as possible to get the job done. It has saved us a lot of time, and I hope it can do the same for you!

> **Goal:** The goal of this wiki is twofold: provide documentation for [mod authors](#mod-authors-guide) and [developers (coming soon)](#) who may wish to contribute/fork their own version.

## Table of Contents
1. [File Locations](#file-locations)
2. [Requirements](#requirements)
3. [Mod Authors Guide](#mod-authors-guide)
   1. [Download Guide](#download-guide)
   2. [Setup Extension Settings](#setup-extension-settings)
	 3. [Features and Usage](#features-and-usage)

### File Locations 📂
- [Github (source code)](https://github.com/ghostboats/bg3_mod_helper)
- [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper)

### Requirements 🛠️
- [Visual Studio Code](https://code.visualstudio.com/)
- [LSLib](https://github.com/Norbyte/lslib/releases)
- Python (for working with icons/dss's/png's)

> **Note:** Previous versions of the extension required direct use of `divine.exe`. This has since been replaced with [LSLib](https://github.com/Norbyte/lslib/releases). Make sure your path now points to the directory containing `lslib`.

# Mod Authors Guide

## Download Guide
There are several ways to download the extension, but below is the easiest method.
1. Open VS Code
2. Click on the "View" tab on the top ribbon
3. Click on "Extensions"
4. In the "Search Extensions in Marketplace" search box, enter `bg3`
5. Click "Install" on the correct extension (bg3_mod_helper)

![installextension-ezgif.com-optimize.gif](/tutorials/bg3-mod-helper/installextension-ezgif.com-optimize.gif)

## Setup Extension Settings
After installing the extension, you will most likely see a message like this:

![error_message_on_start.png](/tutorials/bg3-mod-helper/error_message_on_start.png)

There are a few quick setup steps that the extension requires to be in a working state, namely adjusting the paths in the extension's settings. There are a few ways to get to these settings, with the following being the easiest:
1. Click on "File" in the top ribbon in VSCode
2. Click on "Preferences" > "Settings"
3. Search for `bg3` in the settings search bar

You should be seeing something like this (settings seem to move around):
![settings.png](/tutorials/bg3-mod-helper/settings.png)

Before we actually look at any of the settings we need to understand the difference between User settings and Workspace settings in vscode. In the picture above showing the settings, we can see an option for User and Workspace. User settings persist over vscode windows. Workspace settings are for that specific vscode window. This distinction is important because of how the extension handles paths for you. You will understand more as you go though each setting option below but understanding this distinction is important, especially for Root Mod Path.

Let's go through each settings option.
- **Auto Launch On Pack:** Toggle this setting to do exactly as the name implies. If you pack your mod with the extension while this is toggled, your game will launch upon packing.
- **Excluded Files:** Enter in full paths to files that you wish to not have converted when the mod is packed. This is done to avoid creation of non essential files (creation of meta.lsf or ClassDescriptions.lsx, etc). These files wont affect your work but do clutter up your space so adding them to excluded can be valuable to avoid the clutter. The fastest way to add an item to the list is to simply right click on a file in your file tree in vscode and select the new menu option added by the extension which says "Add to Conversion Exclusion List". At the moment, the entered path is very specific. Ensure a lowercase drive letter and you use /. ie c:/Users/ghostboats/Desktop/Squire/Public/Squire/ClassDescriptions/ClassDescriptions.lsx
- **Hover: Enabled:** Toggle this to turn the uuid/handle hover information (users say it can be too much and obstruct the page, an alternative solution would be below)
- **Hover: Max Files:** Enter a number into the field to limit the amount of entries returns when looking for uuid/handles to display via hover, for visibility.
- **Hover: Show Path:** Not working and will probably be removed in future, dont worry about this. Probably leave it checked but it shouldnt do anything.
- **Launch Continue Game:** Toggle this do exactly as stated, launch the game with continue game flag so it will auto start your last save instead of waiting at the game menu.
- **Lslib Path:** Previously this setting was for supplying the path to divine.exe. The extension has since grown and can leverage lslib directly. You will need to supply the path to your lslib. Typically this will be something like this C:\Users\ghostboats\Desktop\ExportTool-v1.19.5\Packed.
- **Max Cache Size:** Integer value field. Caching is used to reduce lag and stop hover information from re-searching when hovering over already hovered uuids/handles which makes its position in the hover box shift around and hard to read. Typically you wont need to adjust this setting.
- **Mod Destination Path:** This field is for supplying the path to the Mods folder for baulder gate 3. When you pack your mod with the extension, it will get set to this folder so you want to point it straigh to the mods folder for the game. For most people this will typically be C:/Users/{username}/AppData/Local/Larian Studios/Baldur's Gate 3/Mods, just make sure to replace username with your actual name.
- **Root Mod Path:** This field is a bit unique. We actually do not want to touch this setting. When we open a folder in vscode, the extension will automatically populate this field with your current workspace folder. In User settings, it should be blank and you should not enter anything here. If you want to confirm your root mod was correctly auto set, change to the Workspace settings tab and take a look. 

## Features and Usage
### 1. **UUID/Handle Creation**
> **Purpose:**
{.is-info}

- Right-click on an open editor to generate a UUID or handle at that location.
- If a UUID/handle is highlighted when generating a UUID/handle, it will replace the entry with whatever was generated.
- Generate a UUID/Handle using the keystrokes `control+shift+U` and `control+shift+H`, respectively.
- When handles are generated, if an XML file exists, it will add the newly created handle to the XML as well.

![genhandle-ezgif.com-optimize.gif](/tutorials/bg3-mod-helper/genhandle-ezgif.com-optimize.gif)

### 2. **File Conversions (lsx<>lsf, xml<>loca)**
- Open a custom webview tab where users can manage converting lsx, lsf, loca, xml, etc., files.
- Quick convert options in the data provider dropdown.
- Single file conversion via right-click menu from file tree.
- Auto-convert files on pack, including an exclusion list managed in the extension's settings.


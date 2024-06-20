---
title: VSCod(e/ium) Extension
description: A extension for VSCode and VSCodium by @khbsd and @ghostboats that has lots of helpful features for modders.
published: true
date: 2024-06-20T08:21:35.534Z
tags: vscode, vscodium, bg3-mod-helper, tool, tools, ghostboats, khbsd
editor: markdown
dateCreated: 2024-04-25T01:43:35.054Z
---

# BG3 Mod Helper - A VSCod(e/ium) Extension
Created by ghostboats and khbsd, this VSCod(e/ium) extension is designed to help mod authors speed up their mod creation workflows. The extension has multiple useful utilities that include but are not limited to:
- **Mod Packing/Unpacking**
- **UUID/Handle Generation**
- **UUID Mapping**
- **Handle Management**
- **LSX/XML/LOCA/ETC File Conversions**
- **Generate Mod Templates**
- **And More!**

If all of this sounds gouda, and you are comfortable with initial setup and just want to see what the extension can do, please jump to [here](#features-and-usage) while we cover the basics.

Although the extension is still receiving regular updates, it's very functional, and has lots of tools and tricks useful to mod authors. It is built off the philosophy of "Few clicks, few tabs" ie, being able to mod without having to tab out as often and requiring as few clicks as possible to get the job done. It has saved us a lot of time, and I hope it can do the same for you!

> While I use "VSCode" in this article, it is in the marketplace for both VSCode and VSCodium
{.is-info}

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
4. [Developers Guide](#developers-guide)

### File Locations 📂
- [Github (source code)](https://github.com/ghostboats/bg3_mod_helper)
- [VSCode Marketplace](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper)

### Requirements
- [Visual Studio Code](https://code.visualstudio.com/)
- [LSLib](https://github.com/Norbyte/lslib/releases)

> **Note:** Previous versions of the extension required direct use of `divine.exe`. This has since been replaced with [LSLib](https://github.com/Norbyte/lslib/releases). Make sure your path now points to the directory containing `lslib`. Likewise, previous versions of the extension required python and some external modules (ImageMagick, PIL, etc). This has been removed and only the `lslib` folder is required.

# Mod Authors Guide

## Limitations
Nothing is perfect, let's get the rough stuff out of the way before we start to possibly save you time incase this extension is not what you are looking for.
- Unable to work with multiple workspaces in one VSCode window
- Unable to edit pngs/dds in VSCode (can resize, convert, generate atlas texture, and apply backgrounds to transparent pngs though)
- Buggy when having other folders within your workspace
- Buggy when using multiple VSCode windows (need to confirm)
- Possible lag due to folder/file size (need to confirm)
- No references to base game uuids/handles (coming soon?)

> Being on this list doesn't guarantee that it will or will not be possible in the future. Just that it is unlikely.
{.is-info}

## Download Guide
There are several ways to download the extension, but below is the easiest method.
1. Open VS Code
2. Click on the `View` tab on the top ribbon
3. Click on `Extensions`
4. In the `Search Extensions in Marketplace` search box, enter `bg3`
5. Click `Install` on the correct extension (bg3_mod_helper)

![installextension-ezgif.com-optimize.gif](/tutorials/bg3-mod-helper/installextension-ezgif.com-optimize.gif)

> It is recommended that you restart VSCode after installing. In fact, you should restart VSCode everytime you change your workspace.
{.is-warning}

## Getting Started
After installing the extension, you will see a message like this:

![error_message_on_start.png](/tutorials/bg3-mod-helper/error_message_on_start.png)
or this:
![no_workspace_set.png](/tutorials/bg3-mod-helper/no_workspace_set.png)
in the bottom right of VSCode, especially if this is your first time using the extension.

There are a few quick setup steps that the extension requires to be in a working state, namely adjusting the paths in the extension's settings. I cover that [below](#setup-extension-settings), but first let's get a proper workspace set up so you can utilize all the features of the extension. Once installed, the extension is designed to launch right when you start VSCode.

> While the extension doesn't perform any actions while in the background, it is technically always on. This shouldn't hinder your other non-modding projects, but it's good practice to disable or delete any extension if you don't plan on using it for a while.
{.is-info}

The key working with the extension is setting up a workspace. There are a few different ways to do it but here is the simplest and safest.

0) Optional but recommended: close all other VSCode windows.
1) Open a new VSCode window and make sure no previous workspace is open. Your explorer tab should have options like this picture. You will need to press `Open Folder`.
![blank_workspace.png](/tutorials/bg3-mod-helper/blank_workspace.png)
2) The extension is designed to have what would be the "Shared" folder as your mods workspace. So when you select `Open Folder`, you should select the folder that contains your Localization, Mods, and Public folder as your workspace folder. You should see the message below if you have opened up your workspace correctly (and have your settings set up which I cover in the section below)
![no_workspace_set.png](/tutorials/bg3-mod-helper/workspace_set.png)

> VSCODE QUICK TIP: In Windows, you can pin VSCode to your taskbar and simply right click on it. This will give you the option to open previously opened workspaces right away or open an empty workspace. Also, it is possible to add an `Open with Code` option when right clicking a folder on your desktop (or anywhere) to instantly open and add a folder to VSCode. It's useful to learn these methods should you swap between mod folders a lot. More info and possible steps [here.](https://stackoverflow.com/questions/37306672/visual-studio-code-open-with-code-does-not-appear-after-right-clicking-a-folde)
{.is-info}

## Setup Extension Settings
As I mentioned, **you better have been listening**, if it's your first time starting the extension (or if you have an error on startup which could be unrelated) you may see the image below when you open up VSCode or a workspace.

This error means `LSLib.dll` isn't in the folder in your settings. 
![error_message_on_start.png](/tutorials/bg3-mod-helper/error_message_on_start.png)

This error means there's something wrong with your **Root Mod Path**.
![no_workspace_set.png](/tutorials/bg3-mod-helper/no_workspace_set.png)

There are a few quick setup steps that the extension requires to be in a working state, namely adjusting the paths in the extension's settings. There are a few ways to get to these settings, with the following being the easiest:
1. Click on "File" in the top ribbon in VSCode
2. Click on "Preferences" and then "Settings"
3. Search for `bg3` in the settings search bar

You should be seeing something like this (settings seem to move around):
![settings.png](/tutorials/bg3-mod-helper/settings.png)

Before we actually look at any of the settings we need to understand the difference between User settings and Workspace settings in VSCode. In the picture above, we can see options for User and Workspace. User settings persist across multiple VSCode windows. Workspace settings are for that specific VSCode window. This distinction is important because of how the extension handles paths for you. Things will make more sense as you go though each setting option below, but understanding this distinction is important, especially for Root Mod Path.

Let's go through each settings option.
- **Auto Launch On Pack:** Toggle this setting to do exactly as the name implies. If you pack your mod with the extension while this is toggled, your game will launch upon packing (disabled at the momemnt, just hit launch game in data provider).
- **Excluded Files:** Enter in full paths to files that you wish to not have converted when the mod is packed. This is done to avoid creation of non essential files. These files wont affect your work but do clutter up your space so adding them to excluded can be valuable to avoid the clutter. The fastest way to add an item to the list is to simply right click on a file in your file tree in VSCode and select the new menu option added by the extension which says "Add to Conversion Exclusion List". At the moment, the entered path is very specific. Ensure a lowercase drive letter and you use /. ie c:/Users/ghostboats/Desktop/Squire/Public/Squire/ClassDescriptions/ClassDescriptions.lsx 

> Certain files/folders are automatically excluded, like meta.lsx
{.is-info}

- **Hover: Enabled:** Toggle this to turn the uuid/handle hover information (users say it can be too much and obstruct the page, an alternative solution would be below)
- **Hover: Max Files:** Enter a number into the field to limit the amount of entries returns when looking for uuid/handles to display via hover, for visibility.
- **Hover: Show Path:** Not working and will probably be removed in future, dont worry about this. Probably leave it checked but it shouldnt do anything.
- **Launch Continue Game:** Toggling this does exactly as stated, launches the game with the `-continueGame` flag; it will auto load your last save when it gets to the maine menu.
- **Lslib Path:** Previously this setting was for supplying the path to divine.exe. The extension has since grown and can leverage lslib directly. You will need to supply the path to your lslib. Typically this will be something like this: `C:\Users\ghostboats\Desktop\ExportTool-v1.19.5\Packed`.
- **Max Cache Size:** Integer value field. Caching is used to reduce lag and stop hover information from re-searching when hovering over already hovered uuids/handles which makes its position in the hover box shift around and hard to read. Typically you wont need to adjust this setting.
- **Mod Destination Path:** This field is for supplying the path to the Mods folder for baulder gate 3. When you pack your mod with the extension, it will get set to this folder so you want to point it straigh to the mods folder for the game. For most people this will typically be C:/Users/{username}/AppData/Local/Larian Studios/Baldur's Gate 3/Mods, just make sure to replace username with your actual name.
- **Root Mod Path:** This field is a bit unique. We actually do not want to touch this setting. When we open a folder in VSCode, the extension will automatically populate this field with your current workspace folder. In User settings, it should be blank and you should not enter anything here. If you want to confirm your root mod was correctly auto set, change to the Workspace settings tab and take a look.
- **Game Install Location:** The path to your `Baldur's Gate 3` install folder (C:\Program Files (x86)\Steam\steamapps\common\Baldur's Gate 3). This is used to launch the game from VSCode.

## Features and Usage
### 0. **The Data Provider**
While the extension has many other capabilities and shortcuts, the best way to access the features of the extension are to use the data provider. Im sure when you first installed the extension you noticed the little box on the far left (given you havent moved around your VSCode ui). Clicking it opens up the data provider, which is a quick one stop shop for alot of (but not all) the main functionality of the extension.
![data_providerr.png](/tutorials/bg3-mod-helper/data_providerr.png)

# Some important notes:

> If you see a `>` before an option, such as Pack/Unpacking Tool, it means that button does multiple things. If you press the text of the button it will do its main action, typically open up some sort of webview to work with that tool/process. Your other option would be to hit the `>`, revealing a dropdown list of quick options you can do without access the more intensive main action.
{.is-info}

> If you see `(in development)` next to an option, it is clearly in development. Expect issues with these and please don't bother me with errors that pop up. It is known, `dear user`.
{.is-info}

> If you don't see the cardboard box, you don't have the extension installed correctly or something is corrupted.
{.is-info}

> If none of the options are available when you click the data provider (it will say something like nothing to display), something failed when the extension loaded up. It could be a number of things but the first thing to check would be the make sure all the paths you have provided in settings are correct and that you do have lslib downloaded.
{.is-info}

---


I will cover most of what these do below, but here is each current setting and a very quick breakdown of what they are.
- **Pack/Unpacking Tool:** Allows the user to pack their current workspace mod and unpack mods (duh). Has quick actions only at the moment.
- **Converstion Tool:** Open a webview tab which allows the user to handle conversion related features regarding lsx and loca files. Has quick actions.
- **Launch Game:** Launch the game directly from VSCode
- **Generate Folder Structure :** Lets the user quickly deploy mod templates. Only class mod templates working at the moment.
- **Atlas Generator:** By supplying a folder of correctly sized PNGs, the user can generate a PNG that can then be right click converted to a dds to use as a atlas texture file.
- **Version Generator:** Open a webview tab which allows the user to quickly generate a version number for their meta, as well as quickly apply it to your meta file.
- **Rotation Tool:** Dont worry about this one for now.
- **DDS Viewer:** In development still but opens a webview that shows information about all the dds files in your workspace. While in development, it is only search for dds files in the `Mods` folder so please place your dds files in there temporarily if you wish to test and use while this tool is in development.
- **Debug Command:** "Don't press this please, I use this for development"- Ghostboats

> I hear you saying "reading is annoying!" and "I don't want to read all this."
***Too bad.***
The one thing you should get comfy with, even if you ~~stupidly~~ don't care about some of the shortcuts and other features, is the data provider. It will always house the most powerful features of the tool and it would be ~~stupid~~ a waste not to use them.
{.is-danger}


### 1. **UUID/Handle Creation**

- Right-click on an open editor to access the context menu, or press F1 and choose "Generate UUID" or "Generate Handle" to insert a UUID or handle at the cursor's location.
- If text is selected when generating a UUID or handle, the selected text will be replaced with the generated value. For handles, the selected text will be used as the handle's context if local XML files exist.
- All this functionality also supports multiple cursors.
- You can also generate a UUID or handle using the default keystrokes Ctrl+Shift+U and Ctrl+Shift+H, respectively.
- When handles are generated, if an XML file exists, it will add the newly created handle to the XML. *Tip: you can easily create one with [Create BG3 File](https://wiki.bg3.community/Tools/bg3-mod-helper#h-6-other-actions)*. Handle-y!


> Use the `Add Handles To All Locas` setting to apply the newly created handle to all your loca files should you have multiple. Otherwise, you will be prompted to select which files to insert the handle in.


### 2. **File Conversions (lsx<>lsf, xml<>loca)**
- Open a custom webview tab where users can manage converting lsx, lsf, loca, xml, etc., files. by clicking on `Conversion Tool` in the data provider.
![conversion_tab.png](/tutorials/bg3-mod-helper/conversion_tab.png)
- Can also quick convert without the converter tab by clicking the dropdown arrow on `Conversion Tools` to display quick options regarding conversion such as `Convert all XML to LOCA` or `Convert all LSX to LSF`.
- Single file conversion via right-click menu from file tree.
- Auto-convert files when packing, including an exclusion list managed in the extension's settings.

>Look for `Excluded Files` in the settings to add files to exclude. You can also right click on a file and click `Add to Conversion Exclusion List` or `Remove from Conversion Exclusion List`.


### 3. **Pack/Unpack Mods**
- Open a custom webview tab where users can manage packing and unpacking related features (webview in development, quick actions currently working though).
- Can also quick pack/unpack without the packaging tool by clicking the dropdown arrow on `Pack/Unpacking Tool` to display quick options regarding packing such as `Pack Mod` and `Unpack Mod`.
- `Pack Mod` performs a number a background checks.
--Ensures a meta exists and will prompt you to create one if not.
--Converts all non excluded .lsx and .xml files for you automatically.
--Will move the newly made .pak to the games Mods folder.
--Can autolaunch game after packing if settings are enabled (disabled at the meowment).


> Look for `Auto Launch On Pack` to launch game right away after packing, chains well with the `Launch Continue Game` setting.

### 4. **UUID/Handle Hover Information**
- Hover over UUIDs/handles in your files to see hoverable boxes which display all your related UUIDs/handles in your workspace. It breaks it down by the following per entry found:
--The entire line the UUID/handle is found on, starting at the first whitespace occurance.
--The file that line is found in. If you click it, it will open the file in the editor at that line for quick access.


> Look for `Hover: Enabled` in the settings to disable the hover feature of the extension to avoid visual clutter if you see fit. Look for `Hover: Max Files` for a better solution as it will limit the amount of files returned to help with visual clarity. Look for `Max Cache Size` if you are dealing with lag issues.

### 5. **PNG/DDS Manipulation**
- Convert PNG files to DDS files (and vice versa) by right clicking on a file in the file tree and selecting `Convert To  DDS` or `Convert To PNG`.
--When converting an atlas texture, it will correctly convert the PNG to dds, not DDS
- Resize PNG/DDS files by right clicking on a PNG/DDS file and hovering over `Resize Image`. Four options will appear:
--`Resize Image Custom` which will prompt the user to select a length and width (make them the same please)
--`Resize Image to Controller (144x144)`
--`Resize Image to Hotbar (64x64)`
--`Resize Image to Tooltip (380x380)`
- If you have a PNG image with a transparent background that you plan to use as an icon in the game, you can add a background to to it by right clicking on the PNG in the file tree and clicking `Add Icon Background` which will prompt the user to select from multiple in game backgrounds or a custom one if you have one to supply.

## 6. **Other Actions**
- Generate BG3 related template files (ClassDescriptions.lsx, etc) quickly by right clicking in the file tree and clicking `Create BG3 File` or press `Control + 1` which will give the user a dropdown of files templates to make.
- Open online export tools (BG3 Search Engine, LSX Validator and Stats Validator) in a VSCode tab by right clicking in an open editor and hovering over `Export Tools` and select the relevant option.
- Hovering over BG3 related functions will provide information on them
--VERY LIMITED WHILE STILL GETTING FUNCTION INFORMATION
- Autocomplete for data entries
--VERY VERY LIMITED


# Developer's Guide
Coming soon, you heathens.
![nodders-nodding.gif](/tutorials/bg3-mod-helper/nodders-nodding.gif)
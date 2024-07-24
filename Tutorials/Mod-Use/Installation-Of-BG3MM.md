---
title: Install BG3MM (BG3 Mod Manager)
description: A comphrensive guide on how to install mods via BG3MM 
published: true
date: 2024-07-24T18:18:44.920Z
tags: bg3mm, guide, installation
editor: markdown
dateCreated: 2024-04-25T01:54:07.278Z
---

# How to install BG3MM (BG3 Mod Manager)

Use the following guide to install BG3MM on to your PC. Note, this is not a guide for installing BG3MM on Mac computers or Steam Decks.

## 1. Running the game
Using your game launcher (Steam, GOG, etc), open and run BG3 at least once. Its recommended to at least go through the menu and get to the Character Creation Screen. After this, you can close the game.

Doing this creates a profile and mod folders in the game files that BG3MM needs.

## 2. Download .NET files (if needed)
You **must** have the following installed on your PC. If you are not sure if you have these, its safer to download and install anyway.

- [.NET Framework 4.7.2](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net472)
- [.NET 7.0 Desktop Runtime (v7.0.13)](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-7.0.13-windows-x64-installer)

## 3. Download the latest version of BG3MM
Download the latest version of BG3MM from [LaughingLeaders GitHub](https://github.com/LaughingLeader/BG3ModManager/releases/latest).

> The **only** official download location for BG3MM is LaughingLeaders GitHub. **DO NOT TRUST OR USE ANY OTHER SITE CLAMING TO BE A DOWNLOAD SOURCE FOR BG3MM**
{.is-warning}

Note, that the latest release on GitHub may look older, but BG3MM automatically prompts you to update upon launch when a new update is pushed out. There is no reason to redownload from GitHub once you have installed it, unless it was deleted.

## 4. Extract BG3MM into a folder
> Its recommended to **not** extract BG3MM inside a protected folder.
{.is-info}

Extract BG3MM into a folder on your computer. Its recommended to install it either inside the hard drive where your steam in installed or any other location where you want to hold BG3MM. Please note the screens and gifs below show it installed in a dedicated game drive, but you can install it anywhere you choose.

## 5. Run the BG3ModManager.exe
After extracting the files to a new location, you will see a BG3ModManager.exe.

Click and run the BG3ModManager.exe The pathways needed by the exe should automatically be detected upon running the exe file.

If the exe fails to establish the pathways, then you will need to do the following:
- Manually set the pathways in Settings > Preferences
- Click save and close the preferences box
- Click the refresh button

If you have correctly followed the guide, your BG3MM should look like the screenshot below. Note, that the profile should say *Public*. 

## Common causes of issues
If you are experiencing any issues with BG3MM after using the guide, consult the follow list of common causes of issues:
- Check that you have no subfolders in your mod folders. To do this, click the search icon on your taskbar, type *run*, and hit enter. You should see the below window open. In the search bar, copy and paste (%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\Mods) and click enter. Your mod folder will open.
- Double check that in Step 5 that the Game Data path has been set correctly.
- Double check the last part of Step 5 and make sure a campaign is selected (ex. Main).
- If your mods are reseting/you get a warning that mods were disabled when you load into the game, this means that one of the mods you have installed is broken or not compatiable with another mod. 
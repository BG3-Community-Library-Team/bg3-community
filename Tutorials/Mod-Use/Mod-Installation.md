---
title: Installation of BG3MM (BG3 Mod Manager)
description: A comphrensive guide on how to install mods via BG3MM 
published: false
date: 2024-04-25T23:40:35.498Z
tags: bg3mm, guide, installation
editor: markdown
dateCreated: 2024-04-25T01:54:07.278Z
---

##  **Set up of BG3MM (Baldur's Gate 3 Mod Manager):**


This guide will be split up in 3 parts to make it easier:

1. How to set up BG3MM 
2. How to install .pak files. 
3. How to install manual/loose file mods (mods that do not come as .pak file but as folders). 

> *This is a guide meant for Windows steam users and BG3MM. However, GOG users can use this guide as well; they just need to find the GOG equivalent of the Steam paths.*
{.is-info}

---


## 1. Install BG3MM via github


Link: https://github.com/LaughingLeader/BG3ModManager/releases/tag/1.0.10.0
Latest release: October 20, 2023. 
Version: 1.0.10.0 

> You will need these: .NET Framework 4.7.2 and NET. 7.0.13 
> Usually these will already be installed on your Windows system, but if you encounter problems with the usage of BG3MM, make sure you have .NET Framework 4.7.2 and NET. 7.0.13 installed. 
{.is-info}


You will see this when you open the link:

![bg3mm.png](/tutorials/bg3mm.png =x650)

You will need to press on "BG3ModManager_Latest.zip" that is highlighted in red in the bottom. 

This will prompt a download. It will be a zip file. 

## 2. Set BG3MM up correctly

Now you need to extract the zip file. The zip file should be in your downloads folder ín file explore. 

Windows support zip files: all you need to do is right click, and click on "Extract all" and then press "Extract" in the menu as shown below.

![extract.png](/tutorials/extract.png =x450)

![extraction.png](/tutorials/extraction.png)

Now you have BG3ModManager_Latest as a folder. 
Delete the zip file, you no longer need it. 

Move the folder to an area where you can remember it; for example on the desktop, or in the documents folder. 
> 
> It is important you do not extract it inside any folders related to BG3 as this is an external program. 
Likewise do not put the folder into any steam, Larian Studios or BG3 related folders. 
> Do not move the exe out of the folder either. It belongs in the folder and should never be removed. 
{.is-warning}

## 3. Configuring BG3MM. 

Open the folder "BG3ModManager_Latest". 
And double click on the exe:

![bg3mm_exe.png](/tutorials/bg3mm_exe.png)

Your BG3MM should look something like this: 

![bg3mm_overview.png](/tutorials/bg3mm_overview.png =x460)


> You will notice that there is two "mods" that are already installed. These are base files which got added in patch 5. They will get hidden next BG3MM update. 
> They should be ignored, and not set to active and stay in the inactive section.
> LaughingLeader has a way to hide them already, if needed (explanation below): https://raw.githubusercontent.com/LaughingLeader/BG3ModManager/master/src/GUI/Resources/IgnoredMods.json. 
{.is-info}

![ll_explanation.png](/tutorials/ll_explanation.png)

When you have opened BG3MM, go to the top left, and click "settings", then "preferences": 

![settings.png](/tutorials/settings.png)

It will open up a menu in BG3MM, which should look a lot like this:

![preferences.png](/tutorials/preferences.png =x500)

Here, you will need to make sure the highlighted areas "Game Data Path" and "Game Executable Path" something a like this. This will look different depending on where you have installed BG3. If there is nothing in these areas, close BG3MM, open the game to main menu and quit. Then open BG3MM, Settings, then preferences again and it should be fixed. 

if not you will need to find where your game is installed. For steam, this is very easy: 

Go to your steam library. 
Right click on BG3, hover over "Manage" and click on "Browse local files". 

![steam.png](/tutorials/steam.png)

File explore should open up to this folder (called the root installation folder): 

![bg3_folder.png](/tutorials/bg3_folder.png =x250)

Click into the "Data" folder, and copy the path. Paste it into the "Game Data Path" in BG3MM, Settings, Preferences. It should be looking a lot like this which is depending on where you installed it:  

`\SteamLibrary\steamapps\common\Baldurs Gate 3\Data`

Click back, and click into the bin folder. Copy the path and paste it into the "Game Executable Path" in BG3MM, Settings, Preferences. 
You will need to add \bg3.exe in the end: 

`\SteamLibrary\steamapps\common\Baldurs Gate 3\bin\bg3.exe`
---
title: How to install manual/loose file mods
description: 
published: false
date: 2024-05-01T02:27:49.991Z
tags: 
editor: markdown
dateCreated: 2024-05-01T01:34:11.948Z
---

# How to install manual/loose file mods

This is part 3 and the final part on how to install BG3MM, mods and loose file mods. 

Part 1: How to install BG3MM: https://wiki.bg3.community/en/Tutorials/Mod-Use/Installation-Of-BG3MM
Part 2; How to install Pak files: https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-Install-Pak-Files

## What is loose/manual mods? 

What is loose file mods? Loose file mods are mods that are not managed by a mod manager. This can for example be tattoo mods or make up mods. You can identify them with coming in a zip, 7zip or rar and when you extract them they typically have folders which can be named; "Data", "Bin", "Public", "Generated". 
When you open these folders, it will typically be a bunch of folders ending with different files such as DDS or other files. Meaning, these will not end in files that are ".pak" files. 

These folders shouold not be put in the mods folder (`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`) but instead the data or the bin folder in your root installation folder (`\SteamLibrary\steamapps\common\Baldurs Gate 3`)

However Vortex can manage them, but it is not a good idea as there are potential risk such as Vortex putting the folders and files in a wrong place which can but is not limited to these bugs: 

BG3 crashing
BG3 not responding
BG3 not opening
Weird textures
Mods not working correctly
Mods not showing up
Mods having compatbility issues when there should be none etc. 

This is where this guides comes in to provide information with how to install these manually. 
For Unique Tav which also have a loose file aspect, look through this guide instead: (On To-Do)

## 1. Find and download the mod you wish to install from Nexus

Nexus Website: https://www.nexusmods.com/baldursgate3

For this guide, Coven Elf tattoo and make up mod will be the example: https://www.nexusmods.com/baldursgate3/mods/1684?tab=description

> You will need to press on "manual download" as highlighted below. Do not press "download with mod manager" if there is such an option. That is for vortex and through a mod manager, which is not recommended with loose file mods. 
{.is-warning}


![firstmanualinstallpng.png](/tutorials/install_manual_mods/firstmanualinstallpng.png =x300)

It should show up as a zip, 7zip or a rar file. In this case, it is a rar file. 

Now extract it in your downloads folder: 

![extract.png](/tutorials/install_manual_mods/extract.png =x250)

![extraction.png](/tutorials/install_manual_mods/extraction.png)

When you have done this, just delete the rar, zip or 7zip file. 

You should now end up with a folder called the exact same as the zip, rar or 7zip file. 
It may also come out called "Generate", "Bin", "Data" or "Public". 

If the folder is called the same thing as the file you just extracted, you need to go one folder deeper until you find either "Generated", "Public" or "Data" or "Bin". 

Like this: 
![onefolderdeeper.png](/tutorials/install_manual_mods/onefolderdeeper.png)
As you can see, I clicked into the "CovenElf - Tattoo and Makeup Collection-1684-v1-2-1-1694224111" and inside that folder, is the folder "Generated" which I need. D
o not go deeper into the folder: you only need to move the first "Generated", "Public", "Bin" or "Data" folder you find. 

The difference between all of these are just where they go. 

> "Generated" and "Public" act the same and goes in the same folder. 
> "Data" and "Bin" act the same and goes into the same folder. 
{.is-info}


## Generated and Public folders - where do they go?

When you have extracted the zip, rar or 7zip file and found either a "Generated" or a "Public" folder, you will need to find your data folder in another window of your file explore. 

How to do this, you will need to go on Steam, then to your Library and then right click on BG3, hover over "Manage" and click "Browse local files": 

![steam.png](/tutorials/steam.png)

For GOG users, you will need to find the GOG equivalevant of the folders


---
title: How to install Pak Files
description: 
published: true
date: 2024-04-27T03:32:58.911Z
tags: bg3mm, guide, installation, moduse
editor: markdown
dateCreated: 2024-04-27T00:49:12.642Z
---

# How to install .Pak files via BG3MM

This is part 2 of the guide "How to install Mods in BG3". 
First part: https://wiki.bg3.community/e/en/Tutorials/Mod-Use/Installation-Of-BG3MM

> This guide is for Windows, Steam users and BG3MM users. 
> However it will point out in the guide if there is an alternative way for Vortex.
> GOG users is basically the same, provided you followed the first guide. 
{.is-info}


## 1. Find the mod you wish to install

Best website for mods is nexus. 
You will find a wide varity on there: https://www.nexusmods.com/baldursgate3

You will need an account to download the mods, so make one before you move on with the guide. 
If you have one, log in so you can download the mods. 

> Remember to read the mod description of the mod you wish to download! 
> The mod description outlines things such as: Installation, compatbility issues, load order (if it has a specific load order), other things you may wish to keep in mind such as bugs. 
> A lot of issues can be prevented if you remember to the read the description!
{.is-warning}

## 2. Download the mod 

When you have found the mod you wish to download, then you click onto the mod page. 
Here you will see a description of the mod. If you scroll a little down, right above the description itself, you will see a bar with different tabs; "Description", "Files", "Images", "Videos", "Posts", etc. 


![files.png](/tutorials/files.png =x400)

Click on the highlighted "Files" as in the above screenshot. 

Here you will see where the files themselves are stored. 
You will notice that there is a button called "Mod Manager Download" - do not use this if you are using BG3MM. This is for Vortex users. You need to press the "Manual Download" if you are using BG3MM as highlighted below: 

![download.png](/tutorials/download.png =x515)

The mod will install as a zip or a 7zip file most of the time. Other times it can be as a .rar file which is almost the same as a zip file, so it is recommended to install 7zip (https://www.7-zip.org/) so that you are able to extract the mod from the archive (zip, 7zip, rars). 
However, most of the time your Windows PC should support these type of files. 

> Vortex users should use the mod manager download button and ignore rest of the guide. This may seem like the easy way out, but Vortex has it cons (bugs) in the long run and most modders recommend BG3MM. However if used correctly, and being aware of the bugs, Vortex can be used for most mods. 
{.is-info}

## 3. Install the mod

There are a few ways to install the mod. This guide will outline two of these. 
Just choose one of the ways; in the long run it does not matter much. 

The mod will be downloaded as a zip, 7zip or rar file in most cases. 

- 3.1 Extraction/double click and manually place it in the mods folder. 

First you will see the mod in your downloads folder. 

![trashcan_download.png](/tutorials/trashcan_download.png)

Right click on it, and click "extract all"

![trashcan_extract.png](/tutorials/trashcan_extract.png =x400)


Out will come a folder or .pak file and maybe a few others files. If a folder comes out, go one folder deep until you find a .pak file. 
Delete everything besides the .pak file as that is the only thing you need. 
(Provided the mod description does not specify otherwise)

> Tip: You can also double click on the zip, 7zip or rar file, and it will open up inside the zip file. No need for deleting anything in here. Just remember the .pak file is the only thing what you need, and ignore the rest.
{.is-info}

---

When you have extracted it, open BG3MM, and click on "Mods folder" in the bar to the top, right beside "Shortcuts" as highlighted below: 

![bg3mm_modsfolder.png](/tutorials/bg3mm_modsfolder.png)

It will open this folder: 

![modsfolder.png](/tutorials/modsfolder.png =x200)

This is the mod folder. The folder path will always be: 

`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`

This is something that is determined by Larian and cannot be changed.


---

Now that you have opened the mods folder, just simply take the .pak file from your downloads folder or zip folder, and place it in the mods folder as seen below in the two screenshots:

![movethemod.png](/tutorials/movethemod.png =x450)


![movedthemod1.png](/tutorials/movedthemod1.png =x400)

> In the mods folder it should always only have .pak files inside of it. 
> No folders, subfolders, json, readme's, txt, zip, 7zip, rar, etc files. 
> Having other file types, such as a folder, can lead to issues and the mods never actually get installed.
{.is-warning}

When you have done this, you will need to refresh in BG3MM: 

![refreshlonger.png](/tutorials/refreshlonger.png)


---

- 3.2: Use the import function in BG3MM

Instead of extracting and manually place the .pak file inside of the mods folder, simply just open BG3MM. 
Go to the top left, click on "Files" and then choose "Import mod". 

![importmod.png](/tutorials/importmod.png)

Find the mod in the downloads folder.

![importmods11.png](/tutorials/importmods11.png =x500)


When this is done, it will return to BG3MM.

> This is an easier way, however you need to be aware that you will still need to check your mods folder (`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`) that it has not imported any folders, or excess files as the only files that should be in this folder are the .pak files. 
{.is-info}

## 4. How to activate the mod

Your BG3MM should look something like this: 

![bg3mmwithmods.png](/tutorials/bg3mmwithmods.png =x600)

To activate the mod, you will need to drag it over to the active side which is the left side. 
Remember not to make DiceSet_06 and Honour active, and leave them in the right side of BG3MM
See also: https://wiki.bg3.community/en/Tutorials/Mod-Use/Installation-Of-BG3MM

![activemod.png](/tutorials/activemod.png =x290)

Now you need to press "export order" or "save order". 
Either one will do, you can do both but generally they will do the same thing. 
Always export or save order when you add a mod, remove a mod, change the load order or make a mod inactive. 

![saveorder.png](/tutorials/saveorder.png)

Or

![exportorder.png](/tutorials/exportorder.png)

Done! Now you have installed your first mod! 


## 5. Installing two of the most necessarry mods (mod fixer and Improved UI) when you use mods. Do not skip. Important.
Improved UI by Djmr: https://www.nexusmods.com/baldursgate3/mods/366
Mod fixer by figs999: https://www.nexusmods.com/baldursgate3/mods/141

These two are a requirement for many mods; especially mod fixer. 

Improved UI is a mod that makes it so you can choose the modded options in character creation or the mirror if you have modded hair, faces, spells, subclasses, classes, feats. Without it you will not be able to scroll.

Mod fixer is a mod that makes it so you can actually use the mods; you will get a naked durge harem instead of character creation if you do not have it. 
Screenshot below; 

![nomodfixerpng.png](/tutorials/nomodfixerpng.png =x400)

Mod fixer will also sometimes be baked into the mod you are installing, one popular mod is for example the mod Basket of Equipment. 
In that case you do not necessarily need the mod fixer, as you will already have mod fixer because of that mod.

You can see in BG3MM if the mod has mod fixer embedded into the mod or the mod uses/needs Script Extender. 
Highlighted below:

The little notes icon is the mod fixer:

![modhasmodfixer.png](/tutorials/modhasmodfixer.png)

The yellow indicator is Script Extender: 

![hasscriptextender.png](/tutorials/hasscriptextender.png)
If you have a red indicator, it means you do not have Script Extender installed.
See also: How to install Script Extender

---
Download and install them per method above untill you get to the part of making the mods active.

![overrides.png](/tutorials/overrides.png =x500)


You will notice that the mods automatically went down to a new category called "overrides". 
All mods that goes into overrides, are always enabled and should never be put in the load order. Leave them alone. 
BG3MM will automatically know which mods should be there and when any mods goes into overrides, they should stay in overrides. 

Remember to save or export order after refreshing/importing the mod. 

Brown mods and overrides, such as Improved UI and mod fixer, cannot be disabled even if you make them inactive in BG3MM. 
This is because they are overriding vanilla game files, and therefore will always be active. 
You will need to remove them completely from the mods folder to disable them 
(`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`) 


---

## Other relevant guides and credits

How to install BG3MM, mods and manual/loose file mods series: 
Part 1: How to install BG3MM: https://wiki.bg3.community/en/Tutorials/Mod-Use/Installation-Of-BG3MM
Part 3: How to install manual/loose file mods 

How to install SE 
How to install Native mod loader
How to install Unique tav

Made by: Maze 
Credits: Arrow, LaughingLeader, Norbyte, Derk, NellsRelo, Meowcat




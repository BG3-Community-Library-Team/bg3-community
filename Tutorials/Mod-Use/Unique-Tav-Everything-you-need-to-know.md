---
title: Unique Tav: Everything you need to know
description: 
published: false
date: 2024-05-04T01:55:54.051Z
tags: bg3mm, installation, loose-file-mods, manual-mods, manual, how-to, unique-tav, loose-file, loose
editor: markdown
dateCreated: 2024-05-03T22:55:56.961Z
---

# Unique Tav guide & everything you need to know

This is a guide that will cover all of [Unique Tav](https://www.nexusmods.com/baldursgate3/mods/2754)
What is Unique Tav? Unique Tav is a mod that functions as a tool for a lot of mod users and mod creators, where they can customize their character a lot more than you would have been able to in vanilla BG3. For example you need unique tav for body tattoo's.

If you are a beginner to modding BG3, it is recommended you stick with the beginning of this guide. 
The beginning is how to install unique tav and compatbility. 

If you are an experienced user, there will be a lot of useful information in this guide, however take a look at [Kartoffel's YouTube Video](https://www.youtube.com/watch?v=g67eTrz9fWg) Unique Tav.

As this is going to be a big guide, here are the things it will cover:
1. [How to install Unique Tav](#how-to-install-unique-tav)
	- [How to install the Pak file](#how-to-install-the-pak-main-file)
  	- [Load order in BG3MM/Vortex](#load-order-in-bg3mm/vortex)
  	- [How to install the Data main file](#how-to-install-the-data-main-file)
1. [Compatibility](#compatibility)
1. [How to switch tattoo and makeup mods](#how-to-switch-tattoo-and-makeup-mods)
	- [Makeup and tattoo mods that have not been optimised for Unique Tav](#makeup-and-tattoo-mods-that-have-not-been-optimised-forunique-tav)
1. [How to make other loose file mods compatible with Unique Tav](#how-to-make-other-loose-file-mods-compatible-with-unique-tav)
1. [General usage such as changing tattoo colors](#general-usage-such-as-changing-tattoo-colors)
1. [Common issues, user errors and how to fix them](#common-issues,-user-errors-and-how-to-fix-them)
1. [Other information](#other-information)


## How to install unique Tav
Installing unique Tav, it is recommended to not use Vortex but use BG3MM and install the data part as a loose file mod, simply because of how complex this mod is. If you use Vortex, install the pak file as normal and then follow [how to install the data main file](#how-to-install-the-data-main-file-in-unique-tav).

The first thing you need to do is go to [Unique Tav's mod page](https://www.nexusmods.com/baldursgate3/mods/2754) and download both main files.
You will also need [Trips' Old Shader Pack](https://www.nexusmods.com/baldursgate3/mods/4752).

> Both main files are a requirement. 
> Likewise Trips' Old Shader Pack also a requirement. 
> Mac players will likely have an issue because of Trips' Old Shader Pack but the mod cannot function correctly without it. 
{.is-warning}

## How to install the Pak main file

When you have downloaded both Trips' Old Shader Pack and the main pak file from Unique Tav, you will need to import the pak main file and Trips' Old Shaderpack into BG3MM/vortex.
If in BG3MM, remember to put the mod into the active side and "save/export order". 
If you do not know how to install a pak file, follow the guide on [How-to-Install-Pak-Files](/Tutorials/Mod-Use/How-to-Install-Pak-Files)

If in Vortex, remember to deploy and fix the load order after according to the guide below.

## Load order in BG3MM/Vortex

Trips' Old Shader pack will be in the overrides section of BG3MM and likely locked in Vortex. 
Leave those there. Everytime BG3MM puts a mod in the overrides, it is for a reson and that is because they override base game files. As Trips' Old Shaderpack is also brown and an override, you cannot disable/make it inactive without deleting it from your mods folder (`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`)

It should look something like this in BG3MM: 

![tripsshaders.png](/tutorials/unique_tav/tripsshaders.png)

Unique Tav should be relatively low on your load order, which means it should be below any heads and cosmetic mods you may have, but above any patches you may have. Technically it can be below any patches you have, but this way it makes sure the patches override Unique Tav if any of them have to. The lower a mod is on the load order, the more it will override if it can override some of the above mods.

Low means the higher number in both Vortex and BG3MM. 
Higher on the load order means the lowest number in BG3MM and Vortex.

For example like this: 

![uniquetavloadorder.png](/tutorials/unique_tav/uniquetavloadorder.png)

If you are using other mods such as [Eyes of Beholder](https://www.nexusmods.com/baldursgate3/mods/315) or [Astralities' Glow Eyes](https://www.nexusmods.com/baldursgate3/mods/4964) you will need the patches from Unique Tav as well. It will be under "files" on Unique Tav's Nexus Page, then under "optional files":

![files.png](/tutorials/unique_tav/files.png)

Then under the "optional files". 

![eyesofbeholderpatch.png](/tutorials/unique_tav/eyesofbeholderpatch.png =x490)

**Or**

![gloweyespatch.png](/tutorials/unique_tav/gloweyespatch.png =x490)

Astralities does have a patch under her own Astralities' Glow Eyes mod. Both are fine and can be used, just use one of them.

Remember not to choose both as Astralities' Glow Eyes and Eyes of Beholder are incompatible.

The load order has It would look something like this: 

![eyesofbeholder.png](/tutorials/unique_tav/eyesofbeholder.png =x120)

This example has Eyes of Beholder, but it will be the exact same load order just with Glow eyes patch from Unique Tav and just without a preset from Glow eyes. It should look something like this:

![gloweyesloadoeder.png](/tutorials/unique_tav/gloweyesloadoeder.png =x110)

So all in all for Unique tav with Eyes of Beholder and Glow eyes, low on your load order below any head mods and above your patches. 

<kbd>**Load order with Eyes of Beholder:**</kbd>
- Unique Tav main file 
- Eyes of Beholder Main File 
- Eyes of Beholder Preset
- Unique Tav Eyes of Beholder patch 

<kbd> **Load order with Astralities' Glow Eyes:** </kbd>
- Unique Tav 
- Astralities' Glow Eyes main file 
- Unique Tav Glow Eyes patch

> Remember Astralities' Glow Eyes and Eyes of Beholder are incompatible. They will override each other, so you will need to choose one or the other, and not both. 
> Only one preset from Eyes of beholder at a time as the mod page specifically says the presets will be incompatible with each other. 
{.is-warning}

## How to install the Data main file

> For this section it is better you install it manually, and follow this section. This is because it can be a bit harder to customize the mod later, and make sure the mod is installed correctly.
{.is-info}

For this part you will need to find your data folder. Your data folder is located here: `\SteamLibrary\steamapps\common\Baldurs Gate 3\Data`

You can use steam to find the data folder. GOG users will need to find the equivalent to steam folders. 

Go into your steam, then library. Right click on BG3, then hover over "Manage" and click on "Browse local files": 

![steam.png](/tutorials/steam.png)

Then File explore should open this folder: 

![bg3folder.png](/tutorials/install_manual_mods/bg3folder.png)

When you have done that, make sure you have downloaded the data main file from Unique Tav's main page.
When you have downloaded the data main file, it should come in a 7z file. 
Extract the file in your downloads folder: 

![uniquetavextract.png](/tutorials/unique_tav/uniquetavextract.png)

![extractuniquetavs.png](/tutorials/unique_tav/extractuniquetavs.png)

This process may take a hot minute.

When you have extracted the mod in your folder, there should be a folder called "unique tav data" and a bunch of numbers.
Delete the 7z file, you no longer need it. 
Now you need to go one folder deeper in the folder named "Unique tav data", so you find the folder named generated: 

![folderuniquetav.png](/tutorials/unique_tav/folderuniquetav.png)

![generateduniquetav.png](/tutorials/unique_tav/generateduniquetav.png)

When you have found the Generated folder, you will need to drag it into the "Data" folder you found before. 
Like this: 
![utmovegenerated.png](/tutorials/unique_tav/utmovegenerated.png)

And then it becomes like this:

![utmovedthegen.png](/tutorials/unique_tav/utmovedthegen.png)

When you have done this, installed the pak file and Trips Old Shader Pack, then you have now installed Unique Tav correctly. 

If you have issues then go to [Common issues, user errors and how to fix them](#common-issues,-user-errors-and-how-to-fix-them)

> If your Tav has a blue body, it is because you missed [Trips' Old Shader Pack](https://www.nexusmods.com/baldursgate3/mods/4752)
{.is-danger}


## Compatibility 

A few words about compatibility

- Heads

Heads will need Unique Tav support and Eyes of Beholder support if you use that as well. 
Most of the modders have different main files of their head mods. You will need to take the one marked clearly for "Unique Tav", or "Unique Tav + Eyes of Beholder" for example: 

![heads.png](/tutorials/unique_tav/heads.png =x400)

Some heads do have built in support for Unique Tav, such as [New Character Creation Presets WIP By Toarie](https://www.nexusmods.com/baldursgate3/mods/205)

You will need to read mod description and posts for compabitility

- Races

Modded races are not supported by default, and it is something you may need a patch for. 
There are a few patches on Nexus for Unique Tav, so it will depend on which race you have downloaded. 

- Good mods to have for compatibility with Unique Tav 

A mod that is good, even without Unique Tav is [Patches for CC Mods (Races Hairs Heads Cosmetic and such) by Padme4000](https://www.nexusmods.com/baldursgate3/mods/353)

This mod covers a lot, which is why it is split up in different uploads. Overall it patches different mods so they can be used together without any issues. Remember to read the mod description to get an overview of what it does. 

- Tatto's and makeup 

All tattoo and makeup mods can be compatible with Unique Tav. 
Some of them have been optimised for Unique tav from the get go by the mod author themselves, however some may not have been optimised for Unique Tav, which in case you will need to look through [How to switch tattoo and makeup mods](#how-to-switch-tattoo-and-makeup-mods) and [Makeup and tattoo mods that have not been optimised for Unique Tav](#makeup-and-tattoo-mods-that-have-not-been-optimised-forunique-tav)


> However, for now you can only have one makeup, one tattoo and one body tattoo at all times when using Unique Tav.
> So you cannot install two face tattoo's, you will need to choose one. Same with body and makeup mods.
{.is-info}


- Other loose file mods such as Boring Tieflings and smooth body

This is basically the same as above. 
The mods can be made compatible, but it requires renaming and moving some files around. 
How to do that can be found in this section: [How to make other loose file mods compatible with Unique Tav](#how-to-make-other-loose-file-mods-compatible-with-unique-tav)

> All of this is the same for [Kaz Virtual Tav - Custom Appearance System](https://www.nexusmods.com/baldursgate3/mods/8912)
> Patches will work the same, and how to handle it will work the same. 
> For users, this will look like the same mod, however internally they handle things differently. (See mod description of Kaz Virtual Tav - Custom Appearance System)
{.is-info}


## How to switch tattoo and makeup mods 

## Makeup and tattoo mods that have not been optimised for Unique Tav 

## How to make other loose file mods compatible with Unique Tav 

## General usage such as changing tattoo colors

## Common issues, user errors and how to fix them

## Other information




  

---
title: Unique Tav: Everything you need to know
description: 
published: false
date: 2024-05-04T00:25:52.974Z
tags: bg3mm, installation, loose-file-mods, manual-mods, manual, how-to, unique-tav, loose-file, loose
editor: markdown
dateCreated: 2024-05-03T22:55:56.961Z
---

# Unique Tav guide & everything you need to know

This is a guide that will cover all of [Unique Tav](https://www.nexusmods.com/baldursgate3/mods/2754)
What is Unique Tav? Unique Tav is a mod that functions as a tool for a lot of mod users and mod creators, where they can customize their character a lot more than you would have been able to in vanilla BG3. For example you need unique tav for body tattoo's.

If you are an experienced user, there will be some useful information in this guide, however take a look at [Kartoffel's YouTube Video](https://www.youtube.com/watch?v=g67eTrz9fWg) Unique Tav.

As this is going to be a big guide, here are the things it will cover:
1. [How to install Unique Tav](#how-to-install-unique-tav)
	- [How to install the Pak file](#how-to-install-the-pak-main-file)
  	- [Load order in BG3MM/Vortex](#load-order-in-bg3mm/vortex)
  	- [How to install the Data main file](#how-to-install-the-data-main-file)
1. Compatibility 
1. How to switch tattoo and makeup mods 
1. How to make other loose file mods compatible with Unique Tav 
	- Makeup and tattoo mods that have not been optimised for Unique Tav 
1. Other loose file mods such as boring tieflings, smooth body etc. 
1. General usage such as changing tattoo colors
1. Common issues and user errors 
	- How to fix them 
1. Other information


## How to install unique Tav

Installing unique Tav, it is recommended to not use Vortex but use BG3MM and install the data part as a loose file mod, simply because of how complex this mod is. If you use Vortex, install the pak file as normal and then follow [how to install the data main file](#how-to-install-the-data-main-file-in-unique-tav).

The first thing you need to do is go to [Unique Tav's mod page](https://www.nexusmods.com/baldursgate3/mods/2754) and download both main files.
You will also need [Trips' Old Shader Pack](https://www.nexusmods.com/baldursgate3/mods/4752).

> Both main files are a requirement. 
> Likewise Trips' Old Shader Pack also a requirement. 
> Mac players will likely have an issue because of Trips' Old Shader Pack but the mod cannot function correctly without it. 
{.is-warning}

#### How to install the Pak main file

When you have downloaded both Trips' Old Shader Pack and the main pak file from Unique Tav, you will need to import the pak main file and Trips' Old Shaderpack into BG3MM/vortex.
If in BG3MM, remember to put the mod into the active side and "save/export order". 
If you do not know how to install a pak file, follow the guide on [How-to-Install-Pak-Files](/Tutorials/Mod-Use/How-to-Install-Pak-Files)

If in Vortex, remember to deploy and fix the load order after according to the guide below.

> Trips' Old Shader pack will be in the overrides section of BG3MM and likely locked in Vortex. 
> Leave those there. Everytime BG3MM puts a mod in the overrides, it is for a reson and that is because they override base game files. 
> As Trips' Old Shaderpack is also brown and an override, you cannot disable/make it inactive without deleting it from your mods folder (`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`)
{.is-info}

#### Load order in BG3MM/Vortex

Unique Tav should be relatively low on your load order, which means it should be below any heads and cosmetic mods you may have, but above any patches you may have.
Low means the higher number in both Vortex and BG3MM. 
Higher on the load order means the lowest number in BG3MM and Vortex.

For example like this: 

![uniquetavloadorder.png](/tutorials/unique_tav/uniquetavloadorder.png)

If you are using other mods such as [Eyes of Beholder](https://www.nexusmods.com/baldursgate3/mods/315) or [Astralities' Glow Eyes](https://www.nexusmods.com/baldursgate3/mods/4964) you will need the patches from Unique Tav as well. It will be under "files" on Unique Tav's Nexus Page, then under "optional files":

![files.png](/tutorials/unique_tav/files.png)

Then under the "optional files". 

![eyesofbeholderpatch.png](/tutorials/unique_tav/eyesofbeholderpatch.png =x490)

(Astralities does have a patch under her own Astralities' Glow Eyes mod. Both are fine and can be used, just use one of them). 

**Or**

![gloweyespatch.png](/tutorials/unique_tav/gloweyespatch.png =x490)

Remember not to choose both as Astralities' Glow Eyes and Eyes of Beholder are incompatible.

The load order has It would look something like this: 

![eyesofbeholder.png](/tutorials/unique_tav/eyesofbeholder.png =x120)

This example has Eyes of Beholder, but it will be the exact same load order just with Glow eyes patch from Unique Tav and Glow eyes main file and preset from Glow eyes. 

Example with Astralities' Glow Eyes and Unique Tav patches: 

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



#### How to install the Data main file
  

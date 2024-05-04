---
title: Unique Tav: Everything you need to know
description: 
published: false
date: 2024-05-04T21:31:55.634Z
tags: bg3mm, installation, loose-file-mods, manual-mods, manual, how-to, unique-tav, loose-file, loose
editor: markdown
dateCreated: 2024-05-03T22:55:56.961Z
---

# Unique Tav guide & everything you need to know

This is a guide that will cover all of [Unique Tav](https://www.nexusmods.com/baldursgate3/mods/2754)
What is Unique Tav? Unique Tav is a mod that functions as a tool for a lot of mod users and mod creators, where they can customize their character a lot more than you would have been able to in vanilla BG3. For example you need unique tav for body tattoo's.

If you are a beginner to modding BG3, it is recommended you stick with the beginning of this guide. 
The beginning is how to install unique tav, compatiblity and common errors. 

If you are an experienced user, there will be a lot of useful information in this guide, however take a look at [Kartoffel's YouTube Video](https://www.youtube.com/watch?v=g67eTrz9fWg) about Unique Tav.

As this is going to be a big guide, here are the things it will cover:
1. [How to install Unique Tav](#how-to-install-unique-tav)
	- [How to install the Pak file](#how-to-install-the-pak-main-file)
  	- [Load order in BG3MM/Vortex](#load-order-in-bg3mm/vortex)
  	- [How to install the Data main file](#how-to-install-the-data-main-file)
1. [Compatibility](#compatibility)
1. [Common issues and how to fix them](#common-issues-and-how-to-fix-them)
1. [How to switch tattoo and makeup mods](#how-to-switch-tattoo-and-makeup-mods)
	- [Makeup and tattoo mods that have not been optimised for Unique Tav](#makeup-and-tattoo-mods-that-have-not-been-optimised-for-unique-tav)
1. [How to make other loose file mods compatible with Unique Tav](#how-to-make-other-loose-file-mods-compatible-with-unique-tav)
1. [General usage such as changing tattoo colors](#general-usage-such-as-changing-tattoo-colors)
1. [Other information](#other-information)

## How to install unique Tav
Installing unique Tav, it is recommended to not use Vortex but use BG3MM and install the data part as a loose file mod, simply because of how complex this mod is. If you use Vortex, install the pak file as normal and then follow [How to install the Data main file](#how-to-install-the-data-main-file)

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

If you have issues then go to [Common issues and how to fix them](#common-issues-and-how-to-fix-them)

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
Nothing bad will happen if you do not have a patch, but you will just not be able to use body tatto's etc, 

- Good mods to have for compatibility with Unique Tav 

A mod that is good, even without Unique Tav is [Patches for CC Mods (Races Hairs Heads Cosmetic and such) by Padme4000](https://www.nexusmods.com/baldursgate3/mods/353)

This mod covers a lot, which is why it is split up in different uploads. Overall it patches different mods so they can be used together without any issues. Remember to read the mod description to get an overview of what it does. 

- Tatto's and makeup 

All tattoo and makeup mods can be compatible with Unique Tav. 
Some of them have been optimised for Unique tav from the get go by the mod author themselves, however some may not have been optimised for Unique Tav, which in case you will need to look through [How to switch tattoo and makeup mods](#how-to-switch-tattoo-and-makeup-mods) and [Makeup and tattoo mods that have not been optimised for Unique Tav](#makeup-and-tattoo-mods-that-have-not-been-optimised-for-unique-tav)


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

## Common issues and how to fix them

#### Invisible body:

If your Tav has an invisible body, you need to check if you have installed the pak file correctly. Look through [How to install the Pak file](#how-to-install-the-pak-main-file)

It may also be a load order issue, which in that case look through [Load order in BG3MM/Vortex](#load-order-in-bg3mm/vortex). 

Remember: High on the load order means the lowest number (0, 1, 2, etc) in BG3MM/Vortex and low on the load order means the highest number (depending on mods, 50, 51, etc). 
Unique Tav needs to be placed relatively low on the load order. 

If it is none of those things, check if you installed the data main file correctly. Look through [How to install the Data main file](#how-to-install-the-data-main-file)

#### Blue body

If you have a blue body, it is because you are missing [Trips' Old Shader Pack](https://www.nexusmods.com/baldursgate3/mods/4752). 

Remember this mod is a must! It is a requirement. Sadly, if you have a mac you may encounter issues when you use this mod. 

This was not an requirement before Patch 5, which changed a lot of textures and how they work. 

#### Tattoos or makeup mods does not work

Make sure you do not have any other tatto or makeup mods installed. These will likely be outside of the Unique Tav folders in "Generated" in your Data folder. 

If it does not work, try moving your "Generated" folder from your data folder, reinstall the data main file from Unique Tav, and the make/tattoo mod you want. 

Look here through these two to properly install face/body tattoo's and make up mods: [How to switch tattoo and makeup mods](#how-to-switch-tattoo-and-makeup-mods) and [Makeup and tattoo mods that have not been optimised for Unique Tav](#makeup-and-tattoo-mods-that-have-not-been-optimised-forunique-tav)

## How to switch tattoo and makeup mods 

You will first need to find a face tattoo, makeup mod or a body tattoo mod to download. The mod used in this guide is [Mari's makeup](https://www.nexusmods.com/baldursgate3/mods/4201)

Go under files, then you will need to download the one that specifies it is for Unique Tav. You will need to download via manual download. 

![maridownload.png](/tutorials/unique_tav/maridownload.png =x370)

When you have downloaded it, you will need to extract it. 

![maridownloaded.png](/tutorials/unique_tav/maridownloaded.png)

![mariextractt.png](/tutorials/unique_tav/mariextractt.png)

When you have extracted it, delete the zip file and go one folder deeper, until you find the "Generated" folder. 

![generatedmari.png](/tutorials/unique_tav/generatedmari.png)

Now you need to drag it into your Data folder (`\SteamLibrary\steamapps\common\Baldurs Gate 3\Data`). Make sure not to drag it on top of other folders. 

![marimovedgen.png](/tutorials/unique_tav/marimovedgen.png)

Now this will come up: 

![sayyestoreplace.png](/tutorials/unique_tav/sayyestoreplace.png)

It is important you say "Replace the file in the destination" as otherwise the change will not happen, as you did not replace the file it needed to replace. 

When you have done this, you have now replaced either a body or a face tattoo. 
Remember: you can only have one face tattoo and one body tattoo, not two at the same time. 

> You will notice you already have a "Generated" in your Data folder, which is how it is supposed to be. The new "Generated" folder will replace either a singular file or a few files in the data "Generated" folder as seen above. Do not worry, it will not replace the whole "Generated" folder.
>
> If you had a face tattoo before you installed Unique Tav, you need to delete it before installing a new one. Otherwise you may not see any modded face tattoo's at all in the mirror or character creation.
{.is-warning}

## Makeup and tattoo mods that have not been optimised for Unique Tav 

> For this part, you will need to have "file extension" on. This guide will show how to put that on in Windows 11. If you have Windows 10, it may be a bit different: [How to view file extension for windows 7, 8 and 10](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-enable-hidden-file-extensions-in-Windows.html)
{.is-warning}

How to view file extension on Windows 11: 

![fileextension.png](/tutorials/fileextension.png =x500)

#### Makeup, face tattoo mods

Some mods, such as [CovenElf's Tattoo and Makeup Collection (v1.2 Update)](https://www.nexusmods.com/baldursgate3/mods/1684) is not optimised for Unique Tav. This means you will need to be a little more hands on than above. 

You will do the exact same as [How to switch tattoo and makeup mods](#how-to-switch-tattoo-and-makeup-mods): download, extract the mod in your downloads folder, and find the "Generated" folder in the mod you downloaded. When you find the "Generated" folder, you will need to keep going to find the end files. The files should be in the folder called "Resources". These end files should look like this: 

![endfiles.png](/tutorials/unique_tav/endfiles.png)

Now you need to find the Unique Tav version of these files. 
Go into your Data folder, then "Generated". 
Follow this path: `\SteamLibrary\steamapps\common\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\FACE`

You should see three files: 

![facetattoo.png](/tutorials/unique_tav/facetattoo.png)

You will now need to replace some names and file extensions. 

First you copy Unique Tav's version of the face tatto (`Skin_Atlas_Head_SHR_Tattoo_A_MSK.DDS`) and replace the name on the newly downloaded face tattoo in your downloads folder. 

For example CovenElf's (or the mod you downloaded) face tattoo goes from: `Skin_Atlas_Head_SHR_Tattoo_A_MSK1.dds` to `Skin_Atlas_Head_SHR_Tattoo_A_MSK.DDS`

When you have renamed the new version to Unique Tav's version, drag the renamed file into the Unique Tav's "FACE" folder: 

![renameandreplace.png](/tutorials/unique_tav/renameandreplace.png)

After this, you will need to replace the file: 

![sayyestoreplace.png](/tutorials/unique_tav/sayyestoreplace.png)

Now you do the same with the makeup mod, So the file name goes from: `Skin_Atlas_Head_SHR_Makeup_A_MSK2.dds` to `Skin_Atlas_Head_SHR_Makeup_A_MSK.DDS`

Drag the newly renamed file into Unique Tav's "FACE" folder: 

![makeupreplacee.png](/tutorials/unique_tav/makeupreplacee.png)

And then you say yes to replace again: 

![sayyestoreplace.png](/tutorials/unique_tav/sayyestoreplace.png)

When you have done this, you're good to go and have installed the new MakeUp or Face Tattoo mod. 

> Note: Some modded tattoo's does not work on modded faces and it will instead show the vanilla tattoo's. Unfortunately there is not fix to this, other than report a bug to the mod creator of the modded face. 
{.is-info}


#### Body tattoo's that does not have the folder "Generated"

Most of the time, Body Tattoo's will come ready with a "Generated" folder to put into the Data folder. However, sometimes that may not be the case. 

For example, Unique Tav's own optional file "Tattoo varient" does not come with a "Generated" folder, but rather each individual tattoo in their own folder. 

You need to do as above, download and extract the body tattoo you wish. Then find the end file from the mod you downloaded: 

![bodytattoo.png](/tutorials/unique_tav/bodytattoo.png)

Then you find the Unique Tav folder where the body tattoo's are placed: 
`\SteamLibrary\steamapps\common\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\BODY\TATTOO`

![utbodytattopng.png](/tutorials/unique_tav/utbodytattopng.png)

No need to rename the file, as all body tattoo's automatically should be named the same. 
So all you need to do, is to drag the downloaded body tattoo into Unique Tav's folder "TATTOO": 

![utbodytattoomove.png](/tutorials/unique_tav/utbodytattoomove.png)

You will need to replace again: 

![bodytattooreplace.png](/tutorials/unique_tav/bodytattooreplace.png)

When you have done so, you have successfully changed the body tattoo. 

## How to make other loose file mods compatible with Unique Tav 

#### Loose files that changes companions, head replacers, or adds clothes in the game

These files does not need to be made Unique Tav compatible. 
You can follow [How to install manual or loose file mods](/Tutorials/Mod-Use/How-to-install-manual-or-loose-file-mods)

#### Other loose file mods such as texture mods 

These mods include mods such as [Boring Tieflings](https://www.nexusmods.com/baldursgate3/mods/2228) and [Smooth and muscular Githyanki F Body](https://www.nexusmods.com/baldursgate3/mods/1902). 
There are tons of other mods out there like these, so instead of going through them all, this guide will show how to make Boring Tieflings compatible with Unique Tav. 
This method will apply to all other loose file mods that needs to be made compatible (mostly texture mods) with Unique Tav. 

> For this part, you will need to have "file extension" on. This guide will show how to put that on in Windows 11. If you have Windows 10, it may be a bit different: [How to view file extension for windows 7, 8 and 10](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-enable-hidden-file-extensions-in-Windows.html)
{.is-warning}

How to view file extension on Windows 11: 

![fileextension.png](/tutorials/fileextension.png =x500)

You will first need to download the mod via manual download from Nexus, and extract the mod inside your downloads folder. 

![boringtief.png](/tutorials/unique_tav/boringtief.png)

![extractboringtief.png](/tutorials/unique_tav/extractboringtief.png)

Then you will to find the end files in the extracted folder in your downloads folder. 
You can also delete the zip, rar or 7z file because you no longer need it. 

![boringtiefendfiles.png](/tutorials/unique_tav/boringtiefendfiles.png)

When you have found the end files, you will need to find your data folder, then the "Generated" in your data folder. 

![generatedfolder.png](/tutorials/unique_tav/generatedfolder.png)

When you have found this, you will need to find the corresponding files. Now, if you have downloaded a mod like Smooth body for Githyanki, this will take some time, because you will need to find every single corresponding file and then you will need to renmame and replace the files. 

This guide will show you this is done. 

As seen in the previous screenshot of Boring Tieflings, I decided to download Boring Tieflings for females. 
I will now need to go into the "Generated" folder in my data folder, and find the Tieflings section. You do this by following the folders in Unique Tav. 

Since I choose a tiefling texture mod, I will need to go into the folder called "TIF", and then choose the folder named "Female" because I choose a mod for the female tiefling textures. 

![tiffoldeer.png](/tutorials/unique_tav/tiffoldeer.png)

![tieflingfemalefolder.png](/tutorials/unique_tav/tieflingfemalefolder.png)

You should now see a folder like this: 

![femaletiffolderpng.png](/tutorials/unique_tav/femaletiffolderpng.png)

Now you go back to the end files from before, and compare the files: 

![boringtiefendfiles.png](/tutorials/unique_tav/boringtiefendfiles.png)

From comparing, I know the Unique Tav version of "`TIF_F_NKD_Body_A.gr2`" is "`UNIQUE_TIF_F_NKD_BODY_A.GR2`"
I also know the Unique Tav version of "`TIF_F_Tail_A.GR2`" is "`UNIQUE_TIF_F_NKD_Tail_A.GR2`"

I will now need to rename the Boring Tiefling files to the Unique Tav version. 
When I have done that, I will need to drag the new files into the Unique Tav Tiefling Female section like this: 

![renametif.png](/tutorials/unique_tav/renametif.png)

![movetiftotif.png](/tutorials/unique_tav/movetiftotif.png)

You will need to replace the files as shown below: 

![tifreplace.png](/tutorials/unique_tav/tifreplace.png)

When you have done this for all of the files, you are done and have made the mod compatible and installed the mod. 
Yes, you will need to do this for all of the files.

> This method works for all texture mods that replaces textures on your own Tav (character). 
> TLDR: Find the corresponding files in Unique Tav folders, and rename the texture mods you downloaded to Unique Tav's version, and replace the Unique Tav's version with the newly renamed texture files.
>
> You will need to change the file extensions, to be uppercase rather than lower case!
{.is-info}


## General usage such as changing tattoo colors


> This is for advanced users as this requires opening up a pak and repacking it again
{.is-warning}

You will need a few programs for this. 

- You will need either multitool or Lslib to unpack the pak and pack the pak again
- You will need NotePad++ or VSCode to open the unpacked pak and make edits
> 
> Which pak you will open up depends on if you use Eyes of Beholder or Astralities' Glow Eyes as well. 
> If you use either of those two, you will need to open up Eyes of Beholder or Astralities' Glow Eyes. 
> If you do not use either of those, then you need to open up and edit Unique Tav itself. 
> This is because Eyes of Beholder or Glow Eyes overrides Unique Tav, so editing Unique Tav will not yield any results.
{.is-info}



When you have opened up the pak, you will need to edit for the individual race or subrace. So for example, if you play a tiefling, you would need to edit one of the tieflings subraces, and then you will further need to find the body type as well. Each race has their own section under "PAK_CharacterVisuals": 

![pak.png](/tutorials/unique_tav/pak.png)

For example, if you wish to edit the tattoo color and metallics of body type 1, female, of asmodeus tiefling then search for "female" under "tieflings.lsf.lsx" (ctrl + f in VSCode), and you will find: "Tieflings_Female_Asmodeus_Player_Dev_fecb40db-3672-480a-a1d4-4439ffb031cd". If you want the strong body type, you search for female and choose the strong version, "Tieflings_Female_Asmodeus_Player_Strong_7abd78c4-41cc-4910-aaf2-4e06fd314303". 

Under these you will see a lot of visual nodes, but you will focus on these three under the body, race and subrace you want to edit: 

"BodyTattooColor" controls the tattoo color. You will need to replace "1 0 0" with a sRBG color you find on google or via multitool color picker. 

								<node id="Vector3Parameters">
									<attribute id="Color" type="bool" value="False" />
									<attribute id="Custom" type="bool" value="True" />
									<attribute id="Enabled" type="bool" value="True" />
									<attribute id="Parameter" type="FixedString" value="BodyTattooColor" />
									<attribute id="Value" type="fvec3" value="1 0 0" />
								</node>

"TattooMetalNess" controls if the tatto's are metallic or not. 0 means they are not, 1 means they are. 
							
              <node id="ScalarParameters">
									<attribute id="Color" type="bool" value="False" />
									<attribute id="Custom" type="bool" value="True" />
									<attribute id="Enabled" type="bool" value="True" />
									<attribute id="Parameter" type="FixedString" value="TattooMetalness" />
									<attribute id="Value" type="float" value="0" />
								</node>

"Reflectance" controls the intensity. If you have it at 0, it will not be enabled and not be metallic. More than 0 enables it. From 0-2 controls how intense the metallicness will be.

								<node id="ScalarParameters">
									<attribute id="Color" type="bool" value="False" />
									<attribute id="Custom" type="bool" value="True" />
									<attribute id="Enabled" type="bool" value="False" />
									<attribute id="Parameter" type="FixedString" value="Reflectance" />
									<attribute id="Value" type="float" value="0.6" />
								</node>
                
When you have done your edits, remember to save and then pak the file. Replace the pak in your mods folder, save/export order and you should see the effect take place. 

## Other information
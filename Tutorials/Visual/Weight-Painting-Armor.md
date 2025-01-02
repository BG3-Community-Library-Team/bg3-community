---
title: Weight Painting Armor and Clothes
description: Tutorial on how to weight paint armor and clothes in Blender.
published: false
date: 2025-01-02T13:42:21.421Z
tags: visual, tutorial, blender, meshes, armor, clothes, weight painting
editor: markdown
dateCreated: 2025-01-01T21:58:19.593Z
---

# Weight Painting Armor and Clothes

***[WORK IN PROGRESS]***

This tutorial is  aimed at teaching you the basics of how to weight paint armor and clothes in Blender, so that your custom-made equipment properly moves and follows character animations in the game.
## Table of Contents
1. [Pre-requisites](#pre-requisites)
1. [Finding similar vanilla armor](#finding-similar-vanilla-armor)
1. [Bringing the vanilla assets into Blender](#bringing-the-vanilla-assets-into-blender)
1. [Transfering weights](#transfering-weights)
1. [Testing the weights](#testing-the-weights)
1. [Fixing weights issues](#fixing-weights-issues)
1. [Weight painting stiff armor pieces](#weight-painting-stiff-armor-pieces)
1. [Limiting weights](#limiting-weights)
1. [Exporting and testing](#exporting-and-testing)
1. [Final touches](#final-touches)

## Pre-requisites
> This tutorial assumes that:
• You have Blender (3.6 and above) installed and you are minimally familiar with its interface
• You have the Blender plugin [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter) installed to import and export game meshes to and from Blender.
• You have [Modder's Multitool](https://wiki.bg3.community/Tutorials/Visual/getting-started-with-3d-modding#tools-modders-multitool) or the [Baldur's Gate 3 Toolkit](https://mod.io/g/baldursgate3/r/installing-the-toolkit#heading-3) installed to look up and extract meshes from the game.
• **You have an armor or clothes mesh that is already fitted to your body type and race of choice**.
{.is-success}

> This tutorial is ***not*** going to teach you how to create armor and clothes.
{.is-warning}

> It is recommended to weight paint your armor and clothing ***before*** refitting it to other body types and races.
{.is-info}


Now let's get started!

## Finding similar vanilla armor
The first step is to find armor or clothing in the game files that is roughly similar to your custom armor, so that we can steal the weights from it. The closest in shape to your custom armor the vanilla asset is, the better the weight transfer will be.

For the duration of this tutorial, we will be weight painting this 100% custom armor set:
![1_armor_in_blender.png](/weight_painting_armor_tutorial/1_armor_in_blender.png)
*Source:* https://artstn.co/m/RGmbB



Since our armor is composed of full plate armor, with a skirt and a cloak, and is fitted to Humanoid Body Type 1, we will search for similar body type 1 assets using the Toolkit's Resource Manager or Modder's Multitool.
> All armors and clothes in the game have the same naming structure using a combination of tags. 
They all start with `RACE_BODYTYPE_ARM` for armor and `RACE_BODYTYPE_CLT` for clothing.
ㅤ
To find armor for your chosen body type, refer to the following list of tags:
ㅤ
***RACE:***
`DGB` for Dragonborn
`DWR` for Dwarf
`GTY` for Githyanki
`GNO` for Gnome
`HFL` for Halflings
`HRC` for Half-Orcs
`HUM` for Humans, Elves, Drows, Half-Elves and Tieflings
ㅤ
***BODY TYPE:***
`F` for Body Type 1 (fem)
`M` for Body Type 2 (masc)
`FS` for Body Type 3 (fem strong, only for HUM races)
`MS` for Body Type 4 (masc strong, only for HUM races)
{.is-info}

In our case, we are looking for humanoid feminine armors, so we are going to type `HUM_F_ARM` in the search bar of the Toolkit or the Multitool. 
![2_toolkit_mesh_search.png](/weight_painting_armor_tutorial/2_toolkit_mesh_search.png)

The Oathbreaker armor is very close to our custom armor, so we will be using the whole set for out example.
![3_oathbreaker_armor.png](/weight_painting_armor_tutorial/3_oathbreaker_armor.png)
It doesn't have a front skirt though, so we will also be borrowing the loincloth from the Barbarian starting armor.
![4_barbarian_skirt.png](/weight_painting_armor_tutorial/4_barbarian_skirt.png)

Now that we have identified the vanilla armor pieces that are similar to our custom armor, we can go ahead and extract them.

> Baldur's Gate 3 uses the GR2 file format to store its 3D objects and meshes.
{.is-info}

> In the Toolkit, right click on an asset and click Extract Visual Data to extract the GR2.
> In Modder's Multitool, click on the Extract File icon.
{.is-info}

## Preparing the vanilla assets in Blender
Now that we have extracted the GR2 files, it's time to import them into Blender.
> We need the Blender plugin [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter) installed to import and export GR2 files to and from Blender.
{.is-warning}


## Transfering weights
## Testing the weights
## Fixing weights issues
## Weight painting stiff armor pieces
## Limiting weights
## Exporting and testing
## Final touches
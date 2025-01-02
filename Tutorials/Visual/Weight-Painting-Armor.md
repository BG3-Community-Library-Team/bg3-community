---
title: Weight Painting Armor and Clothes
description: Tutorial on how to weight paint armor and clothes in Blender.
published: false
date: 2025-01-02T16:48:41.164Z
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
1. [Preparing the vanilla assets in Blender](#preparing-the-vanilla-assets-in-blender)
1. [Transfering weights](#transfering-weights)
1. [Testing the weights](#testing-the-weights)
1. [Fixing weights issues](#fixing-weights-issues)
1. [Weight painting stiff armor pieces](#weight-painting-stiff-armor-pieces)
1. [Limiting weights](#limiting-weights)
1. [Exporting and testing](#exporting-and-testing)
1. [Final touches](#final-touches)

## Pre-requisites
> This tutorial assumes that:
• You have Blender (3.6 and above) installed and you are at least minimally familiar with its interface
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

Since our armor is fitted to Humanoid Body Type 1 (fem), we will search for similar body type 1 assets using the Toolkit's Resource Manager or Modder's Multitool.
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
ㅤ
So for example if you are looking for armor that specifically fits masculine Githyanki frames, you have to search for `GTY_M_ARM`
{.is-info}

- In our case, we are looking for humanoid feminine armors, so we are going to **type `HUM_F_ARM` in the search bar of the Toolkit or the Multitool**. 
![2_toolkit_mesh_search.png](/weight_painting_armor_tutorial/2_toolkit_mesh_search.png)

The Oathbreaker armor is very close to our custom armor, so we will be using the whole set for out example.
![3_oathbreaker_armor.png](/weight_painting_armor_tutorial/3_oathbreaker_armor.png)
It doesn't have a front skirt though, so we will also be borrowing the loincloth from the Barbarian starting armor.
![4_barbarian_skirt.png](/weight_painting_armor_tutorial/4_barbarian_skirt.png)
And lastly for the cape we will be using HUM_F_ARM_Cape_Long_A
![5_cape.png](/weight_painting_armor_tutorial/5_cape.png)

- Now that we have identified the vanilla armor pieces that are similar to our custom armor, we can go ahead and **extract** them.

> Baldur's Gate 3 uses the GR2 file format to store its 3D objects and meshes.
{.is-info}

> In the Toolkit, right click on an asset and click Extract Visual Data to extract the GR2.
> In Modder's Multitool, click on the Extract File icon.
{.is-info}

## Preparing the vanilla assets in Blender
Now that we have extracted the GR2 files, it's time to import them into Blender.
> We need the Blender plugin [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter) installed to import and export GR2 files to and from Blender.
{.is-warning}

- In the same Blender file as your custom armor, import the GR2s by going to `File > Import > .gr2` and import all of the GR2s we have extracted, one by one.

- Once you have imported all of the vanilla meshes, select all of them, and with your cursor in the viewport press `CTRL+A` and `Apply All Transforms`

  ![6_apply_transforms.png](/weight_painting_armor_tutorial/6_apply_transforms.png)

- Next, you can go ahead and **delete all the LOD meshes**, we won't need them. 
  You can also **delete meshes or mesh parts that are useless** and don't match up with your custom armor well. If we don't delete the extra meshes that we don't need, they could throw off the weight transfer.

In our example's case, we will get rid of the hanging belt, the unnecessary barbarian pants and the back skirt of the barbarian skirt.
> Keeping the Cloth Meshes is a good idea, you can reuse them to add cloth physics to your skirts and capes, although we will not be covering cloth physics in this tutorial.
{.is-success}

We end up with an armor set that is very similar to our custom armor:
![7_armor_comparison.png](/weight_painting_armor_tutorial/7_armor_comparison.png)
Don't worry if yours doesn't match as well, the weight transfer will still work.

- Next, we will **merge the vanilla armor meshes together** to have an easier time during weight transfer. Even if the vanilla meshes you chose overlap, just merge them together. 
> The only vanilla mesh parts you shouldn't merge with the rest are parts like the **skirt** or the **cape**, since they will receive cloth physics and are weighted differently than the rest of the armor.
{.is-warning}

> To merge meshes in Blender, select them and press `CTLR+J` with your cursor in the viewport.
{.is-info}

Our vanilla armor is now all cleaned up and ready to be used for weight transfer!
- It's a good idea to once again select all the meshes and armatures and **Apply All Transforms**.

![8_cleaned_up_vanilla_armor.png](/weight_painting_armor_tutorial/8_cleaned_up_vanilla_armor.png)
## Transfering weights
We will now transfer weights from the vanilla armor to our custom armor.
For this step you need both your custom armor meshes and the vanilla meshes visible in Blender.
> Make sure your custom armor doesn't already have weights. 
**Delete all the weights from your custom armor before proceeding.**
> ![9_deleting_weights.png](/weight_painting_armor_tutorial/9_deleting_weights.png)
{.is-warning}

- **Select the vanilla armor and then your custom armor**. They must both be selected at the same time, and you must select your custom armor second. 
If your custom armor is separated into several meshes, just choose one mesh to select.
ㅤ
- Go to **weight paint mode** 
ㅤ
  ![10_weight_paint_mode.png](/weight_painting_armor_tutorial/10_weight_paint_mode.png)
ㅤ
- Go to `Weights > Transfer Weights`
ㅤ
  ![11_weight_transfer.png](/weight_painting_armor_tutorial/11_weight_transfer.png)
ㅤ
- Transfer Weights settings should have appeared on the bottom left of your screen. Expand that window.
ㅤ
- Change the `Vertex Mapping` setting to `Nearest Face Interpolated` and `Source Layers` setting to `By Name` like in the picture below. Then **click out of that window to confirm the settings**.
![12_weight_transfer_settings.png](/weight_painting_armor_tutorial/12_weight_transfer_settings.png)


Congratulations, you have transfered weights from the vanilla armor to your custom armor! You can verify that the operation was successfull by clicking on vertex groups and checking that weight paint is showing up on your mesh.
![13_weights_showing.png](/weight_painting_armor_tutorial/13_weights_showing.png)

Now do the same thing for all of the meshes in your custom armor. 
Fortunately, the Transfer Weights settings get saved and you don't have to set those each time, so that should speed up the process.

> For the cape we will transfer weights from the vanilla cape instead of from the vanilla armor. The same principle goes for the skirt. 
Select the vanilla cape first, then the custom cape second, and Transfer Weights.
{.is-warning}

## Testing the weights
## Fixing weights issues
## Weight painting stiff armor pieces
## Limiting weights
## Exporting and testing
## Final touches
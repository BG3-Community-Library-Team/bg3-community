---
title: Weight Painting Armor and Clothes
description: Tutorial on how to weight paint armor and clothes in Blender.
published: false
date: 2025-01-02T00:54:56.529Z
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

Let's take this armor set for example (we will be using it for the duration of this tutorial):

Since our armor is composed of full plate armor, with a skirt and a cloak, and is fitted to Humanoid Body Type 1, we will search for similar body type 1 assets using the Toolkit's Resource Manager or Modder's Multitool.
> All armors and clothes in the game have the same naming structure using tags, they all start with `RACE_BODYTYPE_ARM` for armor and `RACE_BODYTYPE_CLT` for clothing. To find armor for your chosen body type, refer to the following list of tags:
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

In our case, we are looking for humanoid feminine armors, so we are going to type `HUM_F_ARM` in the search bar.

## Bringing the vanilla assets into Blender
## Transfering weights
## Testing the weights
## Fixing weights issues
## Weight painting stiff armor pieces
## Limiting weights
## Exporting and testing
## Final touches
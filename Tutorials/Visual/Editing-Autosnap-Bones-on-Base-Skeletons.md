---
title: Editing Hair Autosnap Bones on Base Skeletons
description: How to edit the autosnaps on a bodytype's base skeleton to improve how hair fits.
published: false
date: 2025-09-27T19:14:26.040Z
tags: hair, skeleton
editor: markdown
dateCreated: 2025-09-27T18:23:28.968Z
---

# Editing Hair Autosnap Bones to Improve Hair Fit for Bodytype.
I want to start by saying, I don't recommend using this mod for anything other than the short races.

**Note:** This will not work on Half-Orcs because Half-Orcs do not use autosnap hair.

**Why?** Most NPCs are the tall types. So any edits you make to the base skeleton will affect every NPC!
Meanwhile, there are only a very small number of short race NPCs that you can speak to throughout game. If you don't mind some NPCs very rarely looking slightly off to improve the fit for your favorite head, then you can follow your dreams!

What you will need:
Larian's Official Toolkit (henceforth TK)
A lot of patience for trial and error

You're going to need a new project, whether you're starting from scratch or plan on using Gnome More Clipping (GMC) as the base. If importing Gnome More Clipping, select the pak after clicking the Import button. All Kelo asks is that you do not claim the base work as your own if you choose to make the edits public and please link back to the original mod.

When the TK asks you to load a level, search for and load Character Creation SYS_CC_I. There are some caveats around testing and the TK crashing but we will cross that bridge when we get to it.

Onto the guide!!

TODO will explain how i version controlled a TK mod because the TK hates symlinking and is weird about restoring edits.

Identify the race you plan on editing. In this guide, we're going to edit halfling Head 1 because it's a great example of why you may want to make a personal edit. Our example hair is Ballerina Buns.

(show image)
When we put Ballerina Buns on Head 1 we can see that the fringe is still clipping pretty noticeably into her right brow. This is even with GMC installed!!

Here is what the fringe is suppose to look like on Head 3. Notice how it extends cleanly over the right brow.
(show image)

Before we continue, please keep in mid that changes you make to the autosnap bones with one hair in mind, will affect the fit of ALL the hairs on ALL heads of that race.

Okay.

1) Open the Resource Manager by clicking on "Create or View Resources"
	(image)

2) If starting from scratch: click the All folder in the top left. Then in the search bar above it, we are going to search for the SkeletonResource we need to edit. For Halfling BT1, that's HFL_F_Base. To be absolutely clear: the Name is HFL_F_Base and the Type is SkeletonResource. Then you will need to Right Click + Select Override in Active Mod

For all races, they follow the format of RACE_M/F_Base.
	Key: Dwarf - DWR
  		 Halfling - HFL
       Gnome - GNO
       BT1 - F
       BT2 - M
       
If using GnomeMoreClipping as the base, you can see the models Kelo already edited in if you click GnomeMoreClipping > Assets. If you are starting from scratch, you will see your overridden files in the same place but the mod project folder name will be different.
(image)

We want to edit the halfing, so we're going to double click HFL_F_BASE_000. This will open the Skeleton Editor.
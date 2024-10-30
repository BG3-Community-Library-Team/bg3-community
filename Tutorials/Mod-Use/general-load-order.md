---
title: General Load Order Guide
description: Setting up a solid Load Order
published: true
date: 2024-10-30T00:10:58.708Z
tags: bg3-mod-helper, guide, mod use, mod load, load order, general load order, bg3 load order
editor: markdown
dateCreated: 2024-05-01T03:29:26.549Z
---

# General Load Order
This guide will give a general overview of how to handle Mod Load Orders. It's not meant to be a strict prescription, but it will assist in ensuring your load order has minimal issues and is easier to troubleshoot. 

**If playing in Multiplayer, it's important to note that you must have the exact same mods and load order as the other player, including mods listed in the inactive pane or loose-file mods, or you may run into problems.**

> Do not load/delete these entries:
> - Honour.pak
> - DiceSet_06.pak
> These are base game files that show in the Inactive Mods pane. They should stay in the Inactive Mods pane.
<!-- {blockquote:.is-danger} -->

> A note on Mod Load Order: There are a lot of ways people reference the order in which mods load. You'll often hear things like:
> - Higher/Lower on your Load Order
> - Earlier/Later on your Load Order
> - Biggest/Smallest Number
> - Top/Bottom of your Load Order
>
> The most important thing to be aware of is that the lower the number, the earlier a mod loads. To that end, I recommend talking about Load Order in terms of Early to Late loading mods, to clear up confusion. 0 is the Earliest mod to load, and mods loaded later than other mods may overwrite the earlier mod's changes. 
<!-- {blockquote:.is-info} -->

# Load Order Recommendations

Load orders should be set up in an order following the below structure. As always, if a mod's page recommends a specific placement load order, go with the author's suggestion.

## 1. Early Loaders
The first types of mods you should have on your list are **Library mods** and **Single-Purpose SE mods**.

- **ImpUI (ImprovedUI)** mod should be loaded the earliest! It makes changes to the existing game UI and is a requirement for various Races, Classes, UI's and many other mods! 
- **Library Mods** are mods that are relied on by other mods. Examples include 5eSpells, Unlock Level Curve, Community Library, Mod Configuration Menu (MCM),and Vlad's Grimoire.
- **Single-purpose SE mods** are mods that are standalone, and limited in scope. Examples include Loz's Autosave mods, and KvCampEvents, as well as most Frameworks.

## 2. New Items/Spells/Actions and Fixes
Next are mods that provide **playable actions, items, and dyes**, and mods that **fix base-game content and/or affect general gameplay** (ex. Concentration Failsafe, Shields Overhaul) should go next. Often these will rely on Early Loaders, or are mods that are expected to get overridden or referenced by other mods as well.

## 3. Expanded Content
The third chunk of mods you should place in your order are those that provide **new content to existing structures** (ex. FeatsExtra, Metamagic Extended, WildMagicD100)

> I recommend ordering these by type
{.is-info}

These types of mods also fall under this category:
- Additional Feats
- Additional Races/Subraces
- Additional Classes
- Additional Subclasses (organized by main class)

## 3.5 User Interface mods
UI mods like the Better Hotbar 2 mod can go here! 
> I recommend ordering them like this:
{.is-info}
- Dynamic Sidebar
- Better Character and Party Panels (BCPP)
- Better Containers
- Better Tooltips
- Better Hotbar or Better Hotbar 2
- Better Inventory UI

## 4. Visual Mods
Visual mods can technically go anywhere in the load order, but I've found having them load just before Late Loaders to be the most reliable.

> I recommend ordering these by type
{.is-info}

Examples of these include:
- Skin/Hair/Eye Color mods
- Custom Hairs
- Custom Cosmetics
- Custom Heads
- Custom Horns/Tails
- Custom Accessories
- Custom Tattoos
- Custom Dice

## 4.1 Unique Tav or Appearance Overrides
If you want more information on how to use Unique Tav, refer to the [UT Guide](/Tutorials/Mod-Use/Unique-Tav-Everything-you-need-to-know).

Mods that override the appearance of Tav or Companions, such as Unique Tav, have a very specific load order. You will know that it is incorrectly installed if you have issues such as blue or black skin, missing limbs, torso, or head.

>The following suggested load order for visual mods is only needed if you have UT or Appearance Override mods. Note that you must check all your visual mods to download UT patches or determine if they are compatible with UT.
{.is-info}

Examples of these include:
- Skin/Hair/Eye Color mods
- Custom Hairs
- Custom Cosmetics
- Custom Heads
- Custom Horns/Tails
- Custom Accessories
- UniqueTav/Appearance Override Mods
- UniqueTav Patches* 
- Custom Tattoos
- Custom Dice

## 5. Late Loaders
These types of mods should _always_ be near the bottom of your load order. They either overwrite existing content, or rely on the existence of other content.

> Minor patches should go closer to their primary mods - like the WarlockUndead5eSpells patch should go next to WarlockUndead
{.is-info}

Examples of Late Loaders include:
- Mods that consist only of Compatibility Framework insertions (so the Feat Every 2/3 levels - Compatibility Framework version, for example)
- Major patch mods (ex. Patches for CC Races, Spell List Combiner, Compatibility Framework)
- Compatibility Framework is last to load  
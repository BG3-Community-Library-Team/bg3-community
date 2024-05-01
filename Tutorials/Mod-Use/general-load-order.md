---
title: General Load Order Guide
description: Setting up a solid Load Order
published: true
date: 2024-05-01T05:00:49.737Z
tags: moduse, mod use
editor: markdown
dateCreated: 2024-05-01T03:29:26.549Z
---

# General Load Order
This guide will give a general overview of how to handle Mod Load Orders. It's not meant to be a strict prescription, but it will assist in ensuring your load order has minimal issues, and is easier to troubleshoot.

> Do not load these entries:
> - Honour.pak
> - DiceSet_06.pak
<!-- {blockquote:.is-danger} -->

> A note on Mod Load Order: There are a lot of ways people reference the order in which mods load. You'll often hear things like:
> - Higher/Lower on your Load Order
> - Earlier/Later on your Load Order
> - Biggest/Smallest Number
> - Top/Bottom of your Load Order
>
> The most important think to be aware of is that the lower the number, the earlier a mod loads. To that end, I recommend talking about Load Order in terms of Early to Late loading mods, to clear up confusion. 0 is the Earliest mod to load, and mnods loaded later than other mods may overwrite the earlier mod's changes. 
<!-- {blockquote:.is-info} -->

## Load Order Recommendations

Load orders should be set up in an order following the below structure. As always, if a mod's page recommends a specific placement load order, go with the author's suggestion.

### 1. Early Loaders
The first types of mods you shoul have on your list are Library mods and Single-Purpose SE mods.

Library Mods are mods that are relied on by other mods. Examples include 5eSpells, Unlock Level Curve, Community Library, and Vlad's Grimoire.
Single-purpose SE mods are mods that are standalone, and limited in scope. Examples include Loz's Autosave mods, and KvCampEvents, as well as most Frameworks.

### 2. New Items/Spells/Actions and Fixes
Next up are mods that provide playable actions, items, and dyes, and Mods that fix base-game content and/or affect general gameplay (ex. Concentration Failsafe, Shields Overhaul) should go next. Often these will rely on Early Loaders, or are mods that are expected to get overridden or referenced by other mods as well.

### 3. Expanded Content
The third chunk of mods you should place in your order are those that provide new content to existing structures (ex. FeatsExtra, Metamagic Extended, WildMagicD100)

> I recommend ordering these by type
{.is-info}


These types of mods also fall under this category:
- Additional Feats
- Additional Races/Subraces
- Additional Classes
- Additional Subclasses (organized by main class)

### 4. Visual Mods
Visual mods can technically go anywhere in the load order, but I've found having them load just before Late Loaders to be the most reliable.

> I recommend ordering these by type
{.is-info}

Examples of these include:
- Skin/Hair/Eye Color mods
- Custom Hairs
- Custom Cosmetics
- Custom Heads
- Custom Dice

### 5. Late Loaders
These types of mods should _always_ be near the bottom of your load order. They either overwrite existing content, or rely on the existence of other content.

> Minor patches should go closer to their primary mods - like the WarlockUndead5eSpells patch should go next to WarlockUndead
{.is-info}

Examples of Late Loaders include:
- Mods that consist only of Compatibility Framework insertions (so the Feat Every 2/3 levels - Compatibility Framework version, for example)
- Major patch mods (ex. Patches for CC Races, Spell List Combiner, Compatibility Framework)
- Compatibility Framework is last to load


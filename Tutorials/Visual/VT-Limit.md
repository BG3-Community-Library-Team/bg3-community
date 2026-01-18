---
title: Limits on Virtual Textures
description: 
published: false
date: 2026-01-18T11:33:31.420Z
tags: 
editor: markdown
dateCreated: 2026-01-18T11:33:31.420Z
---

# Limits on Virtual Textures
The official modding toolkit provides tools for creating and overriding virtual textures, but it imposes practical limits on how many can be added. In contrast, Script Extender removes these constraints.

## The Limit
Divinity Engine imposes a practical limit on the number of unique virtual textures the game can load and reference at runtime. The total number of tilesets is 64, minus the 16 base-game tilesets, minus 1 more from Script Extender. This leaves 47 VT tilesets the game will load in from mods. 

Exceeding this can result in:
- Textures failing to load (resulting in pink/black placeholders or blurry fallbacks).
- Crashes during area transitions or rendering.
- Performance degradation due to memory overflows in the virtual texture page table (the system that maps and streams VT tiles).

## Why This Limit Exists

Larian’s engine prioritizes cross-platform performance and memory efficiency. Since the Toolkit is designed for official Mod.io uploads, it emphasizes lightweight, compatible mods by adhering to the engine’s vanilla resource bounds. A VT limit also encourages modders to work within this limit and therefore maintain the game’s overall size and stability.

In practice, texture-heavy mods often hit this limit when combined with others, meaning modders may choose to prioritize or use non-VT alternatives.

However, Toolkit limits aren't "broken"—they're intentional and designed for broad user compatibility.

## How Script Extender Removes the Limit

BG3 Script Extender is a modding tool that allows modders to add unlimited .GTS files (the format for VT) by remapping how the game handles texture data.

SE intercepts during game launch, locates VT-enabled mods with SE mapping (meaning any VTs made using SE) and merges their texture data into one large file. Therefore, there is technically only one modded VT loaded into the game and the cap is never reached. 

However, SE isn’t magic - having a huge number of mods and / or VTs loaded in can still impact loading times. Performance will depend on your PC’s hardware and how many mods you’re using. 

Importantly, SE only does this with VTs compiled using SE – not the toolkit. 
 
> Mod creators can utilise VT Libraries to reduce their mods' contributions towards the VT limit - click here for more information.
{.is-info}

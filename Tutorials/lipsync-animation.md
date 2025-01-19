---
title: Making New Lipsync Animations
description: A guide to making new lipsync animations for the game, without using FaceFX.
published: false
date: 2025-01-19T15:05:10.682Z
tags: 
editor: markdown
dateCreated: 2025-01-19T15:05:10.682Z
---

# Making New Lipsync Animations
Hi! You'll probably need some background information on how dialogue system for the game before continuing with this guide. If you're not already familiar with the BG3 dialogue files and how they work, please check out these resources here:

- [A New Voice In Town - A Pretty Comprehensive Guide To Editing Dialog](https://www.nexusmods.com/baldursgate3/mods/10086)
- [Editing Dialogue Files](https://wiki.bg3.community/en/Tutorials/dialogue-files-tutorial)
- [Adding New Voice Lines And Dialogue](https://wiki.bg3.community/en/Tutorials/new-voice-lines)

That last tutorial is especially important, because this guide is designed to accompany it!

You've added your voice lines to the game. Now you just need lipsync!

...Which does require a little bit of a workaround.

As explained in the guide to adding new voice lines, the lipsync for Baldur's Gate 3 is generated via a program called FaceFX, which is prohibitively expensive for most modders, and while you can reuse the existing lipsync found in the game, it's not ideal if you want to write your own dialogue.

However, we *do* have a workaround—and it's a really good one.

By making our lipsync animations in Blender, and referencing them in the dialog timeline files through the TLAdditiveAnimation effect component, we can bypass the need to use FaceFX and .ffxanim files, while still being able to use the emotion rig system in the game.

This means you won't have to redo all your lipsync when you want to tweak a character's expressions, and you also won't have to drop $900 just to get your character to open their mouth when they speak. And look, there's nothing wrong with the occasional bout of ventriloquism, but that's not always what everyone wants for their characters.

So, let's get started!

### Requirements

- [Blender](https://www.blender.org/) (4.2 or higher)
- [BG3 IK Animation Rigs](https://www.nexusmods.com/baldursgate3/mods/14077) by [kirixiar](https://next.nexusmods.com/profile/kirixiar?gameId=3474)
- [Rhubarb Lip Sync NG](https://github.com/Premik/blender_rhubarb_lipsync_ng) (Blender plugin for generating and editing lipsync)
- [LSLib](https://github.com/Norbyte/lslib) (For converting animations and dialogue .lsf files)
- A code editor, I recommend [VSCode](https://code.visualstudio.com/)
- An understanding of how to edit dialogue timeline files for BG3
- A basic understanding of navigating and editing things in Blender (technically optional, but this will be much easier if you're familiar with the program)

### Getting Started

#### Installing the Rhubarb Lip Sync NG Plugin

#### Gathering your files

### Making The Animations

#### Building shapekeys

#### Pose library

#### Non-linear animation editor

### Adding your animations to the game

#### TLAdditiveAnimation and Dialogue Timelines

#### Packaging your mod
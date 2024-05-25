---
title: Getting Started with Visual Modding
description: Covers the basics of setting up the needed tools
published: false
date: 2024-05-25T14:10:25.729Z
tags: hair, visual, guide, head, beginner, armor
editor: markdown
dateCreated: 2024-05-25T14:10:25.728Z
---

# Getting Started with Visual Modding
Looking to get into modding game assets like heads, hair, armor, etc.? 

This guide will try to focus on setting up the basics needed to get started. The focus is currently primarily on working with 3D assets.

What it won't cover is whatever you want to do after the initial set up, i.e. the creation of visuals mods. These will be on their own pages, a list of which listed at the end of this guide.


## Tools overview

> These are just listed here for quick reference. A step-by-step guide to set up follows below.
{.is-success}


Tools for finding/extracting game assets:
- [LSLIB](https://github.com/Norbyte/lslib)
- [Modder's Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool)

Tools for 2D/3D editing:
- [Blender](https://www.blender.org/), plugins:
  - [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter)
  - [LaughingLeader's Blender Helpers](https://github.com/LaughingLeader/laughingleader_blender_helpers)
- [Gimp](https://www.gimp.org/), [Paint.net](https://www.getpaint.net/index.html), Photoshop, etc.

Tools for mod file setup:
- [VSCode](https://code.visualstudio.com/), plugins:
  - [XML Support](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml)
  - [BG3 Mod Helper](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper)
  - [BG3 GUID infos](https://marketplace.visualstudio.com/items?itemName=FallenStar.bg3guidinfos)
  - [Bracket Select](https://marketplace.visualstudio.com/items?itemName=chunsen.bracket-select)

Other useful things:
- [BG3 Search Engine](https://bg3.norbyte.dev/search)


## LSLIB

> [LSLIB](https://github.com/Norbyte/lslib/releases)
> use latest beta release
{.is-success}

> LSLIB is used for many things. Unpacking game/mod paks, converting various game file formats, creating paks, etc. 
> 
> (TODO: create/link page here on how to use various LSLIB functions)
{.is-info}

First, download the latest ExportTool zip file and make sure you have the listed .NET dependency first (linked on the release).

![2024-05-25_15_39_51.png](/tutorials/getting_started_visual/2024-05-25_15_39_51.png)

You can install/extract this where you want your modding utilities to be. 

For the purposes of this guide I have a directory for BG3 Utilities and have extracted it here:

![utilites-folder.png](/tutorials/getting_started_visual/utilites-folder.png)

At the moment there isn't too much to set up, a few notes:

![lslib.png](/tutorials/getting_started_visual/lslib.png)

- Game: is set to Baldur's Gate 3
- For most purposes you will want to have X-flip meshes turned OFF (default is on)


## Modder's Multitool


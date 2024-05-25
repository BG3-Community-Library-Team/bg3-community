---
title: Getting Started with Visual Modding
description: Covers the basics of setting up the needed tools
published: false
date: 2024-05-25T16:46:04.552Z
tags: hair, visual, guide, head, beginner, armor
editor: markdown
dateCreated: 2024-05-25T14:10:25.728Z
---

# Getting Started with Visual Modding
Looking to get into modding game assets like heads, hair, armor, etc.? 

This guide will try to focus on setting up the basics needed to get started. The focus is currently primarily on working with 3D assets.

What it won't cover is what happens after the initial set up, i.e. the creation of visuals mods. These will be on their own pages, a list of which listed at the end of this guide.


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

### Initial setup
To download, head over to Releases and grab the latest ExportTool zip. For those unfamiliar with Github, the releases will look like this. Just grab the zip and (if you need it) the .NET dependency via the link.

![2024-05-25_15_39_51.png](/tutorials/getting_started_visual/2024-05-25_15_39_51.png)

You can install/extract this where you want your modding utilities to be. 

For the purposes of this guide I have a directory for BG3 Utilities and have extracted it here:

![utilites-folder.png](/tutorials/getting_started_visual/utilites-folder.png)

At the moment there isn't too much to set up, a few notes:

![lslib.png](/tutorials/getting_started_visual/lslib.png)

- Game: is set to Baldur's Gate 3
- For most purposes you will want to have X-flip meshes turned OFF (default is on)


## Modder's Multitool

> [Modder's Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases)
> use latest release
{.is-success}

> MMT is another way to unpak/pak game files and mods. Additionally it is used for indexing these game files for searching.
{.is-info}

### Initial Setup
Same as with LSLIB, download from releases.

Instructions for installation and configuration can also be found on the Github page [here](https://github.com/ShinyHobo/BG3-Modders-Multitool/wiki/Installation).

For most cases you DO NOT need to mass unpack any game files. What you will want to do is index them so that you can use the "Search Index" option later.

![mmt.png](/tutorials/getting_started_visual/mmt.png)


## Blender

> [Blender](https://www.blender.org/)
> as of this writing most plugins will function with v4+ and can be used safely. Using at least v3.6+ is recommended.
>
>Note: you may have multiple versions installed on your PC
{.is-success}

> Blender is a free 3D modeling/animation software. Using plugins made for BG3 we can import/export GR2 files and edit them.
{.is-info}

### Important BG3 plugins

[BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter)
- This is a necessary plugin to import/export the games extracted GR2 files
- Requires LSLIB and setting a path to it in its settings

First, download 


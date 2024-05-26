---
title: Getting Started with 3D Modding
description: Covers the basics of setting up the needed tools
published: true
date: 2024-05-26T12:53:05.261Z
tags: hair, visual, guide, head, beginner, armor, 3d
editor: markdown
dateCreated: 2024-05-25T14:10:25.728Z
---

# WIP Getting Started with 3D Modding
Looking to get into modding game assets like heads, hair, armor, weapons, etc.? 

This guide will try to focus on setting up the basics needed to get started. The focus is currently primarily on working with 3D assets.

What it won't cover is what happens after the initial set up, i.e. the creation of head/hair/armour/etc. mods. These will be on their own pages, a list of which listed at the end of this guide.

### Overview of Guide
> - **Tools**
> 	- Download and setup of main tools needed to extract, import, and edit assets
> - **Finding assets**
> 	- Useful references
>   - Searching the files
> - **Next steps**
> 	- Links to specific guides regarding how to proceed, depending on what area you would like to mod.

## Tools
### Tools Overview

> This first part covers the installation of a few core tools needed to get you up and running.
> Includes:
> - LSLIB
> - Modder's Multitool
> - Blender and core related add-ons
> - VSCod(e/ium) and some useful extensions


## Tools: LSLIB

> [LSLIB](https://github.com/Norbyte/lslib/releases)
> use latest beta release
{.is-success}

> LSLIB is used for many things. Unpacking game/mod paks, converting between various game file formats and editable ones, creating paks, creating virtual textures, etc. 
> 
> (TODO: create/link page here on how to use various LSLIB functions)
{.is-info}

### Initial setup
To download, head over to Releases and grab the latest ExportTool zip. For those unfamiliar with Github, the releases will look like this. Just grab the zip and (if you need it) the .NET dependency via the link.

![lslib-release.png](/tutorials/getting_started_visual/lslib-release.png)

You can install/extract this where you want your modding utilities to be. 

For the purposes of this guide I have a directory for BG3 Utilities and have extracted it here:

![utilites-folder.png](/tutorials/getting_started_visual/utilites-folder.png)

At the moment there isn't too much to set up, a few notes:

![lslib.png](/tutorials/getting_started_visual/lslib.png)

- Game: is set to Baldur's Gate 3
- For most purposes you will want to have X-flip meshes turned OFF (default is on)


## Tools: Modder's Multitool

> [Modder's Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases)
> use latest release
{.is-success}

> MMT is another way to unpak/pak game files and mods. Additionally it is used for indexing these game files for searching and extracting.
{.is-info}

### Initial Setup
Same as with LSLIB, download from releases.

Instructions for installation and configuration can also be found on the Github page [here](https://github.com/ShinyHobo/BG3-Modders-Multitool/wiki/Installation).

For most cases you DO NOT need to mass unpack any game files. What you will want to do is index them so that you can use the "Search Index" option later.

![mmt.png](/tutorials/getting_started_visual/mmt.png)


## Tools: Blender

> [Blender](https://www.blender.org/)
> as of this writing most plugins will function with v4+ and can be used safely. Using at least v3.6+ is recommended.
>
>Note: you may have multiple versions installed on your PC
{.is-success}

> Blender is a free 3D modeling/animation software. Using plugins made for BG3 we can import/export the game's GR2 files and edit them.
{.is-info}

Once we have Blender installed, it's time to get some core plugins.

### Important BG3 Plugins

#### [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter)

> - This is a necessary plugin to import/export the games extracted GR2 files
> - Requires LSLIB and setting a path to it in its settings
{.is-info}


First, download zip from Github, located here:

![bg3plugin-gh.png](/tutorials/getting_started_visual/bg3plugin-gh.png)

Now go into Blender, Edit -> Preferences -> Add-ons -> ...Install

![blender-install-addon.png](/tutorials/getting_started_visual/blender-install-addon.png)

Find the .zip you downloaded:

![blender-install-addon-2.png](/tutorials/getting_started_visual/blender-install-addon-2.png)

And hit Install Add-on. It should now appear in the list of Add-ons. 
Now we need to edit its preferences. Expand the Add-on and enter here the path to the divine.exe inside your LSLIB directory.

![blender-bg3plugin-prefs.png](/tutorials/getting_started_visual/blender-bg3plugin-prefs.png)

If you wish you can tick "Convert to GR2 by Default" (otherwise it will always default to .dae export).

#### [LaughingLeader's Blender Helpers](https://github.com/LaughingLeader/laughingleader_blender_helpers)

> - Necessary plugin for settings involved with export (i.e. Export Order of meshes, LOD Level/Distance, and some options for mesh type)
> - Github page says for Blender 2.79 but it can be used with current versions
{.is-info}


Download and install the same way we did the BG3/DOS2 Collada Exporter.
There aren't any specific add-on preferences to set here, and once installed you should see this in the Outliner under Object properties (yellow square):

![blenderhelpers-outliner.png](/tutorials/getting_started_visual/blenderhelpers-outliner.png)

Some notes about common settings:
- **Export Order**: for exports with multiple meshes, the order of them needs to be set starting with 1. This order will be replicated in your VisualBank and is important for having the correct materials on the correct meshes.
- **LOD Level**: LODs are less resource intensive/lower quality version of the same mesh intended to be loaded in the further zoomed out the game camera is. Most modders choose to delete all LODs but 0 (the highest quality). For this it is important to set the LOD Distance to 0m.
- **LOD Distance**: The max distance the mesh loads with before the lower quality LOD loads in. I.e. 
  - LOD0 set to 6m: highest quality, working mesh. Will be loaded in until after 6m.
  - LOD1 set to 12m: next lower quality, will load in after 6m. If there is a LOD3 it will load in after 12m.

### Other Useful Plugins

- [Padme4000's Blender Add-ons](https://www.nexusmods.com/baldursgate3/mods/346)
	- Includes add-ons for setting head export order, creating LODs, transferring normalmaps, and easy setting of transforms.
- [BG3 Armature Tools](https://www.nexusmods.com/baldursgate3/mods/464)
	- Tools for creating custom head skeletons for modded heads - tutorial for making these found [here](/Tutorials/Visual/mrboneswildguide)
- [Outfit Builder](https://www.nexusmods.com/baldursgate3/mods/3683)
	- Refit armours via shapekeys (requires shapekeyed body meshes - tutorial for making these found LINK HERE)
- [Mesh Data Transfer](https://mmemoli.gumroad.com/l/tOKEh)
	- Tool for transferring mesh data from a source mesh to a target mesh.
- [Volno's Texture Toolbox](https://www.nexusmods.com/baldursgate3/mods/4310)
	- not a plugin per se but a shader set useful for rendering an approximation of textures in Blender.


## Tools: Text Editing / Mod Structure Stuff
#### oh no
> 
> This section is covered pretty well over on the [Setting up a Dev Environment](/Tutorials/General/setting-up-a-dev-environment) page.
{.is-info}


## Finding Assets

### References
- References regarding Head, Hair, Beard, Body, Horns, etc. found [here](/Information/Meshes)
	- Includes in-game names, file names, icons, and relevant UUIDs.

### Searching

- Using [BG3 Search Engine](https://bg3.norbyte.dev/search)

- Using Modder's Multitool


...WIP


## Next Steps

So now we have the basics set up to start some modding. If you're thinking "that's great, now what" then below you'll find links to pages detailing how to mod these things.

### Creating Hair Mods
...WIP

### Creating Head Mods
...WIP

### Creating Armor Mods
...WIP

### Creating Weapon Mods
...WIP

### Creating Accessories Mods
...WIP

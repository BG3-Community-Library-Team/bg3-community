---
title: Getting Started with 3D Modding
description: Covers the basics of setting up the needed tools
published: true
date: 2025-06-10T10:59:26.464Z
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
> - LSLIB / ConverterApp
> - Modder's Multitool
> - Blender and core related add-ons
> - VSCod(e/ium) and some useful extensions


## Tools: LSLiB

> [LSLIB](https://github.com/Norbyte/lslib/releases)
> use latest beta release
{.is-success}

> LSLiB is used for many things. Its front end application, ConverterApp.exe is used for unpacking game/mod paks, converting between various game file formats and editable ones, creating paks, creating virtual textures, and more. 
> 
> (TODO: create/link page here on how to use various LSLiB functions)
{.is-info}

### Initial setup
To download, head over to Releases and grab the latest ExportTool zip. For those unfamiliar with Github, the releases will look like this. Just grab the zip and (if you need it) the .NET dependency via the link.

*NOTE: the release in the screenshot below may be outdated - just go ahead and grab the most recent beta*
![lslib-release.png](/tutorials/getting_started_visual/lslib-release.png)

You can install/extract this where you want your modding utilities to be. 

For the purposes of this guide I have a directory for BG3 Utilities and have extracted it here:

![utilites-folder.png](/tutorials/getting_started_visual/utilites-folder.png)

Inside `ExportTool-vX.X\Packed` you will find ConverterApp.exe (colloquially, LSLiB), open it.
At the moment there isn't too much to set up, a few notes:

![lslib.png](/tutorials/getting_started_visual/lslib.png)

- Game: is set to Baldur's Gate 3
- For most mesh purposes you will want to have X-flip meshes turned OFF (default is on)


## Tools: Modder's Multitool

> [Modder's Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases)
> use latest release
{.is-success}

> MMT is another way to unpak/pak game files and mods. Additionally it is used for indexing these game files for searching and extracting.
{.is-info}

### Initial Setup
Same as with LSLiB, download from releases.

Instructions for installation and configuration can also be found on the Github page [here](https://github.com/ShinyHobo/BG3-Modders-Multitool/wiki/Installation).

Remember to set up your directories in Configuration:
![mmt-config.png](/tutorials/getting_started_visual/mmt-config.png)

For most cases you DO NOT need to mass unpack any game files. What you will want to do is index them so that you can use the "Search Index" option later.

![mmt.png](/tutorials/getting_started_visual/mmt.png)

### Further Setup
If you want to use the index search for finding/extracting meshes (GR2 files), there is one more step required as MMT itself does not contain a necessary file to deal with GR2. The granny.

![logo_granny.png](/tutorials/getting_started_visual/logo_granny.png)

Head over to where you installed LSLiB and copy the granny.dll file from here:
![granny-lslib2.png](/tutorials/getting_started_visual/granny-lslib2.png)

and paste it in your MMT directory here:
![granny-lslib2.png](/tutorials/getting_started_visual/granny-mmt.png)

### Using the Index Search
A small guide on using the index search here. (link coming soon)

## Tools: Blender

> [Blender](https://www.blender.org/)
> as of this writing most plugins will function with v4+ and can be used safely. Using at least v3.6+ is recommended.
>
>Note: you may have multiple versions installed on your PC
{.is-success}

> Blender is a free 3D modeling/animation software. Using plugins made for BG3 we can import/export the game's GR2 files and edit them.
{.is-info}

Once we have Blender installed, it's time to get some core plugins.

> Some people have had some issues directly installing these plugins with Blender versions 4+.
> It is possible to have multiple versions of Blender installed! So, grab 3.6, install the plugins there, and when you update to a newer version it should take your plugins and settings with it.
{.is-warning}

> Also, while Blender does have an in-app function to directly import add-ons from zip files, this does not always work with older plugins and can cause it to nest one folder too deep in the install location. 
{.is-warning}



### Important BG3 Plugins

#### [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter)

> - This is a necessary plugin to import/export the games extracted GR2 files
> - Requires LSLIB and setting a path to it in its settings
{.is-info}



First, download zip from Github, located here:

![bg3plugin-gh.png](/tutorials/getting_started_visual/bg3plugin-gh.png)

Unfortunately this cannot be directly installed from Blender due to having an extra folder. So what we need to do is extract the zip, look inside for a folder called "**io_scene_dos2de**", grab it and drop it into 

`..\AppData\Roaming\Blender Foundation\Blender\4.1\scripts\addons`
(4.1 or whatever version of Blender you are using)

If you do not yet have a scripts\addons directory you may create it.

If you look inside this folder it should look like this (minus the `_pycache_` as this gets autogenerated later):

![plugin-gr2-location.png](/tutorials/getting_started_visual/plugin-gr2-location.png)


Now we need to edit its configuration in Blender. To to Edit -> Preferences -> Add-ons. Use the search box for bg3 and it should be here. Expand it with the little arrow and enter here the path to the divine.exe inside your LSLIB directory.

![blender-bg3plugin-prefs.png](/tutorials/getting_started_visual/blender-bg3plugin-prefs.png)

If you wish you can tick "Convert to GR2 by Default" (otherwise it will always default to .dae export).

#### [LaughingLeader's Blender Helpers](https://github.com/LaughingLeader/laughingleader_blender_helpers)

> - Necessary plugin for settings involved with export (i.e. Export Order of meshes, LOD Level/Distance, and some options for mesh type)
> - Github page says for Blender 2.79 but it can be used with current versions
{.is-info}


Download and install the same way we did the BG3/DOS2 Collada Exporter.
However, in this case there aren't any specific add-on preferences to set here, and once installed you should see this at the bottom right under Object properties (yellow square):

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


## Tools: Getting it into the Game
#### oh no
> 
> For "classic" modding, this section is covered pretty well over on the [Setting up a Dev Environment](/Tutorials/General/setting-up-a-dev-environment) page.
>
>Additionally, consider using the official Modding Toolkit - documentation for it may be found [on Larian's BG3 Modding site](https://docs.baldursgate3.game/index.php?title=Main_Page) and [on Mod.io](https://mod.io/g/baldursgate3/r) 
{.is-info}


## Finding Assets

### References
- References regarding Head, Hair, Beard, Body, Horns, etc. found [here](/Information/Meshes)
	- Includes in-game names, file names, icons, and relevant UUIDs.

### Searching

- Using [BG3 Search Engine](https://bg3.norbyte.dev/search)

- Using Modder's Multitool

- Using the official BG3 Modding Toolkit asset browser


## Next Steps

So now we have the basics set up to start some modding. If you're thinking "that's great, now what" then below you'll find links to pages detailing how to mod these things.

### Creating Hair Mods
[Preparing-To-Mod](/Tutorials/Visual/Creating-A-Hair-Mod/Preparing-To-Mod)
[Creating-Hair-Mesh-Blender](/Tutorials/Visual/Creating-A-Hair-Mod/Creating-Hair-Mesh-Blender)
[exporting-conforming](/Tutorials/Visual/Creating-A-Hair-Mod/exporting-conforming)
[File-Setup](/Tutorials/Visual/Creating-A-Hair-Mod/File-Setup)

### Creating Head Mods
...WIP

### Creating Armor Mods
...WIP

### Creating Weapon Mods
...WIP

### Creating Accessories Mods
...WIP

---
title: Dev Environment Set-up
description: Guide to getting started creating mods
published: true
date: 2024-04-27T21:17:42.007Z
tags: 
editor: markdown
dateCreated: 2024-04-27T19:03:07.632Z
---

<div class="row">
  <div class="col col-offset-1 col-10">

# Setting up a Development Environment
Just getting started? This guide will help you figure out how to make sure you have the right set-up to beign creating a mod.

  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">
    
## Folder Structure
> The Community Library Team has prepared a base template that may be helpful as a starting point, which can be found [on GitHub](https://github.com/BG3-Community-Library-Team/Sample-Template).
When creating mods, you want to be sure you have the right project setup. This will ease the process a bit, as well as keep things organized. A common convention is to use a folder structure like this:
```
Mods/ProjectName/
						 Readme.md/txt
             Source/
                     Localization/
                                  LANGUAGENAME/
                                               modname-english.xml
                     Mods/
                          MODNAME/
                                  meta.lsx
                     Public/
                            MODNAME/
             Assets/
             Releases/
```

The `Assets` and `Releases` folders exist to store artifacts relating to publishing your mods - zipped up .pak files, images for your nexus page, etc. 

`Source` is there the meat of your mod will be, and consists of three folders: `Localization`, `Mods`, and `Public`. 
- `Localization` requires a subfolder for the language you're localizing in, and a `.xml` file of any name.
- `Mods` contains a folder with the name of your mod, within which you'll need a `meta.lsx` file, which defines the metadata, including the UUID, Name, and expected folder of your mod.
- `Public` contains a folder with the name of your mod, within which you'll place the data files you work with, matching Larian's folder structure. 

  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">
 
### Script Extender Folder Structure
> The Community Library Team has prepared a base Script Extender template that may be helpful as a starting point, which can be found [on GitHub](https://github.com/BG3-Community-Library-Team/SETemplate).
If you intend on working with Script Extender(SE), you'll need a little bit more as well. Within your `Source/Mods/MODNAME` folder, you'll want the following file structure:
```
Source/Mods/MODNAME/
                    meta.lsx
                    ScriptExtender/
                                   Config.json
                                   Lua/
                                       BootstrapServer.lua
                                       BootstrapClient.lua
```

The `Config.json` file defines a few aspects of your mod for Script Extender, including which SE modules you want to use and what the minimum required version of SE should be.

The `Lua` folder contains two files - you technically only need one of these, but this guide lists both as they're both potentially important.
- `BootstrapServer.lua` is for code that should run on the server.
- `BootstrapClient.lua` is for code that should run on the client.

More information can be found in the [official SE Documentation](https://github.com/Norbyte/bg3se/blob/main/Docs/API.md#getting-started).


  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">
    
## Useful Tools
Listed below are tools that will help you in creating mods.

  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">
    
### [LSLib](https://github.com/Norbyte/lslib/releases) v. 1.19.5 or higher
This is an important tool to have when modding Baldur's Gate 3. It performs various functions related to modding. One of its most important features is converting localization .xml files to .loca.


  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">
    
### [BG3 Mod Manager](https://github.com/LaughingLeader/BG3ModManager)
This simplifies the mod installation process. You can drag the .zip file of a mod into this program, and it will install it automatically for you. All you have to do is drag it from the inactive load order to the active load order, click Save, and click Export. You can also adjust the load order of your mods, which prevents conflicts and ensures functionality between mods that depend on other mods to function.


  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">
    
### [Git](https://git-scm.com/downloads/)
> See [A Modder's Guide to Git](/Tutorials/Tools/modders-guide-to-git) if you're new to the idea of Git or Version Control, or just want a refresher.

Git is a useful way to keep track of different versions of your code. It allows you to easily store and backup your project at various states. If you don't have Git, we highly recommend it as a way to handle versioning and manage your code. It's a lifesaver.


  </div>
</div>
<div class="row">
  <div class="col col-offset-1 col-10">

### [Visual Studio Code](https://code.visualstudio.com/)
Visual Studio Code(VSCode) or [VSCodium](https://vscodium.com/) is the preferred file editor for creating BG3 Mods:
- The [BG3 Mod Helper](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper) add-on, though still a work in progress, is extremely useful. In the future it will support a variety of LSLib tasks, including packaging mods. It is also capable of identifying and generating UUIDs, assisting in navigation, updating localization files, and creating templates for several BG3 LSX files.
- The [BG3 Text Support](https://marketplace.visualstudio.com/items?itemName=chromosome16.bg3-text-support) add-on automatically applies colorization for Data items (often stored in .txt files). This makes it easier to spot faulty data entries and just generally makes coding easier on the eyes. It includes syntax highlighting, auto-formatting, and customization capabilities.
- VSCode has a Project Folder Sidebar. You can designate which folder is your Project folder, and it will display a tree view of all folders and files within the Project folder. This makes it easier to get to or create the file you need. By selecting your main modding folder, you can view any unpaked data files from the game in the Multitool's folder.
- VSCode autofills commands across files. For example, if you've added a status entry in `CL_Status_BOOST.txt`, you can start typing it and select the full name from a list. It can also search every file in a project at once. This is especially useful if you need to find and replace every instance of a UUID.
- VSCode can display multiple files at once in the same window. Notepad++ can display up to 2 files side-by-side. I'm not really sure if Atom has a limit, but it can display at least 8 files at once. I find a three file layout works best for me.
- VSCode has Github integration built in, letting you to fetch, change branches, and more, all from within the editor. This can be especially useful if you're not a fan of using git via the command line.

![VSCode in action](https://i.imgur.com/Wi9zXr0.png)

---
    
[TODO: Add more tools]
  
</div>
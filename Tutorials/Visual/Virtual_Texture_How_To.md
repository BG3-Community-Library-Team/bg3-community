---
title: Virtual Texture How-To
description: 
published: false
date: 2024-05-12T02:06:01.802Z
tags: 
editor: markdown
dateCreated: 2024-05-12T02:05:40.666Z
---

# Header
Creating and utilizing a gtp/gts file requires 4 things, textures to convert, a configuration for conversion and a VirtualTextures.json file for mapping and loading them in game and a version of LSLIB higher than 1.19.0

LSLIB can be found [here](https://github.com/Norbyte/lslib)

Textures can be located anywhere and the path is defined in the conversion config

Lslib steps:
![lslibvt.png](/lslibvt.png)
1. Open LSLIB and go to the 'Virtual Textures' tab and the 'Build Tile Set' subsection
2. Point LSLIB to your creation config file and mod root path - 
(EX C:\..\Modname\Configs\Config.xml) for the config and (EX C:\..\Modname\) for the root
![examplexml.png](/examplexml.png)
3. 

> VirtualTextures.json is located in '\Modname_Here\Mods\Modname_Here\ScriptExtender\'
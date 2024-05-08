---
title: VSCod(e/ium) Extension
description: an extension for VSCode and VSCodium by @khbsd and @ghostboats that has lots of helpful features for modders.
published: true
date: 2024-05-08T09:52:43.740Z
tags: vscode, vscodium, bg3-mod-helper, tool, tools, ghostboats, khbsd
editor: markdown
dateCreated: 2024-04-25T01:43:35.054Z
---

# BG3 Mod Helper - A VSCod(e/ium) Extension
<br>

### File Locations
- [Github (source code)](https://github.com/ghostboats/bg3_mod_helper)
- [Vscode marketplace](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper)

Create by ghostboats and khbsd, this vscode extension is designed to help mod authors speed up their mod creation workflows. The extension has multiple useful utilities that include but are not limited to:
- Mod Packing
- UUID/Handle generation
- UUID Mapping
- LSX/XML/LOCA/ETC File Conversions
- Generate mod templates
- And then some

While the extension is still recieving regular updates, it's at a stable point where it can be very useful to mod authors and save them alot of time. It is built off the philosopy of being able to mod without having to tab out as often while requiring as little clicks as possible to get the job done. It has saved us alot of time and I hope it can do the same for you! The goal of this section of the the wiki is two fold: Provide documentation for users of the extension and provide documentation for developers who may wish to contribute or fork their own version.

# Requirements
- [Visual Studio Code](https://code.visualstudio.com/)
- [LSLib](https://github.com/Norbyte/lslib/releases)
- Python (for working with icon's/dss's/png's)

> Previous versions of the extension required direct use of divine.exe. This has since been replaced and you will need [LSLib](https://github.com/Norbyte/lslib/releases) and make sure the old path that pointed to divine.exe now points the directory containing your lslib
<!-- {blockquote:.is-info} -->

This guide is broken down into two section like I mentioned above. Users of the extension only need to continue ahead. If you wish to work with the extension directly to make your own personal edits or just understand what is going on under the hood, please jump here (adding link later).

# Mod Authors Guide

## Download/Installation
##### Download via VS Code
1) Open VS Code
2) Click on the "View" tab on the top ribbon
3) Click on "Extensions"
4) In the "Search Extensions in Marketplace" search box that has just opened, enter bg3
5) Click "Install" on the correct extension (bg3_mod_helper)
![installextension-ezgif.com-optimize.gif](/tutorials/bg3-mod-helper/installextension-ezgif.com-optimize.gif)

## Features and Usage
1) **UUID/Handle Creation and Display**
-- Right click on an open editor to generate a UUID or handle at that location
-- If a UUID/handle is highlighted when generating a UUID/handle, it will replace the entry with whatever was generated.
-- Generate a UUID/Handle using the keystrokes control+shift+U and control+shift+H respectively. 
-- When handles are generated, if a xml file exists, it will add the newly created handle in the xml as well![genhandle-ezgif.com-optimize.gif](/tutorials/bg3-mod-helper/genhandle-ezgif.com-optimize.gif)

2) **File Conversions (lsx<>lsf, xml<>loca)**
-- Open a custom webview tab where users can manage converting lsx,lsf,loca,xml,etc files
-- Quick convert options in data provider dropdown
-- Single file conversion via right click menu from file tree
-- Auto convert files on pack including exclusion list managed in extension settings

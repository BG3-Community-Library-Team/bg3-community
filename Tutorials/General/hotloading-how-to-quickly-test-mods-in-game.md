---
title: Hotloading - How to quickly test mods in game
description: Hotloading is a way to greatly speed up your modding workflow by reducing the number of times you have to open and close the game.
published: true
date: 2024-07-24T20:20:56.555Z
tags: guide, guides, hotloading, mod testing, mod workflow
editor: markdown
dateCreated: 2024-07-24T17:47:11.642Z
---

# Hotloading - How to quickly test mods in game
## What is hotloading in BG3 Modding?
Hotloading is a way to greatly speed up your modding workflow by reducing the number of times you have to open and close the game. It can be very tedious to restart the entire game to test every time you make a change to your mod. With hotloading, you can leave the game open and still see your changes reflected live in game.

## What can I use it for?
You can use hotloading for .GR2 aka mesh/model files and .DDS files. For example, if you are creating a custom head by editing one of the vanilla ones, you can hotload your custom head .GR2 into the game, open Character Creator, and then swap to your custom head each time you export a new version from Blender to see what your changes look like in game. Very handy! All you have to do is make sure you swap away from your hotloaded asset and back to load any new changes. For armor, you may have to un-equip and re-equip it to see the changes. 

In addition you can also hotload scripts created with Script Extender and load stats like Spells or Boosts by using a simple Script Extender script.

## How do I Hotload?
To hotload, you need to create a mirror of your mod’s files inside Baldur’s Gate 3’s Data files.

For example, say one of your mods has a head .GR2 located here:

`>SampleMod\Generated\Public\SampleMod\Assets\HUM_F_NKD_Head_LI.GR2
`
You can then hotload it by creating this filepath in your BG3 Data directory:

`C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Generated\Public\SampleMod\Assets\HUM_F_NKD_Head_LI.GR2`

Then open the game with your .pak loaded and you should see the new head. If you replace the .GR2 inside the Data directory, swapping to another head and back should reflect the new changes without having to restart the game.

If you want to hotload your scripts, add them in the same manner.

For example, say one of your mods has the Script Extender folder located here:

`>SampleMod\Mods\SampleMod\ScriptExtender\Lua\Server\MyFirstSEScript.lua
`
You can then hotload it by creating this filepath in your BG3 Data directory:

`C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Mods\SampleMod\ScriptExtender\Lua\Server\MyFirstSEScript.lua`

Then open the game with your .pak loaded and your script should load. If you make changes to the script in the Data directory, then enter `reset` in the Script Extender console, your script will be loaded again without having to restart the game.

Alternatively you can use [symlinks](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-4-symlinking) to link your workspace to your Data folder.

## Credits
Thank you to EmeraldTechno and LazyIcarus



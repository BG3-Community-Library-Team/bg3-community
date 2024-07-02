---
title: BG3 Mod Types and how to install them
description: 
published: false
date: 2024-07-02T15:48:23.246Z
tags: guide, moduse, wip
editor: markdown
dateCreated: 2024-07-02T06:32:16.092Z
---

# How to use mods in Baldur's Gate 3

![soon_tm.webp](/test/alithea/soon_tm.webp)


Modding games is a wonderful way to enhance and individualize your game experience, it's also never entirely safe. Especially if the game is still regularly patched like Baldur's Gate 3. 
Mods modify game files, if those game files are altered by a patch or hotfix, it can cause the mod to not being able to work properly anymore. This may lead to being unable to load a savegame or cause gameplay issues. It is important to check if updates are needed each time Larian provides a patch or hotfix.
Please understand that modding comes with the possibility of something not working right. Which can cause frustration and wasted time and effort and it can potentially screw something up in your game.
This guide will hopefully help to prevent that.

## Minimize the risks with a few simple steps:
### Backup your savegames
before
- starting to mod an ongoing playthrough
- adding new or more complex mods
- updating your game

Go to your story folder, highlight everything and copy it to a separate location. Default savegame folder path: 
```C:\Users\USERNAME\AppData\Local\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public\Savegames\Story```

### Read mod descriptions
Mod authors usually provide crucial information about their creations in the description. Please read it and pay extra attention to 
- install instructions
- requirements
- load order
- compatibility between mods

It also doesn't hurt to read sticky posts in the comments and to have a quick glance at the most recent entries.

### Disable auto-updating your game
- Steam: go to Library - Baldur’s Gate 3 - right click Properties - Updates - select *Only update this game when i launch it*
- GOG: go to Settings - Game features - uncheck *Auto-update games*

Alternatively the game can be started directly from the bg3.exe or bg3_dx11.exe found in the games bin folder.
Default bin folder path:
```C:\Program files\Steam\steamapps\common\Baldur's Gate 3\bin```

## Mod types and how to install them

### Tab {.tabset}
#### PAK
Pak files are conveniently packaged data bundles. They make installing and uninstalling Mods easier, quicker and safer. Paks can include a variety of modifications to game elements such as textures, sounds, objects, and others.

Installation:

1. Install the mod manager of your choice. We recommend Laughing Leader's Baldur's Gate 3 Mod Manager. [Follow this guide on how to install and set up BG3MM.](https://wiki.bg3.community/en/Tutorials/Mod-Use/Installation-Of-BG3MM)
2. Go to the mod page, read it, and download the desired version of the mod you want to a location outside of program or game files.
3. Open the archive and drag or copy the pak into your Mods Folder
Default Mod folder path:
```C:\Users\USERNAME\AppData\Local\Larian Studios\Baldur's Gate 3\Mods```
4. Start BG3MM or if it is already running, click refresh to see the new mod. It most likely will appear in Inactive Mods to the right.
5. Drag the mod from Inactive Mods to Active Mods. Keep load order requirements in mind while doing so. [General Load Order Guide](/Tutorials/Mod-Use/general-load-order)
> Some mods are *overrides*. They will appear in a separate section called Overrides at the bottom of the Active Mods panel.
*DiceSet_06* and *Honor* in the Inactive Mods panel to the right are game files.
Leave them all where they are and don't move them into the Active Mods panel.
{.is-warning}
6. 

#### MOD FIXER
Mod fixer is still neccessary. If it isn't installed, character creation will not be available. Instead this lovely view will appear on screen:

![durgeharem.webp](/mod-use/install-mods/durgeharem.webp)

Installation:
1. [download mod fixer](https://www.nexusmods.com/baldursgate3/mods/141)
2. move ModFixer.pak into the mod folder

That's it.

[Norbyte, the creator of Mod fixer explains how it works in his post on Larian Studio's discord](https://discord.com/channels/98922182746329088/767804218819477515/784392518883868674)

#### LOOSE FILES
Default Data folder path:
```C:\Program files\Steam\steamapps\common\Baldur's Gate 3\Data```
#### NATIVE MODS
Default bin folder path:
```C:\Program files\Steam\steamapps\common\Baldur's Gate 3\bin```

## Modding and Achievements
Modding Baldur's Gate 3 disables all achievements. They can be re-enabled using Script Extender or the native mod Achievement Enabler.

Happy modding!

![cmty_pride_logo.webp](/test/alithea/cmty_pride_logo.webp)
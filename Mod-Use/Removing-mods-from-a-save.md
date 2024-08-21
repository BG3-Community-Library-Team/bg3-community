---
title: Removing mods from a save
description: This guide focuses on removing individual mods from a save while being able to resume gameplay after the mods are removed.
published: true
date: 2024-08-21T18:19:57.938Z
tags: mods, mod uninstall, modsuse, mod uninstaller, uninstall, remove
editor: markdown
dateCreated: 2024-08-21T18:05:24.644Z
---

# Uninstalling mods from saves/campaigns

You may wish to uninstall mods from your game while also keeping your save files. This guide will help you do that.

## Before using this guide

* This guide is written assuming you are using [BG3MM](https://github.com/LaughingLeader/BG3ModManager) and Windows;
* This guide focuses on removing individual mods from your game while being able to resume gameplay after the mods are removed; [if you want a clean slate, follow this guide](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods);

* * *

## Cleaning mod data from your save files

Cleaning mod data from your save files is optional and only required if you want to continue using your save file. This step helps ensure that residual data from uninstalled mods does not cause issues when trying to load your save. Simply disabling a mod and loading a save can lead to issues, as the game attempts to access data that no longer exists, likely causing the game to return to the main menu.

### Broad categories of mod content that can cause issues

Uninstalling a mod mid-playthrough in BG3 can be challenging because mods often distribute items across various parts of the game, such as containers or trader inventories. The following are some broad categories of mod content that can cause issues:

* **Items**: These are especially problematic if the player has moved on from the area where the items were placed or just can't remember/find where these items are. Deleting such items manually is a laborious process and requires a lot of trial and error to check if all items were indeed removed.
* **Statuses:** Mods can add new statuses or modify existing ones. Removing such mods can cause issues with entities such as characters or containers that have these statuses, in a similar fashion to items, although mods using them are less common, and most statuses vanish after a long rest;
* **Classes/leveling:** Mods can add new classes or modify existing ones. Removing such mods can cause issues with characters that have these classes or have leveled up with these classes. It is easier to respec the characters to something vanilla. Note that this group also includes subclasses, spells, feats, and other character progression-related features; your best bet is to respec to vanilla content and stay on level 1 until you are sure that all modded content is removed.

### Using Mod Uninstaller

_Mod Uninstaller_ is a mod that offers an automated way to remove mod items and stats (statuses, passives). This tool allows you to remove mods via the Mod Configuration Menu (MCM) interface or the Script Extender (SE) console, making it easier to cleanly uninstall mods that add items. And best of all, mod authors do not need to integrate their mods with Mod Uninstaller.

Here is how you can use it:

* Download [Mod Uninstaller](https://www.nexusmods.com/baldursgate3/mods/9701) from the Nexus Mods page and install it and its requirements as usual;
* Open the MCM window in-game;
* Click the Mod Uninstaller tab and wait for mod data to be analyzed;
* Select the mod you want to uninstall, and click uninstall.
* Save your game and exit.

This process will remove all items and statuses associated with the mod, **greatly increasing the chances of a successful uninstallation.**

You may now remove the mod(s) from your load order. You should be able to load that last save (despite the warning about missing mods) and continue playing without issues.

You can also uninstall mods with the `!MU_Uninstall_Mod <modUUID>` command via the SE console.

* * *

If a mod is not listed, it probably simply overrides vanilla content, and you might be able to safely remove it without even using Mod Uninstaller.

**Note that this tool is not perfect and may not be able to remove all items or statuses associated with a mod.**
For example, you may encounter issues with complex or weirdly structured mods, or mods that apply stats without using SE. In any case, feel free to report issues on the mod page.

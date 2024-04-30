---
title: Shipping Items to Users
description: This tutorial will teach you how to how to ship both vanilla, and modded items using the four main methods of item distribution.
published: false
date: 2024-04-30T09:45:16.583Z
tags: tutorial, guide, tutorial chest, item shipment framework, treasuretables, treasure tables, isf, vendor, shop, items, console command, templateaddto, add items, ship items, merchant inventories, vendor inventories, shop inventories, merchant
editor: markdown
dateCreated: 2024-04-30T09:43:22.722Z
---

# Shipping Items to Users
After you have spent the time to create a shiny new item, or even if you'd like to use a specific item from the vanilla game, you've probably wondered how to actually ship that item to your users. This guide will showcase four ways to do so, two of which utilizing systems that are available in the base-game, and two which utilize the Script Extender.

However you end up shipping items to your users, it is recommended to create a custom container to house all of those items. Not only will it make it more efficient for updating your mod down the line, but it also makes it more convenient for users, and their inventories to stay organized. You can find a guide for how to create custom items here[TODO: port container template guide to the wiki], as well as custom container templates here: [Aether's Container Templates](https://www.nexusmods.com/baldursgate3/mods/8418)

## Item Shipment Framework
The [Item Shipment Framework](https://www.nexusmods.com/baldursgate3/mods/8295) (ISF for short) is a script extender based mod, which allows mod authors to **directly ship vanilla or modded items into the camp chest or host's inventory**. It aims to provide a superior alternative to the Tutorial Chest and Vendor Inventory item shipment approaches.

It also includes an integrated Tutorial Chest located in the camp chest, which can be manually refreshed via a command scroll included with the framework. As well as another command scroll, which allows users to refresh the ISF Mailbox to duplicate the items shipped to them via the framework.

**The ISF doesn't force mods into a mandatory dependency with the Script Extender**. The configuration file will be picked up in case users have ISF installed, but will simply remain inert otherwise. **Therefore, if your mod is designed to function without the Script Extender, integrating with the ISF will not change this**.

### Quick Start
To get your mod up and running with ISF, you can drag and drop its main folder inside our bespoke web tool that will parse the contents of the mod folder and generate an ISF configuration JSON file based on your mod's contents:

1. **Drag and drop your mod folder onto the [ISF Config Generator website](https://bg3-isf-config-generator.vercel.app/)**. Alternatively, you can copy and paste it.
2. **Click "Save ISF JSON"** to download the generated file.
3. **Place the JSON file alongside your mod's `meta.lsx` file**.

**That's it!** With this tool, you can easily generate the necessary ISF configuration for your Baldur's Gate 3 mod. Now, **please, review the generated JSON file** and **make sure it's correct and fits your mod's needs**.

For further customization of the generated JSON file, you may consult the [ISF Wiki's Config Settings](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/ISF-Config-Settings) page, as it will teach you what each setting does, and how they could be used for your mod.

> **Default settings**: the default settings, also used by this generated JSON, will:
> - Send a single copy of each item to all four possible mailboxes, and none directly to the host's inventory.
> - Verify if an item exists in the player's party inventories, mailboxes, and perform an internal ISF check using ModVars.

### ISF Example Mods
These mods were created with the purpose of showcasing multiple different use-cases for how the ISF might be utilized in mods. These links will redirect you to the Item Shipment Framework wiki, where each example mod's config settings get explained in detail.
* [Camp Clothes in the Camp Chest](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/Example-Mods#camp-clothes-in-the-camp-chest) - Single Container and UUID, the simplest possible ISF integration.
* [Debug Book in the Host's Inventory](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/Example-Mods#debug-book-in-the-hosts-inventory) - This mod spawns the Debug Book into the host's inventory as early as spawning in on the Nautiloid during the tutorial.
* [Infinite Supply Packs](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/Example-Mods#infinite-supply-packs) - This mod spawns a Heavy Supply Pack in the host's inventory when the player chooses to end the day and ISF detects that the player does not have any.

## Tutorial Chest
Will be expanded upon.

## Vendor Inventories
Will be expanded upon.

## Script Extender Console Command
Will be expanded upon.

Place the UUID/MapKey for the item between the quotes, and change the `1` to the amount of the item you would like recieve.

`TemplateAddTo("", GetHostCharacter(), 1)`
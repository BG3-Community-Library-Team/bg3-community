---
title: Shipping Items to Users
description: This tutorial will teach you how to how to ship both vanilla, and modded items using the four main methods of item distribution.
published: false
date: 2024-05-02T12:02:59.192Z
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

> **Default Settings:** The default settings, also used by this generated JSON, will:
> * Send a single copy of each item to all four possible mailboxes, and none directly to the host's inventory.
> * Verify if an item exists in the player's party inventories, mailboxes, and perform an internal ISF check using ModVars.
<!-- {blockquote:.is-info} -->

### ISF Example Mods
These mods were created with the purpose of showcasing multiple different use-cases for how the ISF might be utilized in mods. These links will redirect you to the Item Shipment Framework wiki, where each example mod's config settings get explained in detail.
* [Camp Clothes in the Camp Chest](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/Example-Mods#camp-clothes-in-the-camp-chest) - Single Container and UUID, the simplest possible ISF integration.
* [Debug Book in the Host's Inventory](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/Example-Mods#debug-book-in-the-hosts-inventory) - This mod spawns the Debug Book into the host's inventory as early as spawning in on the Nautiloid during the tutorial.
* [Infinite Supply Packs](https://github.com/AtilioA/BG3-item-shipment-framework/wiki/Example-Mods#infinite-supply-packs) - This mod spawns a Heavy Supply Pack in the host's inventory when the player chooses to end the day and ISF detects that the player does not have any.

## Tutorial Chest
The "Tutorial Chest" is a Cartilaginous Chest located on the Nautiloid, in the tutorial of the game. It can be found in the room containing the "Eldritch Rune", just past Shadowheart's Mind Flayer Pod.

This guide will show you how to create a Treasure Table, and place items into the Tutorial Chest.
<details>
  <summary>Why you should use the Tutorial Chest</summary>
The Tutorial Chest offers a quick and easy way to ship items to your users, is a method that only takes a few minutes to set up, and is widely recognized as the standard way to ship items to users.

- Users will have almost immediate access to your items during the Tutorial.
- It functions for users who do not have access to the Script Extender, such as people who play on Mac.
</details>
<details>
  <summary>Why you shouldn't use the Tutorial Chest</summary>
The modding community has been placing items into this tutorial chest as a crutch to easily distribute items to users since the game was in beta, due to there not being an easier alternative to give items directly to users at the time. This has led many custom item mods to use the Tutorial Chest for item shipment, and has caused issues such as:

- If too many mods that use the chest are installed, it will take multiple seconds to open it, and cause lag due to engine limitations.
- The chest is only located in the tutorial, leading to users being unable to acquire items from the chest after they've made it to Act 1. 
- It is a requirement to use a tutorial chest summoning mod if you wish to get an item from it after the tutorial.
- If too many mods that use the Tutorial Chest are installed, the chest will become cluttered and hard to sort through.
- There is no granularity or customization in the way you can utilize the Tutorial Chest, such as choosing when an item will spawn, or if there will be a cost to acquire the item.
- If a user wishes to have multiple of an item found in the chest, authors must include multiple of the same item. Else users will have to use a tutorial chest summoning mod to duplicate the chest.
</details>

### Getting Started

Create a directory in your mod's main project folder which looks like this:

`ProjectFolder\Public\ProjectTitle\Stats\Generated\TreasureTable.txt`

Replace `ProjectFolder`, and `ProjectTitle` with the names of your mod's main folder directory, and the folder name you have assigned in your mod's meta.lsx file.

For example, [Aether's Black Dye](https://www.nexusmods.com/baldursgate3/mods/1177)'s directory looks like this:

`AethersBlackDye\Public\AethersBlackDye\Stats\Generated\TreasureTable.txt`

Next, place the code block below into the TreasureTable.txt file, and replace `I_GameObject_Stats_Name` with the "Stats" name you chose for your custom item, inside of your mod's root template, verifying that the "I_" prefix is also included.

If you would like to increase the amout of an item you send, change the first number in the `new subtable` section to the amount you wish to ship.

```txt
new treasuretable "TUT_Chest_Potions"
CanMerge 1
new subtable "1,1"
object category "I_GameObject_Stats_Name",1,0,0,0,0,0,0,0
```

  <img src="https://images2.imgbox.com/0f/a6/XOms11nH_o.png" />

In the example treasure table below, one modded Black Dye, and ten vanilla Supply Packs will be shipped to the Tutorial Chest.
```txt
new treasuretable "TUT_Chest_Potions"
CanMerge 1
new subtable "1,1"
object category "I_Aethers_Black_Dye",1,0,0,0,0,0,0,0
new subtable "10,1"
object category "I_OBJ_Camp_Pack",1,0,0,0,0,0,0,0
```

## Vendor Inventories
CLUTTER CLUTTER CLUTTER

<details>
  <summary>Why you should use Vendor Inventories</summary>
Words
  
- You can set a specific price that users pay to acquire your item.
- The method is more lore, and roleplay friendly.
</details>
<details>
  <summary>Why you shouldn't use Vendor Inventories</summary>
While there are certainly pros to sending your items via Vendor Inventory lists, there are some downsides which can't be overlooked:

- Sending items to your users via Trader Inventories will halt any chance of your mod being able to be uninstalled from the game once a playthrough has been started.
- Installing multiple mods which send items via vendor inventories will cause vanilla items to spawn less frequently during the long rest item rotation.
- This will lead to seeing the same modded items over and over again inside of different stores rather than new vanilla items.
</details>

## Script Extender Console Command
You can also spawn in items with the [Script Extender Console](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender#h-3-how-to-install-the-console).

`TemplateAddTo("", GetHostCharacter(), 1)`

Above is the console command to spawn an item into your own inventory, simply paste it into the SE Console, place the UUID/MapKey for the item you want between the quotes, and change the `1` to the amount of the item you would like recieve.
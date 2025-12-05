---
title: Updating Epilogue Outfits with Osiris
description: A guide to updating character epilogue outfits using Osiris.
published: false
date: 2025-12-05T03:01:05.581Z
tags: 
editor: markdown
dateCreated: 2025-12-04T22:07:24.777Z
---

# Updating Epilogue Outfits with Osiris

Hi! This page is a short guide on how to update character epilogue outfits with Osiris, Larian's Story Scripting language.

## Tools and Requirements

This tutorial assumes you already know a little bit about modding, like packaging mods for the game, but you won't need to know much about Osiris.

#### Tools needed:

- A program that can edit **.txt** files
	Some suggestions:
	- [Notepad++](https://notepad-plus-plus.org/)
  - [VS Code](https://code.visualstudio.com/)
  - [VSCodium](https://vscodium.com/)
  
- A way to find the name and UUIDs of characters, flags, and items in the game
	I'd recommend: [https://bg3.norbyte.dev/](https://bg3.norbyte.dev/)! (aka Norb Search)
  - The [Modders Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool) is also a viable option, though its search function runs more slowly than Norb Search
  - You can also use the official BG3 Toolkit
- Your preferred method of making and packing mods
	Suggestions:
  - [Modders Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool)
  - BG3 Toolkit

That's all!

## Working With Osiris

There are two methods of working with Osiris scripts! You can use Larian's official toolkit (which does have a very helpful debugger if you get stuck!), or you can write a script manually in a .txt file, and drop it into this file path in your mod:

`//Your external mod folder/Mods/Your mod folder/Story/RawFiles/Goals/Your script.txt`

If you're using the toolkit, you can drop that same .txt file into the same file path in your toolkit project! You may need to manually create the file path to do so, but when you do, you should be able to see your script in the toolkit's Story Editor. You can find a guide on using the Story Editor [here!](https://mod.io/g/baldursgate3/r/scripting-using-the-story-editor)

This tutorial will cover how to make an Osiris script using a .txt file. Whether you'd prefer to manually package your mod or use the toolkit afterwards is up to you!

# Writing Your Script

First, make a new .txt file. You can name it what you'd like, but I'd recommend including an abbreviation of your username in it, so that file will be unique to you. 
> Osiris scripts with the same name will conflict with each other, so to be safe, always put something unique to you in the name of your scripts!
{.is-info}

Copy the following into your file:

```
Version 1
SubGoalCombiner SGC_AND
INITSECTION


KBSECTION

EXITSECTION

ENDEXITSECTION
```

Osiris uses Databases (DBs), to store information needed in different functions. The DB used to store information about Epilogue outfits is `DB_EPI_Epilogue_PartyEquipment`, which looks like this!

```
DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Wyll_Duke_7f89e3b8-61ef-498b-bd1b-77f996c5ec42);
```

This is the DB for Wyll's clothing if he becomes the Grand Duke of Baldur's Gate in the ending of his quest.

To add that outfit to him in the epilogue, DB_EPI_Epilogue_PartyEquipment stores the following information:

The character the clothing should be added to, the flag it should check for to add the clothing, whether the flag is true or not (if it's checking for that flag being False, it'll have a 0 there instead!), and the item to equip to the character.

In that example, the item EPI_Camp_Wyll_Duke is added to Wyll if the flag GLO_Wyll_State_GrandDuke is True.

He also has a separate DB for his shoes:

```
DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Shoes_Wyll_Duke_4aa0dbb1-f51a-45bc-8a58-814ac5063035);
```

Each epilogue clothing DB will only add one item at a time, so you'll need separate DBs if you'd like to add other items.


## Clearing DBs

To update the epilogue clothing for a given character, you'll first need to clear the existing DB for their clothing.

You can do that by taking the DB you want to clear, putting it in the INITSECTION your file, and writing NOT in front of it. This will clear the DB when your script is loaded for the first time.

Do this for each piece of equipment you want to replace.

Your file should now look like this:

```
Version 1
SubGoalCombiner SGC_AND
INITSECTION

//Clear Wyll's Grand Duke Equipment DBs

NOT DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Wyll_Duke_7f89e3b8-61ef-498b-bd1b-77f996c5ec42);
NOT DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Shoes_Wyll_Duke_4aa0dbb1-f51a-45bc-8a58-814ac5063035);

KBSECTION

EXITSECTION

ENDEXITSECTION
```

In this example, I'm clearing both the DB for his outfit, and the DB for his shoes. I've also placed a comment above this section, so I'll be able to tell at a glance what that section of my script does. Putting // before a line in an Osiris script will comment it out, making it nonfunctional.

## Adding New Equipment

```
Version 1
SubGoalCombiner SGC_AND
INITSECTION

//Clear Wyll's Grand Duke Equipment DBs

NOT DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Wyll_Duke_7f89e3b8-61ef-498b-bd1b-77f996c5ec42);
NOT DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Shoes_Wyll_Duke_4aa0dbb1-f51a-45bc-8a58-814ac5063035);



//City of Brass and Pointed-Toe Shoes for Grand Duke Wyll

//City of Brass
DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)ARM_Camp_Patriars_A_Red_c65c5dd5-705c-4103-904c-0835d81bd846);

//Pointed-toe shoes
DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)ARM_Camp_Shoes_F_16a8aee6-568c-458e-b006-cb3344cac4fb);


KBSECTION

EXITSECTION

ENDEXITSECTION
```

I've now set up new DBs that will give the City of Brass and Pointed-Toe Shoes outfits to Grand Duke Wyll when the epilogue starts.

When making your own script, you'll want to substitute the names and UUIDs of the character, flag, and items you want instead.

**All items added will need to be in the camp clothes slots!**

Characters are placed into camp clothes automatically in the epilogue, so if you give them armour, you won't be able to see it.


**A note about flags:** You don't have to stick to just the existing flag being set here! When the existing DBs are cleared, you can set up outfits based on other flags. https://bg3.norbyte.dev/ is a good way to look for flags you want to check.


## Retroactively Updating Outfits

Setting up the DBs here will make sure the character will get the appropriate outfits when the epilogue *starts,* but not if the player is already in the epilogue.

To make sure the outfits you want are added to the character retroactively, you could add them through an Osiris procedure like this:

```
PROC
PROC_Your Username Abbreviation_EpilogueOutfits_RetroactiveApply()
AND
DB_LevelLoadedOnce("EPI_Main_A")
AND
DB_Your Username Abbreviation_EpilogueOutfits((CHARACTER)_Character, (FLAG)_Flag, _Bool, (ITEMROOT)_NewItem,_Slot)
AND
GetFlag(_Flag,_Character,_Bool)
AND
GetEquippedItem(_Character,_Slot,_OldItem)
THEN
Unequip(_Character,_OldItem);
Equip(_Character,_NewItem);
```

An Osiris procedure can be used to perform different actions when it's called, and will only run when it's called, so it won't be constantly checking its conditions.

I'll explain how to call this procedure in a little bit, but first, let's go over what it does.

This procedure is meant to do the following, in this order:

- Check whether the epilogue level has already been loaded once. If it has, it means the player has reached the epilogue, and will need the new outfits to be applied retroactively.
- It then checks a custom DB, which you'll be setting up in a moment. This DB checks for the following information: The character to give the equipment to, the flag to check, the bool value (0 or 1) that will check whether the flag is True or False, the new item to add, and the slot it should go in (like camp clothes, camp shoes, and underwear, etc).
- Using the flag(s) and character(s) you set up in each entry of your custom DB, GetFlag will check whether each flag on their linked character

## Other Epilogue Clothing DBs

There are also two DBs for Underwear, DB_EPI_Epilogue_PartyUnderwear and DB_EPI_Epilogue_FallbackPartyUnderwear.

```
DB_EPI_Epilogue_PartyUnderwear((CHARACTER)S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12,(ITEMROOT)Underwear_Laezel_185ab1be-e93d-4518-b053-d6d4d7168d68);

DB_EPI_Epilogue_FallbackPartyUnderwear((TAG)REALLY_TIEFLING_7bf7207f-7406-49c0-b501-eaaa2bb4efd7,(ITEMROOT)Underwear_Tieflings_A_498c155f-8675-4a55-9cb0-89dd7270469f);
```

DB_EPI_Epilogue_PartyUnderwear stores the following information:

The character to add the underwear to, and the roottemplate of the underwear item to add.


And the information stored in DB_EPI_Epilogue_FallbackPartyUnderwear is this:

The tag for the race to give underwear to, and the underwear item to give characters with that tag.

The clothing for player characters is stored in the DB_EPI_Epilogue_FallbackPartyEquipment DB, which looks like this:

```
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_PartyTav_1_edb02b0e-3d91-4a81-a37d-f151bad68c6d, 1);
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_Shoes_PartyTav_1_7dec9f3e-3a90-4588-a995-2986340866c6, 1);

DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_PartyTav_2_98cdd18d-2d8a-4aca-a46b-c4829833482f, 2);
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_Shoes_PartyTav_2_ff7d64c3-3969-44f6-98ee-0add1fb69fef, 2);

DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_PartyTav_3_782e430e-caef-42eb-abc4-6406544e9714, 3);
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_Shoes_PartyTav_3_773924ee-02cd-42e7-8480-0c42896f700e, 3);

DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_PartyTav_4_eedda7b5-c1f4-4633-8034-30e63f7ce581, 4);
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)EPI_Camp_Shoes_PartyTav_4_810351d6-75ff-4c95-8f65-fcbfb5d0c19d, 4);
```

The first bit of information here is the item to add to the player, and I believe the second number refers to different players in a multiplayer session, but I'd need to test this out.

To update all of this information, you should be able to use the exact same techniques as replacing other epilogue equipment.
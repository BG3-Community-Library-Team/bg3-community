---
title: Updating Epilogue Outfits with Osiris
description: A guide to updating character epilogue outfits using Osiris.
published: false
date: 2025-12-07T08:17:26.954Z
tags: 
editor: markdown
dateCreated: 2025-12-04T22:07:24.777Z
---

# Updating Epilogue Outfits with Osiris

(hi to anyone who stumbles on this tutorial, **this is not done yet!!!!** it turns out there's a lot more that's required to tie into the epilogue clothing system, and i actually believe it'd be best to tie into the epilogue setup using a script framework, rather than people having multiple scripts of their own. this page is going to be a bit of a mess for a minute until i can put together a proper guide and explanation of how it works. please bear with me!)

```
Version 1
SubGoalCombiner SGC_AND
INITSECTION

DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_TavDurge((ITEMROOT)ARM_Vanity_ElegantRobe_2f7aadd5-65ea-4ab6-8c55-88ee584c72df, "VanityBody");
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_TavDurge((ITEMROOT)ARM_Camp_Shoes_Sandals_A_Blue_2290f957-2e17-4ceb-870f-bd53f81f866c, "VanityBoots");

DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(ITEMROOT)ARM_Vanity_ElegantRobe_2f7aadd5-65ea-4ab6-8c55-88ee584c72df, "VanityBody");
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(ITEMROOT)ARM_Camp_Shoes_Sandals_A_Blue_2290f957-2e17-4ceb-870f-bd53f81f866c, "VanityBoots");

DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12,,(ITEMROOT)ARM_Vanity_ElegantRobe_2f7aadd5-65ea-4ab6-8c55-88ee584c72df, "VanityBody");
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12,,(ITEMROOT)ARM_Camp_Shoes_Sandals_A_Blue_2290f957-2e17-4ceb-870f-bd53f81f866c, "VanityBoots");

//put the vanilla outfits you'd like to replace here! Copy the entire DB_EPI_Epilogue_PartyEquipment you want to replace, 
DB_MGNTN_EPIOutfitReplacers_PartyEquipmentToReplace((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Wyll_Duke_7f89e3b8-61ef-498b-bd1b-77f996c5ec42);
DB_MGNTN_EPIOutfitReplacers_PartyEquipmentToReplace((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Shoes_Wyll_Duke_4aa0dbb1-f51a-45bc-8a58-814ac5063035);

DB_MGNTN_EPIOutfitReplacers_PartyEquipmentToReplace((CHARACTER)S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679,(FLAG)ORI_Shadowheart_State_RejectShar_KilledParents_e9060caf-66b0-4701-8dfd-5ae1125f5afd, 1,(ITEMROOT)EPI_Camp_Selune_79bb5a64-2019-4818-a898-de179b6bc44c);
DB_MGNTN_EPIOutfitReplacers_PartyEquipmentToReplace((CHARACTER)S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679,(FLAG)ORI_Shadowheart_State_RejectShar_SavedParents_486d69d4-a7c2-4cb5-8fcb-8f2cb738ada9, 1,(ITEMROOT)EPI_Camp_Selune_79bb5a64-2019-4818-a898-de179b6bc44c);

//NPC/Companion underwear to replace
DB_MGNTN_EPIOutfitReplacers_PartyUnderwearToReplace((CHARACTER)S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679,(ITEMROOT)Underwear_Shadowheart_b460bd0c-58fe-4a56-831c-af92fd4ba7e2);


//Tav clothing to replace
DB_MGNTN_EPIOutfitReplacers_FallbackPartyEquipmentToReplace((ITEMROOT)EPI_Camp_PartyTav_1_edb02b0e-3d91-4a81-a37d-f151bad68c6d, 1);
DB_MGNTN_EPIOutfitReplacers_FallbackPartyEquipmentToReplace((ITEMROOT)EPI_Camp_Shoes_PartyTav_1_7dec9f3e-3a90-4588-a995-2986340866c6, 1);

//Tav/fallback underwear to replace
DB_MGNTN_EPIOutfitReplacers_FallbackPartyUnderwearToReplace((TAG)REALLY_ELF_772b1dc6-14be-417f-afa3-c6cf364f45b4,(ITEMROOT)Underwear_Elves_A_0ec7d956-e65f-4bfa-b677-22f399f81a32);
DB_MGNTN_EPIOutfitReplacers_FallbackPartyUnderwearToReplace((TAG)REALLY_HUMAN_8e288154-e7ca-4277-b2df-e61639b1cce8,(ITEMROOT)Underwear_Humans_A_d40b567d-6b66-447e-8923-2bbd0d7aea00);




//set up the outfits you want to add to the character(s) here!
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)ARM_Camp_Patriars_A_Red_c65c5dd5-705c-4103-904c-0835d81bd846,"VanityBody");
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)ARM_Camp_Shoes_F_16a8aee6-568c-458e-b006-cb3344cac4fb,"VanityBoots");


DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679,(FLAG)ORI_Shadowheart_State_RejectShar_KilledParents_e9060caf-66b0-4701-8dfd-5ae1125f5afd, 1,(ITEMROOT)ARM_Camp_Body_Laezel_54de4a07-c57c-421e-912c-7e8bd93ca0c4,"VanityBody");
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679,(FLAG)ORI_Shadowheart_State_RejectShar_SavedParents_486d69d4-a7c2-4cb5-8fcb-8f2cb738ada9, 1,(ITEMROOT)ARM_Camp_Body_Laezel_54de4a07-c57c-421e-912c-7e8bd93ca0c4,"VanityBody");

//Tav equipment replacers
DB_MGNTN_EPIOutfitReplacers_ReplacementFallbackEquipment((ITEMROOT)ARM_Vanity_ElegantRobe_2f7aadd5-65ea-4ab6-8c55-88ee584c72df, 1,"VanityBody");
DB_MGNTN_EPIOutfitReplacers_ReplacementFallbackEquipment((ITEMROOT)ARM_Camp_Shoes_Sandals_A_Blue_2290f957-2e17-4ceb-870f-bd53f81f866c, 1,"VanityBoots");

//NPC/Companion underwear replacers

//if you don't want to test for flagged conditions for underwear, use the 'character default' DB! this will be overridden if a character has a flagged DB for their underwear, and they fulfilled the conditions for the flag in that DB.
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_CharacterDefault((CHARACTER)S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679,(ITEMROOT)Underwear_Laezel_185ab1be-e93d-4518-b053-d6d4d7168d68,"Underwear");

//flagged underwear DB. allows you to check for flag conditions for underwear. Helpful for setting up accessories in the underwear slot for different story conditions for each companion!
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255,(FLAG)(FLAG)ORI_Astarion_State_StayedVampireSpawn_2724b881-6be1-49a7-8375-a49e9acb4546, 1,(ITEMROOT)Underwear_Laezel_185ab1be-e93d-4518-b053-d6d4d7168d68,"Underwear");

//Tav/fallback underwear replacers
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Fallback((TAG)REALLY_ELF_772b1dc6-14be-417f-afa3-c6cf364f45b4,(ITEMROOT)Underwear_Incubus_5fa043bf-0445-49ad-9e82-0df77c639fe2,"Underwear");
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Fallback((TAG)REALLY_HUMAN_8e288154-e7ca-4277-b2df-e61639b1cce8,(ITEMROOT)Underwear_Incubus_5fa043bf-0445-49ad-9e82-0df77c639fe2,"Underwear");

//The previous DBs will help with adding the outfits when the player is already in the epilogue!
PROC_MGNTN_EpilogueOutfitReplacers_RetroactiveApply();

KBSECTION

//This is the script for the framework. You will not need to include this in your own mod, but I wanted to put it here to explain how it works!

//***epilogue setup start***

//REGION Clear DBs for equipment being replaced

//If a DB for epilogue equipment to replace matches an existing party equipment DB, clear that DB.


//companion/NPC equipment

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_EPI_Epilogue_PartyEquipment((CHARACTER)_Char,(FLAG)_Flag,_Bool,(ITEMROOT)_Item)
AND
DB_MGNTN_EPIOutfitReplacers_PartyEquipmentToReplace((CHARACTER)_Char,(FLAG)_Flag,_Bool,(ITEMROOT)_Item)
THEN
NOT DB_EPI_Epilogue_PartyEquipment((CHARACTER)_Char,(FLAG)_Flag,_Bool,(ITEMROOT)_Item);


//companion/NPC underwear

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_EPI_Epilogue_PartyUnderwear((CHARACTER)_Char,(ITEMROOT)_Item)
AND
DB_MGNTN_EPIOutfitReplacers_PartyUnderwearToReplace((CHARACTER)_Char,(ITEMROOT)_Item)
THEN
NOT DB_EPI_Epilogue_PartyUnderwear((CHARACTER)_Char,(ITEMROOT)_Item);


//fallback/player equipment

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)_Item,_Int)
AND
DB_MGNTN_EPIOutfitReplacers_FallbackPartyEquipmentToReplace((ITEMROOT)_Item,_Int)
THEN
NOT DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)_Item,_Int);

//fallback/player underwear

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_EPI_Epilogue_FallbackPartyUnderwear((TAG)_Tag,(ITEMROOT)_Item)
AND
DB_MGNTN_EPIOutfitReplacers_FallbackPartyUnderwearToReplace((TAG)_Tag,(ITEMROOT)_Item)
THEN
NOT DB_EPI_Epilogue_FallbackPartyUnderwear((TAG)_Tag,(ITEMROOT)_Item);


//END_REGION Clear DBs for equipment being replaced


//REGION avernus equipment replacers

//avernus clothing should take precedence!

//avernus equipment, tav/durge

//If a tav/durge avernus equipment DB exists for the Vanity Body/camp clothes slot, a non-origin player went to avernus, and they have the vanilla DB for the avernus clothes, clear the avernus camp clothing DB, and set the default player clothing instead.
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_TavDurge((ITEMROOT)_Item, "VanityBody")
AND
NOT DB_Origins(_Char)
AND
QRY_EPI_Epilogue_IsInAvernusWithKarlachorWyll(_Char)
AND
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Avernus_24149d5d-c509-48dc-b026-491c11e60a5c)
THEN
NOT DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Avernus_24149d5d-c509-48dc-b026-491c11e60a5c);
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, _Item);

//same as above, but for camp shoes replacers. (they're separated specifically so if someone only replaced one, they'll still have the other part of the avernus equipment.)
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_TavDurge((ITEMROOT)_Item, "VanityBoots")
AND
NOT DB_Origins(_Char)
AND
QRY_EPI_Epilogue_IsInAvernusWithKarlachorWyll(_Char)
AND
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Shoes_Avernus_c36967e4-26c5-4f2f-b25b-f351a6bac804)
THEN
NOT DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Shoes_Avernus_c36967e4-26c5-4f2f-b25b-f351a6bac804);
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, _Item);

//avernus equipment, companions

//if the character has an avernus equipment DB, went to avernus, and has the vanilla DB for the avernus clothes, clear the avernus camp clothing DB, and set the default player clothing instead.
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)_Char,(ITEMROOT)_Item, "VanityBody")
AND
QRY_EPI_Epilogue_IsInAvernusWithKarlachorWyll(_Char)
AND
DB_EPI_Epilogue_PartyEquipment((CHARACTER)_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Avernus_24149d5d-c509-48dc-b026-491c11e60a5c)
THEN
NOT DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Avernus_24149d5d-c509-48dc-b026-491c11e60a5c);
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, _Item);

//same as above, but for camp shoes replacers. (again, they're separated specifically so if someone only replaced one, they'll still get the other part of the avernus equipment.)
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)_Char,(ITEMROOT)_Item, "VanityBoots")
AND
QRY_EPI_Epilogue_IsInAvernusWithKarlachorWyll(_Char)
AND
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Shoes_Avernus_c36967e4-26c5-4f2f-b25b-f351a6bac804)
THEN
NOT DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Shoes_Avernus_c36967e4-26c5-4f2f-b25b-f351a6bac804);
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, _Item);


//END_REGION avernus equipment replacers



//REGION non-avernus equipment replacers


//companion/NPC equipment:

//If a character has an epilogue clothing replacer in the Vanity Body/camp clothes slot, has the vanilla DB for avernus clothes, and doesn't have an avernus equipment DB for the camp clothes slot, clear the avernus camp clothing DB. (this is to prevent clearing of avernus equipment that uses the vanilla items, but was set up by the modder deliberately.)

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Avernus_24149d5d-c509-48dc-b026-491c11e60a5c)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)_Char,_,_,_,"VanityBody")
AND
NOT DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)_Char,_, "VanityBody")
THEN
NOT DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Avernus_24149d5d-c509-48dc-b026-491c11e60a5c);

//If a character has an epilogue clothing replacer in the Vanity Boots/camp shoes slot, has vanilla DB for the avernus shoes, and doesn't have an avernus equipment DB for the camp clothes slot, clear the avernus camp shoes DB.

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Shoes_Avernus_c36967e4-26c5-4f2f-b25b-f351a6bac804)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)_Char,_,_,_,"VanityBoots")
AND
NOT DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)_Char,_, "VanityBoots")
THEN
NOT DB_EPI_Epilogue_PartyEquipment(_Char, NULL_00000000-0000-0000-0000-000000000000, 1, EPI_Camp_Shoes_Avernus_c36967e4-26c5-4f2f-b25b-f351a6bac804);

//Add contents of epilogue outfit replacer DBs to DB_EPI_Epilogue_PartyEquipment if the player went to avernus, but doesn't have any avernus equipment DBs.
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)_Char,(FLAG)_Flag, _Bool, (ITEMROOT)_Item,_)
AND
QRY_EPI_Epilogue_IsInAvernusWithKarlachorWyll(_Char)
AND
NOT DB_MGNTN_EPIOutfitReplacers_AvernusEquipment_Companions((CHARACTER)_Char,_,_)
THEN
DB_EPI_Epilogue_PartyEquipment((CHARACTER)_Char,(FLAG)_Flag, _Bool, (ITEMROOT)_Item);

//Add contents of epilogue outfit replacer DBs to DB_EPI_Epilogue_PartyEquipment if the player didn't go to avernus.
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)_Char,(FLAG)_Flag, _Bool, (ITEMROOT)_Item,_)
AND
NOT QRY_EPI_Epilogue_IsInAvernusWithKarlachorWyll(_Char)
THEN
DB_EPI_Epilogue_PartyEquipment((CHARACTER)_Char,(FLAG)_Flag, _Bool, (ITEMROOT)_Item);


//fallback/player equipment:

//Add contents of epilogue fallback outfit replacer DBs to DB_EPI_Epilogue_FallbackPartyEquipment
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementFallbackEquipment((ITEMROOT)_Item,_Int,_)
THEN
DB_EPI_Epilogue_FallbackPartyEquipment((ITEMROOT)_Item,_Int);

//END_REGION non-avernus equipment replacers



//REGION underwear replacers

//companion/NPC underwear:

//check for flagged underwear DB. if none exists, but default DB does, add info from default DB to party underwear DB.

PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
NOT DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)_Char, _, _, _, _)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_CharacterDefault((CHARACTER)_Char,(ITEMROOT)_Item,_)
THEN
DB_EPI_Epilogue_PartyUnderwear((CHARACTER)_Char,(ITEMROOT)_Item);


//check for flagged underwear DB. if flag conditions match, add info from flagged underwear DB to party underwear DB.
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)_Char, (FLAG)_Flag, _Bool, (ITEMROOT)_Item,_)
AND
GetFlag(_Flag,_Char,_Bool)
THEN
DB_EPI_Epilogue_PartyUnderwear((CHARACTER)_Char,(ITEMROOT)_Item);


//if flag conditions *don't* match, but default DB exists, add info from default underwear DB to party underwear DB.
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)_Char, (FLAG)_Flag, _Bool, _, _)
AND
NOT GetFlag(_Flag,_Char,_Bool)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_CharacterDefault((CHARACTER)_Char,(ITEMROOT)_Item,_)
THEN
DB_EPI_Epilogue_PartyUnderwear((CHARACTER)_Char,(ITEMROOT)_Item);


//player/fallback underwear:

//Add contents of epilogue fallback underwear replacer DBs to DB_EPI_Epilogue_FallbackPartyUnderwear
PROC
PROC_EPI_Epilogue_SwapEquipment((CHARACTER)_Char,(INTEGER)_)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Fallback((TAG)_Tag,(ITEMROOT)_Item,_)
THEN
DB_EPI_Epilogue_FallbackPartyUnderwear((TAG)_Tag,(ITEMROOT)_Item);

//END_REGION player fallback equipment/underwear replacers



//***epilogue setup end***


//REGION retroactive outfit application

//Retroactive equipment application will only apply to companions/NPCs! Since the player can dress their own character, you could run the risk of unequipping clothes the player chose if you tried to update their outfits retoactively.

//Since the player can't change companion/NPC clothing directly in the epilogue, retroactive replacers for them are fine.

//if the retroactive apply proc is called, check if the player is currently in the epilogue before proceeding.
PROC
PROC_MGNTN_EpilogueOutfitReplacers_RetroactiveApply()
AND
DB_CurrentLevel("EPI_Main_A")
THEN
PROC_MGNTN_ReplaceEpilogueOutfits();
PROC_MGNTN_ReplaceEpilogueUnderwear();


//check if character has flag that matches their replacer DB. if they do, add a copy of the replacer item to the character, and the roottemplate of the item to the replacer item tracker.
PROC
PROC_MGNTN_ReplaceEpilogueOutfits()
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementEquipment((CHARACTER)_Char, (FLAG)_Flag, _Bool, (ITEMROOT)_NewItemRoot,_)
AND
GetFlag(_Flag,_Char,_Bool)
THEN
TemplateAddTo((ITEMROOT)_NewItemRoot, (CHARACTER)_Char, 1, 0);
DB_MGNTN_RetroactiveEpilogueOutfitItemAddedTracker((ITEMROOT)_NewItemRoot, (CHARACTER)_Char);

//check if character has default replacer underwear, and if they have flagged underwear replacers. if they have a default replacer, but not a flagged one, add a copy of the default replacer item to the character, and the roottemplate of the item to the replacer item tracker.
PROC
PROC_MGNTN_ReplaceEpilogueUnderwear()
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_CharacterDefault((CHARACTER)_Char,(ITEMROOT)_NewItemRoot,_)
AND
NOT DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)_Char, _, _, _, _)
THEN
TemplateAddTo((ITEMROOT)_NewItemRoot, (CHARACTER)_Char, 1, 0);
DB_MGNTN_RetroactiveEpilogueOutfitItemAddedTracker((ITEMROOT)_NewItemRoot, (CHARACTER)_Char);


//check for flagged underwear DB. if they have one, and the character has a flag that matches their replacer DB, add a copy of the replacer item to the character, and the roottemplate of the item to the replacer item tracker.
PROC
PROC_MGNTN_ReplaceEpilogueUnderwear()
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)_Char, (FLAG)_Flag, _Bool, (ITEMROOT)_NewItemRoot,_)
AND
GetFlag(_Flag,_Char,_Bool)
THEN
TemplateAddTo((ITEMROOT)_NewItemRoot, (CHARACTER)_Char, 1, 0);
DB_MGNTN_RetroactiveEpilogueOutfitItemAddedTracker((ITEMROOT)_NewItemRoot, (CHARACTER)_Char);


//check for flagged underwear DB. if they have one, but they don't have a flag that matches their replacer DB, and they Do have a default DB, add a copy of the default replacer item to the character, and the roottemplate of the default item to the replacer item tracker.
PROC
PROC_MGNTN_ReplaceEpilogueUnderwear()
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_Flagged((CHARACTER)_Char, (FLAG)_Flag, _Bool, _, _)
AND
NOT GetFlag(_Flag,_Char,_Bool)
AND
DB_MGNTN_EPIOutfitReplacers_ReplacementUnderwear_CharacterDefault((CHARACTER)_Char,(ITEMROOT)_NewItemRoot,_)
THEN
TemplateAddTo((ITEMROOT)_NewItemRoot, (CHARACTER)_Char, 1, 0);
DB_MGNTN_RetroactiveEpilogueOutfitItemAddedTracker((ITEMROOT)_NewItemRoot, (CHARACTER)_Char);


//if an item is added to a character in the epilogue, and the item has a roottemplate linked to that character in the replacer item tracker, equip that item to them. Then, clear the template from the replacer item tracker, to prevent the game from repeatedly trying to equip items with that roottemplate to the character.
IF
TemplateAddedTo((ITEMROOT)_NewItemRoot,(ITEM)_NewItem,(CHARACTER)_Char,_)
AND
DB_CurrentLevel("EPI_Main_A")
AND
DB_MGNTN_RetroactiveEpilogueOutfitItemAddedTracker((ITEMROOT)_NewItemRoot, (CHARACTER)_Char)
THEN
Equip(_Char,_NewItem);
NOT DB_MGNTN_RetroactiveEpilogueOutfitItemAddedTracker(_NewItemRoot, _Char);

//END_REGION retroactive outfit application


EXITSECTION

ENDEXITSECTION
ParentTargetEdge "Act3c_EPI"

```




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

If you're using the toolkit, you can drop that same .txt file into the same file path in your toolkit project! You may need to manually create the file path to do so, but when you do, you should be able to see your script in the toolkit's **Story Editor**. You can find a guide on using the Story Editor [here!](https://mod.io/g/baldursgate3/r/scripting-using-the-story-editor)

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

To add that outfit to him in the epilogue, `DB_EPI_Epilogue_PartyEquipment` stores the following information:

The character the clothing should be added to, the flag it should check for to add the clothing, whether the flag is true or not (if it's checking for that flag being False, it'll have a 0 there instead!), and the item to equip to the character.

In that example, the item `EPI_Camp_Wyll_Duke` is added to Wyll if the flag `GLO_Wyll_State_GrandDuke` is True.

He also has a separate DB for his shoes:

```
DB_EPI_Epilogue_PartyEquipment((CHARACTER)S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d,(FLAG)GLO_Wyll_State_GrandDuke_0e223e4d-be63-89f4-380f-5cc755817abd, 1,(ITEMROOT)EPI_Camp_Shoes_Wyll_Duke_4aa0dbb1-f51a-45bc-8a58-814ac5063035);
```

Each epilogue clothing DB will only add one item at a time, so you'll need separate DBs if you'd like to add other items.


## Clearing DBs

To update the epilogue clothing for a given character, you'll first need to clear the existing DB for their clothing.

You can do that by taking the DB you want to clear, putting it in the `INITSECTION` your file, and writing **NOT** in front of it. This will clear the DB when your script is loaded for the first time.

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


**A note about flags:** You don't have to stick to just the existing flag being set here! When the existing DBs are cleared, you can set up outfits based on other flags. [https://bg3.norbyte.dev/](https://bg3.norbyte.dev/) is a good way to look for flags you want to check.


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

There are also two DBs for Underwear, `DB_EPI_Epilogue_PartyUnderwear` and `DB_EPI_Epilogue_FallbackPartyUnderwear`.

```
DB_EPI_Epilogue_PartyUnderwear((CHARACTER)S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12,(ITEMROOT)Underwear_Laezel_185ab1be-e93d-4518-b053-d6d4d7168d68);

DB_EPI_Epilogue_FallbackPartyUnderwear((TAG)REALLY_TIEFLING_7bf7207f-7406-49c0-b501-eaaa2bb4efd7,(ITEMROOT)Underwear_Tieflings_A_498c155f-8675-4a55-9cb0-89dd7270469f);
```

`DB_EPI_Epilogue_PartyUnderwear` stores the following information:

The character to add the underwear to, and the roottemplate of the underwear item to add.


And the information stored in `DB_EPI_Epilogue_FallbackPartyUnderwear` is this:

The tag for the race to give underwear to, and the underwear item to give characters with that tag.

The clothing for player characters is stored in the `DB_EPI_Epilogue_FallbackPartyEquipment` DB, which looks like this:

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
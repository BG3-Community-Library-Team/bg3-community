---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-04-30T23:18:56.150Z
tags: reference, osiris
editor: markdown
dateCreated: 2024-04-30T23:08:53.092Z
---

# Osiris DB Reference
The below is a list of Osiris DB's, and their Parameters.

# Types {.tabset}

## Combat
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CombatFlee_BlockedInLevel|List of levels where fleeing is blocked|1|String (Level Scenario ID)||||| 
## Game Management
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_StoryReloaded|?|1|Integer as Boolean|--|--|--|--|

## Location
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CurrentLevel|String ID of Current Level (Scenario)|1|String ID|||||

## Origins
|DB_PredefinedStartOrigin|?|1|UUID|||||
|DB_Origins_UnavailableForRandom|?|1|UUID|||||
|DB_RandomizeStartOrigin|?|1|Integer|||||
|DB_CharacterCreationStarted|?|1|Integer|||||
|DB_Origins|List of Origin Character UUIDs|1|UUID|||||
|DB_Origins_Random|?|1|UUID|||||
|DB_RandomStartOrigin|?|1|UUID|||||
|DB_CharacterCreation_FirstDummy|?|1|UUID|||||
|DB_CharacterCreation_FirstDummy|?|1|UUID|||||
|DB_CharacterCreation_FirstDummy|?|1|UUID|||||
|DB_CharacterCreation_FirstDummy|?|1|UUID|||||
|DB_ChosenOriginWaitingForTeleport|?|||||||
|DB_GLO_PlayerCharactersSetup|?|||||||
|DB_PredefinedStartOrigin|?|||||||


## Party
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Players|List of registered Player Character IDs|1||||||
|DB_Avatars|List of registered Player Avatar Character IDs|1||||||
|DB_PredefinePartyPreset_Loaded|?|||||||

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_QRYRTN_GetCharacterOwnerIfItemSummon|?|1||||||

## Scenes
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_SceneManager|?|2|Character UUID||--|--|--|
|PROC_SceneManager_HandleViolence|?|5|Integer as Boolean|||String||
|DB_InternScene_DeathHandled|?|2|?|Character UUID|--|--|--|
|PROC_SceneInterrupted|?|5|Character UUID|UUID||String|--|
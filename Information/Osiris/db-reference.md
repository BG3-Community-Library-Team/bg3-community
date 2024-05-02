---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-05-02T03:13:31.785Z
tags: reference, osiris
editor: markdown
dateCreated: 2024-04-30T23:08:53.092Z
---

# List:Osiris DB Reference
This page is a list of existing informational documentation relating to Osiris Databases.

## Pages
- [Character Management](character-dbs)
- [Class-Specific](class-dbs)
- [Combat](combat-dbs)
- [Crime](crime)
{.links-list}


# Types {.tabset}


## Game Management
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_StoryReloaded|?|1|Integer as Boolean|--|--|--|--|
|DB_NOOP|Hacky Osiris solution to dumb things|1|Integer|--|--|--|--|
|DB_InternalGroup_Count|?|1|Integer|--|--|--|--|
|DB_LogicOr|?|3|Integer|Integer|Integer|--|--|
|DB_GLO_DieFlag|?|4|UUID|UUID|Integer|UUID|--|
|DB_GLO_ItemInventoryLockFlag|?|3|UUID|UUID|UUID|--|--|
|DB_GLO_SetupForAct_CurrentLevel|?|1|Level ID|--|--|--|--|
|DB_IsEditor|(Non-functional) If in Editor Gamemode|1|Integer as Boolean|--|--|--|--|
|DB_ZZZ_LevelLoaded|?|1|Level ID String|--|--|--|--|
|DB_LevelLoadedOnce|?|1|Level ID String|--|--|--|--|
|DB_LevelGameplayLoadedOnce_WaitForGameplay|?|1|String|--|--|--|--|
|DB_CharacterCreationStarted|Has Character Creation Started?|1|?|--|--|--|--|
|DB_ObjectCountHelper|?|3|UUID String|Flag String ID|?|--|--|
|DB_GlobalFlag|List of Active Global Flags|1|Flag UUID|--|--|--|--|

## Location
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_ActiveCamp|?|1|?|--|--|--|--|
|DB_Camp|?|4|?|?|?|UUID|--|
|DB_CurrentLevel|String ID of Current Level (Scenario)|1|String ID|--|--|--|--|
|DB_WaypointInfo|?|4|?|?|?|?|--|
|DB_WaypointUnlocked|List of Unlocked Waypoints|2|?|Character UUID|--|--|--|
|DB_BlockedWaypointZone|List of Blocked Waypoints|1|Region String|--|--|--|--|

## Misc
### Tabs {.tabset}

#### Buried Treasures
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_TaggedItemTracker|?|2|UUID String|UUID|--|--|--|
|DB_Shovel_ChestMoundType|Types of Chest Mounds|4|Integer|Integer|Mound UUID|Behavior UUID|--|
|DB_ShovelArea|?|2|Object UUID|Object UUID|--|--|--|
|DB_Shovelling_Mound|?|4|?|?|Object UUID|?|--|
#### Configs
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_AnubisConfigsOverrideStack|?|3|UUID|String|Integer|
|DB_AnubisConfigs|?|2|Character UUID|String|--|
|DB_AnubisConfigs_DelayAssignment|?|2|Character UUID|String|--|
|DB_AnubisConfigOverride_NewConfig|?|3|Character UUID|String|Integer|
|DB_AnubisConfigOverride_UpdatedConfig|?|1|Integer|--|--|
|DB_AnubisConfigs_CharacterSavedStates|?|2|Character UUID|State|--|

#### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|
|-----|----|----|----|
|DB_QRYRTN_AnubisConfigOverrideIndex|?|1|?|

#### Utilities
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CustomUseItemResponse|?|3|Character UUID|?|Integer|--|--|
|DB_DialogMoneyTransfer|?|3|Integer|Character UUID|Integer (Price)|--|--|
|DB_ReportKiller|?|2|?|Tag UUID|--|--|--|
|DB_Helper_GetAnyRandomPositionInArea_Result|?|3|Integer X Coordinate|Integer Y Coordinate|Integer Z Coordinate|--|--|

## Story
### Tabs {.tabset}
#### Dialog
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_AutomatedDialog|?|1|Integer|--|--|--|--|
|DB_AutomatedDialogIsVB|?|1|Integer|--|--|--|--|
|DB_DialogDeath|?|1|Character UUID|--|--|--|--|
|DB_DialogEnding|?|2|DialogResource|Integer|--|--|--|
|DB_DialogName|?|2|DialogResource|Integer|--|--|--|
|DB_DialogNumPlayers|Amount of Players in a Dialog|2|Integer|Dialog Resource|--|--|--|
|DB_DialogNumNPCs|Amount of NPCs in a Dialog|2|Integer|Dialog Resource|--|--|--|
|DB_DialogNPCs|List of NPCs in a Dialog|2|Integer|Dialog Resource|--|--|--|
|DB_DialogPlayers|List of Players in a Dialog|3|Integer|UUID String|?|--|--|
|DB_DialogRequestFailed|?|2|DialogResource|Integer|--|--|--|
|DB_DialogSpeakers|List of Spekaers in a Dialog|3|Integer|UUID String|?|--|--|
|DB_OnDialogAttackRequested|?|3|Character UUID|Character UUID|Integer|--|--|
|DB_InteractiveDialogSpeaker|?|2|Integer|?|--|--|--|

#### Plot (Spoilers)
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_GLO_Absolute_Entails|?|2|Flag UUID|Flag UUID|--|--|--|
|DB_GLO_Absolute_TrueSoul|Character IDs that are True Souls|1|Character UUID|--|--|--|--|

#### Scenes
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_SceneManager|?|2|Character UUID|?|--|--|--|
|PROC_SceneManager_HandleViolence|?|5|Integer as Boolean|?|?|String|?|
|DB_InternScene_DeathHandled|?|2|?|Character UUID|--|--|--|
|PROC_SceneInterrupted|?|5|Character UUID|UUID|?|String|--|

## UI
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_InCharacterRespec|Characters respec'ing|2|UUID|String|--|--|--|
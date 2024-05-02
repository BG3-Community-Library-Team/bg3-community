---
title: Utility DB Reference
description: DBs that seem to be more for general utility
published: true
date: 2024-05-02T16:28:42.073Z
tags: reference, osiris, db, dbs
editor: markdown
dateCreated: 2024-05-02T16:28:42.073Z
---

# Utility DBs

# {.tabset}
## Utility
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
|DB_CustomUseItemResponse|?|3|Character UUID|?|Integer|--|--|
|DB_DialogMoneyTransfer|?|3|Integer|Character UUID|Integer (Price)|--|--|
|DB_ReportKiller|?|2|?|Tag UUID|--|--|--|
|DB_Helper_GetAnyRandomPositionInArea_Result|?|3|Integer X Coordinate|Integer Y Coordinate|Integer Z Coordinate|--|--|

## Anubis
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_AnubisConfigsOverrideStack|?|3|UUID|String|Integer|
|DB_AnubisConfigs|?|2|Character UUID|String|--|
|DB_AnubisConfigs_DelayAssignment|?|2|Character UUID|String|--|
|DB_AnubisConfigOverride_NewConfig|?|3|Character UUID|String|Integer|
|DB_AnubisConfigOverride_UpdatedConfig|?|1|Integer|--|--|
|DB_AnubisConfigs_CharacterSavedStates|?|2|Character UUID|State|--|

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|
|-----|----|----|----|
|DB_QRYRTN_AnubisConfigOverrideIndex|?|1|?|
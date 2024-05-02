---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-05-02T16:29:15.639Z
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
- [Utilities](game-management-dbs)
{.links-list}


# Types {.tabset}

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
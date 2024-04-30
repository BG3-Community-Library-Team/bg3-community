---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-04-30T23:36:30.345Z
tags: reference, osiris
editor: markdown
dateCreated: 2024-04-30T23:08:53.092Z
---

# Osiris DB Reference
The below is a list of Osiris DB's, and their Parameters.

# Types {.tabset}

## Character Management
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Players|List of registered Player Character IDs|1|Character UUID|--|--|--|--|
|DB_Avatars|List of registered Player Avatar Character IDs|1|Character UUID|--|--|--|--|
|DB_PartyMembers|List of registered Party Member Character IDs|1|Character UUID|--|--|--|--|
|DB_PredefinePartyPreset_Loaded|?|||||||

## Combat
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CombatFlee_BlockedFor|List of Characters for whom fleeing combat is blocked|1|Character UUID|--|--|--|--|
|DB_CombatFlee_BlockedInLevel|Levels where fleeing is blocked|1|String (Level Scenario ID)|--|--|--|--| 
|DB_CombatFlee_LastResortTrigger|?|2|String (Level Scenario ID)|Start Point UUID|--|--|--|
|DB_CombatFlee_MinimumDistanceToFlee|Minimum Distance (m) required to flee|1|Integer|--|--|--|--|
|DB_CombatFlee_WaitForCombatLeave|?|2|Character UUID|UUID|--|--|--|
|DB_CombatGroups_CheckedDialog|?|2|UUID|UUID|--|--|--|
|DB_CombatGroups_Iterator|?|4|Combat Group ID|UUID|?|?|--|
|DB_CMB_StatusOnInit|?|2-4|UUID|String|Integer|UUID|--|
|DB_DoNotChangeAttitudeAfterCombat|Prevent attitude change on Character after combat.|1|UUID|--|--|--|--|
|DB_CombatStarted|DB Boolean determining if Combat has Started|1|Integer as Boolean|--|--|--|--|
|DB_Was_InCombat|?|2|UUID|?|--|--|--|
|DB_SwitchedCombat|?|2|?|?|--|--|--|
|DB_Is_InCombat|?|2|UUID|UUID|--|--|--|
|DB_CMB_RoundCounter|?|2|UUID|Integer|--|--|--|
|DB_Downed|List of Downed Characters|1|Character UUID|--|--|--|--|

## Game Management
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_StoryReloaded|?|1|Integer as Boolean|--|--|--|--|
|DB_NOOP|Hacky Osiris solution to dumb things|1|Integer|--|--|--|--|

## Location
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_ActiveCamp|?|1|?|--|--|--|--|
|DB_Camp|?|4|?|?|?|UUID|--|
|DB_CurrentLevel|String ID of Current Level (Scenario)|1|String ID|--|--|--|--|
|DB_InCamp|List of Characters Currently in Camp|1|Character UUID|--|--|--|--|
|DB_WaypointInfo|?|4|?|?|?|?|--|
|DB_WaypointUnlocked|List of Unlocked Waypoints|2|?|Character UUID|--|--|--|

## Misc
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_InDangerZone|?|2|Character UUID|?|--|--|--|

## Origins
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
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

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_QRYRTN_GetCharacterOwnerIfItemSummon|?|1|--|--|--|--|--|
|DB_QRYRTN_CombatFlee_FoundFleeWaypoint|?|3|Character UUID|UUID|?|--|--|

## Scenes
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_SceneManager|?|2|Character UUID|?|--|--|--|
|PROC_SceneManager_HandleViolence|?|5|Integer as Boolean|?|?|String|?|
|DB_InternScene_DeathHandled|?|2|?|Character UUID|--|--|--|
|PROC_SceneInterrupted|?|5|Character UUID|UUID|?|String|--|
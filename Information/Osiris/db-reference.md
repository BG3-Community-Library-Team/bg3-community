---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-05-01T04:15:38.526Z
tags: reference, osiris
editor: markdown
dateCreated: 2024-04-30T23:08:53.092Z
---

# Osiris DB Reference
The below is a (currently incomplete) list of Osiris DBs, and their Parameters.

# Types {.tabset}

## Anubis Configs
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_AnubisConfigsOverrideStack|?|3|UUID|String|Integer|--|--|
|DB_AnubisConfigs|?|2|Character UUID|String|--|--|--|
|DB_AnubisConfigs_DelayAssignment|?|2|Character UUID|String|--|--|--|
|DB_AnubisConfigOverride_NewConfig|?|3|Character UUID|String|Integer|--|--|
|DB_AnubisConfigOverride_UpdatedConfig|?|1|Integer|--|--|--|--|
|DB_AnubisConfigs_CharacterSavedStates|?|2|Character UUID|State|--|--|--|

### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRYRTN_AnubisConfigOverrideIndex|?|1|?|--|--|

## Buried Treasures
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_TaggedItemTracker|?|2|UUID String|UUID|--|--|--|
|DB_Shovel_ChestMoundType|Types of Chest Mounds|4|Integer|Integer|Mound UUID|Behavior UUID|--|
|DB_ShovelArea|?|2|Object UUID|Object UUID|--|--|--|
|DB_Shovelling_Mound|?|4|?|?|Object UUID|?|--|

## Character Creation
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CharacterCreationDummy|?|Character UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_TUT_CharacterCreation_Started|?|1|Integer|--|--|--|--|
|DB_TUT_CharacterCreation_IntroMovieFinished|?|1|Integer|--|--|--|--|
|DB_TUT_CharacterCreation_InitialShown|?|1|Integer|--|--|--|--|

### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRYRTN_TUT_CharacterCreation_GetUserDummy|?|1|?|--|--|

## Character Management
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Players|List of registered Player Character IDs|1|Character UUID|--|--|--|--|
|DB_Avatars|List of registered Player Avatar Character IDs|1|Character UUID|--|--|--|--|
|DB_PartyMembers|List of registered Party Member Character IDs|1|Character UUID|--|--|--|--|
|DB_PredefinePartyPreset_Loaded|?|?|--|--|--|--|--|
|DB_Following|Character that is following|2|Character UUID|?|--|--|--|
|DB_CantAct|Character can perform actions|1|CCharacter UUID|--|--|--|--|
|DB_IsArrested|List of Arrested Characters|2|?|Character UUID|--|--|--|
|DB_InBlockedWaypointZone|List of Characters Currently in a Blocked Waypoint Zone|2|Character UUID|Region String|--|--|--|
|DB_InCamp|List of Characters Currently in Camp|1|Character UUID|--|--|--|--|
|DB_InDangerZone|List of Characters in a Danger Zone|2|Character UUID|?|--|--|--|
|DB_InRegion|List of Characters currently in region|2|Character UUID|Region String ID|--|--|--|
|DB_IsOrWasInParty|List of Characters that have been in Party|1|Character UUID|--|--|--|--|
|DB_Dead|List of Dead Characters|1|Character UUID|--|--|--|--|
|DB_PlayerSummons|List of Characters Summoned by Player|1|Character UUID|--|--|--|--|
|DB_PartyFollowers|List of Party Followers|1|Character UUID|--|--|--|--|
|DB_TutorialCompanion|List of Tutorial Companions|1|Character UUID|--|--|--|--|


### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|----|----|
|DB_QRYRTN_GetCharacterOwnerIfItemSummon|?|1|?|--|--|

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
|DB_CantTalk_IgnoreStatusesCombat|?|1|UUID|--|--|--|--|
|DB_GLO_CombatFirstTurnStarted|?|1|?|--|--|--|--|
|DB_GLO_Combat_TemporaryHostile|?|1|UUID|--|--|--|--|
|DB_GLO_Combat_PermanentlyHostile|?|1|UUID|--|--|--|--|
|DB_EnterCombatRequested|?|1|UUID String|--|--|--|--|

### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRYRTN_CombatFlee_FoundFleeWaypoint|?|3|Character UUID|UUID|?|

## Crime
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CRIME_WaitingForDialogStop|?|2|?|Integer|--|--|--|

## Dialog
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
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CustomUseItemResponse|?|3|Character UUID|?|Integer|--|--|

## Origins
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_PredefinedStartOrigin|?|1|UUID|--|--|--|--|
|DB_Origins_UnavailableForRandom|?|1|UUID|--|--|--|--|
|DB_RandomizeStartOrigin|?|1|Integer|--|--|--|--|
|DB_CharacterCreationStarted|?|1|Integer|--|--|--|--|
|DB_Origins|List of Origin Character UUIDs|1|UUID|--|--|--|--|
|DB_Origins_Random|?|1|UUID|--|--|--|--|
|DB_RandomStartOrigin|?|1|UUID|--|--|--|--|
|DB_ChosenOriginWaitingForTeleport|?|--|--|--|--|--|--|
|DB_GLO_PlayerCharactersSetup|?|--|--|--|--|--|--|
|DB_PredefinedStartOrigin|?|--|--|--|--|--|--|

## Scenes
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
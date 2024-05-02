---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-05-02T02:36:36.146Z
tags: reference, osiris
editor: markdown
dateCreated: 2024-04-30T23:08:53.092Z
---

# Osiris DB Reference
The below is a (currently incomplete) list of Osiris DBs, and their Parameters.

# Types {.tabset}

## Anubis Configs

### Tabs {.tabset}

#### Configs
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_AnubisConfigsOverrideStack|?|3|UUID|String|Integer|--|--|
|DB_AnubisConfigs|?|2|Character UUID|String|--|--|--|
|DB_AnubisConfigs_DelayAssignment|?|2|Character UUID|String|--|--|--|
|DB_AnubisConfigOverride_NewConfig|?|3|Character UUID|String|Integer|--|--|
|DB_AnubisConfigOverride_UpdatedConfig|?|1|Integer|--|--|--|--|
|DB_AnubisConfigs_CharacterSavedStates|?|2|Character UUID|State|--|--|--|

#### Query Returns
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

## Characters
### Tabs {.tabset}

#### Character Creation
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

#### Character Management
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
|DB_DiedInCombat|List of Characters that Died in Combat|2|Character UUID|?|--|--|--|

#### Origins
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

#### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|----|----|
|DB_QRYRTN_GetCharacterOwnerIfItemSummon|Returns Owner if UUID corresponds to a summoned item|1|Character UUID|--|--|
|DB_QRYRTN_CharacterGetOwnerOrSelf|Returns Owner or Queried Character UUID|1|Character UUID|--|--|

## Class-Specific

### {.tabset}
#### Bard
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CRIME_MusicalPerformance_DC|?|2|Integer DC|Tag UUID Difficulty|--|--|--|
|DB_CRIME_MusicalPerformance_Status|?|3|String Status|String Crime Type|String Event|--|--|
|DB_Bard_InstrumentRootToSpell|?|2|UUID|String Instrument Suffix|--|--|--|
|DB_CRIME_MusicalPerformance|?|3|?|Character UUID|String Crime Type|--|--|
|DB_CRIME_MusicalPerformance_WaitForFlourishesToStop|?|1|?|--|--|--|--|
|DB_CRIME_MusicalPerformance_Flourish|?|3|?|?|Character UUID|--|--|
|DB_CRIME_MusicalPerformance_SoundNames|?|3|?|?|?|--|--|
|DB_CRIME_MusicalPerformance_Listener|?|3|Integer|Character UUID|Character UUID|--|--|
|DB_CRIME_MusicalPerformance_SoundStarted|?|2|Character UUID|String|--|--|--|
|DB_CRIME_MusicalPerformance_Confronted|?|3|Integer|Character UUID|?|--|--|
|DB_CRIME_MusicalPerformance_NPCIgnoring|?|3|Character UUID|String|String concatenatedString|--|--|
|DB_CRIME_MusicalPerformance_NPCs|?|3|Integer|?|Character UUID|--|--|

#### Cleric
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_GLO_Spells_DivineInterventionSpells|List of Divine Intervention Spells|1|Spell ID|--|--|--|--|

#### Paladin
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Debug_GLO_PaladinOathbreaker_ForceOathbreaker|Force an Oath Break|1|Integer|--|--|
|DB_GLO_Spells_DominatedOwnerStatus|List of Statuses that fall under Dominated|2|Status ID|Status ID|--|--|--|
|DB_GLO_Spells_TurnCharactersEvilStatuses|List of statuses that turn characters Evil|1|Status ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_RedemptionPrice|Cost of Redemption at a given level|2|Integer (Level Number)|Integer (Price)|--|--|--|
|DB_GLO_PaladinOathbreaker_LinkedDialogues|Linked Dialogs relating to Oathbreaker|1|Dialog Resource ID|--|--|--|--|
|DB_GLO_PaladinOathbreakerPath_SelectedOathbreaker|List of Characters that have selected Oathbreaker|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_CrimeID|?|2|Character UUID|Crime ID|--|--|--|
|DB_GLO_PaladinOathbreakerPath_WaitForCrime|?|2|Character UUID|Crime ID|--|--|--|
|DB_GLO_PaladinOathbreakerPath_KnightTalkedTo|List of Characters that have spoken to the Oathbreaker Knight|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreakerPath_WaitForDialog|?|1|Dialog Resource|--|--|--|--|
|DB_GLO_OathbreakerKnight_StartFirstAppearanceWith|?|1|?|--|--|--|--|
|DB_GLO_PaladinOathbreaker_Oathbreakers|List of Oathbreakers|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_SinsAndCrimeTypes|Sins and Crime Types that can proc an Oath-break|1|Flag String ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_GenericCrimes|Generic Crimes that can proc an Oath-break|1|Flag String ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_ProtectedNPCs|List of protected NPCs relating to Oath Breaking|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_SubclassTags|Link between Subclass Tag and Oath-Breaker Subclass Tag|2|Subclass Tag UUID|Oathbreaker Subclass Tag UUID|--|--|--|
|DB_GLO_PaladinOathbreaker_SubclassOathBrokenFlags|Link between Subclass Tag and Oath Broken Flag UUID|2|Broken Oath Flag|Subclass Tag UUID|--|--|--|
|DB_GLO_PaladinOathbreaker_EvilTags|Tags that prevent an Oath-break|1|Tag UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_CrimesToReact|Crimes that will cause a reaction from characters for specific Paladin Oaths|3|Subclass Tag ID|Crime String ID|NPC Tag ID|--|--|
|DB_GLO_PaladinOathbreaker_PotentialCrimeID|ID of Potential Oathbreaking Crime|1|Crime ID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_NotifyAfterDialogEnds|?|3|Dialog Resource|Integer|?|--|--|
|DB_GLO_PaladinOathbreaker_ReactedToBreakingOath|?|1|Character UUID|--|--|--|--|
|DB_GLO_PaladinOathbreaker_RedemptionFromOathbreaker|Character that's gained Redemption|1|Character UUID|--|--|--|--|

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
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|Parameter 6|Parameter 7|
|-----|----|----|----|----|----|----|----|----|----|
|DB_CRIME_WaitingForDialogStop|?|2|?|Integer|--|--|--|--|--|
|DB_CRIME_FindSourceInvestigators|?|3|Integer|Integer|String Crime State Id|--|--|--|--|
|DB_CRIME_SourceInvestigation_Discovered|?|3|Integer|Integer|String Crime State Id|--|--|--|--|
|DB_CRIME_SourceInvestigation_NotDiscovered|?|3|Integer|Integer|String Crime State Id|--|--|--|--|
|DB_CRIME_SourceInvestigationRollStealthFail|?|1|Integer|--|--|--|--|--|--|
|DB_CRIME_AttackInvestigation_CrimeStoryActionLink|?|2|Integer|Integer|--|--|--|--|--|
|DB_CRIME_AttackInvestigation_OriginalCrimeType|?|2|String Crime ID|String|--|--|--|--|--|
|DB_Crime_IncapacitatedOriginalAssaultType|?|2|Integer|?|--|--|--|--|--|
|DB_CRIME_InvestigateAssaultSourceLocation|?|7|String Crime ID|Character UUID|Integer X Coordinate|Integer Y Coordinate|Integer Z Coordinate|Character UUID|Integer|
|DB_InvestigatingAssaultSource|?|2|String Crime ID|Character UUID|--|--|--|--|--|
|DB_CRIME_AttackInvestigation_Attentive|?|1|Character UUID|--|--|--|--|--|--|
|DB_CRIME_AttackInvestigation_HandledRoll|?|1|Integer|--|--|--|--|--|--|
|DB_CRIME_SourceInvestigationRollStealthFail|?|1|Integer|--|--|--|--|--|--|
|DB_CRIME_InvestigationCriminalLocation|?|4|String Crime ID|Integer  X Coordinate|Integer Y Coordinate|Integer Z Coordinate|--|--|--|
|DB_CRIME_AssaultSourceMarker|?|2|String Crime ID|?|--|--|--|--|--|

### Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRYRTN_CRIME_GetOriginalAttackCrime|?|1|?|--|--|
|DB_QRYRTN_CRIME_GetAssaultMurderWithInvestigationVariant|?|1|?|--|--|
|DB_QRYRTN_CrimeIncapacitatedAssaultGetCrimeType|?|1|String Crime State ID|--|--|
|DB_QRYRTN_InvestigateAssaultSourceAdvantage|?|1|Integer|--|--|

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
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CustomUseItemResponse|?|3|Character UUID|?|Integer|--|--|
|DB_PermaDefeated|List of Permanently Defeated Characters|1|Character UUID|--|--|--|--|
|DB_OffStage|?|1|Character UUID|--|--|--|--|
|DB_DialogMoneyTransfer|?|3|Integer|Character UUID|Integer (Price)|--|--|
|DB_ReportKiller|?|2|?|Tag UUID|--|--|--|

## Story
### Tabs {.tabset}
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

## UI
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_InCharacterRespec|Characters respec'ing|2|UUID|String|--|--|--|
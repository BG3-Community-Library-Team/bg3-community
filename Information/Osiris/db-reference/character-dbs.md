---
title: Character DB Reference
description: Osiris Character DBs
published: true
date: 2024-05-07T00:43:38.387Z
tags: osiris, db, characters, character creation
editor: markdown
dateCreated: 2024-05-02T03:08:57.566Z
---


# Characters DBs
The following DBs are ones that relate specifically to Characters.

# Tabs {.tabset}
## Character Creation
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CharacterCreationDummy|List of Character Creation Dummy UUIDs|Character UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_CharacterCreation_FirstDummy|?|1|UUID|--|--|--|--|
|DB_TUT_CharacterCreation_Started|?|1|Integer|--|--|--|--|
|DB_TUT_CharacterCreation_IntroMovieFinished|?|1|Integer|--|--|--|--|
|DB_TUT_CharacterCreation_InitialShown|?|1|Integer|--|--|--|--|

## Character Management
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Players|List of registered Player Character IDs|1|Character UUID|--|--|--|--|
|DB_Avatars|List of registered Player Avatar Character IDs|1|Character UUID|--|--|--|--|
|DB_PartyMembers|List of registered Party Member Character IDs|1|Character UUID|--|--|--|--|
|DB_HiddenCharacters|?|2|Character UUID|?|--|--|--|
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
|DB_PermaDefeated|List of Permanently Defeated Characters|1|Character UUID|--|--|--|--|
|DB_OffStage|?|1|Character UUID|--|--|--|--|
|DB_PartOfTheTeam|Characters that are Part of the Team|1|Character UUID|--|--|--|--|

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

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|----|----|
|DB_QRYRTN_GetCharacterOwnerIfItemSummon|Returns Owner if UUID corresponds to a summoned item|1|Character UUID|--|--|
|DB_QRYRTN_CharacterGetOwnerOrSelf|Returns Owner or Queried Character UUID|1|Character UUID|--|--|
|DB_QRYRTN_GetBestAvatarForCompanion|Returns best avatar for a given companion|2|Character UUID|Avatar UUID|--|
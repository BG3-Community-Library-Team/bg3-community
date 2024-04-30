---
title: Osiris Database Reference
description: Detailed list of all Osiris Databases in the BG3 Code
published: true
date: 2024-04-30T23:12:46.005Z
tags: reference, osiris
editor: markdown
dateCreated: 2024-04-30T23:08:53.092Z
---

# Osiris DB Reference
The below is a list of Osiris DB's, and their Parameters.

# Types {.tabset}

## Game Management

|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_StoryReloaded||1|Integer as Boolean|--|--|--|--|
|DB_InternScene_DeathHandled||2|?|Character UUID|--|--|--|
|DB_SceneManager||2|Character UUID||--|--|--|
|PROC_SceneManager_HandleViolence||5|Integer as Boolean|||String|--|
|DB_StoryReloaded||1|Integer as Boolean|||||

## Origins

|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_PredefinedStartOrigin||1|UUID|||||
|DB_Origins_UnavailableForRandom||1|UUID|||||
|DB_RandomizeStartOrigin||1|Integer|||||
|DB_CharacterCreationStarted||1|Integer|||||
|DB_Origins||1|UUID|||||
|DB_Origins_Random||1|UUID|||||
|DB_RandomStartOrigin||1|UUID|||||
|DB_CharacterCreation_FirstDummy||1|UUID|||||
|DB_CharacterCreation_FirstDummy||1|UUID|||||
|DB_CharacterCreation_FirstDummy||1|UUID|||||
|DB_CharacterCreation_FirstDummy||1|UUID|||||
|DB_CurrentLevel||1|String ID|||||
|DB_ChosenOriginWaitingForTeleport||||||||
|DB_PredefinePartyPreset_Loaded||||||||
|DB_GLO_PlayerCharactersSetup||||||||
|DB_PredefinedStartOrigin||||||||


## Party

|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_Players||||||||
|DB_Avatars||||||||

## Query Returns

|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_QRYRTN_GetCharacterOwnerIfItemSummon||1||||||
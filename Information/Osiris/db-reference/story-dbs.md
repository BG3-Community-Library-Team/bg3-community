---
title: Story DB Reference
description: Osiris DBs that relate to Story Content
published: true
date: 2024-05-04T20:02:11.498Z
tags: reference, osiris, db, dbs
editor: markdown
dateCreated: 2024-05-02T16:35:51.588Z
---

# Story
The following DBs relate to the Story.

# Tabs {.tabset}
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

## Functionality
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_GLO_BloodElixirs_RacialElixirTemplates|Links Item & Tag ID for reward for giving blood to Araj Oblodra.|3|Tag ID|Item ID|?|--|--|

## Plot (Spoilers)
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_GLO_Absolute_Entails|?|2|Flag UUID|Flag UUID|--|--|--|
|DB_GLO_Absolute_TrueSoul|Character IDs that are True Souls|1|Character UUID|--|--|--|--|

## Scenes
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_SceneManager|?|2|Character UUID|?|--|--|--|
|PROC_SceneManager_HandleViolence|?|5|Integer as Boolean|?|?|String|?|
|DB_InternScene_DeathHandled|?|2|?|Character UUID|--|--|--|
|PROC_SceneInterrupted|?|5|Character UUID|UUID|?|String|--|
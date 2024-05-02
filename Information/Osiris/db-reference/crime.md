---
title: Crime DB Reference
description: Osiris Databases relating to Crimes
published: true
date: 2024-05-02T16:30:44.657Z
tags: osiris, crime, db
editor: markdown
dateCreated: 2024-05-02T03:05:44.902Z
---

# Crime DBs
The following DBs are ones that relate specifically to Crime.

# {.tabset}
## General
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

## Camp
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|Parameter 6|Parameter 7|
|-----|----|----|----|----|----|----|----|----|----|
|DB_CRIME_OriginTeam_AnnoyedReaction|?|2|Integer|String|--|--|--|--|--|

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRYRTN_CRIME_GetOriginalAttackCrime|?|1|?|--|--|
|DB_QRYRTN_CRIME_GetAssaultMurderWithInvestigationVariant|?|1|?|--|--|
|DB_QRYRTN_CrimeIncapacitatedAssaultGetCrimeType|?|1|String Crime State ID|--|--|
|DB_QRYRTN_InvestigateAssaultSourceAdvantage|?|1|Integer|--|--|

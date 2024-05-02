---
title: Combat DB Reference
description: Osiris DBs relating to Combat
published: true
date: 2024-05-02T03:11:43.018Z
tags: osiris, db, dbs, combat
editor: markdown
dateCreated: 2024-05-02T03:11:16.182Z
---

# Combat

# {.tabset}
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

## Query Returns
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|
|-----|----|----|----|----|----|
|DB_QRYRTN_CombatFlee_FoundFleeWaypoint|?|3|Character UUID|UUID|?|
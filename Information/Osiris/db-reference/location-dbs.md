---
title: Location DB Reference
description: Osiris DBs that relate to Locations
published: true
date: 2024-05-04T20:39:09.388Z
tags: reference, osiris, db, dbs
editor: markdown
dateCreated: 2024-05-02T16:33:41.366Z
---

# Location DBs
The following DBs are ones that relate to Location.

# Tabs {.tabset}
## Location
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_ActiveCamp|?|1|?|--|--|--|--|
|DB_Camp|?|4|?|?|?|UUID|--|
|DB_CurrentLevel|String ID of Current Level (Scenario)|1|String ID|--|--|--|--|
|DB_WaypointInfo|?|4|?|?|?|?|--|
|DB_WaypointUnlocked|List of Unlocked Waypoints|2|?|Character UUID|--|--|--|
|DB_BlockedWaypointZone|List of Blocked Waypoints|1|Region String|--|--|--|--|

## Buried Treasures
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_TaggedItemTracker|?|2|UUID String|UUID|--|--|--|
|DB_Shovel_ChestMoundType|Types of Chest Mounds|4|Integer|Integer|Mound UUID|Behavior UUID|--|
|DB_ShovelArea|?|2|Object UUID|Object UUID|--|--|--|
|DB_Shovelling_Mound|?|4|?|?|Object UUID|?|--|

## Camp
|DB Name|Description|# of Parameters|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Parameter 5|
|-----|----|----|----|----|----|----|----|
|DB_CampNight_AvatarDream|?|2|Flag ID|Flag ID|--|--|--|
|DB_ORI_DarkUrge_SetupNights|?|1|Act ID|--|--|--|--|
|DB_CampNight|?|2|Flag ID|Integer|--|--|--|
|DB_CampNight_Camp|?|2|Flag ID|String Locational ID|--|--|--|
|DB_CampNight_CancelledBy|?|2|Flag ID|Flag ID|--|--|--|
|DB_CampNight_Requirement|?|2|Flag ID|Character ID|--|--|--|
|DB_CampNight_RomanceNight|?|2-4|Flag ID|Character ID|Flag ID|Flag ID|--|
|DB_CampNight_Requirement_CanStartDating|?|2|Flag ID|Character ID|--|--|--|
|DB_CampNight_ExclusiveMoment|?|1|Flag ID|--|--|--|--|
|DB_CampNight_Requirement_Approval|?|3|Flag ID|Character ID|Integer|--|--|
|DB_CAMP_GoblinHuntCelebration_SexScenes|?|3|Flag ID|Flag ID|Character UUID|--|--|
|DB_CampNight_Requirement_Dating|?|2|Flag ID|Character ID|--|--|--|
|DB_CampNight_CRD|?|4|Flag ID|Character ID|Flag ID|UUID|--|
|DB_CampNight_IVB|?|4|Flag ID|Flag ID|Character ID|UUID|--|
|DB_CampNight_SoloDream|?|3|Flag ID|Character ID|Flag ID|--|--|
|DB_CampNight_Completed|?|1|Flag ID|--|--|--|--|
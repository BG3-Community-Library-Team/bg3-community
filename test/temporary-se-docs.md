---
title: (Wikithon suggestion) Improving SE docs
description: 
published: true
date: 2026-01-14T22:59:17.405Z
tags: 
editor: markdown
dateCreated: 2026-01-14T22:58:17.562Z
---

# Suggestions for improving SE API documentation

This temporary page has been created for collaboration on WIP docs before opening PRs on GitHub. 

## Missing modules

Several major namespaces defined in `ExtIdeHelpers` are completely absent from `API.md`.
### `Ext.Audio` (client-side)

This module allows audio manipulation (Banks, Events, RTPC, etc). The entire API is not formally documented.
Add new section "Audio API" in `API.md`.
### `Ext.Loca`

This module provides access to reading and writing locales and is essential for managing translations with SE.
Add new section "Localization" in `API.md`.
### `Ext.IO`

This module provides access to file I/O operations, such as reading and writing files. While there is scattered guidance throughout the docs, the API is not formally documented.
Add new section "File I/O" in `API.md`.
### `Ext.Template`

This module provides access to item, character templates, etc. The entire API is not formally documented.
Add new section "Templates" in `API.md`.
### `Ext.StaticData`

Accessing static game data (Resources like UUIDs for races, classes, etc.) is vital for data-driven mods.
Add new section "Static Data" in `API.md`.
### `Ext.Resource`

This module provides access to game resources (like meshes, materials, etc.) and is essential for customizing appearance (`StaticData` too); it is used by mods such as CPF and UT/KAVT UAP.

Add new section "Resources" (?) in `API.md`.
### `Ext.Level` (Pathfinding & physics)

This module contains essential gameplay logic functions like raycasting, pathfinding, and checking for entities on specific tiles. The entire API is not formally documented.
Add new section "Levels, pathfinding & physics" in `API.md`.

## Important gaps

Several useful or prominent methods are missing from `API.md`. The sections below list some of them.
### Type mismatches

- ExtIdeHelpers: Defined in `Ext_Timer` as `Ext.Timer.MonotonicTime`.
- API.md: Incorrectly documented as `Ext.Utils.MonotonicTime`.
### Missing methods related to `Ext.Entity`

Several methods are missing, namely methods related to subscribing to entity events, such as:

```lua
--- @field OnChange fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?, a4:uint64?):uint64?
--- @field OnCreate fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?, a4:boolean?, a5:boolean?):uint64
--- @field OnCreateDeferred fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?):uint64
--- @field OnCreateDeferredOnce fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?):uint64
--- @field OnCreateOnce fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?):uint64
--- @field OnDestroy fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?, a4:boolean?, a5:boolean?):uint64
--- @field OnDestroyDeferred fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?):uint64
--- @field OnDestroyDeferredOnce fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?):uint64
--- @field OnDestroyOnce fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?):uint64
--- @field OnSystemPostUpdate fun(a1:ExtSystemType, a2:FunctionRef, a3:boolean?):uint64
--- @field OnSystemUpdate fun(a1:ExtSystemType, a2:FunctionRef, a3:boolean?):uint64
--- @field Subscribe fun(a1:ExtComponentType, a2:FunctionRef, a3:EntityHandle?, a4:uint64?):uint64?
--- @field Unsubscribe fun(a1:uint64):boolean
```
These methods can be useful for modders to subscribe to events related to entities, such as when a component is added or removed, in order to react to changes in the game world.
### Missing methods related to `Ext.UI`

```lua
Ext.UI.GetPickingHelper(playerId: uint16): EclPlayerPickingHelper
```
Returns the picking helper which contains data about what is currently under the player's cursor (world position, entities, etc.). Essential for point-and-click mechanics.

```lua
Ext.UI.GetCursorControl()
Ext.UI.GetDragDrop()
```
### Missing methods related to `Ext.Utils`
Example:
```lua
Ext.Utils.GetGlobalSwitches(): GlobalSwitches
```
Allows access to engine setting/toggles like `AiEnableSwarm`, `CanAutoSave`, etc. For example, `NrOfAutoSaves` can be set beyond UI limits to allow more autosaves (used by Smart Autosaving).

### Incomplete and incorrect `Ext.Mod` documentation

- ExtIdeHelpers: `GetMod(modGuid: FixedString): Module`
- API.md: Documents `GetModInfo(modGuid)`
The helper return type `Module` contains specific fields (`Info`, `Dependencies`) that are not detailed in API.md.
API.md does not cover `GetModManager():ModManager`.
### Document difference between timer methods

```lua
WaitFor fun(a1:number, a2:Ref, a3:number?):uint64
WaitForPersistent fun(a1:number, a2:FixedString, a3:Ref, a4:number?):uint64
WaitForRealtime fun(a1:number, a2:Ref, a3:number?):uint64
```
From Norbyte:
> `WaitFor` uses game clock, `WaitForRealtime` uses OS clock; most of the time they are the same, but there are cases when the game timer is paused and time doesn't "progress".
> Game timer can also be affected by the tick throttling logic if the framerate drops too low
> `WaitForPersistent` creates a persistent handle that is written to the savegame so your timer survives a save/reload.
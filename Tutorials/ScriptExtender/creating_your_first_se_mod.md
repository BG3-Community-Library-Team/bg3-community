---
title: Creating your first SE Mod
description: A follow along tutorial for creating your first Script Extender Mod that stops companions from returning to their tent when in camp. Optional toggleable version
published: false
date: 2024-05-04T11:31:03.361Z
tags: tutorial, guide, script extender, lua
editor: markdown
dateCreated: 2024-05-01T14:54:45.494Z
---

# Creating your first SE Mod

This tutorial will walk you through creating a simple Mod with Norbyte's Script Extender(SE).

We will create mod that stops your companions from going back to their tent once in camp.
Aditionally we will utilize SE together with `stats` to make this toggleable.

This tutorial is based on **Alithea Ancunín's** implementation of [Please Stay] (include link here)


> If you have not used SE before, you might want to have a look at [Getting started with Script Extender](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted)
{.is-info}



## 1. Outlining your strategy

- console time
- research all necessary functions
- research al necessary flags etc




## 2. Preparing your workspace

- change the meta file
- create all the files



## 3. Writing the code

```lua
-- variables

FLAG_IN_CAMP = "161b7223-039d-4ebe-986f-1dcd9a66733f"
```

```lua
-- methods

---@param character GUIDSTRING     - the character who will stop moving in camp
function stopMoving(character)
    if Osi.GetFlag(FLAG_IN_CAMP, character) == 1 then
        Osi.ClearFlag(FLAG_IN_CAMP, character)  
    end
end
```

```lua

---@param character GUIDSTRING     - the character who will start moving again in camp
function startMoving(character)
    if Osi.GetFlag(FLAG_IN_CAMP, character) == 0 then
        Osi.SetFlag(FLAG_IN_CAMP, character)
    end
end



```



## 4. Interdiscipline: Using stats file in conjunction with SE

### 4.1 Status


```
new entry "STAY_STILL_STATUS"
type "StatusData"
data "StatusType" "BOOST"
data "DisplayName" "h38fc0213b20a4412bf0f223aeda5a7e974a9"
data "Description" "hd5dfdb8b7aa34a808f628362b0f04fa8884a"
data "Icon" "Spell_Conjuration_DimensionDoor"
data "StackId" "STAY_STILL_STATUS"

```

### 4.2 Passive


```
new entry "STAY_STILL_PASSIVE"
type "PassiveData"
data "DisplayName" "h03652d052f114f8ebbc10bc2602cddc835e7"
data "Description" "h31d5cb6c31ed4d198231d44624caf7c59f5b"
data "Icon" "Spell_Conjuration_DimensionDoor"
data "Properties" "IsToggled;ToggledDefaultAddToHotbar"
data "ToggleOnFunctors" "ApplyStatus(STAY_STILL_STATUS,100,-1)"
data "ToggleOffFunctors" "RemoveStatus(STAY_STILL_STATUS)"


```


### 4.3 Localization File

```
<?xml version="1.0" encoding="utf-8"?>
<contentList>

    <!-- Toggle for entity to stay still in camp -->

    <content contentuid="h03652d052f114f8ebbc10bc2602cddc835e7" version="1">Stay still in Camp</content>
    <content contentuid="h31d5cb6c31ed4d198231d44624caf7c59f5b" version="1">When this is active, the companion will not move back to their tent while in camp</content>

    <!-- Passive Applied to entity when it is standing still -->

    <content contentuid="h38fc0213b20a4412bf0f223aeda5a7e974a9" version="1">Standing still</content>
    <content contentuid="hd5dfdb8b7aa34a808f628362b0f04fa8884a" version="1">Entity will not move back to Camp</content>
</contentList>

```



### 4.4 Using SE to Handle the Stats


```lua

---@param character GUIDSTRING     - the character receiving the passive
---@return passive - string         - the passive being added to the character
function addPassive(character, passive)
    if Osi.HasPassive(character, passive) == 0 then
        Osi.AddPassive(character, passive)
    end
end

```

```lua

-- Adds the "Stay in Camp" toggle to each partymember
Ext.Osiris.RegisterListener("LevelGameplayStarted", 2, "after", function(_, _)
    _P("LevelGameplayStarted")

    local party = Osi.DB_PartyMembers:Get(nil)
    for i = #party, 1, -1 do
        addPassive(party[i][1],"STAY_STILL_PASSIVE")
    end

end)
```


```lua

-- Adds the "Stay in Camp" toggle to a partymember added during gameplay
Ext.Osiris.RegisterListener("CharacterJoinedParty", 1, "after", function(character)
    addPassive(character,"STAY_STILL_PASSIVE")
end)

```


```lua
-- Stops the partymember from moving if "Stay Still" is activated and they are teleported to camp
Ext.Osiris.RegisterListener("TeleportedToCamp", 1, "after", function(character)
    _P("Teleported to camp")  
    if Osi.HasPassive(character, "STAY_STILL_PASSIVE") == 1 then
        _P("character has ", "STAY_STILL_PASSIVE")
        stopMoving(character)
    end
end)


```


```lua

-- Stops the partymember from moving if "Stay Still" is activated and they are already in camp
Ext.Osiris.RegisterListener("StatusApplied", 4, "after", function(character, status, _, _)
    if status == "STAY_STILL_STATUS" then
		stopMoving(character)
	end
end)

```


```lua

-- Allows the partymember to move again if "Stay Still" is deactivated
Ext.Osiris.RegisterListener("StatusRemoved", 4, "after", function (character, status, _, _)
	if status == "STAY_STILL_STATUS" then
		startMoving(character)
	end
end)


```



![yfsem_workspace_structure_final.png](/tutorials/your_first_se_mod/yfsem_workspace_structure_final.png)


Credits: 

*Alithea Ancunín* for the idea. Without her this would not exist.
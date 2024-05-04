---
title: Creating your first SE Mod
description: A follow along tutorial for creating your first Script Extender Mod that stops companions from returning to their tent when in camp. Optional toggleable version
published: false
date: 2024-05-04T11:26:38.208Z
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

![yfsem_workspace_structure_final.png](/tutorials/your_first_se_mod/yfsem_workspace_structure_final.png)


Credits: 

*Alithea Ancunín* for the idea. Without her this would not exist.
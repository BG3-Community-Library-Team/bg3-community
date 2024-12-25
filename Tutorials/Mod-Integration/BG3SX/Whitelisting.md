---
title: Whitelisting for BG3SX
description: 
published: false
date: 2024-12-25T09:22:38.863Z
tags: script extender, bg3sx, mod integration
editor: markdown
dateCreated: 2024-12-25T07:23:13.330Z
---

# BG3SX Whitelisting

> This Tutorial will walk you through the steps of intgegrationg your race mod, or character with **BG3SX**. An adult mod for Baldur's Gate 3.
> Please note that due to the adult nature of this mod, it is not linked in this tutorial.
{.is-info}

> ᛫ **BG3SX** and affiliated parties are not responsible for the content users decide to modify for usage with the mod. 
> ᛫ While we do not condone any inappropriate use of the mod, the reality is that we cannot control what you do on your on devices.
> ᛫ Mod responsibly
{.is-warning}


## 1 Whitelisting Basics
### 1.1 What is Whitelisting

In **Baldur's Gate 3 Modding** a popular mod type is [Race mods](https://www.nexusmods.com/baldursgate3/mods/categories/15/). 
When a race has been made compatible with **BG3SX**, we call it *Whitelisted* 

### 1.2 Why is Whitelisting necessary?

To prevent inappropriate actions and to stay compliant with Nexus Terms of Service, **BG3SX** only allows the vanilla medium and tall humanoid races.

Whitelisting allows other modders to add their races to the **BG3SX** system.

In addition, you can also use this system to *Blacklist* your mod.
For example if your race uses a non-default skeleton and is thus not compatible with any of your animations. See [link to script section]for more details.

*Blacklisting* always has a higher priority than *Whitelisting* to ensure author control.

### 1.3 How to tell if a mod uses Whitelisting?

Mod authors don't usually notify the development team of **BG3SX** about integration, so there is no list with Whitelisted races.

If you want to know if a race mod you are using is compatible with BG3SX, you want to check the description of the mod page and see if the author has added compatibility.

> If you want to ask about, or request compatibility, remember to be kind and accept if the author declines the request.
{.is-warning}

### 1.4 Is it possible to Whitelist a mod that you are using and you are not the creator of?

Yes. This is technically possible, but we encourage you to wait for the author to implement compatibility themselves. 

If you want to create a **BG3SX** patch for a mod that you are not the author of and you want to use it for your personal use, you can follow the guide and create the patch as an [optional addon](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#as-an-optional-addon). 

> **<ins>Personal use<ins>** **means that the file does not leave your computer!**
> **Do not share files that you did not get permission for creating.**
{.is-danger}


### 1.5 Can vanilla races be Whitelisted?

  Yes. Vanilla races can be Whitelisted just like any modded race.
  For this follow the guide for [optional addons](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#as-an-optional-addon). 
  
  Before sharing your vanilla Whitelist mod, make sure it is compliant with the Terms of Service of the website you want to publish it on. 
 
  
### 1.6 Can single characters be whitelisted?
  
  If you do not want to whitelist an entire race but only one character, for example **Withers**, but not all UNDEAD entities, or **Haarlep**, but not all FIEND entities, you can Whitelist specific characters. For this follow [insert link here]
  
## 2 Whitelisting Guides

### 2.1 How to Whitelist when you already have some modding experience.
  
  The following section shortly explain how to *Whitelist*/*Blacklist* your race or character when you already know the basics of creating a workspace and finding tags. If you need a detailed explanation, jump to [INSERT DETAILED EXPLANATION LINK HERE]#
  
  You can either *Whitelist*/*Blacklist* your race with a simple script, or by using the [Tag Framework Mod](https://www.nexusmods.com/baldursgate3/mods/6545) you cannot *Whitelist*/*Blacklist* single characters. For that follow [INSERT SINGLE CHARACTER GUIDE HERE]
 
  
  #### 2.1.1  With a script
  
  ##### 2.1.1.1 For races
  
  Add the following code snippet to your `BootstrapServer.lua` script:
 

```lua
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {}
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID]
  wList["TagName"] = {TAG = "TagUUID", Allowed = true}
end
```
  Replace `"TagName"` and `"TagUUID"` with the corresponding data.

  
  
  
```lua
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {}
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID]
  wList["MyCoolRaceTagName"] = {TAG = "413dcf04-586d-409f-aef1-1cf457711f5e", Allowed = true}
end
```
  
  
If your race has multiple tags, make sure to include all regular, and all "Really" tags
  
  
```lua
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {}
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID]
  wList["MyCoolRaceTagName"] = {TAG = "413dcf04-586d-409f-aef1-1cf457711f5e", Allowed = true}
  wList["MyCoolRaceTagName2"] = {TAG = "03d1fdaa-eb79-469c-a3b3-57a3b98fa484", Allowed = true}
  wList["MyCoolRaceTagName3"] = {TAG = "2e6b73f8-20cb-4515-b9aa-83531ee8fa96", Allowed = true}
end
```
  
  Similary, you can *Blacklist*  your race by setting `Allowed` to `false`
  You can also include an optional reason that will be shown in the error message.

  
```lua
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {} 
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID]
  wList["MyCoolRaceTagName"] = {TAG = "413dcf04-586d-409f-aef1-1cf457711f5e", Allowed = false, Reason = "YourMod - No fitting Genitals"}
  wList["MyCoolRaceTagName2"] = {TAG = "03d1fdaa-eb79-469c-a3b3-57a3b98fa484", Allowed = false, Reason = "YourMod - No Animations for Rig"}
end
  
```
  

##### 2.1.1.2 For single entities

  Add the following code snippet to your `BootstrapServer.lua` script:
  
```lua
  
if Mods.BG3SX then
  table.insert(Mods.BG3SX.Data.WhitelistedEntities, "characterUUID")
end

```
  
  Replace `"characterUUID"` with the uuid of the character you want to add
  
  ```lua
  
if Mods.BG3SX then
  -- Withers UUID
  table.insert(Mods.BG3SX.Data.WhitelistedEntities, "0133f2ad-e121-4590-b5f0-a79413919805")
end

```
  
#### 2.1.2  With the Tag Framework

Single character cannot be *Whitelisted/Blacklistes* with the [Tag Framework Mod](https://www.nexusmods.com/baldursgate3/mods/6545) and are only possible with a script
  
```json
  
"Tags": [
  {
    "modGuids": ["bfc31d95-8fd5-4bdc-a92b-ec3bfce13f86"],
    "Type": "Race",
    "Tag": "Ghouls_Dunmer_f34cadf5-ccfb-4e56-9596-356619569108",
    "ReallyTag": "REALLY_Ghouls_Dunmer_6a018dee-2f04-4bda-93c4-958422c3ed0a",
    "BG3SX_Support": {
      "Allowed": false,
      "Reason": "The MPAA are watching me type",
      "IncludeReally": true,
      "RaceModGuid": "bfc31d95-8fd5-4bdc-a92b-ec3bfce13f86"
      }
  },
  
```  
  
  Replcace x with y
  
  
```json
  
"Tags": [
  {
    "modGuids": ["bfc31d95-8fd5-4bdc-a92b-ec3bfce13f86"],
    "Type": "Race",
    "Tag": "Ghouls_Dunmer_f34cadf5-ccfb-4e56-9596-356619569108",
    "ReallyTag": "REALLY_Ghouls_Dunmer_6a018dee-2f04-4bda-93c4-958422c3ed0a",
    "BG3SX_Support": {
      "Allowed": false,
      "Reason": "The MPAA are watching me type",
      "IncludeReally": true,
      "RaceModGuid": "bfc31d95-8fd5-4bdc-a92b-ec3bfce13f86"
      }
  },
  
```  
  
### 2. Detailed Whitelisting guide

#### As a part of the main mod

#### As an optional addon
    
> Load the optional addon after BG3SX. If you are using the in game mod manager, don't
{.is-warning}

  
### 3. Custom Genitals
  
  -- sometimes races are not set up correctly so bpdytype 2 is actually not strong -> default to regular human peen and looks wird
  -- authors might want to use their custom penises.
  
Your content here


test content


  -- TODO: CHeck the optional addon link


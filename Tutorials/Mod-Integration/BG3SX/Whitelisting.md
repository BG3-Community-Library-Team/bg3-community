---
title: Whitelisting for BG3SX
description: 
published: false
date: 2024-12-25T08:14:50.801Z
tags: script extender, bg3sx, mod integration
editor: markdown
dateCreated: 2024-12-25T07:23:13.330Z
---

# BG3SX Whitelisting

> This Tutorial will walk you through the steps of intgegration your race mod with **BG3SX**, an adult mod for Baldur's Gate 3.
> Please note that due to the adult nature of this mod, it is not linked in this tutorial.
{.is-info}

## 1 Whitelisting Basics
### 1.1 What is Whitelisting

In **Baldur's Gate 3 Modding** a popular mod type is [Race mods](https://www.nexusmods.com/baldursgate3/mods/categories/15/). 
When a race has been made compatible with **BG3SX**, we call it *Whitelisted* 

### 1.2 Why is Whitelisting necessary?

To prevent inappropriate actions and to stay compliant with Nexus Terms of Service, **BG3SX** only allows the vanilla medium and tall humanoid races.

Whitelisting allows other modders to add their races to the **BG3SX** system.

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
  
  #### With a script
  
  Add this to your BootstrapServer.lua script:
(One entry per Tag you create that an entity might have (All regular AND "Really" Tags))

```lua
------------------------------------
-- BG3SX Compatibility
------------------------------------
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {} -- To declare that a new entry named after your Mods UUID will be an empty table
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID] -- Write 'ModuleUUID' to automatically fill in your mods UUID
  wList["TagName1"] = {TAG = "TagUUID1", Allowed = true} -- Set to true or false
  wList["TagName2"] = {TAG = "TagUUID2", Allowed = true}
  wList["TagName3"] = {TAG = "TagUUID3", Allowed = false, Reason = "YourMod - No fitting Genitals"} -- Optional reasons merge with regular error message
  wList["TagName3"] = {TAG = "TagUUID3", Allowed = false, Reason = "YourMod - No Animations for Rig"}
end
```

```lua
------------------------------------
-- For Animators/Genital creators
-- If you happen to create animations/genitals for races that might not had some before, you can manually edit race tag entry in our whitelist
------------------------------------
if Mods.BG3SX and Ext.Mod.GetMod(TheRaceModUUID) then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {}
  local wList = Mods.BG3SX.Data.ModdedTags[TheRaceModUUID]
  wList["TagName7"] = {TAG = "TagUUID2", Allowed = true} -- You may have created genitals for them
  wList["TagName2"] = {TAG = "TagUUID3", Allowed = true} -- Or animations
end
```

    -- for single entities





```
  
  ### With the Tag Framework

  -- for races
  
  -- single entity whitelisting is not possible with tag framework
  

  
  
  The [Tag Framework Mod](https://www.nexusmods.com/baldursgate3/mods/6545) now has BG3SX Support, so if you are using it for your custom race mod, you can enable a check for every tag you create to include it in our mod automatically.
```lua
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
  
  
  
### 2. Detailed Whitelisting guide

#### As a part of the main mod

#### As an optional addon
    

  
### 3. Custom Genitals
  
  -- sometimes races are not set up correctly so bpdytype 2 is actually not strong -> default to regular human peen and looks wird
  -- authors might want to use their custom penises.
  
Your content here


test content




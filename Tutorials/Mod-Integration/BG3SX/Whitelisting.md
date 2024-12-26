---
title: Whitelisting for BG3SX
description: 
published: false
date: 2024-12-26T20:05:05.351Z
tags: script extender, bg3sx, mod integration
editor: markdown
dateCreated: 2024-12-25T07:23:13.330Z
---

# BG3SX Whitelisting

> This Tutorial will walk you through the steps of integrating your race mod, or character with **BG3SX**. An adult mod for Baldur's Gate 3.
> Please note that due to the adult nature of this mod, it is not linked in this tutorial.
{.is-info}

> ᛫ **BG3SX** and affiliated parties are not responsible for the content users decide to modify for usage with the mod and may distribute via various media types on other platforms. 
> ᛫ While we do not condone any inappropriate use of the mod, the reality is that we cannot control what you do on your own devices.
> ᛫ Mod responsibly
{.is-warning}


## 1 Whitelisting Basics
### 1.1 What is Whitelisting

In **Baldur's Gate 3 Modding** a popular mod type is [Race mods](https://www.nexusmods.com/baldursgate3/mods/categories/15/). 
When a race has been made compatible and is allowed to be used with **BG3SX**, we call it *Whitelisted* 

### 1.2 Why is Whitelisting necessary?

To prevent inappropriate actions and to stay compliant with Nexus Terms of Service, **BG3SX** only allows the vanilla medium and tall humanoid races.

Whitelisting allows other modders to add their races to the **BG3SX** system.

In addition, you can also use this system to *Blacklist* your mod.
For example if your race uses a non-default skeleton and thus may not be compatible with any of the BG3SX default/any Addons animations. See [link to script section]for more details.

*Blacklisting* always has a higher priority than *Whitelisting* to ensure author control.

### 1.3 How to tell if a mod uses Whitelisting?

Mod authors don't usually notify the development team of **BG3SX** about integration, so there is no list of Whitelisted races.

If you want to know if a race mod you are using is compatible with BG3SX, you want to check the description of the mod page and see if the author has added a note about compatibility or an optional file to download.

> If you want to ask about, or request compatibility, remember to be kind and accept if the author declines the request.
{.is-warning}

### 1.4 Is it possible to Whitelist a mod that you are using and you are not the creator of?

Yes. This is technically possible, but we encourage you to wait for the author to implement compatibility themselves. 

> If a mod author does not want to implement compatibility for BG3SX, please respect their decision and do not share screenshots or other content of their character/race in a sexual context.
{.is-warning}


If you want to create a **BG3SX Whitelist** patch for a mod that you are not the author of and you want to use it for your personal use, you can follow the guide and create the patch as an [optional addon](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#as-an-optional-addon). 

> **<ins>Personal use<ins>** **means that the file does not leave your computer!**
> **Do not share files that you did not get permission for creating.**
> **If you want to share it, get the authors permission first!**
{.is-danger}

### 1.5 Can vanilla races be whitelisted?

  Yes. Vanilla races can be Whitelisted just like any modded race.
  For this follow the guide for [optional addons](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#as-an-optional-addon). 
  
  Before sharing your vanilla Whitelist mod, make sure it is compliant with the Terms of Service of the website you want to publish it on. 
 
  
### 1.6 Can individual characters be white-/blacklisted?
  
  If you do not want to whitelist an entire race but only one character, for example **Withers**, but not all UNDEAD entities, or **Haarlep**, but not all FIEND entities, you can Whitelist specific characters. For this follow [insert link here]
  
  In the same vein, modders who create a custom NPCs, can also just as much blacklist them individually if they want to.
  
## 2 Whitelisting Guides

>  Do you learn information better by trying things out yourself?
> Download the [**Example race mod with BG3SX support** or the **Example race mod with optional BG3SX addon**](https://www.nexusmods.com/baldursgate3/mods/14435?tab=description) to see what a correct implementation looks like.
{.is-info}

  
### 2.1 How to Whitelist when you already have some modding experience.
  
  The following section shortly explain how to *Whitelist*/*Blacklist* your race or character when you already know the basics of creating a workspace and finding tags. If you need a detailed explanation, jump to [INSERT DETAILED EXPLANATION LINK HERE]#
  
  You can either *Whitelist*/*Blacklist* your race with a simple script, or by using the [Tag Framework Mod](https://www.nexusmods.com/baldursgate3/mods/6545).
  Keep in mind that if you are using it, you cannot automatically also *Whitelist*/*Blacklist* single characters.
  This still needs to be done manually - For that follow [INSERT SINGLE CHARACTER GUIDE HERE]
 
  
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
  wList["REALLY_MyCoolRaceTagName2"] = {TAG = "2e6b73f8-20cb-4515-b9aa-83531ee8fa96", Allowed = true}
end
```
  
  Similary, you can *Blacklist*  your race by setting `Allowed` to `false`
  You can also include an optional reason that will be shown in an error message, both On-Screen and the console.

  
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
    "modGuids": ["YourModGUID"],
    "Type": "Race",
    "Tag": "YourRaceTag",
    "ReallyTag": "YourReallyRaceTag",
  },
  
```  
  
  Add the `BG3SX_Support section
  
```json
  
"Tags": [
  {
    "modGuids": ["YourModGUID"],
    "Type": "Race",
    "Tag": "YourRaceTag",
    "ReallyTag": "YourReallyRaceTag",
    "BG3SX_Support": {
      "Allowed": true_or_false,
      "Reason": "Your Reason",
      "IncludeReally": true,
      "RaceModGuid": "YourModGUID"
      }
  },
  
```  
  
  Replace the following content: 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"YourModGUID"` with the UUID of your mod
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"YourRaceTag"` with the UUID of your race tag
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"YourReallyRaceTag"` with the UUID of your really race tag
  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`true_or_false` with true if you want to allow BG3SX support
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`true_or_false` with false if you want to disallow BG3SX support
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"Reason"` with your custom reason for your decision
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"YourModGUID"` with the UUID of your mod (same as above)
  
  

  
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

If your mod does not have any ScriptExtender content yet, you want to add the necessary folders and files to your mod.
  
> Don't want to create the files yourself? 
> Download the Script Extender sample mod [here], drag the `ScriptExtender` folder to the correct location and modify the files
{.is-info}

  
Create a `ScriptExtender` folder in your `ModName` folder in `Mods` where your `meta.lsx` file is located.
 
  
[insert image here]
  
In your `ScriptExtender` folder, create a `Lua` folder and a `Config.json` file.
  
> On windows, the file extensions are hidden by default.
> This causes files to sometimes be created as "Filename.json.txt"
> To make sure you create the correct file extension, we suggest [you enable "File Extensions"](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/) 
{.is-info}

  
[Insert image here]
  
  
Edit your `Config.json` file.
  
The Required Version is the minimum version of Script Extender your mod requires.
This is usually irrelevant for most mods. If you are unsure which version to use here, use the version that **BG3SX** uses.
Version `1.4.9` requires ScriptExtender version `21`.
  
Replace `"YourCoolModName"` with your mod name.

```json  
  
{
    "RequiredVersion": 21,
    "ModTable": "YourCoolModName",
    "FeatureFlags": ["Lua"]
}
  
  ```
  
In your `Lua` folder, create a `BootstrapServer.lua` file.
  
[insert image here]
  
  
  
  
#### As an optional addon
    
> Load any optional Whitelist addon **AFTER** BG3SX. If you are using the in game mod manager, we advise you to use [BG3MM](https://github.com/LaughingLeader/BG3ModManager/releases) instead as the in game Mod Manager does not allow you to reorder your mods.
{.is-warning}

  
### 3. Custom Genitals
  
  -- sometimes races are not set up correctly so bpdytype 2 is actually not strong -> default to regular human peen and looks wird
  -- authors might want to use their custom penises.
  
Your content here


test content


  -- TODO: CHeck the optional addon link


  
  
  
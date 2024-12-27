---
title: Whitelisting for BG3SX
description: 
published: false
date: 2024-12-27T12:27:16.927Z
tags: script extender, bg3sx, mod integration
editor: markdown
dateCreated: 2024-12-25T07:23:13.330Z
---


> This Tutorial will walk you through the steps of integrating your race mod, or character with **BG3SX**. An adult mod for Baldur's Gate 3.
> Please note that due to the adult nature of this mod, it is not linked in this tutorial.
{.is-info}

> ᛫ **BG3SX** and affiliated parties are not responsible for the content users decide to modify for usage with the mod and may distribute via various media types on other platforms. 
> ᛫ While we do not condone any inappropriate use of the mod, the reality is that we cannot control what you do on your own devices.
> ᛫ Mod responsibly
{.is-warning}


# 1. Whitelisting Basics
## 1.1 What is Whitelisting

In **Baldur's Gate 3 Modding** a popular mod type is [Race mods](https://www.nexusmods.com/baldursgate3/mods/categories/15/). 
When a race has been made compatible and is allowed to be used with **BG3SX**, we call it *Whitelisted* 

## 1.2 Why is Whitelisting necessary?

To prevent inappropriate actions and to stay compliant with Nexus Terms of Service, **BG3SX** only allows the vanilla medium and tall humanoid races.

Whitelisting allows other modders to add their races to the **BG3SX** system.

In addition, you can also use this system to *Blacklist* your mod.
For example if your race uses a non-default skeleton and thus may not be compatible with any of the BG3SX default/any Addons animations. See [The script section](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-21-with-a-script) for more details.

*Blacklisting* always has a higher priority than *Whitelisting* to ensure author control.

## 1.3 How to tell if a mod uses Whitelisting?

Mod authors don't usually notify the development team of **BG3SX** about integration, so there is no list of Whitelisted races.

If you want to know if a race mod you are using is compatible with BG3SX, you want to check the description of the mod page and see if the author has added a note about compatibility or an optional file to download.

> If you want to ask about, or request compatibility, remember to be kind and accept if the author declines the request.
{.is-warning}

## 1.4 Is it possible to Whitelist a mod that you are using and you are not the creator of?

Yes. This is technically possible, but we encourage you to wait for the author to implement compatibility themselves. 

> If a mod author does not want to implement compatibility for BG3SX, please respect their decision and do not share screenshots or other content of their character/race in a sexual context.
{.is-warning}


If you want to create a **BG3SX Whitelist** patch for a mod that you are not the author of and you want to use it for your personal use, you can follow the guide and create the patch as an [optional addon](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-32-as-an-optional-addon). 

> **<ins>Personal use<ins>** **means that the file does not leave your computer!**
> **Do not share files that you did not get permission for creating.**
> **If you want to share it, get the authors permission first!**
{.is-danger}

## 1.5 Can vanilla races be whitelisted?

  Yes. Vanilla races can be Whitelisted just like any modded race.
  For this follow the guide for [optional addons](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-32-as-an-optional-addon). 
  
  Before sharing your vanilla Whitelist mod, make sure it is compliant with the Terms of Service of the website you want to publish it on. 
 
  
## 1.6 Can individual characters be white-/blacklisted?
  
  If you do not want to whitelist an entire race but only one character, for example **Withers**, but not all UNDEAD entities, or **Haarlep**, but not all FIEND entities, you can Whitelist specific characters. For this follow [the section for single entities](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-212-for-single-entities)
  
Modders who create a custom NPCs, can also just blacklist them individually if they want to.
  
  
# 2. How to Whitelist - Short Explanation
  
> Do you learn information better by trying things out yourself?
> Download the [**Example race mod with BG3SX support** or the **Example race mod with optional BG3SX addon**](https://www.nexusmods.com/baldursgate3/mods/14435?tab=description) to see what a correct implementation looks like.
{.is-info}  

  
  The following section shortly explain how to *Whitelist*/*Blacklist* your race or character when you already know the basics of creating a workspace with SE functionality. If you need a detailed explanation jump to [the detailed guide here](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-3-detailed-whitelisting-guide)
  
  You can either *Whitelist*/*Blacklist* your race with a simple script, or by using the [Tag Framework Mod](https://www.nexusmods.com/baldursgate3/mods/6545).
  Keep in mind that the Tag Framework mod only supports races, not single characters.


  ## 2.1  With a script
  
  ### 2.1.1 For races
  
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
  You can also include an optional reason that will be shown in an error message, both on-screen and in the console.

  
```lua
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {} 
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID]
  wList["MyCoolRaceTagName"] = {TAG = "413dcf04-586d-409f-aef1-1cf457711f5e", Allowed = false, Reason = "YourMod - No fitting Genitals"}
  wList["MyCoolRaceTagName2"] = {TAG = "03d1fdaa-eb79-469c-a3b3-57a3b98fa484", Allowed = false, Reason = "YourMod - No Animations for Rig"}
end
  
```
  

### 2.1.2 For single entities

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

  For *Blacklisting* use `Data.BlacklistedEntities` instead of `Data.WhitelistedEntities`
  
  
## 2.2  With the Tag Framework

Single character cannot be *Whitelisted/Blacklistes* with the [Tag Framework Mod](https://www.nexusmods.com/baldursgate3/mods/6545) and are only possible with a script.
  
  For single entities see the section [here](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-212-for-single-entities)
  
  
Create your `TagFrameworkConfig.json` as explained in the [Tag Framework guide](https://github.com/BG3-Community-Library-Team/TagFramework/wiki)   
  
```json
  
"Tags": [
  {
    "modGuids": ["YourModGUID"],
    "Type": "Race",
    "Tag": "YourRaceTag",
    "ReallyTag": "YourReallyRaceTag",
  },
  
```  
  
  Add the `BG3SX_Support` section
  
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
  
# 3. Detailed Whitelisting guide

> This tutorial assumes you know a few basics about mod creation.
> If you are not familiar with the basics of creating, or paking a mod, We recommend you have a look at one of our other [Tutorials](https://wiki.bg3.community/en/Tutorials) first.
{.is-success}

  
>   If at any point it looks like your changes don't do anything, verify that your changes are saved and the newest version of your mod is loaded.
{.is-warning}

  
## 3.1 As a part of the main mod
  
> If you implement the whitelisting directly in your mod, make sure your users load it **AFTER** BG3SX. We advise you recommend them to use [BG3MM](https://github.com/LaughingLeader/BG3ModManager/releases) instead of the in game mod manager, as the latter does not allow you to reorder your mods.
>
> ![loadorder.png](/tutorials/bg3sx/loadorder.png)
{.is-warning}


### 3.1.1 Create all folders and files
  
If your mod does not have any ScriptExtender content yet you want to add the necessary folders and files to your mod.
  
> Don't want to create the files yourself? 
> Download the Script Extender sample mod [here](https://www.nexusmods.com/baldursgate3/mods/14435), drag the `ScriptExtender` folder to the correct location and modify the files
{.is-info}

  
Create a `ScriptExtender` folder in your `ModName` folder in `Mods` where your `meta.lsx` file is located.

```
project-folder/
│
├── Localization/
│
├── Mods/
│   └── YourModName
│ 			│   
│  	 	├── ScriptExtender/
│   		└── meta.lsx
|
└── Public

```
  
  <br>
  
<div style="text-align: center;">
  <img src="/tutorials/bg3sx/creatingsefolder.png" alt="Creating SE Folder" width="300" height="700">
</div>

  <div style="text-align: center;">
Creating a ScriptExtender folder.
</div>

  
  <br>
  
  

  
In your `ScriptExtender` folder, create a `Lua` folder and a `Config.json` file.
  
  
```
project-folder/
│
├── Localization/
│
├── Mods/
│   └── YourModName
│      	│ 
│  	  	├── ScriptExtender/
│ 		 	│  	 │ 
│  			│ 		├── Lua/
│  			│		 └── config.json
│ 			 │ 
│   		 └── meta.lsx
|
└── Public

```
  
> On windows, the file extensions are hidden by default.
> This causes files to sometimes be created as "Filename.json.txt"
> To make sure you create the correct file extension, we suggest [you enable "File Extensions"](https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/) 
{.is-info}

  
<br>
  
<div style="text-align: center;">
  <img src="/tutorials/bg3sx/creatingluafolder.png" alt="Creating Lua Folder" width="300" height="700">
</div>

  <div style="text-align: center;">
Creating a Lua folder and Config.json.
</div>

  
<br>
  
  
  
Edit your `Config.json` file.
  
The Required Version is the minimum version of Script Extender your mod requires.
This is usually irrelevant for most mods. If you are unsure which version to use here, use the version that **BG3SX** uses.
**BG3SX** Version `1.4.9` requires ScriptExtender version `21`.
  
Replace `"YourCoolModName"` with your mod name.

```json  
  
{
    "RequiredVersion": 21,
    "ModTable": "YourCoolModName",
    "FeatureFlags": ["Lua"]
}
  
  ```
  
  

 
  

In your `Lua` folder, create a `BootstrapServer.lua` file and add a print statement so you can check if you have done everything correctly.
  

   ```
project-folder/
│
├── Localization/
│
├── Mods/
│   └── YourModName
│      	│ 
│  	  	├── ScriptExtender/
│ 		 	│  	 │ 
│  			│ 		├── Lua/
│  			│		 │	  └── BootstrapServer.lua
│			  │     │
│  			│		 └── config.json
│ 			 │ 
│   		 └── meta.lsx
|
└── Public

```
  
```lua
  
print("MyModName has been loaded succesfully")
  ```
  

<br>
  
<div style="text-align: center;">
  <img src="/tutorials/bg3sx/whitelisting/creatingbootstrap.png" alt="Creating BS" width="450" height="700">
</div>

  <div style="text-align: center;">
Creating a BootstrapServer.lua file.
</div>

  
<br>
  

You can start the game and load a save to check if your changes were successfull.
  
  ![successfullload.png](/tutorials/bg3sx/successfullload.png)
  
> A more detailed guide for those who are new to ScriptExtender can be found [here](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted)  
{.is-info}

  
### 3.1.2 Gather your tag names and uuids
  
  There are two ways of accessing the data you need to whitelist a race. 
  Either by directly getting them from the mod files, or by checking the **BG3SX** error log.
  
#### 3.1.2.1 By checking your mod files
  
Since you are the author, you probably know where you added the race tags. 
This is usually done in the `Races.lsx` file in `Public\YourModName\Races\Races.lsx`
  
  ![races.lsx.png](/tutorials/bg3sx/races.lsx.png)

This lists all of the Tags you have added to the race.
If they are custom tags, they are disallowed by default.
  
  
  ![raceslsxtags.png](/tutorials/bg3sx/raceslsxtags.png)

  
If you have created custom Tags, you usually find them in the `someTag.lsx` file in `Public\YourModName\Tags\someTag.lsx`  
  
  ![tags.png](/tutorials/bg3sx/tags.png)
  
  
  ![tagexample.png](/tutorials/bg3sx/tagexample.png)

  
Make a note of all your Tag `Name` and `UUID`  
  
  #### 3.1.2.2 By using the BG3SX error code
  
  Non-whitelisted races do not get the ability to use BG3SX content. 
  To trigger the error message, use an allowed character, like any of the companions and attempt an action on the non-whitelisted race.
  
  For example: Select Astarion in your Party. Choose the BG3SX action on the non-whitelisted character. You will now see an error message pop up.
  
![checkfailedondisallowed1.png](/tutorials/bg3sx/checkfailedondisallowed1.png)
  
This message tells you that the race `BG3SX_Example_Whitelisting_Race_Player` with the character UUID `"79ce94d1-2423-8cb6-0b17-af7ce8026069"` has failed the whitelist check because it has a tag with the Name `DISALLOWED1` with the UUID `"2105a2d9-e7ec-4a3f-91ba-a3c548713306"`
  
This data will also be printed in your ScriptExtender console for easy copying.
  
![checkfailedondisallowed1console.png](/tutorials/bg3sx/checkfailedondisallowed1console.png)
 
 Make a note of your Tag `Name` and `UUID`. In this case this would be:
Name `DISALLOWED1` with UUID `"2105a2d9-e7ec-4a3f-91ba-a3c548713306"`
  
After whitelisting one Tag, you might get another error message with another non-whitelisted Tag. So repeat this process until no error messages appear anymore.  
  

### 3.1.2. Whitelist your Tags

  Now follow the previous section [Whitelisting with a script](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-21-with-a-script) and enter all of your tags.
  
```lua  
if Mods.BG3SX then
  Mods.BG3SX.Data.ModdedTags[ModuleUUID] = {}
  local wList = Mods.BG3SX.Data.ModdedTags[ModuleUUID]
  wList["DISALLOWED1"] = {TAG = "2105a2d9-e7ec-4a3f-91ba-a3c548713306", Allowed = true}
  wList["DISALLOWED2"] = {TAG = "bf7fec70-5973-48c6-9d48-7cbe5c9d5035", Allowed = true}
  wList["DISALLOWED3"] = {TAG = "da356c64-8194-45d0-9fc9-6fd72f1eb207", Allowed = true}
end
```   
  
Your race is now allowed to use BG3SX actions.
  
## 3.2 As an optional addon
    
If you want BG3SX support to be optional, you can create a small mod that whitelists your race.
For this, simply create a new mod. We recommend you download the [BG3SX_Addon_For_Incompatible_ExampleRace](https://www.nexusmods.com/baldursgate3/mods/14435) and modify it.
Don't forget to change the UUID in the `meta.lsx` file!

Then you can follow the previous section from [Gather your tag names and uuids](https://wiki.bg3.community/en/Tutorials/Mod-Integration/BG3SX/Whitelisting#h-312-gather-your-tag-names-and-uuids)
  
> Load any optional Whitelist addon **AFTER** BG3SX. If you are using the in game mod manager, we advise you to use [BG3MM](https://github.com/LaughingLeader/BG3ModManager/releases) instead as the in game Mod Manager does not allow you to reorder your mods.
>
> ![screenshot_from_2024-12-27_12-47-17.png](/tutorials/bg3sx/screenshot_from_2024-12-27_12-47-17.png)
{.is-warning}
  
  
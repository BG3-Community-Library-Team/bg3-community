---
title: Creating Custom Animations
description: Tutorial on how to create custom animations
published: false
date: 2024-10-26T02:19:31.349Z
tags: animation
editor: markdown
dateCreated: 2024-10-20T16:06:19.163Z
---

> This is a Work in Progress Tutorial
{.is-warning}

# **Terminology**

- Template
	- A given entities or races RootTemplate
- Animationbank
	- What holds an actual animations data
- AnimationID
	- An ID (UUID) you set for a given animation in its AnimationBank
- MapKey
	- A UUID go link up with an AnimationID to call the animation
- AnimationSet
	- A list of MapKey/AnimationID links
- Waterfall
	- A list of AnimationSets on a Template
- AnimationSetOverride
	- An On-Demand Override of the Waterfall by inserting an AnimationSet with a higher priority

# **Creating Custom Animations**

In this tutorial we will go over every step of creating custom animations: (Non-Toolkit step-by-step)
- Creating an animation in Blender.
- Converting an animation for BG3.
- Creating the necessary links in VSCode.
- Implementing AnimationSets/Waterfalls and Overrides

## 1\. Creating an animation in Blender 
### **1.1\. Setup**

**Required software and Add-on**

[Blender](https://www.blender.org/download/releases/3-6/) – free open-source software for 3D modeling and animation. Recommended version is 3.6 as this the latest version the add-on was created for.

[BG3/DOS2 Collada Exporter for Blender 3.6](https://github.com/Norbyte/dos2de_collada_exporter) - An addon for Blender that allows you to import and export DAE/GR2 files for Baldur's Gate 3.

[Lune's BG3 Blender Animation Template.](https://www.nexusmods.com/baldursgate3/mods/5494)  

This tutorial assumes you have some basic knowledge of how to navigate the Blender interface. If you have no experience at all in Blender I recommend the classic [“How to Create a Donut”](https://www.youtube.com/watch?v=B0J27sf9N1Y) tutorial series by Blender Guru, which has been updated for the latest version of Blender.

This tutorial won’t get into the “why” you’re doing what you’re doing too much as the intent is to get you from the template to an animation quickly.  Also there are many different ways to accomplish the same task – the instructions below are simply easier to convey. Over time you will (and should) discover shortcuts and more efficient ways of accomplishing the same task. Control+Z is the undo short cut. You’ll probably wear those keys out if you get into animating.


### **1.2\. Creating an animation**
\[Insert Animation Tutorial here]

### **1.3\. How to correctly save your animation**
\[What to do to only select a given animation and only save that animation and not the entire model/rig]


## 2\. Converting an animation for BG3
### **2.1\. Using LSLib**
\[Using LSLib part about how to convert Blender Animations to a correct GR2 file with fitting Rig assigned]

### **2.2\. Sidenote: Converting BG3 Animations to Blender**
\[Using LSLib and Noesis Part about how to convert BG3 Animations to Blender]


## 3\. Creating the necessary links in VSCode
### **3.1\. Folder Structure**
The general path to use is:

- Public
	- YourModName
  		- Content
    		- Assets
      			- Characters
      				- Humans
          				- [PAK]_Male_Cine
            				- _merged.lsf
		- WhateverNameYouWant - Here You can place your .GR2 files
 		- Stats - Where you might have some spells

### **3.2\. AnimationBank**


### **3.2\. AnimationSet**


## 4\. Implementing AnimationSets/Waterfalls and Overrides
### **4.1\. AnimationSets**


### **4.2\. Waterfalls**


### **4.3\. Overrides**






## **X.0\. Useful Resources**

**_Norbyte_**

Norbytes search engine: [_https://bg3.norbyte.dev/_](https://bg3.norbyte.dev/) - Can give you information about existing animations

Script Extender: [_https://github.com/Norbyte/bg3se/tree/main_](https://github.com/Norbyte/bg3se/tree/main)

SE API Documentation: [_https://github.com/Norbyte/bg3se/blob/main/Docs/API.md_](https://github.com/Norbyte/bg3se/blob/main/Docs/API.md)

SE IDE Helpers: [_https://github.com/Norbyte/bg3se/blob/main/BG3Extender/IdeHelpers/ExtIdeHelpers.lua_](https://github.com/Norbyte/bg3se/blob/main/BG3Extender/IdeHelpers/ExtIdeHelpers.lua)

LsLib: [_https://github.com/Norbyte/lslib_](https://github.com/Norbyte/lslib)

**_Ghostboats & khbsd_**

BG3 Mod Helper VSCode extension: [_https://wiki.bg3.community/en/Tools/bg3-mod-helper_](https://wiki.bg3.community/en/Tools/bg3-mod-helper)

**_FallenStar_**

FallenStar’s VSCode extension: [_https://marketplace.visualstudio.com/items?itemName=FallenStar.bg3-se-snippets_](https://marketplace.visualstudio.com/items?itemName=FallenStar.bg3-se-snippets)

**_LaughingLeader_**

BG3MM: [_https://github.com/LaughingLeader/BG3ModManager_](https://github.com/LaughingLeader/BG3ModManager)

Osi functions: [_https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua_](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua)

Osi Events: [_https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua_](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua)

**_Larian Studios_**

Osiris: [_https://docs.larian.game/Osiris_](https://docs.larian.game/Osiris)



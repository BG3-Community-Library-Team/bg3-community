---
title: Creating Custom Animations
description: Tutorial on how to create custom animations
published: false
date: 2024-10-20T16:09:11.625Z
tags: animation
editor: markdown
dateCreated: 2024-10-20T16:06:19.163Z
---

> This is a Work in Progress Tutorial
{.is-warning}


# **Creating Custom Animations**

In this tutorial we will go over every step of creating custom animations: (Non-Toolkit step-by-step)
- Creating an animation in Blender.
- Converting an animation for BG3.
- Creating the necessary links in VSCode.

## 1\. Creating an animation in Blender 
### **1.1\. Setup**

To start things out, downloading an existing template is adviced. There may be another section later down the line about how to make your own.
One such presets: [Lune's BG3 Blender Animation Template](https://www.nexusmods.com/baldursgate3/mods/5494)

Here you can try yourself at posing and creating a first animation.

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


### **3.3\. Waterfall**




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



---
title: Creating Custom Animations
description: Tutorial on how to create custom animations
published: false
date: 2024-12-17T18:50:35.958Z
tags: animation
editor: markdown
dateCreated: 2024-10-20T16:06:19.163Z
---

> This is a Work in Progress Tutorial
{.is-warning}

# **BG3 Related Terminology**

- **Template** - A given entities or races RootTemplate which gets loaded when the game starts
- **Animationbank** - Like a template for entities but for an animation (includes attributes like the duration or the path of your animation file)
- **AnimationID** - An ID (UUID) you set for a given animation in its AnimationBank
- **MapKey** - A UUID go link up with an AnimationID to call the animation
- **AnimationSet** - A list of MapKey/AnimationID links
- **Waterfall** - A list of AnimationSets on a Template
- **AnimationSetOverride** - An On-Demand Override of the Waterfall by inserting an AnimationSet with a higher priority

# **Creating Custom Animations**

In this tutorial we will go over every step of creating custom animations: (Non-Toolkit step-by-step)
- Creating an animation in Blender.
- Converting an animation for BG3.
- Creating the necessary links in VSCode.
- Implementing AnimationSets/Waterfalls and Overrides

## 1\. Creating an animation in Blender 
### **1.1\. Setup**

**Required software and Add-on**

[Blender](https://www.blender.org/download/releases/3-6/) – free open-source software for 3D modeling and animation. Recommended version is 3.6 as this is the latest version the add-on was created for.

[BG3/DOS2 Collada Exporter for Blender 3.6](https://github.com/Norbyte/dos2de_collada_exporter) - An addon for Blender that allows you to import and export DAE/GR2 files for Baldur's Gate 3.

[Lslib](https://github.com/Norbyte/lslib/releases) – a tool by Norbyte for manipulating Baldur's Gate 3 files.

[Animation Template with BG3 IK Animation Rigs](https://www.nexusmods.com/baldursgate3/mods/14077)  

> This tutorial assumes you have some basic knowledge of how to navigate the Blender interface. If you need a refresher you can refer to the ["Interface Overview"](https://www.youtube.com/watch?v=8XyIYRW_2xk) by the Blender Foundation. If you have no experience at all in Blender I recommend the classic [“How to Create a Donut”](https://www.youtube.com/watch?v=B0J27sf9N1Y) introductory tutorial series by Blender Guru, which has been updated for the latest version of Blender.
{.is-info}


This tutorial won’t get into the “why” you’re doing what you’re doing too much as the intent is to get you from the template to an animation quickly.  Also there are many different ways to accomplish the same task – the instructions below are simply easier to convey. Over time you will (and should) discover shortcuts and more efficient ways of accomplishing the same task. Control+Z is the undo short cut.

Some animation specific terminology you may hear often :

- **A model / mesh** – is a 3D object. It can be anything from a simple sphere to a human or a spaceship. The model itself can’t be turned into an animation unless it has..

- **A rig** – this is basically the “bones” of the 3D object and allows you to control and manipulate it in space. A rig can be as simple as one bone to move a sphere, or dozens of bones on a face to create different expressions.



### **1.2\. Creating an animation**
A relatively quick [YouTube tutorial](https://www.youtube.com/watch?v=GAIZkIfXXjQ) on the basics of Blender's animating functions and UI - **highly** recommended to watch first, if you are not yet familiar with it.

#### Tutorial for working with the IK rigs from Nexus
[Video tutorial](https://drive.google.com/file/d/1hBugCboET8Zxn_rSyC2wo1AZjahSJFKM/view?usp=sharing)![animation_thumbnail.png](/animation_tutorial/animation_thumbnail.png)
Once you have opened the animation template, you will see rigs for 4 different body types. Each body type has a control rig (CR) and a skeleton rig (SK). The control rig is meant for animating on, and serves a puppeteering function for the skeleton rig. The skeleton is where you would bake the animation in the end and what you export out of Blender back into the game.

Make sure you’re in pose mode. We recommend using auto-keying if you’re going to animate manually (so that keyframes are inserted automatically whenever you move/rotate/scale a bone), but remember when it is enabled and disable it if necessary.

Set 30 FPS for the framerate. With the settings we'll be using, any animation you make regardless of the framerate in Blender will play at 30 FPS in the game. Therefore, it is best to set it to 30 FPS in Blender, as this will allow you to render it out later to see how fast or slow your animation is.

Keep it the starting frame of the animation (your frame range) at 0 and not 1, this is the correct setting for animations to be exported to BG3.

All of the rigs are facing in the positive Y direction, and are mirrored, so the limbs you perceive to be on the left are named right, and so on. This is intentional (and is due to Blender's axis mismatch with the game's engine), and any animation you make on them will be mirrored in-game, so keep that in mind.

> Knowing how to manage keyframes will be a big part of your animation process. For more information on the basics of keyframing in Blender refer to ["Keyframe Fundamentals"](https://www.youtube.com/watch?v=SZJswvw9wEs) by the Blender Foundation. The version of blender they use is dated but the core concepts still apply. For a tutorial that uses more recent versions of Blender you can refer to ["Tutorial: Blender Keyframes For Beginners"](https://www.youtube.com/watch?v=8gi9lUYMRcI) by PIXXO 3D.
{.is-info}

#### Additional useful tutorials on Blender's animating functions:

[AnimAide](/https://github.com/augmero/animaide/tree/blender4_fixes) (free Blender animation addon, version for 4.0+), [YouTube tutorial](/https://www.youtube.com/watch?v=r-rFLLkycxI) on AnimAide
[YouTube Tutorial](/https://www.youtube.com/watch?v=mfdufhaiKtI) on Blender's Non-Linear Animation (layered animation) Editor
[Animation Layers](/https://blendermarket.com/products/animation-layers) (paid Blender animation addon)

  


### **1.3\. How to correctly bake and export your animation**
When you’re done with your animation or want to test it in progress, you’ll need to export it in a format that can be converted into the modeling / animation format used by BG3 -  “.gr2”. 

To get there you’ll need to :

- Export the rigged animation into a .dae format.
- Use the lslib tool to convert that file into .gr2

When exporting it’s important to remember that you only want to export the skeleton rig, not the control rig or any of the meshes. For that reason it's also important to remember that while you do your animating on the control rig, the skeleton does not receive any keyframes, it's being constrained (puppeteered) by the control rig. To bake keyframes on the skeleton, you need to Bake the Action on it before exporting. (This is also explained in tutorial video on the template.)

Additional note of the method we will be using for converting our animation to gr2, which is lslib. Lslib only picks up keyframes if there are at least 2 and there is a difference between them, so if all the keyframes for a transformation (movement/rotation/scaling) on a bone are the same across the entire timeline, they will not be picked up. To fix this, after your action is baked, use [this Python script](/animation_tutorial/insert_keyframes_with_small_offset.py) on your skeleton rig, with the static bones selected in Pose Mode. It will insert keyframes with a minor offset from the initial value in a frame of your choice (edit the script in Blender's scripting tab as necessary). This should be negligible visually, but enough to be read by lslib.

To bake the animation on the skeleton, select it in Object Mode, go into Pose Mode and select all bones in the skeleton rig.

![bake_action_1.png](/animation_tutorial/bake_action_1.png)

Go into Pose > Animation > Bake Action and bake it with the following settings in the popup (set the end frame to what your end frame is):

![bake_action_2.png](/animation_tutorial/bake_action_2.png)

![bake_action_4.png](/animation_tutorial/bake_action_4.png)

(Keep in mind that clearing constraints will disconnect the skeleton from the control rig, and moving the control rig will no longer move the skeleton along with it.)

After the action is baked, your skeleton rig will now have its own keyframes on the timeline.

To fix the aforementioned issue with lslib only picking up certain keyframes, run the script linked above with static bones selected in Pose Mode (usually it's safe to just select all bones in the skeleton).
![bake_action_5.png](/animation_tutorial/bake_action_5.png)

Your animation should be ready for export then.

#### Exporting the animation and converting it to gr2

Select your skeleton rig (in Object Mode or Pose Mode) and export as .dae (File > Export > Collada (.dae)

In the pop up window you’ll see options on the right-hand side. On the ‘Main’ tab check the box for “Selection Only”

![animtut_010.png](/tutorials/animation_tutorial/animtut_010.png)

Now select the Anim tab :

- Check the box for “Keep Keyframes”
- *Uncheck* the box for “Include all Actions”

Give your file a name (at the bottom) and save it somewhere you’ll remember by clicking the “Export Collada” button.

![animtut_011.png](/tutorials/animation_tutorial/animtut_011.png)

You now have a file ready for conversion into a .gr2 format.


## 2\. Converting an animation for BG3
### **2.1\. Using LSLib**
To convert your .dae file into .gr2 you’ll be using the Lslib tool. The link to download this tool was provided in the Setup section (1.1).

You’ll be using the first tab only – “GR2 Tools”. The process is fairly straight forward :

1.	Select the Input path and your .dae file. The ellipses button can be used to navigate to your file.
2.	Select the Output path and type the name you want to give the file, and append “.gr2” to the end.
3.	Ensure the “Convert to Y-up” box is checked.
4.	Click the Import button. You’ll see the bones you’re importing on the lower right.
5.	Click the Export button. You’ll get a small pop-up window indicating that your “Export completed successfully”.

![animtut_012.png](/tutorials/animation_tutorial/animtut_012.png)

That’s it, you now have a file BG3 can use for animation.

### **2.2\. Testing your animation**

To test your animation you’ll be temporarily replacing the default “Idle” animation for female models with the animation you just created.  

To do this :
- Create the following directory within your “Baldurs Gate 3\Data\” folder :  "\Public\Shared\Assets\Characters\_Anims\Humans\_Female\HUM_F_Rig\"

- Place a copy of the .gr2 file you just created into this directory
 
- Rename that file **HUM_F_Rig_DFLT_IDLE_Still_Peace_01.GR2**

Note – you can also use the Lslib tool to convert your .dae file into this directory with the required naming. This will speed up your workflow when refining an animation :

![animtut_013.png](/tutorials/animation_tutorial/animtut_013.png)


When you load any save your (medium-sized) female companions should now call on this animation when they’re idle :

![animtest.gif](/tutorials/animation_tutorial/animtest.gif)

Note: Don't worry about the animation cutting off here, as this is a test and replacing the idle animation. The idle animation specifically cycles through various different ones, which results in it getting cut off when the next one plays.

Also note you don’t have to exit the game whenever you want to test an updated version of your animation. Simply save the updated animation file to the directory and reload the save (F8 is the quickload shortcut).

When you’re done testing delete the file and the game’s default idle animation will be re-enabled.





### **2.3\. Sidenote: Converting BG3 Animations to Blender**
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



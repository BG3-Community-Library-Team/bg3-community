---
title: Creating Custom Animations
description: Tutorial on how to create custom animations
published: false
date: 2024-10-27T10:42:14.532Z
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

[Blender](https://www.blender.org/download/releases/3-6/) – free open-source software for 3D modeling and animation. Recommended version is 3.6 as this is the latest version the add-on was created for.

[BG3/DOS2 Collada Exporter for Blender 3.6](https://github.com/Norbyte/dos2de_collada_exporter) - An addon for Blender that allows you to import and export DAE/GR2 files for Baldur's Gate 3.

[Lune's BG3 Blender Animation Template.](https://www.nexusmods.com/baldursgate3/mods/5494)  

This tutorial assumes you have some basic knowledge of how to navigate the Blender interface. If you have no experience at all in Blender I recommend the classic [“How to Create a Donut”](https://www.youtube.com/watch?v=B0J27sf9N1Y) tutorial series by Blender Guru, which has been updated for the latest version of Blender.

This tutorial won’t get into the “why” you’re doing what you’re doing too much as the intent is to get you from the template to an animation quickly.  Also there are many different ways to accomplish the same task – the instructions below are simply easier to convey. Over time you will (and should) discover shortcuts and more efficient ways of accomplishing the same task. Control+Z is the undo short cut. You’ll probably wear those keys out if you get into animating.


### **1.2\. Creating an animation**
Once you’ve installed Blender and the add-on, and have opened the animation template, your screen should look like this. Make sure you’re in pose mode (drop down in the upper left), and that the Auto Keying button is turned on at the bottom.

![animtut_001.png](/tutorials/animation_tutorial/animtut_001.png)

Select the “Output” tab on the right side menu. This is where you can adjust how many frames your animation will have, and how many of those frames will play within a single second - known as the “Frame Rate”, measured in frames per second (FPS). These two values – the number of frames and the frame rate, will determine how long your animation is. By default this template has 286 frames at a rate of 60. With these values the animation would be 4.76 seconds long (286/60). 

For the sake of simplicity lets change the number of frames to 96 and the frame rate to 24. This gives us animation length of exactly 4 seconds (96/24). You can play with the frame rate to achieve different effects. Bringing the frame rate down to 12 for example will slow down the animation and double the length. 

![animtut_002.png](/tutorials/animation_tutorial/animtut_002.png)

Your screen should now look like the below. Notice the timeline at the bottom has changed. The last frame is now 96 rather than 286. If you hover your mouse over that timeline and use your mouse wheel you can expand that view.

![animtut_003.png](/tutorials/animation_tutorial/animtut_003.png)

Now select the right shoulder bone by left-clicking on it. Notice that bone shows up in the summary in the lower left, and the keyframe marker at frame 0 now has a white tick mark. 

![animtut_004.png](/tutorials/animation_tutorial/animtut_004.png)

You’re now going to create your animation “keyframes”.  In the manual days of animation an animator had to draw every frame individually. With computer animation that’s not necessary. You will only create the keyframes which are basically your major poses, and the program will “fill in the blanks” to animate the frames in between.

Hover your mouse over the right shoulder you have selected and press “I” then “R”. This will :

1.	Insert (I) a keyframe at position 0
2.	Track that keyframe for rotations (R)

The reason we’re only using rotation is that this rig doesn’t have what’s known as a control rig, or an IK rig, so we’re limited to rotating the bones only. This is fine for now. 

Notice that the tick mark is now yellow. This indicates that you now have a selected keyframe here that’s telling the program you want the shoulder to be rotated in this way at this specific frame.

![animtut_005.png](/tutorials/animation_tutorial/animtut_005.png)

Now you’re going to duplicate this keyframe at position 0 and copy it over to the last frame at position 96. With your mouse hovering inside the timeline press Shift+D. This will create a duplicate keyframe you can control with your mouse. Drag that keyframe all the way to the right and place it at frame 96, and left-click. 

You now have identical keyframes at the start and end of your animation. This is especially important when you’re creating looped animations. If your start and ending keyframes aren’t identical your looping animations may not look seamless.

![animtut_006.png](/tutorials/animation_tutorial/animtut_006.png)

As of now there’s been no change of rotation on that right shoulder. All you’ve done is created a start and ending keyframe with no change in between. If you press the “play” button right now (the large right facing triangle at the bottom), your model will do nothing.

So now you’re going to create a new keyframe with a different pose, say, with the model extending her arm out sideways.

With the right shoulder still selected use your mouse cursor to drag the blue keyframe marker to say, position 50. Then with your cursor hovering in the main window press “R” then “Y” then “-90”, and press enter. This should “R”otate the model’s right arm (on the “Y” axis) at about 90 degrees.

You’ll notice that Blender has inserted the keyframe for you since you enabled the “Auto Keying” button at the very beginning. 

![animtut_007.png](/tutorials/animation_tutorial/animtut_007.png)

Now hit the play button. If you’ve done it correctly you should now see a looped animation of the model raising and lowering her right arm. Congratulations you’ve created your first animation!

![animtemplate.gif](/tutorials/animation_tutorial/animtemplate.gif)


The next section will describe how to export your animation in a format compatible with BG3.




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



---
title: Creating Custom Animations
description: Tutorial on how to create custom animations
published: false
date: 2024-10-27T16:09:24.563Z
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

[Lune's BG3 Blender Animation Template.](https://www.nexusmods.com/baldursgate3/mods/5494)  

This tutorial assumes you have some basic knowledge of how to navigate the Blender interface. If you have no experience at all in Blender I recommend the classic [“How to Create a Donut”](https://www.youtube.com/watch?v=B0J27sf9N1Y) introductory tutorial series by Blender Guru, which has been updated for the latest version of Blender.

This tutorial won’t get into the “why” you’re doing what you’re doing too much as the intent is to get you from the template to an animation quickly.  Also there are many different ways to accomplish the same task – the instructions below are simply easier to convey. Over time you will (and should) discover shortcuts and more efficient ways of accomplishing the same task. Control+Z is the undo short cut.

Some animation specific terminology you may hear often :

- **A model / mesh** – is a 3D object. It can be anything from a simple sphere to a human or a spaceship. The model itself can’t be turned into an animation unless it has..

- **A rig** – this is basically the “bones” of the 3D object and allows you to control and manipulate it in space. A rig can be as simple as one bone to move a sphere, or dozens of bones on a face to create different expressions.



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

> Knowing how to manage keyframes will be a fundamental part of your animation process. For more information on the basics of keyframing in Blender refer to ["Tutorial: Blender Keyframes For Beginners"](https://www.youtube.com/watch?v=8gi9lUYMRcI) by PIXXO 3D.
{.is-info}



Hover your mouse over the right shoulder you have selected and press “I” then “R”. This will :

1.	Insert (I) a keyframe at position 0
2.	Track that keyframe for rotations (R)

The reason we’re only using rotation is that this rig doesn’t have what’s known as a control rig, or an IK rig, so we’re limited to rotating the bones only. This is fine for now. 

Notice that the tick mark is now yellow. This indicates that you now have a selected keyframe here that’s telling the program you want the shoulder to be rotated in this way at this specific frame.

![animtut_005.png](/tutorials/animation_tutorial/animtut_005.png)

Now you’re going to duplicate this keyframe at position 0 and copy it over to the last frame at position 96. With your mouse hovering inside the timeline press Shift+D. This will create a duplicate keyframe you can control with your mouse. Drag that keyframe all the way to the right and place it at frame 96, and left-click. 

You now have identical keyframes at the start and end of your animation. This is especially important when you’re creating looped animations. If your start and ending keyframes aren’t identical your looping animations may not look seamless.

![animtut_015.png](/animtut_015.png)

As of now there’s been no change of rotation on that right shoulder. All you’ve done is created a start and ending keyframe with no change in between. If you press the “play” button right now (the large right facing triangle at the bottom), your model will do nothing.

So now you’re going to create a new keyframe with a different pose with the model extending her arm out sideways.

With the right shoulder still selected use your mouse cursor to drag the blue keyframe marker to say, position 50. Then with your cursor hovering in the main window press “R” then “Y” then “-90”, and press enter. This should “R”otate the model’s right arm (on the “Y” axis) at about 90 degrees.

>Moving, rotating and scaling objects and bones in Blender is what is known as a "transformation". There are quicker and more elegant ways of doing this than what is described above. For guidance that goes into a bit more detail check out ["Blender Basics 4: Transforming Objects and Adjusting Transformations"](https://www.youtube.com/watch?v=lLJilYum_lQ) by CG Cookie. This focuses on models but the same logic will apply to rigs and bones.
{.is-info}



You’ll notice that Blender has inserted the keyframe for you since you enabled the “Auto Keying” button at the very beginning. 

![animtut_014.png](/tutorials/animation_tutorial/animtut_014.png)

Now hit the play button. If you’ve done it correctly you should now see a looped animation of the model raising and lowering her right arm. Congratulations you’ve created your first animation!

![animtemplate.gif](/tutorials/animation_tutorial/animtemplate.gif)


The next section will describe how to export your animation in a format compatible with BG3.
  


### **1.3\. How to correctly save your animation**
When you’re done with your animation or want to test it in progress, you’ll need to export it in a format that can be converted into the modeling / animation format used by BG3 -  “.gr2”. 

To get there you’ll need to :

- Export the rigged animation into a .dae format.
- Use the lslib tool to convert that file into .gr2

When exporting it’s important to remember that you only want to export the rig (the bones) not the model (mesh) itself. It may be easier to think of this process as exporting instructions on what BG3 is supposed to do with the in-game rig, rather than exporting an animation.

To start, go into Object mode (drop down on the upper left) and then select any bone in the rig. The entire rig should now be selected (all the bones are highlighted). Make sure the model is not selected, .ie. the model should not be lit up. 

![animtut_008.png](/tutorials/animation_tutorial/animtut_008.png)

With the rig (only) highlighted go into the “File” menu and select “Export” then “Collada (.dae)”.

![animtut_009.png](/tutorials/animation_tutorial/animtut_009.png)

In the pop up window you’ll see options on the right-hand side. On the ‘Main’ tab check the box for “Selection Only”

![animtut_010.png](/tutorials/animation_tutorial/animtut_010.png)

Now select the Anim tab :

- Check the box for “Keep Keyframes”
- *Uncheck* the box for “Include all Actions”

Give your file a name (at the bottom) and save it somewhere you’ll remember by clicking the “Export Collada” button.

![animtut_011.png](/tutorials/animation_tutorial/animtut_011.png)

You now have a file ready for conversion into a .GR2 format.


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



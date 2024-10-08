---
title: Making Custom BG3 Head Armatures
description: aka Mr Bones Wild Guide
published: true
date: 2024-09-02T07:44:45.502Z
tags: tutorial, blender, head, skeleton, piercings, bones, armature
editor: markdown
dateCreated: 2024-05-25T09:33:53.534Z
---

# MR BONES’ WILD GUIDE

…or jerinski’s guide to custom BG3 head armatures


## Tools you need:
> 
> • Blender 3.6+ with these plugins:
> 
> • [BG3/DOS2 Collada Exporter](https://github.com/Norbyte/dos2de_collada_exporter) (remember to set the path to your LSLIB divine.exe*)
> 
> • [BG3 Armature Tools](https://www.nexusmods.com/baldursgate3/mods/464) (for **Blender 4+** use the updated plugin)
> 
> • [BG3 Modder’s Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool)
> 
> • [LSLIB](https://github.com/Norbyte/lslib) (must be the **latest beta** version!*)
> 
> • [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91)
{.is-success}


This guide assumes you have already installed these items and have a general idea on how to use them. Despite that, it is hopefully still aimed at beginners. Don’t be afraid of the length, it’s mostly pictures (maybe overexplaining some things to those who are more well-versed but I hope it is more helpful than pure text for those who aren’t).

There is also a supplemental video on Youtube: https://youtu.be/Um_3z2vjMQ8
It does not cover the initial setup section of this guide and gathering of files so please read on.

If it seems like I’m going between a lot of different plugins and tools instead of just using one for everything, it’s because this whole process is rather sensitive to how things are imported/exported and I’ve had the most consistent results this way.   


> *Make sure you have the latest beta version of LSLIB and that you set up the path to its updated divine.exe in the blender exporter plugin settings.
{.is-warning}


*Also disclaimer: not an expert, and there are more ways than one to do this; many roads leading to Rome and all that.*


---

## 1. Setup:

It’s good to first get the items we need before you start. So, we already have your edited head in Blender like so:

![1_getting-started.png](/tutorials/custom_head_armatures/1_getting-started.png)



### 1.1) Collecting Assets

We can use the Multitool to find and grab what we need (it’s handy to toggle the search refine to .gr2 only):

- A GR2 of either the vanilla head you have edited, or in my case as I converted a tiefling head to gith I choose a similar head of the type I’m converting to (I will go with GTY_M_NKD_A).

- A GR2 of the corresponding _Base for that head. This is the skeleton we will be editing later. We can search with the multitool for the name of the head and we will find both:

![2_asset-search.png](/tutorials/custom_head_armatures/2_asset-search.png)

> NOTE for porting between different races/bodytypes: use a vanilla head/base from the race/type you are making your custom head for! “Original head” as seen in the Armature Tool itself is a bit of a misnomer when porting - you don’t need the actual original head).
{.is-info}


Extract these but keep them as GR2 and put them in a working folder (wherever, it’s just handy to have all in one place).


### 1.2) LSLIB conversion

Now we open LSLIB to convert the _Base.GR2 to .dae

(yes Multitool can also convert but in the specific case for armatures LSLIB+Noesis has better results)

Remember to turn off X-flip meshes.

![3_lslib-convert.png](/tutorials/custom_head_armatures/3_lslib-convert.png)


### 1.3) Noesis conversion

And now we open Noesis to convert this .dae to .fbx (we will need both)

Find the _Base.dae in the directory on the left, and right click to Export, and do so with default settings:

![4a_noesis-convert.png](/tutorials/custom_head_armatures/4a_noesis-convert.png)
![4b_noesis-convert.png](/tutorials/custom_head_armatures/4b_noesis-convert.png)

> So now we have:
> 
> • A vanilla head .GR2
> • The _base for that head in .dae
> • The same _base also in .fbx
{.is-success}


---
## 2. Importing to Blender:

For organization, I like to set these up in their own Collections. I will add them like so:

![5_collections-setup.png](/tutorials/custom_head_armatures/5_collections-setup.png)


### 2.1) Importing the vanilla head

**To import the vanilla head .GR2**, use the BG3/DOS2 plugin, default settings:

![6_import-vanilla-head.png](/tutorials/custom_head_armatures/6_import-vanilla-head.png)

… we can delete the LODs, and all submeshes except Head, Mouth, and Eyes. Good idea to apply transforms as well.

![7_vanilla-head-setup.png](/tutorials/custom_head_armatures/7_vanilla-head-setup.png)


### 2.2) Importing the DAE base

**To import the _Base.dae**, use Blender’s default Collada importer, default settings:

![8_import-base-dae.png](/tutorials/custom_head_armatures/8_import-base-dae.png)

> It is important to use the basic Collada importer here instead of the BG3 plugin, as doing so will import the base with an unusably large dummy_root bone and most likely result in a broken custom armature.
{.is-warning}


… go ahead and apply transforms to that as well:

![9_apply-transforms.png](/tutorials/custom_head_armatures/9_apply-transforms.png)


### 2.3) Importing the FBX base

**To import the _Base.fbx**, use Blender’s default FBX importer. Default settings EXCEPT scale at 100 instead of 1:

![10_import-base-fbx.png](/tutorials/custom_head_armatures/10_import-base-fbx.png)

It’s going to import looking like this. It’s normal. Just apply transforms here too.

![10b_fbx-example.png](/tutorials/custom_head_armatures/10b_fbx-example.png)


---
## 3. Preparing the Skeleton:

We finally use the Armature Tool! It can be found on the little vertical tabs between the viewport and outliner.

> What this part does is take the Dummy_Root from the dae armature and attach it to the .fbx armature, where it is missing. The fbx armature is the one which we will be editing later.
{.is-info}


Use the eyedropper tool and plug the 2 armatures into place. In my case “Dummy_root” is “Noesis skeleton” and “Armature.002” is “.dae skeleton”

![11_prepare-skele-a.png](/tutorials/custom_head_armatures/11_prepare-skele-a.png)

Now we can hit “Prepare Skeleton”. If all goes well, it should appear that nothing much has happened to pinhead here. Also, our fbx “Dummy_Root” has become “Ready for BG3”, while the dae has been deleted.

![12_prepare-skele-b.png](/tutorials/custom_head_armatures/12_prepare-skele-b.png)

> This “Ready for BG3” is now a skeleton which can be edited/refit to new faces. 
> 
> If you wish, you can duplicate this “base fbx” Collection to have a fresh backup on hand in case things go awry or you want to quickly redo. You can also now hide the Ready armature(s) for the moment to better see the next step.
{.is-success}




---
## 4. Adjusting the Skeleton:

For this next step we need to prepare the head meshes a bit.

### 4.1) Vanilla head prep

**For the vanilla head mesh**, select the Head, Mouth, and Eyes submeshes and with the cursor in the viewport, Ctrl+J to join them. You can rename if you wish.

![13_join-head-meshes-vanilla.png](/tutorials/custom_head_armatures/13_join-head-meshes-vanilla.png)

### 4.2) Custom head prep

**For our edited head**, we can first hide all submeshes but Head, Mouth, and Eyes. Then, select these and with the cursor in viewport: Shift+D then Esc to duplicate, then Ctrl+J to join these duplicates. You can rename this one as well. I like to hide the rest of the submeshes at this point.

![14_join-head-meshes-edited.png](/tutorials/custom_head_armatures/14_join-head-meshes-edited.png)

At this point we can make visible your “Ready for BG3” Armature.

So now all which is visible is:

- Our custom head’s Armature (here is called Armature.001) + the joined submesh

- The vanilla head’s Armature (here is called Armature) + the joined submesh

- The “Ready for BG3” Armature



> It’s important that each of these has had Transforms applied. If you aren’t sure if you have done so earlier, do it again to be safe.
Additionally, for the next step it is best to have all of these things completely visible.
{.is-warning}


### 4.3) Adjusting the skeleton

Now we plug the components into the Adjust Skeleton part like so:

![15_adjust-skele.png](/tutorials/custom_head_armatures/15_adjust-skele.png)

Click “Adjust Skeleton” and if all has gone well so far they should shift slightly. They should not fly away, fall to the ground, or do any shenanigans. Try zooming out a bit to make sure no bones got yeeted anywhere. If any of this happens, probably transforms weren’t applied earlier on and you need to redo.

This is what mine looks like after adjusting (not much different):

![16_skele-adjusted.png](/tutorials/custom_head_armatures/16_skele-adjusted.png)


## 5. Final Touches:

The tool has adjusted the main head bones to the new facial geometry for us. If we want we could just leave it at that and use it already. BUT, the tool does not adjust the piercing or beard bones*. This we do by hand but it’s fairly easy.

> **Context**: The tool just adjusts the bones on the face and mouth only; from my understanding it does so based on the differences between the vertex group coordinates. And since the ears (or beards) don't have any data for that they are not in the script and therefore you have to manually move them.
>
>In that vein, the tool will likely run into issues if the vertex groups got too funky anywhere in the head sculpting process.
{.is-info}


Now is a good time to make all this easier to see. Select your “Ready for BG3” armature and down in the Data Properties editor change “Viewport Display” from “Octahedral” to “Stick”

![17_view-sticks.png](/tutorials/custom_head_armatures/17_view-sticks.png)

We can also go ahead and hide the vanilla head, the joined-edited submesh of your custom head and the custom head’s own armature. Make visible again our custom head’s actual submeshes:

![18_ready-to-fine-tune.png](/tutorials/custom_head_armatures/18_ready-to-fine-tune.png)

It’s a lot of bones, so to make it easier to edit we can (in Object Mode) click “Separate bones to layers”. At this point we can, for example, select “Piercing” and deselect “All” so that only the piercing bones are visible.

> **Blender 4+ with updated plugin note**: Separating the bones looks a bit different here (see below), but works the same. Additionally there is no “Return bones to layer 0”, I assume this is not needed anymore and have had no issues. Probably safest to have all bone layers visible before exporting later anyway.
{.is-info}


![19_blender4-diff.png](/tutorials/custom_head_armatures/19_blender4-diff.png)

Let’s now do some cleanup to make sure the internal bones are placed right. If they are off you could get cutscene weirdness like piercings flying off or very comical expressions (even for Tav).

### 5.1) The base bones, the gesture bones, and the wrinkle bones.


> if any of these are drastically out of place it could cause: much difficulty getting beards to fit, also piercings/beards which look fine except in some cutscenes where they fly off, or some very exaggerated facial expressions.
{.is-warning}

For this step I recommend importing the appropriate body for your head. It can be found the same way we found our head/base with the multitool, it will be:

> - For Body Type 2 Humans/Elves/Half-elves: HUM_M_NKD_Body_A
Replace “M” with “F” for BT1, and “MS” or “FS” for BT 4 and 3 respectively.
> 
> - For other races instead of HUM you use that of the race your head is for (DWR, GTY, HFL, GNO, HRC, TIF..)
{.is-info}


Import that GR2 with the BG3 plugin default settings. Delete any LODs, keep armature visible for this is what we will need.


Now back to our Skeleton. First go to Xray mode with Alt+Z and use numpad 3 to get a strict lateral view:

![20_root-bones-view.png](/tutorials/custom_head_armatures/20_root-bones-view.png)

Here you see the “Root” bones selected, and how they converge with the converge points on the body armature. If they aren’t like this, what follows is an easy-ish way of moving them into place.

The bones we are interested in are:

> - **Root layer**: “Head_M”
> 
> - **Face layer**: 
>   - **6 little bones called**: “gesture_base”, “gesture_01”, ”wrinkle_base”, “wrinkle_01”, “wrinkle_02”, “wrinkle_03”
> 
> - **Piercing layer**: “piercing_base”
> 
> - **Beard layer**: “beard_base”
{.is-info}


First, in Object Mode select both our armature and the body armature. Switch to Edit Mode.

![21_root-bones-wrong.png](/tutorials/custom_head_armatures/21_root-bones-wrong.png)

In the above image you can see that some of the small horizontal base bones of our armature are not converging at the Head_M and Neck_M point of the body armature (the octahedral yellow bones on the left).

Now we select the end point of either the Head_M or Neck_M of the body armature, then use Shift+S to bring up the radial menu to choose “Cursor to Selected” like so:

![22_root-set-origin.png](/tutorials/custom_head_armatures/22_root-set-origin.png)

This moves the cursor to that spot. The bones listed above will be the ones that will potentially need to be moved here.

To do so, select the whole bone (in the image below one of the little gesture bones), Shift+S, and this time we choose “Selection to Cursor”.

![23_snap-root-bones.png](/tutorials/custom_head_armatures/23_snap-root-bones.png)

After this it should look something like this, with all of those 9 bones stacked on that point:

![24_root-bones-correct.png](/tutorials/custom_head_armatures/24_root-bones-correct.png)

### 5.2) Piercings and beards

For these just try to move them so that the base ball of the bone is somewhat flush with the surface where you want the piercing/beard to sit. It’s a bit of trial and error but here’s a general visual for face bones: (side note for beards, keep in mind that some of Trips’ accessories use beard bones to attach piercings to: beard_smileline1_ r/l for dimple, beard_upper_lip_m for medusa.)

Regarding deleting piercing bones, some testing has shown that it is possible to delete them (if for example you have made an ear where not all piercings will visually fit, you can just delete the bones of those you don't want showing).

![25_piercings-beards-bones-example.png](/tutorials/custom_head_armatures/25_piercings-beards-bones-example.png)

…and here’s the face/jaw bones if you want to compare how they generally should look::

![26_face-jaw-bones-example.png](/tutorials/custom_head_armatures/26_face-jaw-bones-example.png)

> Do not touch the eye bones. The tool should adjust them just fine with the rest of the face bones. If the eye bone clusters are converging in the center of the eyes, that’s good.
{.is-warning}



## 6. Exporting:

First, in object mode click “Return bones to layer 0” *(Note for Blender 4+ this is no longer an option and is fine to ignore this step)*.

Then Select just the “Ready for BG3” Armature (no head meshes!), apply all transforms.

**Export with DOS2/BG3 exporter:**

![27_exporting-base.png](/tutorials/custom_head_armatures/27_exporting-base.png)

Export as GR2. Go with default settings, but use “selected only”

![28_gr2-export.png](/tutorials/custom_head_armatures/28_gr2-export.png)

Here are the GR2 optionsI have selected by default in case (under Show GR2 Options) :

![29_gr2-settings.png](/tutorials/custom_head_armatures/29_gr2-settings.png)

> Now we have for our CustomHead.GR2 a matching custom skeleton: CustomHead_Base.GR2 to load into the game.
> 
> That’s it. :frog:
> 
> Well, aside from tweaking the placements of piercings/beards to get them just right. Hotloading the _Base.GR2 as a loose file is very useful for doing this while keeping the game running.
{.is-success}

> **Note about SkeletonBanks**
> when putting together the merged.lsx for your head, it's a good idea to grab the whole SkeletonBank from the head merged you used for the base, instead of re-using from a template. Incongruencies seem like they can cause issues like wonky eyes or even invisible heads.
{.is-info}



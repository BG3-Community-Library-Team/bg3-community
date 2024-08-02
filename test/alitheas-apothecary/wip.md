---
title: Untitled Page
description: 
published: false
date: 2024-08-02T21:24:31.114Z
tags: 
editor: markdown
dateCreated: 2024-07-30T22:33:35.683Z
---

# Timeline Editing (Working Title)
Guide on how to change Dialogue and Cinematics by Milo Magnetuning
## Requirements



- [LSLib](https://github.com/Norbyte/lslib)
- code editor, i recommend [VSCode](https://code.visualstudio.com/)
- [BG3 Modders Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool/wiki/General-Usage) (for finding files, the multitool can have issues processing dialog files so i Dont recommend packing them with it)
- my [dialog timeline updater](https://www.nexusmods.com/baldursgate3/mods/11295) or similar python script to update things like start and end times, effect component IDs, etc
- an extracted localization file to reference your dialog
- not necessary but highly recommended - [parsed dialog files}(https://www.tumblr.com/roksik-dnd/727481314781102080/bg3-datamined-dialogue-google-drive)

- basic knowledge of BG3 modding, but especially unpacking and converting .lsf files
- basic knowledge of using LSLib and the Multitool index
- basic knowledge of conditional statements in code (so it's easier to understand how bg3 dialog flags work)
## So, What Goes Into Dialogue in Baldur’s Gate 3?

Dialogue in the game is handled by a lot of files, some of which I’m still looking into, but the main ones this tutorial will focus on, and the ones you need to edit existing game dialogue are the following:

-   DialogsBinary files
-   Dialog Timeline files
-   Dialog Scene files

There are two more files you will need to add new dialogue files—which *is* possible, by the way! And you can see an example of that here:


The two files you'll need for adding entirely new dialogue to the game are:

- Generated Dialog Timelines
- Dialog Assets

You'll need extra files to add new voice lines, which I'll be providing in a separate guide for this wiki too.

This tutorial will break down each of these files, and how to edit them. <!--I've provided an annotated sample mod and a mirror of some of this tutorial on Nexusmods, which you can find here! The sample mod breaks each element in the code down line by line, and can serve as a reference for the files as well.-->

> A note on deprecated files:{.is-warning}

You'll likely find Dialog.lsj files with that same file name when extracting the files, as well as an extra Dialog Scene file with the .lsx file extension. These files are both deprecated! (The Dialog Scene files with the .lsf file extension are what you'll need to edit, NOT the .lsx files. Yes, confusing, I know.)

These deprecated files genuinely do nothing. You don't need to edit them or include them in your mods at all, and I do not recommend you do so. You can create fully functional new dialogue without them, so they really do just, nothing.

Thank you very much to <a href="https://next.nexusmods.com/profile/Joell560/about-me">Joell560</a> on Nexusmods for letting me know the files were deprecated! You've saved me a ton of hassle trying to recreate my changes in both files, and it's genuinely saved me so much time.

The Dialogs .lsj files aren't necessary for creating new dialog, either! They really don't seem to do anything in the game. I'd recommend not including them in your mods at all.


Now, let's start breaking down the file, starting with the Dialog Timeline files.

### A Summary of Dialog Timeline Files

The Dialog timeline files are usually found in the this folder in the game's files:

`
\\Data\Public\GustavDev\Timeline\Generated
`

These files control the timing of all elements required to play dialogue and cinematics, including the actual voice lines, character animations, the emotions the characters use, camera angles, sound effects, and more. They control all aspects of dialogue that require full animation and timing—which does not include moments where your character picks dialogue options! Those are found in the DialogsBinary files, which I'll cover shortly.

A good way to think of the dialogue timeline files is to picture it like a movie! With each line of dialogue as a small scene within that movie. The code in the dialogue timeline files gives the game everything necessary to play those scenes, and what element of the scene play when.

Fun fact, by the way: cutscenes are regular dialogue files! They switch between lines of dialogue and cinematics—sections of animation without voice lines—to create a given scene.

This means that cinematics are sorta like mini cutscenes, including the cinematics for kisses!

It’s important to note, these little scenes within the timeline files aren’t played in order. While the timeline itself is like a movie, the game is almost constantly skipping around within it to play the dialogue or cinematic it needs!

And that’s where the DialogsBinary files come in!
####

The DialogsBinary files are generally found in this folder in the game's files:

`
\\Data\Mods\GustavDev\Story\DialogsBinary 
`

They're then further broken down by what section of the game they belong in, like if they’re from Act 3, or the Tutorial level, if they’re Companion dialogue, etc. You might find these files in the Gustav folder, but they’re still organized in a similar way.

Now, if the timeline files are like a movie, then DialogsBinary files are like a chapter skip function on a DVD. These files contain the information the game needs to reference your choices in dialogue, and select which voice lines or cinematics to play, and when. They contain information on dice rolls, links to nested dialogue files—which I’ll explain a more about later—and are where the game tests for whether a line of dialogue or or player response should be accessible or not. They can be used by the game to set flags it can test for in other areas of the game, and can link to information on companion approval.

Dialog Scene files
####

The Dialog Scene files contain information on camera and character positioning when the dialogue is triggered, as well as lighting, which characters can be present in the dialogue, and can be used to control character scale within a scene! Which is fun.

They can inherit information from other files, the most important of which is the default dialogue scene file, which is often linked at the bottom of the file. The default Scene files can be usually found at this file path here:

\\Public\Shared\Timeline\Scenes\Default\

You may not have to edit these files often, but it's still important to note! And they'll absolutely be necessary when creating entirely new dialogue files.

The DialogsBinary, Dialog Timeline, and Dialog Scene files for a given scene will all have the same file name, with the Dialogue Scene files just appending the word Scene to that same file name.

Generated Dialog Timelines
####

The GeneratedDialogTimelines files contain information linking each DialogsBinary file to its proper timeline file, as well as each of the characters, props, scenery, and so on that are referenced by the timeline files. These files are huge, and contain information on most of the dialog timelines in the game. You should generally only include the entries for the dialog timelines you're editing in your mods!

The GeneratedDialogTimelines files can be found at these file paths:

\\Public\Gustav\Content\Generated\[PAK]_GeneratedDialogTimelines\_merged.lsf

\\Public\GustavDev\Content\Generated\[PAK]_GeneratedDialogTimelines\_merged.lsf

Dialog Assets
####

These files contain information on the DialogsBinary files, where the game should look to to find them, and what dialogue files are linked as nested dialogue within a another file. Again, there are often a lot of entries in these files! And you should only include the entries for the dialog files you're editing if necessary.

These files can generally be found at this file path:

\\Public\GustavDev\Content\Assets\Dialogs\

Followed by separate folders breaking down the dialog according to what section of the game they're supposed to happen, just like the DialogsBinary files.

**A note:**

The Dialog Assets files still refer to the dialog .lsj files as the file paths it's looking for to play a given scene. However, the .lsj files are still deprecated! And despite being referred to in the Dialog Assets entries, the game can still refer to the corresponding DialogsBinary.lsf files through that .lsj file path, and will use those files instead. Even entirely new modded dialog files can be referenced without an .lsj file, even when the file path is set to look for an .lsj file.

Alright, now that we've covered the basics, let's get into editing the files!


## How Do You Edit the DialogsBinary Files?

These sections of the tutorial will be broken down into tabs, one containing a further explanation of the DialogsBinary files, one containing information on the elements in them, and one explaining how to edit them.

Honestly, just understanding what you're looking at is half the battle when editing dialogue! So I highly recommend checking out the documentation tab before you begin.

**The How to Edit tab contains a short guide on creating custom game flags!** If you'd like to know how to do so, you can find instructions there!

## Tab {.tabset}

### A Summary

As mentioned before, the DialogsBinary files are essentially like a chapter skip function on a DVD, telling the game which line of dialogue to play and when.

This is done within the code of the DialogsBinary files, which link together a variety of different types of dialogue node. This is done by linking one dialogue node to the ones that are supposed to come after by the “children” attribute. When you list the UUID of one dialogue node as a “child” of another node, the game will see that UUID and know that “child” is the dialogue node that should play next. A dialogue node can have multiple “children,” which can be tested for using the CheckFlags attribute to know which line to play, or these multiple “children” could be sets of player choices following a given line of dialogue, which will then lead to further branching paths depending on what the player selects.

This is how the game navigates through scenes, by following and testing for these different branching paths between different types of dialogue nodes.

And yes, there are different types of dialogue nodes! These types determine what kind of behavior to perform for that node. Is a character speaking, or is the player given the opportunity to respond? Should a dice roll be performed, or is this a cinematic cutscene that needs to be played?

### Documentation

As mentioned in the summary, the main elements in a DialogsBinary file are dialogue nodes.

There are 11 different types of dialogue node that I’ve found so far. Keep in mind this game is huge, and there are a ton of dialogue files and different scenes in the game. There might be something I’ve missed. But I have looked at these files extensively, these are all I’ve found at this point!

These different dialogue nodes are TagGreeting, TagAnswer, TagQuestion,TagCinematic, ActiveRoll, PassiveRoll, RollResult, Alias, Jump, Nested Dialog, and RootNodes.

TagGreeting
####

TagGreeting nodes are the first line of dialogue a character will say to you when speaking to them. These are paired with a corresponding Root Node at the end of the file. These TagGreeting nodes can then be followed by further dialogue nodes, or they could be a single line of dialogue, followed by the end of a conversation. That last bit is really common for NPCs. The greeting a character uses can be tested for using the CheckFlags attribute, allowing a character to use different lines of dialogue when initially speaking to them, depending on the conditions that have been set.

TagAnswer
####

TagAnswer nodes are used for dialogue lines from speaking characters. This is usually the character you’re directly speaking to, but other characters can be included in conversations, such as when companions have voice line reactions to what’s going on. These are given the TagAnswer label.

TagQuestion
####

TagQuestion nodes are used for player dialogue options. These will be listed as “children” under the line of dialogue they’re meant to follow, which will act as a kind of “hub” for these options. The response from the character you’re speaking to when that option is chosen will be listed as a child of the TagQuestion node, allowing the game to navigate through the proper responses to your choices in dialogue.

TagCinematic
####

TagCinematic nodes are generally animations without voice lines. These are essentially what cutscenes are in the game, although most scenes combine multiple lines of dialogue and cinematics together to complete the scene. Again, cutscenes really are just regular dialogue files. Understanding how to edit dialogue will allow you to edit and potentially create cutscenes in the game yourself from the XML level.

ActiveRoll
####

ActiveRoll nodes are dialogue nodes that prompt the player to make a dice roll, and allow you to set different dialogue paths as “children” of the dice roll depending on whether the roll was successful or not. The different outcomes are set via RollResult nodes, which will be set to True or False to give the outcome of the roll.

PassiveRoll
####

PassiveRoll nodes are very similar to ActiveRoll nodes! However, these are the passive rolls, like for perception and arcana, that are made automatically for the player in dialogue. The results for these rolls are  handled via the RollResult dialogue nodes.

RollResult
####

RollResult nodes are linked as childen of ActiveRoll and PassiveRoll nodes. There's generally only two RollResult nodes, one with the Success attribute for the node being listed as "True," and the other with its Success attribute set to "False." These nodes determine what happens as a result of a dice roll, depending on whether the roll succeeded or not.

Alias
####

Alias nodes essentially allow you to play another line of dialogue without having to duplicate everything from the original line. This is really helpful if you need to configure multiple branching paths that contain the same line, because it means you won’t have to duplicate the information for that line in the Dialogue Timeline file every time the it needs to be played. This is a very good thing, and I’ll get more into why when we cover the timeline files.

Jump
####

Jump nodes allow you to jump to different lines of dialogue within a dialogue tree.

Nested Dialog
####

Nested Dialog nodes will allow you to link to Nested Dialog files, which are essentially separate dialogue files that can contain smaller scenes, or dialogue options based on a certain theme, and so on. An example of this is used for companion romance dialogue; most companions have their romance dialogue in nested dialogue files, which are then linked to from their default InParty dialogue.

RootNodes
####

Root nodes are unique, in the sense that they're generally mirrors of other nodes. The root nodes refer to the possible first lines of dialogue in a given scene or conversation, and are generally referring to TagGreeting nodes, but other types of nodes can be referenced as RootNodes. When a dialogue node in a file is considered a root node, that line of dialogue will have a RootNodes entry with its UUID listed at the end of the file, and will  be marked in its own code block with the Root attribute, which will be set to True.

### How To Edit

Honestly, the easiest way to edit these files, at least if you're adding new elements, is to duplicate existing code blocks. This will guarantee you'll keep the code structure the game needs consistent, and saves you a bit of work typing everything out.

<!--I've provided an annotated sample/template mod on Nexusmods <a href="https://www.nexusmods.com/baldursgate3/mods/10086">here,</a> which you can use to follow along with this guide, and understand a bit more about what goes into the code structure for a given node.-->

Now, let's begin!

**Editing existing files**
####

When editing existing files, you'll first need to find the dialogue nodes you'd like to change. This can be done by searching for the dialogue you're looking for in an extracted Localization file, which I've provided in the above link as well, for each language the game has been translated into.

I  *highly* recommend using the <a href="https://www.tumblr.com/roksik-dnd/727481314781102080/bg3-datamined-dialogue-google-drive">parsed dialogue files</a> provided by roksik-dnd on Tumblr. These will not only help you find lines of dialogue from the game, but will  serve as a guide to the structure of the dialogue tree you're editing, which lines of dialogue follow which other lines, the branching paths available in the scene, and so on.

But the extracted Localization file is often necessary, because the dialogue in the DialogsBinary files are referred to by their text handles, which can be found in the Localization files.

These text handles are found under the TaggedTexts attribute for a given node, and determine both the caption for the dialogue, and are linked to the voice line, animations, and lipsync for the dialogue in a character's voicebank.

**Finding the right dialogue nodes**
####

Search for the line of dialogue you're looking for in your extracted Localization file, and then copy the text handle that corresponds to the line. Then search for that text handle in your DialogsBinary file, which should bring you to the correct dialogue node.

Once you've found the right dialogue node, I'd recommend making a comment in the file labeling what it is, so you can come back to it later. You can enclose your comment in a bracket like this to prevent it from affecting your code: \<!-- -->

Once you've found the right dialogue node(s), you can start making your changes.


**Changing dialogue tree paths**
####

The game navigates through the dialogue trees via two things: the UUIDs of the dialogue nodes, and the "children" of each dialogue node. The UUID is the unique identifier of a given node, and the "children" of a node are the dialogue nodes that can directly follow it, referred to by each child node's UUID.

To change the paths the game takes through the dialogue, you'll want to edit these child nodes. You can remove a child from a dialogue node to prevent it from following that node, or you can add a dialogue node as a child of another to make it a possible option the game can take.

You can replace all the children nodes for a given dialogue node if you'd like, or you can remove all of them entirely, which will usually return the player to the last set of player responses available to them.

All you need is the UUID of the dialogue nodes you'd like to remove or add as children of a node, and then you can start configuring your dialogue trees!

A note: when adding player responses (which will be labeled as TagQuestion nodes), the order the children are listed under a dialogue node will  be the order they're displayed in the game, listed from top to bottom.

, when multiple children are listed under a character's speaking line (labeled as a TagAnswer node), and they're not player responses, these are usually lines of dialogue that are being tested for certain conditions, to determine whether they should play or not. In this case, the order the children are listed in is the order the game will test them in, with children placed higher in the list taking priority.

**Checking game flags**
####

The checkflags attribute is how the game tests whether a line of dialogue should be available or not. When a given flag is set to True under the checkflags attribute, that means the dialogue node will only be available if that flag is set to true. When the flag the game is testing for is set to False, then that line of dialogue will only play if the flag is *not* true.

To edit the conditions a line of dialogue will be available under, you can add or remove flags for this attribute. Check their UUIDs to make sure you're testing for the right ones! , take a note of what kind of flag it's testing for; if the game's testing for a Tag, it's testing what character tags a given character has. When the flag type is a Global flag, it's testing for a flag that's present in the game globally, and not just applied to a specific character. Local flags seem to be flags set for the player character, and Object flags are testing to see whether the character you're speaking to has a given flag set for them (these are distinct from tags; flags are conditional, and are usually set during gameplay, as opposed to tags, which are used to determine different qualities of a character, like whether they can participate in dialogue or not!).

**Setting game flags**
####

The setflags attribute will allow you to set game flags when that dialogue node is played. This can be done by listing the UUID for the game flag, and either setting it to True to enable the flag, or setting it to False to disable it. You can  make your own custom flags!

**Making custom game flags**
####

Making custom game flags is pretty straightforward! All you need to do is find an existing game flag file, and duplicate it to begin editing it. Generate a new UUID for the flag within that file, give it a new name, a description to remind you what the flag is for, and then change the file name to the UUID you gave the flag within the code. Keep in mind the usage type! As mentioned above, there are multiple different kinds of flags, which usually correspond to their usage type.

For instance, most HasMet flags (flags that determine whether a given character has met another character) are given usage type 6, which usually corresponds to the Dialog flag type in the DialogsBinary files (I believe this flag type is used to mark flags that are tested in dialog specifically, instead of elsewhere in the game, but I'm not entirely sure yet.) Global flags are often given usage type 5, and so on. I'd recommending finding a flag that has the same flag type in the DialogsBinary files as the flag you're trying to create, so you can keep the usage type consistent.

**Adding Alias nodes**
####

Alias nodes, as described in the documentation tab, are nodes that can emulate another line of dialogue, but will allow you to set different conditions and configure new dialogue paths for that same line. This especially helpful when using the same line of dialogue in a scene multiple times, because it means you won't have to duplicate that line of dialogue in the Dialogue Timeline file. This is a very good thing! Editing the timeline files is not easy, and you'll save yourself a ton of time by using alias nodes instead.

Just list the UUID of the line of dialogue you'd like to emulate as your SourceNode, and you should be good to go.

**Linking Nested Dialogue**
####

Nested dialogue files are files that can be linked to from other dialogue files, usually containing smaller scenes, or dialog based around a certain theme, like companion romance. *These files are especially helpful for compatibilty.*

This is because they have their own unique dialogue timeline files, which, again, are really complicated to edit. And to make mods that edit dialogue timeline files compatible, you’ll need to incorporate all changes made by each modder into the same dialogue timeline for that scene. This is not easy. Editing the DialogsBinary files to link to nested dialogue is much simpler, and will allow for much easier compatibility patching between mods.

To refer to a nested dialogue sequence, you'll need to list the UUID for the nested dialogue found in its Dialog Assets entry, and then set the line of dialogue you'd like to start with in your nested dialogue sequence as a child of the Nested Dialog node.

You'll  need to make sure the nested dialogue you're linking to is listed as a child in the Dialog Assets entry for the original dialogue, and add the original dialogue as a child of the nested dialogue if you'd like to be able to return to it.

I'll be covering more about how to create new nested dialogue files, as well as creating new dialogue files generally at the end of this tutorial! You can scroll to the end of the page to find it.


### How Do You Edit the Dialog Timeline Files?

And now for the Dialog Timeline files. These are very lengthy and complicated files, and some parts of editing them can be extremely tedious, time consuming, and potentially, like, almost impossible without a python script to automate some parts of editing them.

...It's a good thing, then, that I made a tool to automate those tasks! You can find it on Nexusmods <a href="https://www.nexusmods.com/baldursgate3/mods/11295">here.</a>

It's an extremely simple tool, and is basically the Python scripts I've been using to update timeline files put into a tkinter UI, but it's been a lifesaver for me when editing these files.
  
Like the DialogsBinary section, I'm  going to be breaking this section of the tutorial into different tabs.

You can find instructions on how to use my Dialog Timeline updater in the Using the Timeline Updater tab, as well as on the Nexusmods page for the tool.

The Summary tab offers a bit more explanation on how these files work, the Anatomy of a Dialog Timeline tab explains the structure of the files overall, the Effect Components tab will break down the different EffectComponents in the files, the How to Edit tab will go over editing the files, and the Emotion Rigs Quick Ref tab lists out the expression rigs used by the game, with the ID and variation numbers you'll need to reference them in the files.

## Tab {.tabset}

### A Summary

### Anatomy of a Dialog Timeline File

Dialogue timeline files are broken down into a several sections, the biggest of which—EffectComponents—I'll be covering last. The EffectComponents section contains most of the actual information about the dialogue being played, so it is both extremely lengthy, and references a majority of the other sections in the timeline files. Covering the others first will make the EffectComponents section make a lot more sense. I'll be covering each other section in the order they appear in the files, skipping the EffectComponents for now. 

These sections are:  
 

#### **Duration:**

The total duration of all the dialogue and cinematics possible in the scene combined. Make sure you update this to account for anything you add to the dialogue! The elements you've added will not be able to play properly if you don't.

There’s not much to say about it beyond that, honestly! It’s one line, and yet I have managed to say 67 words about it anyway!  
 

#### **Phases:**

Dialogue phases are what control the actual timing of the elements in each dialogue node, as described in the DialogsBinary section of the tutorial. They group together each element that needs to play as part of a given dialogue node, which are linked together via their PhaseIndex. These grouped-together elements can be found in the EffectComponents section, which is covered in the Effect Components tab.

The "Phases" section at the top of the file lists the total duration of each phase, alongside the UUID of the dialogue node in the DialogsBinary file that plays during that phase.


You can find the specific PhaseIndex associated with that dialogue node via that UUID as well! That same UUID will link to a MapKey and associated MapValue number in the TimelinePhases section further down in the file. That MapValue number is linked to the PhaseIndex for the elements in the EffectComponents section. The PhaseIndex number will group together all related effect components for that dialogue node! These components will be the bulk of what you’ll edit for your own dialogue mods.

Another thing to note is that the Phases section is in sequential order, and that order corresponds directly to the MapValue and PhaseIndex for the dialogue node! The timeline  starts counting the phases from 0 (which is how most animation/video program timelines handle things as well). 

Phase 0 is placed at the top of the timeline, and is not given a PhaseIndex number, because it's unnecessary with it at the start of the timeline. This  means that the second listed phase will be PhaseIndex “1”, the third listed phase will be PhaseIndex “2,” and so on. You can mess things up by changing this order!

When adding things to the timeline, I highly recommend adding everything to the end of each section in the file. This will keep your phase order consistent, and prevent you from having to update the entire timeline at once.

You can  prevent dialogue from functioning by skipping PhaseIndex numbers! Make sure you don't have any gaps in your PhaseIndex numbering as well.

Keep both of those things in mind and you should be good! (And  save yourself just, a ton of work.)

####   
TimelineSpeakers: 

Contains the UUIDs of which character is performing what action, and which character is being referenced in general! These UUIDs are specific to a given set of dialogue files, and are linked to in the corresponding DialogBinary file for the timeline, which will be connected to either the UUID for the speaking character, or the UUID for the player character.

The structure of this section is arranged into “Objects,” followed by MapKeys and MapValues, the former of which refers to what speaker number a character was given, and the second is the aforementioned UUID referring to the character.

Speaker 0 is generally the person your character is talking to, with Speaker 1 being your character. Speaker roles after that may be listed if narration is present, or if other characters beyond the character you’re speaking to have lines (like when other companions have reactions during a conversation). You’ll want to cross reference the TimelineSpeaker UUIDs with the same UUIDs in the DialogsBinary file, so you’ll know what character is being referenced by them.


The most important thing to know about the Timeline Speakers, and Timeline Actors is that you want to make sure any components you copy over from other files are updated to use the Timeline Speaker UUIDs from the file you copied them into. If you don't update them, the components you added won't be able to reference the characters properly, and you could end up something like [THIS](https://drive.google.com/file/d/1EIVmKs6qtHvgeUopn5bnDr7q6VgYhQ7w/view). Which is not ideal, for sure!

If you're not sure what any of these terms mean, don't worry! There's more information about them in the Effect Components tab, and I've  be covering how to update timeline speaker UUIDs in the How to Edit tab.

Let's continue on with the other sections in the timeline files, first, .  
 

#### TimelineActorData:

This section contains several long lists mapping out each effect component in the timeline and the UUIDs of the characters performing them, pulled from both the TimelineSpeakers and PeanutSlotIdMap sections. However, I think it's likely these lists are used for Larian's game engine, to allow it to reference the components, and don't seem to do much in the game itself. Even leaving these MapKey lists entirely unedited didn't change anything, in the game, so I don't think you have to worry about the component map.

There *are,* however, things in this section you'll likely need to update, especially when cloning elements from other files. These are the "scenecam" and “scenelighting” actors. These are not characters, but instead refer to specific camera angles and lights necessary for the dialogue, and are  often located in the corresponding Dialogue Scene files, which have their own section on this page. If the camera angles referred to in a dialogue node are not present in the TimelineActorData section, the game will not be able to properly reference the camera, and you'll likely get the camera pinned to the floor instead.

#### TimelinePhases:

As discussed in the Phases section above, this section contains UUIDs in a list of MapKeys and MapValues. The UUIDs here will correspond to the UUIDs in the Phases section of the file. The placement of that phase in the Phases section, as well as in the EffectComponents section will match the MapValue listed for the MapKey in the TimelinePhases, starting from zero. (Again, most animation programs and video editors  start their timelines from 0, so this is probably why BG3 handles its timelines like this, too.) That MapValue number is  the PhaseIndex number you'll be looking for when editing and cloning components in the EffectComponents section for your mods.

That same UUID belongs to a specific dialogue node in the DialogBinary file, and all components related to it are what plays when that line of dialogue is called by the game.

Important to note is that the MapKey order here does not have to match the phase order! Most of the elements of the timeline files have to be sequential, but these do not. I still recommend appending your additions to the end of the section, just to make everything easier to keep track of.


#### PeanutSlotIdMap:

This is similar to the TimelineSpeakers section mentioned above, but it refers to the characters standing behind the player character during a conversation. Like the peanut gallery! Definitely one of my favorite variable names for sure. Any references to “Peanuts” in the dialogue files is about these characters. And the UUIDs here are meant to map out things like emotions/animations/etc for these characters according to what “slot,” or placement behind you the characters are.

From what I can tell, these characters are not ever referred to in the DialogBinary files, unlike the TimelineSpeakers, probably because they don't speak, and can be any companion or hireling character. This means the animations of the characters behind you are tied to which of 3 placements they've been put into, rather than a specific character.  
 
#### AdditionalLocations:

If a scene needs to take you to a different location for the scene to play, the triggers for those locations will be listed here. These can then be called by the TLSwitchLocationEvent effect component.

#### What about the rest of the file?

The rest of the sections in the timeline file are either things that likely should be kept consistent, don't seem to affect much in the game when changed, or don't seem to contain information in most of the files I've seen. I'll be experimenting more with them, ! But you likely won't need to worry about them much for most of your own dialogue mods.

  
…And, with that, we're ready to move on! Check the Effect Components tab to continue with the tutorial.

### Effect Components - Documentation
 
#### OK, I'M READY. WHAT IS GOING ON WITH THOSE EFFECT COMPONENTS?

The EffectComponents section is the bulk of what you’ll be getting into and editing for your dialogue mods. This section contains all the actual information on timing, character animations, poses, staging, expressions, sound effects, voice lines, camera angles, and more that need to be referenced to play the dialogue or cinematic. Most of the other sections in the file are meant to help the game reference this information, but the effect components are the true core of the dialogue system.

Effect components are classified into several different “Types,” each of which performs a unique function, which I'll list below.

There’s a lot to go through, so strap in!  
 

#### What types of effects components you can choose from?

So far, I’ve found the following effect components, each of which controls a different aspect of dialogue, and each of which has different set of attributes, which I’ll explain shortly. For now, , I’m just going to give a brief rundown of each:

-   **TLVoice:** The voice line for the character speaking.
-   **TLAttitudeEvent:** Controls the nodding/motion of the head and animated expressions characters are given when other animations are not being played, i.e. when a character is waiting for you to pick a dialogue choice, or is listening to the character speaking.
-   **TLAnimation:** The animations used by the characters. Mainly used for cinematics, but can be used for unique facial expression overrides as well. A note: the animations used during dialogue outside of cinematics are generally tied to the voice lines itself, and not referenced in the timeline files. This is for animations not tied to voice lines directly.
-   **TLEmotionEvent:** Controls the facial expressions used for the character referenced in the “Actor” section of the component.
-   **TLLookAtEvent:** Controls where the character is looking, as well as whether their eyes are open or closed, head and body turning, etc.
-   **TLMaterial:** Used for temporary material overrides, like for Karlach's glow map colors during romance scenes.
-   **TLShowVisual**: Used to switch different objects into scenes, such as set pieces in the environment.
-   **TLShowWeapon:** Controls whether weapons and instruments are shown during the dialogue or cinematic, and when their visibility is toggled on and off.
- **TLShowArmor** Controls whether different armor or clothing slots are displayed on a character during a scene.
-   **TLShowPeanuts:** Controls whether the characters standing behind your character during dialogue are shown or not. (Again, like the peanut gallery!)
-   **TLSoundEvents:** What sound effects play and when.
-   **TLSwitchStageEvent:** Mainly used for cinematics. I believe this is used when the characters need to change positions from their places in normal dialogue, often for animations.
-   **TLTransform:** Mainly used for cinematics. I believe this controls changes in character position within the game world i.e. if they need to turn or walk from one place to another.
- **TLShapeshift:** Used to swap in different character RootTemplates, so you can change character appearance within a scene.
- **TLSwitchLocationEvent** Used to take you to different locations when necessary in a scene. These locations will be listed in the AdditonalLocations section of the file.
-   **TLShot:** Used to time camera position switches.  
     

#### Ok, cool. What do you mean by “attributes," ?

Each effect component in a timeline file is broken down into several variables, or attributes, which will tell the game how it should handle the effect when calling it in the game. These attributes include things like start and end times, the actors mentioned above, the sound effects/animations the game should be playing, and so on.
  
Keep in mind that not every possible attribute for these components will be present every time! Which means some possible attributes the game can process may not be listed in this tutorial yet. If you find one I missed, please let me know!

, some of the attributes I included in these explanations contradict each other, and will not be found in the same instance of that effects component. I've generally pointed it out when this happens, but a good rule of thumb will be to look at examples of the same type of effect component you're editing, to know what attributes are usually included in them, and which are not.

This section is likely going to be very long, but hopefully having explanations of what everything is makes it a bit less intimidating! These files can be a lot to look at, but the more you understand about them, the less daunting it'll be to edit them.

Let's get into it! I'll start by explaining some common attributes you'll see in most effect components:  
 

#### A Guide to Common Effect Component Attributes

#### Type:

Pretty self explanatory. The type of effect component, which will be one of the kinds of components I listed above.  
 

#### PhaseIndex:

`<attribute id="PhaseIndex" type="int64" value="1" />`

As mentioned above, the PhaseIndex refers to every component belonging to a given dialogue node, which will be played as a group according to their given start and end times (explained below).

For your own mods, you’ll want to make sure this number is unique, sequential, and is tied to the same MapValue number and placement in the TimelinePhases and Phases sections, respectively. You'll  want to make sure all elements you add for your dialogue node have the same PhaseIndex, so they'll be grouped together, and play properly as a unit.

And again, the first dialogue node on the timeline will not have a PhaseIndex listed for its components! Its PhaseIndex number is 0, but, being at the start of the timeline, the game’s code doesn’t require it to be listed.  
 

#### StartTime and EndTime:

`<attribute id="StartTime" type="float" value="7.42" />`

`<attribute id="EndTime" type="float" value="9.21491" />`

Pretty self-explanatory! The start and end time for each component within the phase, according to its placement within the whole dialogue timeline. A few things to note, :

-   The first phase on the timeline, again, starts at 0, so it generally does not list start times for its components, unless one of those components is meant to start partway through the dialogue. It usually will list end times, .
-   The start and end times listed do not have to match the full length of the phase! Some effect components start and/or end partway through the phase, which can be used to add pauses between lines of dialogue, among other things.
-   These start and end times are placed within a massive timeline, and they are, again, sequential. As mentioned earlier, it helps to imagine the dialogue timeline like a movie, and the phases in the timeline are little chapters you can skip to within it, with each component playing at specific times within that chapter, according to these start and end times.

#### Time:

Some components list start and end times, and then are further broken down into “Time” elements. These are seen in components like TLEmotionEvent and TLLookAtEvent, among others. I mentioned this above, but to reiterate, the “Time” attribute refers to when a certain effect is supposed to start, they just don’t have equivalent end times. Instead, the next instance of the “Time” attribute will replace the previous effect listed within the component.

This may be because some of these attributes are meant to persist, even after the game has moved onto the next dialogue node! Two examples of these are TLEmotionEvent and TLAttitudeEvent. The animations from these two effects components are carried into the next node, and are often used to preserve the characters' expressions and attitude animations while you're picking dialogue options. These attributes are not given a definitive end time, because they're meant to persist until the next instance of the attribute is called, or the dialogue ends.  
 

##### A note about timing in general:

The StartTime, EndTime, and Time attributes are all handled *extremely* precisely, with times often being very, very tiny fractions of a second.

This is extremely helpful with facial expressions in particular—each character only has around 8 expression rigs for any given emotion, and the total number they have is relatively small. But by using the precise timing the game allows, it almost never feels like they’re using so few expression rigs. You can make extremely complex sequences of emotions using this method, making the characters’ expressions feel unique, despite how few rigs they use.

I’ll be getting more into the TLEmotionEvent components later! But, for now, there’s still three common elements to talk about:  
 

#### IsSnappedToEnd:

`<attribute id="IsSnappedToEnd" type="bool" value="True" />`

Honestly, I think this might just be used by Larian's game engine, to make sure each effect component snaps to the end of the previous phase. This doesn't seem to affect much when changing it on the .xml level. 
 

#### ID:

`<attribute id="ID" type="guid" value="49292981-224c-4feb-a51b-fa7bf0fb46f3" />`

The unique UUID for the specific effect component you’re looking at. It’s generally a good idea to generate a new one for each effect component you add, which my dialogue updater tool can take care of for you. (More explanation can be found in the

A note: other UUIDs within an effects component are connected to other things, like animations, camera positions, and the characters performing the listed effects. My dialogue updater will only change the IDs for the effects components themselves, and won't touch any other UUIDs, but make sure you're careful if you're manually editing them. You'll want to make sure all other UUIDs are the same as the elements (like camera positions, animations, etc) you want to reference.

Which brings me to the last common attribute:  
 

#### Actor:

`<node id="Actor">`

`            <attribute id="UUID" type="guid" value="55bce89d-670d-f7c9-6e3b-38ebe3322b32" />`

`</node>`

This UUID refers to which character is performing the effects component! These as mentioned before, these are unique to each timeline file, and will usually need to be updated to match when cloning effects components from other files. The component won’t be able to reference the related character if this UUID is not updated.

#### Ok, So, We've Covered the Basics. What About Specific Effects Components?

The moment you’ve all been waiting for! Maybe. I’m now going to be breaking down each kind of effects component by its attributes. These are only example components—they won’t refer to anything specific, and almost all values for the attributes have been generated new (and are almost certainly nonfunctional).

I  provided explanations for all attributes I could find within these code blocks—which means that some of the attributes shown in these blocks contradict each other! And should not be used at the same time. One example is the “IsMimicry” and “PeanutOverride” attributes. These attributes seem to be mutually exclusive; from what I can tell, the IsMimicry tag is used when things like emotions/attitude animations/etc need to be copied over onto “peanut” characters (the characters standing behind your character in conversations) from the player character. The PeanutOverride attribute marks a component block as being a unique override for a peanut character, separate from the player character.

These tags may be a tag for Larian's game engine to process; they don't seem to affect much when changed. But still, they should probably be updated when changing these blocks, and shouldn't be used together.

A good rule of thumb for editing, creating, and adding onto these components is to try and find other components with a similar structure. If you can find other components with the same attributes yours has, you can be sure those attributes will work together!  
 

#### TLVoice:

![](/tutorials/dialogue-files-tutorial/tlvoicevisual.png)

#### TLAttitudeEvent:

![](/tutorials/dialogue-files-tutorial/tlattitudeevenvisual.png)

#### TLAnimation:

#### TLEmotionEvent:

![](/tutorials/dialogue-files-tutorial/tlemotioneventvisual.png)

Emotion and emotion variation ID numbers are handled in the following pattern:

-   12 possible emotions, which are given ID numbers in powers of 2.
-   8 different .GR2 expression rigs for each of these emotions, the first five of which are generally closed mouth poses when the character is not speaking (this would be \[Emotion\]\_A through \[Emotion\]\_E), and the last three of which are generally open mouthed or teeth bared poses (this would be \[Emotion\]\_X through \[Emotion\]\_Z).
-   The different expression rigs are referred to in the game's files as “variations,” and their variation ID/value numbers roughly correspond to the final letter in the rig name. The reference numbers for the letters still start at 0 like other parts of the timeline file! This means that, for example, a character’s Happy\_B expression rig has the ID value of "1," Happy\_C has the ID value of "2," and so on. The X, Y, and Z expression rigs still follow this pattern (although most characters do not have expression rigs between those A-E and X-Z rigs), making the ID numbers for them 23, 24, and 25 respectively.

I've provided a reference for all of them in the Emotion Rigs Quick Ref tab.  


#### TLLookAtEvent:

#### TLShowWeapon:

![](/tutorials/dialogue-files-tutorial/tlshowweaponvisual.png)

#### TLShowPeanuts:

![](/tutorials/dialogue-files-tutorial/tlshowpeanutsvisual.png)

#### TLSoundEvents:

#### TLSwitchStageEvent:

![](/tutorials/dialogue-files-tutorial/tlswitchstageeventvisual.png)

#### TLTransform:

#### TLShot:

![](/tutorials/dialogue-files-tutorial/tlshotvisual.png)


### Emotion Rigs Quick Ref

In this list, you can find the ID numbers of each given emotion (listed first before the emotion name), followed by a list of the corresponding emotion rigs and their variation IDs.

1 = Neutral

-   Neutral\_A = No variation attribute provided; only the emotion is listed.
-   Neutral\_B = 1
-   Neutral\_C = 2
-   Neutral\_D = 3
-   Neutral\_E = 4
-   Neutral\_X = 23
-   Neutral\_Y = 24
-   Neutral\_Z = 25

2 = Happy

-   Happy\_A = No variation attribute provided; only the emotion is listed.
-   Happy\_B = 1
-   Happy\_C = 2
-   Happy\_D = 3
-   Happy\_E = 4
-   Happy\_X = 23
-   Happy\_Y = 24
-   Happy\_Z = 25

4 = Thinking

-   Thinking\_A = No variation attribute provided; only the emotion is listed.
-   Thinking\_B = 1
-   Thinking\_C = 2
-   Thinking\_D = 3
-   Thinking\_E = 4
-   Thinking\_X = 23
-   Thinking\_Y = 24
-   Thinking\_Z = 25

8 = Angry

-   Angry\_A = No variation attribute provided; only the emotion is listed.
-   Angry\_B = 1
-   Angry\_C = 2
-   Angry\_D = 3
-   Angry\_E = 4
-   Angry\_X = 23
-   Angry\_Y = 24
-   Angry\_Z = 25

16 = Fear

-   Fear\_A = No variation attribute provided; only the emotion is listed.
-   Fear\_B = 1
-   Fear\_C = 2
-   Fear\_D = 3
-   Fear\_E = 4
-   Fear\_X = 23
-   Fear\_Y = 24
-   Fear\_Z = 25

32 = Sad

-   Sad\_A = No variation attribute provided; only the emotion is listed.
-   Sad\_B = 1
-   Sad\_C = 2
-   Sad\_D = 3
-   Sad\_E = 4
-   Sad\_X = 23
-   Sad\_Y = 24
-   Sad\_Z = 25

64 = Surprised

-   Surprised\_A = No variation attribute provided; only the emotion is listed.
-   Surprised\_B = 1
-   Surprised\_C = 2
-   Surprised\_D = 3
-   Surprised\_E = 4
-   Surprised\_X = 23
-   Surprised\_Y = 24
-   Surprised\_Z = 25

128 = Disgust

-   Disgust\_A = No variation attribute provided; only the emotion is listed.
-   Disgust\_B = 1
-   Disgust\_C = 2
-   Disgust\_D = 3
-   Disgust\_E = 4
-   Disgust\_X = 23
-   Disgust\_Y = 24
-   Disgust\_Z = 25

256 = Sleeping

-   Sleeping\_A = No variation attribute provided; only the emotion is listed.
-   Sleeping\_B = 1
-   Sleeping\_C = 2
-   Sleeping\_D = 3
-   Sleeping\_E = 4
-   Sleeping\_X = 23
-   Sleeping\_Y = 24
-   Sleeping\_Z = 25

512 = Dead

-   Dead\_A = No variation attribute provided; only the emotion is listed.
-   Dead\_B = 1
-   Dead\_C = 2
-   Dead\_D =3
-   Dead\_E = 4
-   Dead\_X = 23
-   Dead\_Y = 24
-   Dead\_Z = 25

1024 = Confusion

-   Confusion\_A = No variation attribute provided; only the emotion is listed.
-   Confusion\_B = 1
-   Confusion\_C = 2
-   Confusion\_D = 3
-   Confusion\_E = 4
-   Confusion\_X = 23
-   Confusion\_Y = 24
-   Confusion\_Z = 25

2048 = Pain

-   Pain\_A = No variation attribute provided; only the emotion is listed.
-   Pain\_B = 1
-   Pain\_C = 2
-   Pain\_D = 3
-   Pain\_E = 4
-   Pain\_X = 23
-   Pain\_Y = 24
-   Pain\_Z = 25

### How to Edit - Finding the Right Components

#### FINALLY.

You've arrived at how to edit the Dialog Timeline files! This tab will cover basic information on how to navigate the files, to find the effect components you'd like to edit. The How to Edit - Adding to the Timeline tab will cover how to add new dialogue and cinematics to a file, and The How to Edit - Effect Components tab will cover how to edit specific effect components. You'll need to know what you're looking for before you do either!

So, let's get started!

#### Finding the right effect components

First, find the dialogue node you'd like to edit. You can do this by cross referencing the line of dialogue and the text handle for it with the DialogsBinary file, as described in the section on those files.

This will allow you to find the UUID for a specific dialogue node.

Once you've done that, search for that UUID in the dialog timeline file. Look for its listing in the TimelinePhases section. This will give you its MapValue number, which is  its PhaseIndex number. You can search for that PhaseIndex and its effect components in the code by substituting that MapValue number for the "1" in this line of code here (unless, of course, your PhaseIndex *is* 1):

`
<attribute id="PhaseIndex" type="int64" value="1" />`

This will give you all the effect components of a given node.

Keep in mind that dialogue nodes at the start of the timeline file have a PhaseIndex of 0, which will not be listed in the effect component code blocks. Instead, if the dialogue you'd like to edit has a PhaseIndex of 0, search for EffectComponents to take you to the start of that section. Everything that doesn't have a PhaseIndex is part of the dialogue node you'd like to edit.

#### A note about player responses:

Keep in mind that TagQuestion nodes, and other player responses are not present in the timeline file! Only spoken lines of dialogue and cinematics will be present in these files, because they need specific timing to play properly. Things like dialog options, dice rolls, etc are handled only in the DialogsBinary files.

To edit things like the expressions characters use when selecting dialog options, you'll be looking at the line of spoken dialogue or cinematic directly before the player is given a chance to respond. The animations and expressions from that node will be carried over your responses, so if you'd like to edit that, search for the UUID and PhaseIndex for the previous spoken line of dialog.

Now that you've found what you want to edit, navigate to either the How to Edit - Adding to the Timeline tab or the How to Edit - Effect Components tabs!

### How to Edit - Adding to the Timeline

Hi! You can find instructions on how to add to your dialog timeline here.

Each spoken line of dialogue and cinematic you add in your DialogsBinary file will need to have a corresponding set of effect components in your dialog timeline! And here's how you can add them.

#### Cloning effect components

The easiest way to add onto the dialogue timeline, like adding onto the DialogsBinary files, is to clone existing ones and editing what you need to from there.

I'd recommend looking for dialogue nodes that are similar to what you're adding, and then cloning the effect components from that. (And, of course, if you're trying to add an interaction from one file to another, you can just clone that.)

Once you've found the PhaseIndex for the dialog node (or cinematic!) you'd like to clone, you can easily enclose all the effect components for it by searching for the first instance of that PhaseIndex, and putting a bracket with a nonsense word that isn't used anywhere in the code above it (will explain momentarily.)

Then, you'll want to find the last instance of that PhaseIndex, and put a closing bracket with that same nonsense word below it. You should now have something that looks like this:

`<apples>`
  
`  <all the effect components of the PhaseIndex should be enclosed here>`
  
`</apples>  `

To explain, this will allow you to collapse all of the effect components you need to copy in your code editor, so you can easily copy all of them at once. Using a nonsense word will make it easier to find and clean up later (you'll need to delete these tags before using your code in the game), and will  prevent them from being registered as proper code, leading your mod to function improperly.

I generally use apples. Dunno why! You can use any other word you'd like, as long as it's not a proper tag in the code.

A little tip: You can  use this technique to very quickly copy or delete sections of code in other files, too, like the CharacterVisuals files.

Once you've copied the effect components you need to, I recommend pasting them into a separate file while you're working on them. You will need to do this if you plan on using my Dialogue Timeline Updater, by the way!

#### Updating cloned effect components

**Updating the PhaseIndex:**

The first thing you want to do when adding new effect components is to update their PhaseIndex. You can do so via "replace all" commands in your code editor. You can  use the "change all occurences" function in VSCode by right clicking on a highlighted line of code.

To update the PhaseIndex, replace the existing PhaseIndex line:

`
<attribute id="PhaseIndex" type="int64" value="1" />`

With the number that comes after the last PhaseIndex number already in your file, with something like this:

`
<attribute id="PhaseIndex" type="int64" value="232" />`

If the last existing PhaseIndex is 231, you'll want the PhaseIndex of the new effects you're adding to be 232. If the last PhaseIndex is 39, you'll want your new PhaseIndex to be 40, etc.

You can find the last PhaseIndex in the file in two ways, either by searching for PhaseIndex and navigating to the last instance of it, or by searching for TimelineSpeakers, which will be the next section of the file listed after the EffectComponents section, and will take you directly to the end of that section, allowing you to see the last PhaseIndex number.

Remember, it's easiest to add to the end of the timeline in these files, rather than putting it somewhere in the middle. The placement of dialog phases in the timeline doesn't  matter to the game when playing a scene. The DialogsBinary file will be able to tell the game where to go!

You'll be copying anything you add to the end of the EffectComponents section as well, so it'll help to have an easy way to navigate to it.

Make sure the PhaseIndex has been changed for each effect component you're adding! This will make sure they'll all play together as a group.

**Updating the Timeline Actors, and finding Timeline Speakers:**

Next, you'll want to make sure the Actor UUIDs for the elements you're adding match those of the timeline file. You probably won't have to update these if you're cloning effect components from within the same file, but if you're taking them from a different file, you probably will have to update them.

To do so, first search for TimelineSpeakers in the file you're cloning effects from. This will take you to the UUIDs and Speaker ID numbers for each character in the file with spoken dialogue lines, as well as the player character.

Usually, Speaker 0 is the character you're speaking to in a conversation, and Speaker 1 is usually the player character. These Speaker ID numbers will be listed as the MapKey value above the UUID for the character.

There might be more than these two speakers! If other characters have speaking lines in the dialogue, they'll  be given Speaker IDs in this section.

These are the UUIDs you'll want to update. Select the UUID of Speaker 0, and search for it in your cloned effect components. This UUID should be listed as the Actor for many of the components you cloned.

Then, find the UUID for Speaker 0 in the timeline file you're adding to, again by looking for TimelineSpeakers. Replace the UUID for Speaker 0 in your cloned effect components with the UUID for Speaker 0 in the new timeline file! Then do the same for Speaker 1.

You'll want to update the Peanut character IDs as well. Search for PeanutSlotIDMap in the timeline file you cloned from, and then again in the file you're adding to. Replace the UUIDs in your cloned effect components according to the MapKeys for each of the Peanut characters, like you did for the TimelineSpeakers.

The characters in your edited timeline file should now be able to properly perform the new effect components!

**Updating timing and effect component ID numbers:**

To do this, I highly recommend you use my <a href="https://www.nexusmods.com/baldursgate3/mods/11295">Dialogue Timeline Updater tool</a>. An explanation of it can be found in the Using the Timeline Updater tab, as well as on the mod page for the tool,but I'll  explain a little bit about it here, and why updating all of this is necessary.

Since you're adding onto the end of the timeline, you'll need to make sure all your effect components start right when the last effect component ends. To do so, you'll need to make sure the start times of the effect components match the end times of the previous PhaseIndex components, with the exception of components that begin and end partway through the Phase.

You can do this with the tool I've provided by inputting the end time of the last PhaseIndex in the file, and checking the box giving you the option to reset your start times. This will set the start time of all your effect components to the number you've provided, while preserving the timing of the effect components in relation to each other.

You'll  want to make sure each of the IDs of the effect components are updated. These IDs are unique to each effect component, and aren't referenced anywhere else, but will still need to be unique. You can do this with the tool I've provided. Just input your file when running the Update Effect Component IDs function of the tool, and all of the IDs for your effect components will be updated automatically, leaving all other UUIDs intact.

**What if I want the dialog to be a different length than it already is?**

To make the effect components you're adding last for a different amount of time than they currently have, like if you're adding a new voice line that's a different length from the effect components you're adding, you'll  need to update them manually. This should probably be a function of the tool I made, but it currently is not.

It's still doable, though!

You'll want to update the start times for your effect components first. Then find the length of the line you're adding, and add that number to the start time you just updated. You'll be using this as the new end time for your effect components. You can  add additonal time to this number to add pauses between the voice line if you'd like.

Take the new end time you just calculated, and use "replace all" in your code editor to update all your end times in the file. You'll have to double check to make sure the timing for your effect components, like the timing of emotion changes in TLEmotionEvent, are all contained within your new start and end times. This is especially important when setting a shorter end time than the original one.

Setting the timing outside of your start and end times can cause them to overlap with other dialogue nodes, and cause the game to be unsure of which to select! (If you have stuttering expressions or animations, it might be good to double-check to make sure everything's properly contained within the length of the phase.) 

**Updating voice lines:**

In order to get the game to reference the voice line you need, you'll need to update the UUIDs the DialogNodeID and the ReferenceID in the TLVoice effect component, which will need to be included for any voice lines. These are generally the same UUID, and will be the UUID of your dialog node in the DialogsBinary files.

However, it is possible to randomize voice lines, or include multiple voice lines within the dialogue node. This is explained a bit more in the DialogsBinary section of the tutorial, but, to summarize, different lines of text can be listed under the TaggedTexts section of a dialogue node, and will be given a CustomSequenceID number. In this case, you'll want to put the original dialogue node UUID in as the DialogNodeID in the TLVoice component, and the CustomSequenceID in as the ReferenceID for the line.

**Adding cinematics**

All of the steps before can be used for adding cinematics to files, but you won't need to update the voice lines, which will most likely not be present.

#### Ok, cool. Now that I've updated all that, what's next?

Now you can add your effect components back into the file you're editing. Copy all the effect components you just added, and search for TimelineSpeakers to bring you to the end of the EffectComponents section of the file. Paste all of your updated effect components after the last effect component in this section, and you'll have all your new effect components set up!

You'll need to set up two more things in order to get the game to reference them.

**Phases:**

First, you'll need to add an entry for your dialogue node in the Phases section at the top of the file. Search for EffectComponents to bring you to the bottom of the Phases section; the EffectComponents section comes directly after the Phases section, so searching for it will bring you directly to the end of the list. Then add a new Phase code block. You can just duplicate the one that came before it.

Replace the UUID in your duplicated Phase code block for the UUID of your new dialogue node, as listed in your DialogsBinary file. Then update the Duration of the phase. This will be the total amount of time your dialogue or cinematic takes to play, which you can calculate by subtracting the start time of your effect components from the end time. Make sure you're not calculating it based on effects that start partway through the phase.

**TimelinePhases:**

Very confusing wording, I'm not gonna lie, but still very important. Navigate to this section of the file by searching for PeanutSlotIDMap, which follows the TimelinePhases section, and will take you to the end of it. Then duplicate one of the Object entries in the TimelinePhases section.

Replace the UUID for that Object entry with the UUID for your dialogue node. If you're adding a line of dialogue included as a custom sequence within a dialogue node, you'll want to put your CustomSequenceID UUID here. The UUID in the Phases section should still be the UUID for the original dialog node, and NOT the CustomSequenceID.

Then update the MapValue number to match your PhaseIndex number.

**Oh, and one more thing:**

Now that you've added what you'd like to the timeline, make sure you update the duration of the file overall! Find the end time of your newly added effect components, and set the Duration listed at the top of the file to that same end time. You'll need to update this to make sure your new effect components can play.

Now, you should be all good! You've added your new dialogue to the timeline file!

### How to Edit - Effect Components

This section of the tutorial will give you some tips on editing specific common effect components! The Effect Components - Documentation tab does break down a lot of effect components line by line, but I'll go more in-depth on how to edit some common kinds of effect components here.

#### TLEmotionEvent:

One of the most common effect components you might want to edit is the TLEmotionEvent component.

This controls character expressions during cinematics and dialogue. These expressions are swapped in and out according to the Time attribute given to each expression - this is the exact moment an expression rig is swapped in for the character.

Here's an example code block.


								<node id="EffectComponent">
									<attribute id="Type" type="LSString" value="TLEmotionEvent" />
									<attribute id="ID" type="guid" value="49ec2e56-16cf-43f7-a8f2-f3991d8d1e80" />
									<attribute id="StartTime" type="float" value="39.24994" />
									<attribute id="EndTime" type="float" value="43.54994" />
									<attribute id="PhaseIndex" type="int64" value="4" />
									<attribute id="IsSnappedToEnd" type="bool" value="True" />
									<children>
										<node id="Actor">
											<attribute id="UUID" type="guid" value="cdb171e8-361d-e4e1-c29e-9242fb86ab72" />
										</node>
										<node id="Keys">
											<children>
												<node id="Key">
													<attribute id="Time" type="float" value="39.24994" />
													<attribute id="InterpolationType" type="uint8" value="3" />
													<attribute id="Emotion" type="int32" value="64" />
													<attribute id="Variation" type="int32" value="1" />
												</node>
												<node id="Key">
													<attribute id="Time" type="float" value="40.9499" />
													<attribute id="InterpolationType" type="uint8" value="3" />
													<attribute id="Emotion" type="int32" value="2" />
												</node>
											</children>
										</node>
									</children>
								</node>      
                
                
Remember, the Actor UUID refers to the specific character these expression changes belong to!

To change character expressions, all you need to do is swap out the "Emotion" and "Variation" attributes with the emotion you'd like. As explained in the Documentation tab, the Emotion listed in this code block, of course, refers to the specific emotion a character will use, starting from the Time listed above it.

The Variation below it will point to a specific rig for that emotion! Each character usually only has 8 expression rigs for a given emotion. These are all variants on that emotion, and you can swap them out by changing the "value" for the variation attribute.

In the above example, the first emotion listed is the "Surprised" emotion, which has a value ID of 64. Below it is its variation, variation 1. This  corresponds to variant B of the surprised emotion! Meaning its rig will be the Surprised_B rig of the character. Like most things in the timeline files, the value IDs of the emotion variation rigs starts at 0, unlike the emotions themselves.
You can check the Emotion Rigs Quick Ref tab to find the value ID of the emotion you need!

Now, in the above example, the the second emotion listed is Happy, with no variation. This means that the variation ID is 0, and that the character will start using the Happy_A rig at that time! 

To change this, all you need to do is find the value IDs for the emotion and variaton you'd like, and swap them in for the existing emotion and variation values.

You'll  notice the Time attribute for the second emotion starts partway through the dialogue. Specifically, 1.69996 seconds into it. This is where you can adjust the timing of each expression change!

Tweaking the Time attribute will tell the game what emotion should play when, in relation to the start and end times of the dialog. Just make sure you keep those times within the start and end times for the Phase you're editing, otherwise they'll overlap with other dialog effect components.

You can add new emotion changes by duplicating one of the "Keys" listed for expression changes, and adjusting the emotion, variation, and time attributes as necessary.

You can create really complex sequences of emotions this way, exactly how the game does!

#### TLVoice

This component controls the voice line for a node! However, the actual voice line is not referenced within the timeline file. Instead, the specific voice line is linked to the text handle listed for the node in the DialogsBinary file. This text handle is not only referenced in the Localization files, but is  referenced in a character's voicebank file, and will allow the game to reference the proper audio file.

The UUIDs listed in the TLVoice component are  the UUIDs for the dialog node, group id, and/or custom sequence IDs of the dialog in the DialogsBinary file.

To change the voice line, you'll  want to go into the DialogsBinary file instead, and change the text handle of the node to match the line you want to use!


#### TLShot

This controls camera angle changes! The CameraContainer UUID will link to a Scenecam entry later in the file, which will link to a specific camera angle in the Dialog Scene file. To swap in a new camera angle, just find the UUID for the camera you'd like to use, and then set that as the UUID of your CameraContainer in the node. To find a specific camera, you can double check the timeline actors listed for a scenecam; the scenecams will usually list who the camera is looking at, as well as whether a camera is looking over a character's shoulder, etc. 

This is done within a scenecam entry by listing the actor UUIDs for the AttachTo and LookAt attributes. If a scenecam uses the same UUID for the LookAt and AttachTo attributes, that's usually a closeup with no other characters present!

You can add additional camera angle changes to a dialog or cinematic by adding new TLShot nodes, and changing their Start and End times to last for however long you'd want the shot to last!


### Using the Timeline Updater

You can download my Dialogue Timeline Updater tool from Nexusmods here! This section of the tutorial will tell you how to use it.

I highly recommend you check out the other sections of the guide before checking it out. Otherwise this might not make much sense.

#### What is the tool do?

This tool will allow you to update all timing and/or IDs on the dialogue timeline effect components you're editing automatically, eliminating the need for you to do so by hand.

Trust me, there's potentially hundreds or thousands of effect components in a given dialogue timeline file; you do not want to have to update the start and end times and UUIDs on each one of them individually.

That's where the Dialogue Timeline Updater tool comes in!

#### How to use this tool:

1. First, download the tool from Nexusmods, and extract the folder inside the provided .zip file to another place on your computer.
2. Open that folder and run MGNTN_BG3DialogueTimelineUpdater.exe to start the program.
3. Copy all effect components you'd like to update into a new .xml, .lsx, or .txt file. **DO NOT run the program on your entire dialogue timeline file.**
    \
    I've set up a couple failsafes to prevent you from running the tool on your entire dialogue timeline file, but, just to clarify, the tool is only meant to automate updates to the timing of your effect components, and/or to generate new IDs for them.
    \
    You will need to manually copy the effect components you're updating into a new file, and then copy the updated effect components into your dialogue timeline file once you've made the changes you want.
    \
    It's a very, very basic tool, but it's been a lifesaver for me, and hopefully will be for you, too.

#### Updating Effect Component Timing:

To update the timing on your effect components, navigate to the Update Timing tab of the tool.

This tab will let you input an amount of time to increment all of the start and end times in your effect components by. This is referred to as a "time offset" in the tool, and each start and end time will be updated by that amount of time.

This will prevent you from having to manually update all of the timing in the file, and will  preserve the timing of things like emotions, sound effects, camera angle switches etc, within a given set of effect components.

Say you'd like to increment all your start and end times by half a second. To do so, write 0.5 in the input box in the tab. Make sure to leave the "Reset Start Time" box unchecked, otherwise your start times will be set to 0.5!

Then hit the "Select File and Run Updater" button. This will prompt you to select a file. Select the file you copied your effect components into and run the tool.

All changes will be made within the file itself, with a backup file being automatically generated in the same folder when you run the tool, using the .backup file extension.

The tool will tell you how many lines it changed. Check the file you just updated to make sure everything looks correct, and you can make further edits from there!

##### Resetting start times:

To be honest, this tool is mainly just meant to make it easier to place all of your effect components at the end of the existing timeline. That's what the "Reset Start Time" option is for! This option will clear the existing start time, and replace it with the time offset you set in the input box. It will  preserve the timing of all your effect components in relation to that new start time.

This function will make it so you can grab the last end time of your existing timeline file, input that as your time offset, check the Reset Start Times box, and set all of your effect components to start directly after the end of the existing timeline.

<!--You can see a video example of me doing so here:-->

Again, run the tool and select the file you'd like to update, as explained above. Double-check your file after running the tool, and then make any further desired edits from there!

#### Updating effect component IDs:

Each effect component in a timeline file is given a unique UUID, which will need to be changed when cloning existing effect components. This tool will let you do so, while leaving all other UUIDs untouched!

Navigate to the Update Effect Components IDs tab, and hit the Select File and Run Updater button. Select the file you copied your effect components into and run the tool. That's it!

The tool will tell you how many lines were updated, which should match the number of effect components in your file (you can generally find how many effect components you have by searching for \"\<node id="EffectComponent">" in your file.

Once again, all changes will be made within your file itself, with a backup file being generated in the same folder when you run the tool. Make sure everything looks ok, and then make any further edits you'd like from there!

#### Wait, that's it?

Yep, that's it! For now. Again, this is a very basic tool, and it's really just meant to automate the more tedious tasks required to edit the timeline files. But it's still been helpful for me, and I hope it will be for you!

Once you've made all the changes you'd like, you can copy your effect components into the timeline file you're editing. You can keep editing them from there if you'd like! The effect components only need to be placed in a separate file to run the tool.

Check out the "Adding to the Timeline" tab for further information about adding effect components and dialogue nodes!
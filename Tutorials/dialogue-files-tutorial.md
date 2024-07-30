---
title: Dialogue Files Tutorial 
description: A comprehensive guideline on dialogue files and how to edit them.
published: false
date: 2024-07-30T18:09:05.095Z
tags: tutorial, scripting, data
editor: markdown
dateCreated: 2024-06-12T08:03:36.381Z
---

# Editing Dialogue and Cinematics: A How-To Guide

HI!!!! Welcome to Milo Magnetuning’s guide to dialogue files! There’s a lot to cover, and venturing into these files makes you very brave indeed, but I’ll be here to guide you along the way.

Let’s get started, shall we?

## **SO? WHAT GOES INTO DIALOGUE IN BALDUR’S GATE 3?**

Dialogue in the game is actually handled by a lot of files, some of which I’m still looking into, but the main ones this tutorial will focus on, and the ones you need to edit existing game dialogue are the following:

-   DialogsBinary files
-   Dialog Timeline files
-   Dialog Scene files

There are also two more files you will need to add new dialogue files—which *is* possible, by the way! And you can see an example of that here:


The two files you'll need for adding entirely new dialogue to the game are:

- Generated Dialog Timelines
- Dialog Assets

You'll also need extra files to add new voice lines, which I'll be providing in a separate guide for this wiki as well.

This tutorial will be divided into sections, breaking down what the purpose of each of these files is, the components that go into them, and how to edit them. I've also provided an annotated sample mod and a mirror of some of this tutorial on Nexusmods, which you can find here! The sample mod contains example code with notes breaking what each element in the code does line by line, and you can use it to follow along with this tutorial, or use it on its own, if that would work better for you.

> A note on deprecated files:{.is-warning}

You'll likely also find Dialog.lsj files with that same file name when extracting the files, as well as an extra Dialog Scene file with the .lsx file extension. These files are actually both deprecated! (The Dialog Scene files with the .lsf file extension are what you'll need to edit, NOT the .lsx files. Yes, confusing, I know.)

These deprecated files genuinely do nothing. You don't need to edit them or include them in your mods at all, and I do not recommend you do so. You can actually create fully functional new dialogue without them, so they really do just, nothing.

Thank you very much to <a href="https://next.nexusmods.com/profile/Joell560/about-me">Joell560</a> on Nexusmods for letting me know the files were deprecated! You've saved me a ton of hassle trying to recreate my changes in both files, and it's genuinely saved me so much time.

I used to include these files in my mods, because I thought mismatches between the data in the Dialogs .lsj files and the DialogsBinary .lsf files would cause issues, but that wasn't actually the case. Turns out what I thought were issues with data mismatches were actually just, the changes not being made in the DialogsBinary files.

...The Dialogs .lsj files aren't even necessary for creating *new* dialog; they really just, do nothing in the game as far as I can tell. I'm getting ahead of myself, a little, though!

*Let's get started, shall we?*

## **WHAT THE HECK ARE ALL THESE FILES?**

This section of the tutorial will provide a basic summary of each of the dialogue files listed above. Each file will get its own, more in-depth section later, don't worry! But all of these files are, of course, extremely interconnected, and it'll help to have some basic information before we get into specifics.

Let's start with the Dialog Timeline files.
####

The Dialog timeline files can usually be found in the \\Data\Public\GustavDev\Timeline\Generated folder when you extract them from the game. Some timeline files can be found in the Gustav folder as well, but they’ll still be in a \\Timeline\Generated folder.

These files control the timing of all elements required to play dialogue and cinematics, including (but not limited to) the actual voice lines, character animations, the emotions the characters use, camera angles and shot changes, and sound effects. They control all aspects of dialogue that require full animation and timing—which does not include moments where your character picks dialogue options! Those are covered in the DialogBinary files, which I'll be explaining more later.

A good way to think of the dialogue timeline files, and the dialogue in this game in general, is actually to picture it like a movie! With each individual line of dialogue as a small scene within that movie. The code in the dialogue timeline files gives the game everything necessary to play those scenes, and what element of the scene play when.

Fun fact, by the way: cutscenes are actually just regular dialogue files! They switch between lines of dialogue and cinematics—sections of animation without voice lines—to create a given scene.

This also means that cinematics are sorta like mini cutscenes, including the cinematics for kisses!

It’s important to note, though, that these little scenes within the timeline files aren’t actually played in order. While the timeline itself is like a movie, the game is almost constantly skipping around within it to play the scene—or line of dialogue—it needs.

And that’s where the DialogsBinary files come in!
####

The DialogsBinary files are generally found in the \\Data\Mods\GustavDev\Story\DialogsBinary folder when you extract them from the game, and are then further broken down by what section of the game they belong in, like if they’re from Act 3, or the Tutorial level, or if they’re meant to be Companion dialogue, and so on. You might also find these files in the Gustav folder, but they’re still broken down in a similar way.

Now, if the dialogue timeline files are like a movie, then DialogsBinary files are like a chapter skip function on a DVD. These files contain the information the game needs to reference your choices in dialogue, and select which voice lines or cinematics to play, and when. They also contain information on dice rolls, links to nested dialogue files—which I’ll explain a more about later—and are where the game tests for whether a line of dialogue or or player response should be accessible or not. They can also be used by the game to set flags it can test for in other areas of the game, and can link to information on companion approval.

Dialog Scene files
####

The Dialog Scene files contain information on camera and character positioning when the dialogue is triggered, as well as lighting, which characters can be present in the dialogue, and can also be used to control character scale within a scene! Which is fun.

They can also inherit information from other files, the most important of which is the default dialogue scene file, which is often linked at the bottom of the file. The default Scene files can be usually found at this file path here:

\\Public\Shared\Timeline\Scenes\Default\

You actually might not have to edit these files often, but it's still important to note! And they'll absolutely be necessary when creating entirely new dialogue files.

The DialogsBinary, Dialog Timeline, and Dialog Scene files for a given scene will all have the same file name, with the Dialogue Scene files just appending the word Scene to that same file name.

Generated Dialog Timelines
####

The GeneratedDialogTimelines files contain information linking each DialogsBinary file to its proper timeline file, as well as each of the characters, props, scenery, and so on that are referenced by the timeline files. These files are huge, and contain information on most of the dialog timelines in the game. You should generally only include the entries for the dialog timelines you're editing in your mods, though!

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


## **HOW DO YOU EDIT THE DIALOGSBINARY FILES?**

These sections of the tutorial will be broken down into tabs, one containing a further explanation of the DialogsBinary files, one containing information on the elements in them, and one explaining how to edit them.

Honestly, just understanding what you're looking at is half the battle when editing dialogue! So I highly recommend checking out the documentation tab before you begin.

**The How to Edit tab also contains a short guide on creating custom game flags!** If you'd like to know how to do so, you can find instructions there!

## Tab {.tabset}

### A Summary

As mentioned before, the DialogsBinary files are essentially like a chapter skip function on a DVD, telling the game which line of dialogue to play and when.

This is done within the code of the DialogsBinary files, which link together a variety of different types of dialogue node. This is done by linking one dialogue node to the ones that are supposed to come after by the “children” attribute. When you list the UUID of one dialogue node as a “child” of another node, the game will see that UUID and know that “child” is the dialogue node that should play next. A dialogue node can have multiple “children,” which can be tested for using the CheckFlags attribute to know which line to play, or these multiple “children” could actually be sets of player choices following a given line of dialogue, which will then lead to further branching paths depending on what the player selects.

This is how the game navigates through scenes, by following and testing for these different branching paths between different types of dialogue nodes.

And yes, there are different types of dialogue nodes! These types determine what kind of behavior to perform for that node. Is a character speaking, or is the player given the opportunity to respond? Should a dice roll be performed, or is this a cinematic cutscene that needs to be played?

### Documentation

As mentioned in the summary, the main elements in a DialogsBinary file are dialogue nodes.

There are 11 different types of dialogue node that I’ve found so far. Keep in mind this game is huge, and there are a ton of dialogue files and different scenes in the game. There might be something I’ve missed. But I have looked at these files extensively, these are all I’ve found at this point!

These different dialogue nodes are TagGreeting, TagAnswer, TagQuestion,TagCinematic, ActiveRoll, PassiveRoll, RollResult, Alias, Jump, Nested Dialog, and RootNodes.

TagGreeting
####

TagGreeting nodes are the first line of dialogue a character will say to you when speaking to them. These are also paired with a corresponding Root Node at the end of the file. These TagGreeting nodes can then be followed by further dialogue nodes, or they could be a single line of dialogue, followed by the end of a conversation. That last bit is really common for NPCs. The greeting a character uses can be tested for using the CheckFlags attribute, allowing a character to use different lines of dialogue when initially speaking to them, depending on the conditions that have been set.

TagAnswer
####

TagAnswer nodes are used for dialogue lines from speaking characters. This is usually the character you’re directly speaking to, but other characters can be included in conversations, such as when companions have voice line reactions to what’s going on. These are also given the TagAnswer label.

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

PassiveRoll nodes are very similar to ActiveRoll nodes! However, these are the passive rolls, like for perception and arcana, that are made automatically for the player in dialogue. The results for these rolls are also handled via the RollResult dialogue nodes.

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

Root nodes are unique, in the sense that they're generally mirrors of other nodes. The root nodes refer to the possible first lines of dialogue in a given scene or conversation, and are generally referring to TagGreeting nodes, but other types of nodes can be referenced as RootNodes. When a dialogue node in a file is considered a root node, that line of dialogue will have a RootNodes entry with its UUID listed at the end of the file, and will also be marked in its own code block with the Root attribute, which will be set to True.

### How To Edit

Honestly, the easiest way to edit these files, at least if you're adding new elements, is to duplicate existing code blocks. This will guarantee you'll keep the code structure the game needs consistent, and saves you a bit of work typing everything out.

I've actually provided an annotated sample/template mod on Nexusmods <a href="https://www.nexusmods.com/baldursgate3/mods/10086">here,</a> which you can use to follow along with this guide, and understand a bit more about what goes into the code structure for a given node.

Now, let's begin!

**Editing existing files**
####

When editing existing files, you'll first need to find the dialogue nodes you'd like to change. This can be done by searching for the dialogue you're looking for in an extracted Localization file, which I've provided in the above link as well, for each language the game has been translated into.

I also *highly* recommend using the <a href="https://www.tumblr.com/roksik-dnd/727481314781102080/bg3-datamined-dialogue-google-drive">parsed dialogue files</a> provided by roksik-dnd on Tumblr. These will not only help you find lines of dialogue from the game, but will also serve as a guide to the structure of the dialogue tree you're editing, which lines of dialogue follow which other lines, the branching paths available in the scene, and so on.

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

A note: when adding player responses (which will be labeled as TagQuestion nodes), the order the children are listed under a dialogue node will also be the order they're displayed in the game, listed from top to bottom.

Also, when multiple children are listed under a character's speaking line (labeled as a TagAnswer node), and they're not player responses, these are usually lines of dialogue that are being tested for certain conditions, to determine whether they should play or not. In this case, the order the children are listed in is the order the game will test them in, with children placed higher in the list taking priority.

**Checking game flags**
####

The checkflags attribute is how the game tests whether a line of dialogue should be available or not. When a given flag is set to True under the checkflags attribute, that means the dialogue node will only be available if that flag is set to true. When the flag the game is testing for is set to False, then that line of dialogue will only play if the flag is *not* true.

To edit the conditions a line of dialogue will be available under, you can add or remove flags for this attribute. Check their UUIDs to make sure you're testing for the right ones! Also, take a note of what kind of flag it's testing for; if the game's testing for a Tag, it's testing what character tags a given character has. When the flag type is a Global flag, it's testing for a flag that's present in the game globally, and not just applied to a specific character. Local flags seem to be flags set for the player character, and Object flags are testing to see whether the character you're speaking to has a given flag set for them (these are distinct from tags; flags are conditional, and are usually set during gameplay, as opposed to tags, which are used to determine different qualities of a character, like whether they can participate in dialogue or not!).

**Setting game flags**
####

The setflags attribute will allow you to set game flags when that dialogue node is played. This can be done by listing the UUID for the game flag, and either setting it to True to enable the flag, or setting it to False to disable it. You can also make your own custom flags!

**Making custom game flags**
####

Making custom game flags is actually pretty straightforward! All you need to do is find an existing game flag file, and duplicate it to begin editing it. Generate a new UUID for the flag within that file, give it a new name, a description to remind you what the flag is for, and then change the file name to the UUID you gave the flag within the code. Keep in mind the usage type! As mentioned above, there are multiple different kinds of flags, which usually correspond to their usage type.

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

You'll also need to make sure the nested dialogue you're linking to is listed as a child in the Dialog Assets entry for the original dialogue, and add the original dialogue as a child of the nested dialogue if you'd like to be able to return to it.

I'll be covering more about how to create new nested dialogue files, as well as creating new dialogue files generally at the end of this tutorial! You can scroll to the end of the page to find it.


## **HOW DO YOU EDIT THE DIALOG TIMELINE FILES?**

And now for the Dialog Timeline files. These are very lengthy and complicated files, and some parts of editing them can be extremely tedious, time consuming, and potentially, like, almost impossible without a python script to automate some parts of editing them.

...It's a good thing, then, that I made a tool to automate those tasks! You can find it on Nexusmods <a href="https://www.nexusmods.com/baldursgate3/mods/11295">here.</a>

It's an extremely simple tool, and is basically the Python scripts I've been using to update timeline files put into a tkinter UI, but it's been a lifesaver for me when editing these files.
  
Like the DialogsBinary section, I'm also going to be breaking this section of the tutorial into different tabs.

You can find instructions on how to use my Dialog Timeline updater in the Using the Timeline Updater tab, as well as on the Nexusmods page for the tool.

The Summary tab offers a bit more explanation on how these files work, the Anatomy of a Dialog Timeline tab explains the structure of the files overall, the Effect Components tab will break down the different EffectComponents in the files, the How to Edit tab will go over editing the files, and the Emotions Quick Ref tab lists out the expression rigs used by the game, with the ID and variation numbers you'll need to reference them in the files.

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

Another thing to note is that the Phases section is in sequential order, and that order corresponds directly to the MapValue and PhaseIndex for the dialogue node! The timeline also starts counting the phases from 0 (which is how most animation/video program timelines handle things as well). 

Phase 0 is placed at the top of the timeline, and is not given a PhaseIndex number, because it's unnecessary with it at the start of the timeline. This also means that the second listed phase will be PhaseIndex “1”, the third listed phase will be PhaseIndex “2,” and so on. You can actually mess things up by changing this order!

When adding things to the timeline, I highly recommend adding everything to the end of each section in the file. This will keep your phase order consistent, and prevent you from having to update the entire timeline at once.

You can also prevent dialogue from functioning by skipping PhaseIndex numbers! Make sure you don't have any gaps in your PhaseIndex numbering as well.

Keep both of those things in mind and you should be good! (And also save yourself just, a ton of work.)

####   
TimelineSpeakers: 

Contains the UUIDs of which character is performing what action, and which character is being referenced in general! These UUIDs are specific to a given set of dialogue files, and are linked to in the corresponding DialogBinary file for the timeline, which will be connected to either the UUID for the speaking character, or the UUID for the player character.

The structure of this section is arranged into “Objects,” followed by MapKeys and MapValues, the former of which refers to what speaker number a character was given, and the second is the aforementioned UUID referring to the character.

Speaker 0 is generally the person your character is talking to, with Speaker 1 being your character. Speaker roles after that may be listed if narration is present, or if other characters beyond the character you’re speaking to have lines (like when other companions have reactions during a conversation). You’ll want to cross reference the TimelineSpeaker UUIDs with the same UUIDs in the DialogsBinary file, so you’ll know what character is being referenced by them.


The most important thing to know about the Timeline Speakers, and Timeline Actors, though, is that you want to make sure any components you copy over from other files are updated to use the Timeline Speaker UUIDs from the file you copied them into. If you don't update them, the components you added won't be able to reference the characters properly, and you could end up something like [THIS](https://drive.google.com/file/d/1EIVmKs6qtHvgeUopn5bnDr7q6VgYhQ7w/view). Which is not ideal, for sure!

If you're not sure what any of these terms mean, don't worry! There's more information about them in the Effect Components tab, and I've also be covering how to update timeline speaker UUIDs in the How to Edit tab.

Let's continue on with the other sections in the timeline files, first, though.  
 

#### TimelineActorData:

This section contains several long lists mapping out each effect component in the timeline and the UUIDs of the characters performing them, pulled from both the TimelineSpeakers and PeanutSlotIdMap sections. However, I think it's likely these lists are used for Larian's game engine, to allow it to reference the components, and don't seem to do much in the game itself. Even leaving these MapKey lists entirely unedited didn't change anything, in the game, so I don't actually think you have to worry about the component map.

There *are,* however, things in this section you'll likely need to update, especially when cloning elements from other files. These are the "scenecam" and “scenelighting” actors. These are not characters, but instead refer to specific camera angles and lights necessary for the dialogue, and are also often located in the corresponding Dialogue Scene files, which have their own section on this page. If the camera angles referred to in a dialogue node are not present in the TimelineActorData section, the game will not be able to properly reference the camera, and you'll likely get the camera pinned to the floor instead.

#### TimelinePhases:

As discussed in the Phases section above, this section contains UUIDs in a list of MapKeys and MapValues. The UUIDs here will correspond to the UUIDs in the Phases section of the file. The placement of that phase in the Phases section, as well as in the EffectComponents section will match the MapValue listed for the MapKey in the TimelinePhases, starting from zero. (Again, most animation programs and video editors also start their timelines from 0, so this is probably why BG3 handles its timelines like this, too.) That MapValue number is also the PhaseIndex number you'll be looking for when editing and cloning components in the EffectComponents section for your mods.

That same UUID belongs to a specific dialogue node in the DialogBinary file, and all components related to it are what plays when that line of dialogue is called by the game.

Important to note is that the MapKey order here does not have to match the phase order! Most of the elements of the timeline files have to be sequential, but these do not. I still recommend appending your additions to the end of the section, just to make everything easier to keep track of.


#### PeanutSlotIdMap:

This is similar to the TimelineSpeakers section mentioned above, but it actually refers to the characters standing behind the player character during a conversation. Like the peanut gallery! Definitely one of my favorite variable names for sure. Any references to “Peanuts” in the dialogue files is about these characters. And the UUIDs here are meant to map out things like emotions/animations/etc for these characters according to what “slot,” or placement behind you the characters are.

From what I can tell, these characters are not ever referred to in the DialogBinary files, unlike the TimelineSpeakers, probably because they don't speak, and can be any companion or hireling character. This means the animations of the characters behind you are tied to which of 3 placements they've been put into, rather than a specific character.  
 
#### AdditionalLocations:

If a scene needs to take you to a different location for the scene to play, the triggers for those locations will be listed here. These can then be called by the TLSwitchLocationEvent effect component.

#### What about the rest of the file?

The rest of the sections in the timeline file are either things that likely should be kept consistent, don't seem to affect much in the game when changed, or don't seem to actually contain information in most of the files I've seen. I'll be experimenting more with them, though! But you likely won't need to worry about them much for most of your own dialogue mods.

  
…And, with that, we're ready to move on! Check the Effect Components tab to continue with the tutorial.

### Effect Components
 
#### OK, I'M READY. WHAT IS GOING ON WITH THOSE EFFECT COMPONENTS?

The EffectComponents section is the bulk of what you’ll be getting into and editing for your dialogue mods. This section contains all the actual information on timing, character animations, poses, staging, expressions, sound effects, voice lines, camera angles, and more that need to be referenced to play the dialogue or cinematic. Most of the other sections in the file are meant to help the game reference this information, but the effect components are the true core of the dialogue system.

Effect components are classified into several different “Types,” each of which performs a unique function, which I'll list below.

There’s a lot to go through, so strap in!  
 

#### What types of effects components you can choose from?

So far, I’ve found the following effect components, each of which controls a different aspect of dialogue, and each of which has different set of attributes, which I’ll explain shortly. For now, though, I’m just going to give a brief rundown of each:

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
     

#### Ok, cool. What do you mean by “attributes," though?

Each effect component in a timeline file is broken down into several variables, or attributes, as well as the times that each component and attribute will trigger and end. Each type of effect component has a different set of possible attributes, although there are common attributes most if not all component types share. I'll be breaking down each type of effect component and their attributes in this section of the tutorial, with example code blocks explaining what each element of them means line by line.
  
Keep in mind that not every possible attribute for these components will be present every time! Which means some possible attributes the game can process may not be listed in this tutorial yet. If you find one I missed, please let me know!

Also, some of the attributes I included in these explanations contradict each other, and will not be found in the same instance of that effects component. I've generally pointed it out when this happens, but a good rule of thumb will be to look at examples of the same type of effects component you're editing, to know what attributes are usually included in them, and which are not.

This section is likely going to be very long, but hopefully having explanations of what everything is makes it a bit less intimidating! These files can be a lot to look at, but the more you understand about them, the less daunting it'll be to edit them.

Let's get into it! I'll start by explaining some common attributes you'll see in most effect components:  
 

#### A GUIDE TO COMMON EFFECT COMPONENT ATTRIBUTES

#### Type:

Pretty self explanatory. The type of effect component, which will be one of the kinds of components I listed above.  
 

#### PhaseIndex:

`<attribute id="PhaseIndex" type="int64" value="1" />`

As mentioned above, the PhaseIndex refers to every component necessary for a given dialogue node, which will be played as a group according to their given start and end times (explained below). All components with the same PhaseIndex number belong to the same dialogue node! For your own mods, you’ll want to make sure this number is unique, sequential, and is tied to the same MapValue number and placement in the TimelinePhases and Phases sections, respectively. You'll also want to make sure all elements you add for your dialogue node have the same PhaseIndex, so they'll be grouped together, and play properly as a unit.

Also, again, the first dialogue node on the timeline will not have a PhaseIndex listed for its components. Its PhaseIndex number is actually 0, but, being at the start of the timeline, the game’s code doesn’t require it to be listed.  
 

#### StartTime and EndTime:

`<attribute id="StartTime" type="float" value="7.42" />`

`<attribute id="EndTime" type="float" value="9.21491" />`

Pretty self-explanatory! The start and end time for each component within the phase, according to its placement within the whole dialogue timeline. A few things to note, though:

-   The first phase on the timeline, again, starts at 0, so it generally does not list start times for its components, unless one of those components is meant to start partway through the dialogue. It usually will list end times, though.
-   The start and end times listed do not actually have to match the full length of the phase! Some effect components start and/or end partway through the phase, which can be used to add pauses between lines of dialogue.
-   These start and end times are placed within a massive timeline, and they are, again, sequential. As mentioned earlier, it helps to imagine the dialogue timeline like a movie, and the phases in the timeline are little chapters you can skip to within it, with each component playing at specific times within that chapter, according to these start and end times.
     

#### Time:

Some components list start and end times, and then are further broken down into “Time” elements. These are seen in components like TLEmotionEvent and TLLookAtEvent, among others. I mentioned this above, but to reiterate, the “Time” attribute refers to when a certain effect is supposed to start, they just don’t have equivalent end times. Instead, the next instance of the “Time” attribute will replace the previous effect listed within the component.

This may be because some of these attributes are meant to persist, even after the game has moved onto the next dialogue node! Two examples of these are TLEmotionEvent and TLAttitudeEvent. The animations from these two effects components are carried into the next node, and are often used to preserve the characters' expressions and attitude animations while you're picking dialogue options. These attributes are not given a definitive end time, because they're meant to persist until the next instance of the attribute is called, or the dialogue ends.  
 

##### A note about timing in general:

The StartTime, EndTime, and Time attributes are all handled *extremely* precisely, with times often being very, very tiny fractions of a second.

This is extremely helpful with facial expressions in particular—each character actually only has around 8 expression rigs for any given emotion, and the total number they have is relatively small. But by using the precise timing the game allows, it almost never feels like they’re using so few expression rigs. You can make extremely complex sequences of emotions using this method, making the characters’ expressions feel unique, despite how few rigs they actually use.

I’ll be getting more into the TLEmotionEvent components later! But, for now, there’s still three common elements to talk about:  
 

#### IsSnappedToEnd:

`<attribute id="IsSnappedToEnd" type="bool" value="True" />`

Honestly, I think this might just be used by Larian's game engine, to make sure each effect component snaps to the end of the previous phase. This doesn't seem to affect things when changing it on the .xml level. 
 

#### ID:

`<attribute id="ID" type="guid" value="49292981-224c-4feb-a51b-fa7bf0fb46f3" />`

The unique UUID for the specific effect component you’re looking at. It’s generally a good idea to generate a new one for each effect component you add, which my dialogue updater tool can take care of for you. (More explanation can be found in the

A note: other UUIDs within an effects component are connected to other things, like animations, camera positions, and the characters performing the listed effects. My dialogue updater will only change the IDs for the effects components themselves, and won't touch any other UUIDs, but make sure you're careful if you're manually editing them. You'll want to make sure all other UUIDs are the same as the elements (like camera positions, animations, etc) you want to reference.

Which brings me to the last common attribute:  
 

#### Actor:

`<node id="Actor">`

`            <attribute id="UUID" type="guid" value="55bce89d-670d-f7c9-6e3b-38ebe3322b32" />`

`</node>`

This UUID refers to which character is performing the effects component! These are usually unique to each timeline file, and will need to be updated to match when cloning effects components from other files. The component won’t be able to reference the related character if this UUID is not updated.

#### OK, SO, WE’VE COVERED THE BASICS. WHAT ABOUT SPECIFIC EFFECTS COMPONENTS?

The moment you’ve all been waiting for! Maybe. I’m now going to be breaking down each kind of effects component by its attributes. These are only example components—they won’t refer to anything specific, and almost all values for the attributes have been generated new (and are almost certainly nonfunctional).

I also provided explanations for all attributes I could find within these code blocks—which means that some of the attributes shown in these blocks actually contradict each other! And should not be used at the same time. One example is the “IsMimicry” and “PeanutOverride” attributes. These attributes seem to be mutually exclusive; from what I can tell, the IsMimicry tag is used when things like emotions/attitude animations/etc need to be copied over onto “peanut” characters i.e. the characters standing behind your character in conversations. The PeanutOverride attribute marks a component block as being a unique override for a peanut character, separate from the player character.

These tags actually may be a tag for Larian's game engine to process; they don't seem to affect much when changed. But still, as I mentioned in the code blocks below, they should likely still be updated when changing these blocks, and shouldn't be used together.

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
-   The different expression rigs are referred to in the game's files as “variations,” and their variation ID/value numbers roughly correspond to the final letter in the rig name. The reference numbers for the letters still start at 0, though, like other parts of the timeline file! This means that, for example, a character’s Happy\_B expression rig has the ID value of "1," Happy\_C has the ID value of "2," and so on. The X, Y, and Z expression rigs still follow this pattern (even though most characters do not have expression rigs between those A-E and X-Z rigs), making the ID numbers for them 23, 24, and 25 respectively.

I've provided a reference for all of them below.  
 

##### **A quick reference for Emotions and their variation ID numbers:**

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

-   …..
---
title: Dialogue Files Tutorial 
description: A comprehensive guideline on dialogue files and how to edit them.
published: false
date: 2024-07-30T04:50:54.168Z
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



The two files you'll need for adding new dialogue to the game are:

- Generated Dialog Timelines
- Dialog Resources

This tutorial will be divided into sections, breaking down what the purpose of each of these files is, the components that go into them, and how to edit them. I've also provided an annotated sample mod and a mirror of some of this tutorial on Nexusmods, which you can find here! The sample mod contains example code with notes breaking what each element in the code does line by line, and you can use it to follow along with this tutorial, or use it on its own, if that would work better for you.

Now, let's get started, shall we?



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



## **WHAT ARE DIALOGUE BINARY FILES?**



## **WHAT ARE DIALOGUE TIMELINE FILES?**



First, though, I want to get into the timeline files. These are very lengthy and complicated files, and you will absolutely need to use a script to update the start and endtimes of anything you add to them. I’ll be covering mine when I get into how to work with the files in earnest!

I'm starting here for two reasons: one, the timeline files currently have the least documentation—I have not been able to find *any* other resources on them, actually. The information on timeline files in this tutorial was compiled entirely from me experimenting and working with them over the last few months. The other reason is that really, these *are* the hardest files to work with—but once you've gotten a good grasp on how they work, everything that comes after will be a breeze.

(You can, however, find the breakdowns of other kinds of dialogue files in the navigation on this page! If you're getting overwhelmed by the timeline files, DialogBinary files might be a good place to start instead. Once again, venturing into these files makes you a brave soul indeed—but I believe in you all the way! Just, make sure to take breaks when you need to.)

…Now, let's get into it! I'll start by breaking down the elements that go into the timeline files.  
 

### **ANATOMY OF A DIALOGUE TIMELINE FILE**

Dialogue timeline files are broken down into a several sections, the biggest of which—EffectComponents—I'll be covering last. The EffectComponents section contains most of the actual information about the dialogue being played, so it is both extremely lengthy, and references a majority of the other sections in the timeline files. Covering the others first will make the EffectComponents section make a lot more sense. I'll be covering each other section in the order they appear in the files, skipping the EffectComponents for now. 

These sections are:  
 

#### **Duration:**

The total duration of all the dialogue and cinematics possible in the scene combined. Make sure you update this to account for anything you add to the dialogue! The elements you've added will not be able to play properly if you don't.

There’s not much to say about it beyond that, honestly! It’s one line, and yet I have managed to say 67 words about it anyway!  
 

#### **Phases:**

Dialogue phases are what control the actual timing of each dialogue node. A dialogue node refers to each separate line of dialogue a character might have, generally marked by the captions for the dialogue changing! Cinematics—the term the game uses for cutscenes and animations without voice lines—are also counted as unique dialogue nodes within the game’s files. These phases group together all elements for a single dialogue node, allowing them to play out in their proper timing when the dialogue node is called for.

A good way to picture the dialogue timeline files in general is to imagine them like a movie! Each bit of dialogue is contained within that movie, and you can think of phases as being specific, very brief scenes within that movie you can skip to at any time, timestamped for your convenience.  
 

##### These phases have four elements:

-   **Duration:** The total length of the specific dialogue node or cinematic, and all elements included for them.
-   **PlayCount:** The number of times the dialogue will play in a row. I’ve never seen this be anything but 1, likely because it’d just be playing the same dialogue multiple times in a row, which probably isn’t ideal! Although, hm. I guess you could use it for stuff like INFINITE KISS WYLL MOD. A not hypothetical and totally actually real WIP of mine, limited by the fact you cannot actually insert “infinity” as a character into the code (and indefinite recursion is almost always a bad idea in any case). I just love him dearly ok.
-   **DialogueNodeID:** Linked to the TimelinePhases section found later in the file, as well as the UUID for the specific dialogue node the phase is for, which can be found in the DialogBinary files. I’ll be covering DialogBinary files later, but for now, all you need to know is that this UUID will tell the game what group of dialogue elements to play, and when.

You can find the specific phase number associated with that dialogue node via that UUID! That same UUID will link to a MapKey and associated MapValue number, again, in the TimelinePhases section. That MapValue number is linked to the PhaseIndex for the elements in the EffectComponents section. That listed PhaseIndex number groups together all related effect components for that dialogue node! These components will be the bulk of what you’ll edit for your own dialogue mods, and, again, will be covered later.

-   **QuestionHoldAutomation:** I believe this is *might* help automatically trigger pauses for “question” dialogue nodes, i.e., your character’s responses. I haven’t experimented with it much though! Something to note: I’ve not seen any file that didn’t have QuestionHoldAutomation after every dialogue node yet, but most timelines also have a setting later in the file regarding QuestionHoldAutomation that is usually set to “False.” So, who knows! I'd recommend you keep both of these consistent in your own mods, though, just in case.

Another thing to note is that the Phases are in sequential order, and that order corresponds directly to the MapValue and PhaseIndex for the dialogue node! The timeline also starts counting the phases from 0 (which is how most animation/video program timelines handle things as well). Phase 0 is listed at the top of the timeline, and is also not given a PhaseIndex or MapValue number, because it’s unnecessary, being at the start of the timeline. This also means that the second listed phase will be PhaseIndex “1”, the third listed phase will be PhaseIndex “2,” and so on. You can actually mess things up by changing this order!

When adding things to the timeline, I recommend appending everything to the end of each necessary section. This will keep your phase order consistent, and prevent you from having to update the entire timeline at once.

And you can also prevent dialogue from functioning by skipping PhaseIndex numbers! Make sure you don't have any gaps in your PhaseIndex numbers as well.

Keep both of those things in mind and you should be good! (And also save yourself just, a ton of work.)

####   
TimelineSpeakers: 

Contains the UUIDs of which character is performing what action, and which character is being referenced in general! These UUIDs are specific to a given set of dialogue files, and are linked to in the corresponding DialogBinary file for the timeline, which will then be connected to either the global UUID for the speaking character, or the UUID for the player character.

The structure of this section is arranged into “Objects” followed by MapKeys and MapValues, the former of which refers to what speaker number a character was given, and the second is the aforementioned UUID referring to the character.

Speaker 0 is generally the person your character is talking to, with Speaker 1 being your character. These roles are also referenced in the corresponding DialogBinary files. Speaker roles after that may be listed if narration is present, or if other characters beyond the character you’re speaking to have lines (like when other companions have reactions during a conversation). You’ll want to cross reference these TimelineSpeaker UUIDs with the same UUIDs in the DialogBinary file for the scene you're working with, so you’ll know what character is being referenced by them.

  
To give you an example, the UUID for Speaker 0 in the above screenshot actually refers to Lae’zel in the timeline file for her InParty dialogue. You can cross reference that UUID in the corresponding DialogBinary file to find her global character UUID, as well as see the speaker number she's given, which will match the one for her in the timeline file.

Anything that references her UUID from the TimelineSpeakers section is related to her. So, if that UUID is listed as the “Actor” for a voice line (referring to which character is performing what element of the dialogue), that voice line will be spoken by her. If it's listed under a TLEmotionEffect component, then that component controls her expressions in the dialogue. If she's being referred to as the Target in a TLLookAtEvent component, then she's the character being looked at.

The most important thing to know about the Timeline Speakers, though, is that you want to make sure any components you copy over from other files are updated to use the Timeline Speaker UUIDs from the file you copied them into. If you don't update them, the components you added won't be able to reference the characters properly, and you could end up something like [THIS](https://drive.google.com/file/d/1EIVmKs6qtHvgeUopn5bnDr7q6VgYhQ7w/view). Which is not ideal, for sure.

If you're not sure what any of these terms mean, don't worry! They'll all be covered when we get to the EffectComponents section of the tutorial, and I'll also be covering how to update timeline speaker UUIDs when we actually start working with the files.

Let's continue on with the other sections, first, though.  
 

#### TimelineActorData:

This section contains several long lists mapping out each effect component in the timeline and the UUIDs of the characters performing them, pulled from both the TimelineSpeakers and PeanutSlotIdMap sections, the latter of which I'll be covering shortly. However, I think it's likely these lists are used for Larian's game engine, to allow it to reference the components, and don't seem to do much in the game itself. Even leaving these MapKey lists entirely unedited didn't change anything, despite adding new components to the dialogue timeline. All dialogue played as normal, even the newly added components. For this reason, I actually don't think modders need to worry about updating the MapKey lists here at all.

There *are,* however, two actor types contained within this section you will likely need to update, especially when cloning elements from other files—the "scenecam" and “scenelighting” actors. These are not characters, but instead refer to specific camera angles and lights necessary for the dialogue, and are also often located in the corresponding Dialogue Scene files, which will be covered later. If the camera angles referred to in a dialogue node are not present in the TimelineActorData section, the game will not be able to properly reference the camera. This is, in highly technical terms—bad. It won't damage your game or your hardware (Baldur's Gate 3 is very forgiving when it comes to modding issues, which is good, because this is not true of all games. \**Screams in Sims 2\**). It will, however, likely lead to the game's camera getting pinned to the ground at your character's feet, which is not ideal, especially if you want to see what's going on. If you're having trouble with that, make sure you've got all the necessary scenecams and scenelighting you need in this section of the file.  
 

#### TimelinePhases:

As discussed in the Phases section above, this section contains UUIDs in a list of MapKeys and MapValues. The MapKeys in this section will match the UUID for a phase in the Phases section of the file. The placement of that phase in the timeline will match the MapValue listed for the MapKey in this section, starting from zero. (Again, most animation programs and video editors also start their timelines from 0, so this is probably why BG3 handles its timelines like this, too.) That MapValue number is also the PhaseIndex number you'll be looking for when editing and cloning components in the EffectsComponents section for your dialogue mods. That same UUID belongs to a specific dialogue node in the DialogBinary file, and all components related to it in the timeline file are what plays when that line of dialogue is called for by the game.

Important to note is that the MapKey order here does not have to match the phase order! Most of the elements of the timeline files have to be sequential, but these do not. I still recommend appending your additions to the end of the section, just to make everything easier to keep track of.

This is a lot of repeat information, but I thought it'd help to have it listed under the proper header, too!  
 

#### PeanutSlotIdMap:

This is similar to the TimelineSpeakers section mentioned above, but it actually refers to the characters standing behind the player character during a conversation. Like the peanut gallery! Definitely one of my favorite variable names for sure. Any references to “Peanuts” in the dialogue files is about these characters. And the UUIDs here are meant to map out things like emotions/animations/etc for these characters according to what “slot,” or placement behind you the characters are. From what I can tell, these characters are not ever referred to in the DialogBinary files, unlike the TimelineSpeakers, probably because they don't speak, and can be any companion or hireling character. This means the animations of the characters behind you are tied to which of 3 placements they've been put into, rather than a specific character.  
 

### What about the rest of the file?

The rest of the sections in the timeline file are either things that likely should be kept consistent, don't seem to affect much in the game when changed, or don't seem to actually contain information in most of the files I've seen. I'll be experimenting more with them, though! But you likely won't need to worry about them much for most of your own dialogue mods.

  
…And, with that, we're ready to move on!  
 

## **OK, SURE, I'M READY. WHAT IS GOING ON WITH THOSE EFFECT COMPONENTS?**

Again, the EffectComponents section is the bulk of what you’ll be getting into and editing for your dialogue mods. The effect components contain the actual information on timing, character animations, poses, staging, expressions, sound effects, voice lines, camera angles, and more that need to be referenced to play the dialogue or cinematic. Most of the other sections I've covered so far are really meant to help the game properly reference this information—the effect components are the true core of the dialogue system.

Effect components are classified into several different “Types,” each of which performs a unique function—again, from voice lines, to sound effects, camera angle changes, which I'll list below.

I’m going to be very thorough with these, and there’s a lot to go through, so strap in!  
 

### What types of effects components you can choose from?

So far, I’ve found the following effect components, each of which controls a different aspect of dialogue, and each of which has different set of attributes, which I’ll be going into shortly. For now, though, I’m just going to give a brief rundown of each:

-   **TLVoice:** The voice line for the character speaking.
-   **TLAttitudeEvent:** Controls the nodding/motion of the head and animated expressions characters are given when other animations are not being played, i.e. when a character is waiting for you to pick a dialogue choice, or is listening to the character speaking.
-   **TLAnimation:** The animations used by the characters. Mainly used for cinematics, but can be used for unique facial expression overrides as well. A note: the animations used during dialogue outside of cinematics are generally tied to the voice lines itself, and not referenced in the timeline files. This is for animations not tied to voice lines directly.
-   **TLEmotionEvent:** Controls the facial expressions used for the character referenced in the “Actor” section of the component.
-   **TLLookAtEvent:** Controls where the character is looking, as well as whether their eyes are open or closed, head and body turning, etc.
-   **TLMaterial:** Used for temporary material overrides, like for Karlach's glow map colors during romance scenes.
-   **TLShowVisual**: Used to switch different VisualTemplates in and out. Can be used for model swapping/placing objects in scenes/etc.
-   **TLShowWeapon:** Controls whether weapons and instruments are shown during the dialogue or cinematic, and when their visibility is toggled on and off.
-   **TLShowPeanuts:** Controls whether the characters standing behind your character during dialogue are shown or not. (Again, like the peanut gallery!)
-   **TLSoundEvents:** What sound effects play and when.
-   **TLSwitchStageEvent:** Mainly used for cinematics. Used when the characters need to change positions from their places in normal dialogue.
-   **TLTransform:** Mainly used for cinematics. I believe this controls changes in character position within the game world i.e. if they need to turn or walk from one place to another, but I need to do some more experimenting with it.
-   **TLShot:** Used to time camera position switches.  
     

### Ok, cool. What do you mean by “attributes," though?

Each effect component in a timeline file is broken down into several variables, or attributes, as well as the times that each component and attribute will trigger and end. Each type of effect component has a different set of possible attributes, although there are common attributes most if not all component types share. I'll be breaking down each type of effect component and their attributes in this section of the tutorial, with example code blocks explaining what each element of them means line by line.

You can find an .lsx file with all of this information here \[link\], if you need to copy/paste, but this wiki will contain all of the same information contained in that .lsx file, just via screenshots.  
  
Keep in mind that not every possible attribute for these components will be present every time! Which means some possible attributes the game can process may not be listed in this tutorial yet. If you find one I missed, please let me know!

Also, some of the attributes I included in these explanations contradict each other, and will not be found in the same instance of that effects component. I've generally pointed it out when this happens, but a good rule of thumb will be to look at examples of the same type of effects component you're editing, to know what attributes are usually included in them, and which are not.

This section is likely going to be very long, but hopefully having explanations of what everything is makes it a bit less intimidating! These files can be a lot to look at, but the more you understand about them, the less daunting it'll be to edit them. This section will also serve as a reference if you're just looking for information on specific component types. If you’d like to find a breakdown of a specific effect component, you can hit Ctrl+F to search for the name of the one you’re looking for, or use the navigation links on the side of the page.

Let's get into it! I'll start by explaining some common attributes you'll see in most components:  
 

## A GUIDE TO COMMON EFFECT COMPONENT ATTRIBUTES

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
-   The start and end times listed do not actually have to match the full length of the phase! You can actually add pauses at the start and end of dialogue and cinematics by adding a little extra time in the duration of the phase, and adjusting your start and end times to add the pauses where you’d like. You will want to make a note of how much time you added, though, so you can make sure the overall timeline duration matches the actual length of the phases you’ve included.
-   These start and end times are placed within a massive timeline, and they are, again, sequential. As mentioned earlier, it helps to imagine the dialogue timeline like a movie, and the phases in the timeline are little chapters you can skip to within it, with each component playing at specific times within that chapter.  
     

#### Time:

Some components list start and end times, and then are further broken down into “Time” elements. These are seen in components like TLEmotionEvent and TLLookAtEvent, among others. I mentioned this above,  but to reiterate, the “Time” attribute refers to when a certain effect is supposed to start, they just don’t have equivalent end times. Instead, the next instance of the “Time” attribute will replace the previous effect listed within the component.

As an example, the characters’ emotions during dialogue are usually handled with the “Time” attribute. Each “Time” attribute will set the character’s expression, starting at that time. The next “Time” attribute will replace the previous expression at the listed time.

This may be because some of these attributes are meant to persist, even after the game has moved onto the next dialogue node! Two examples of these are TLEmotionEvent and TLAttitudeEvent. The animations from these two effects components are carried into the next node, and are often used to preserve the characters' expressions and attitude animations while you're picking dialogue options. These attributes are not given a definitive end time, because they're meant to persist until the next instance of the attribute is called, or the dialogue ends.  
 

##### A note about timing in general:

The StartTime, EndTime, and Time attributes are all handled *extremely* precisely, with times often being very, very tiny fractions of a second.

This is extremely helpful with facial expressions in particular— each character actually only has around 8 expression rigs for any given emotion, and the total number they have is actually relatively small. But by using the precise timing the game allows, it almost never feels like they’re using so few expression rigs. You can make extremely complex sequences of emotions using this method, making the characters’ expressions feel unique, despite how few rigs they actually use.

I’ll be getting more into the TLEmotionEvent components later! But, for now, there’s still three common elements to talk about:  
 

#### IsSnappedToEnd:

`<attribute id="IsSnappedToEnd" type="bool" value="True" />`

I believe this snaps the components to the end of the phase. This is often set to “True,” but some components are missing the attribute entirely. This is likely because the default is False, and is not necessary to list when the component doesn’t need to be snapped to the end of the phase.  
 

#### ID:

`<attribute id="ID" type="guid" value="49292981-224c-4feb-a51b-fa7bf0fb46f3" />`

The unique UUID for the specific effects component you’re looking at. It’s generally a good idea to generate a new one for each effects component you add, but the dialogue timeline files don’t seem to be able to reference UUIDs from other timeline files, so, as far as I can tell, changing these IDs is only strictly necessary when cloning effects components within the same timeline file.

You do also have to be careful—other UUIDs within an effects component are connected to other things, like animations, camera positions, and the characters performing the listed effects. Make sure you only generate a new UUID for this “ID” attribute, and that all other UUIDs are the same as the elements (like camera positions, animations, etc) you want to reference.

Which brings me to the last common attribute:  
 

#### Actor:

`<node id="Actor">`

`            <attribute id="UUID" type="guid" value="55bce89d-670d-f7c9-6e3b-38ebe3322b32" />`

`</node>`

This UUID refers to which character is performing the effects component! These are usually unique to each timeline file, and will need to be updated to match when cloning effects components from other files. The component won’t be able to reference the related character if this UUID is not updated.

## OK, SO, WE’VE COVERED THE BASICS. WHAT ABOUT SPECIFIC EFFECTS COMPONENTS?

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
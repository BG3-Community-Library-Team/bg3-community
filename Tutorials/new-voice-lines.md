---
title: Adding New Voice Lines And Dialog
description: A guide to adding new voice lines to the game, and how the game utilizes them in dialogue.
published: true
date: 2024-09-11T20:47:58.584Z
tags: 
editor: markdown
dateCreated: 2024-07-09T21:40:21.205Z
---

# Adding New Voice Lines And Dialog - WIP

Hi! Welcome to another guide on dialogue files, made by Milo Magnetuning. This guide will cover voice lines, how the game is able to reference them within dialogue files, and how to add entirely new lines and dialog files without overriding existing ones! (It's still currently a WIP, though, so keep that in mind!)

One thing to note before we start, though—in making this tutorial, I do ask that you respect the wishes and work of voice actors, and *don't* use AI voices for your mods! There's a number of ways to get voice acting for your mods, even if you're on a budget. You don't need AI voices to do so.

Some resources that might help you a ton with voice acting are:

- The website [CastingCall.club](https://www.castingcall.club/), which lets you put up casting calls for voice actors! You'll probably find a bunch of people on that site willing to help out with a mod project, just for fun!
- You could also put out casting calls on social media!
- Check your local library; they might have AV equipment you can check out, and some might even have sound booths you can use!
- You could also try reaching out to university film and acting clubs and programs near you; a lot of people in them are looking for experience, and you'll likely find plenty of people happy to help.
- If you have a little bit of a budget, you could look into equipment rentals.
- You could also use a lavalier mic and your phone, with an app that lets you set recording levels. I've not used it, so I can't personally vet it at the moment, but I've heard good things about RecForge.
- You could also try using cameos from the voice actors, but be up front about the fact it'd be used for a mod. There's a chance their contract doesn't permit them to contribute to mods, but I'm not sure! In any case, don't lie, and of course, credit them!!!
- You can try pulling EA lines, or lines from other media!
- And, if all else fails, you could try editing lines from the game together, YTP style. (Although maybe not...that specific editing style...)

The sky's almost the limit, but don't be rude.
 
...Now, let's get into the tutorial.

## What files do you need for voice lines?

It turns out that voice lines function a bit differently than other sounds used by the game. Things like music, ambient noise, and sound effects are handled within a specific file type, soundbank files, which use the file extension .bnk. These files can be made via the program [Wwise,](https://www.audiokinetic.com/en/wwise/overview/), and I believe they might now be able to be made by the BG3 Modding Tools, but I've not looked into that much!

Voice lines don't use .bnk files, though.

Instead, character voice lines are handled via these four files:

-   A character voicebank .lsf file
-   A .wem audio file
-   A .GR2 animation file for the character's gestures during the line
-   A .ffxanim file for lipsyncing.
-   And .ffxactor and .ffxbones files for the character to use those lipsyncing files.

All of these are referenced within the DialogBinary files via a text handle, which is also used to call to the captions in the localization files! This both means that you can find a specific line of dialogue you're looking for within a DialogBinary file by searching for that text handle, and will usually find the .wem, .GR2, and .ffxanim files belonging to a certain line of dialogue that way, too. There are rare exceptions to this, though! In these cases, that text handle will be referenced in the voicebank file, followed by the actual .wem filename for the line, which will then lead you to the .GR2 and .ffxanim files as well.

…and this also means you can follow this format to add your own new dialogue to the game!

## How do you add new voice lines?

To accompany this guide, I've uploaded a collection of annotated dialog files with a sample mod, A New Voice In Town, which you can find [here!](https://www.nexusmods.com/baldursgate3/mods/10086) I highly recommend following along with those annotations for this mod. You can also see new dialog demonstrated ingame with the sample!

The sample dialog files include an annotated voicebank file, which will help a lot with this portion of the guide.

Adding voice lines to the game is pretty straightforward! You'll need to start by finding the proper voicebank file for a character. This can be done by grabbing the text handle for a line of dialogue from the character, and searching for that via the BG3 Modder's Multitool index.

This text handle will usually pull up the voicebank .lsf file for the character the line belongs to. The name of the voicebank file is usually the UUID of the global/root template for the character, with all hyphens removed! You can double-check to make sure you've got the right character via the UUID listed at the top of the voicebank, which will be under VoiceSpeakerMetaData. If that UUID refers to the character you're looking for, congrats!! You've got the right voicebank file!

You can also use this format to make voicebanks for new characters. Rename your voicebank to the UUID of your character's Root or GlobalTemplate, just with the hyphens removed. Then, take your character's UUID again, and put it at the top of the file, under VoiceSpeakerMetaData. You now have a new voicebank for your character!

Once you've found the proper voicebank file (or made your own), you'll need to copy the format for an existing voice line resource, and edit the information to match your audio file. The easiest way to do this is just by copying and pasting a duplicate of an existing voice line node, which are referred to as VoiceTextMetaData nodes.

If you're restoring a line from early access, make sure the text handle you're using isn't referenced in the full release version of game before you add it! (Once again, you can check via the indexing function with BG3MM.) It might be good practice to generate a new text handle regardless, though!

Create a new localization file, and generate a new text handle for your line. This will both be used as the caption for the line, and as the ID your voicebank will reference.

You'll then want to update the VoiceTextMetaData to account for your audio file. Update the MapKey, and put the text handle you generated. Then, set the compression type. This should probably be kept as VORBIS, which is the compression type the game uses, but you might be able to get the game to register .wem files that use other compression types.

Update the duration listed to match your audio file. You can find the exact duration of the file by using a program like [Foobar2000](https://www.foobar2000.org/)). If you right click on the line in Foobar2000, you can select Properties, and find the exact duration of the line in the Details section. Things like Windows Media Player might round that value up a few decimal places when showing its duration, so you'll want to use a program that won't!

Then set the dialog priority level. This is used to set the kind of dialog the line is for, and what priority it'll take over other dialog in the game. The different priority levels I've found are:

P1_StoryDialog (for cutscene/conversation dialog)
P2_VoiceBark_AD (for combat/overworld voicebarks)
P3_StoryDialog_AD (for story-related overworld AD/automatic dialog)
P4_RepeatingDialog_AD (for repeating/ambient overworld automatic dialog)

Set the priority level that matches your dialog!

Now, update the Source to match your audio file name.

The audio filename should be formatted like this:

`
v[character voicebank ID]_[text handle].wem
`

You can see examples of this in the sample mod I made, [A New Voice In Town](https://www.nexusmods.com/baldursgate3/mods/10086)). This is one of the voice lines for the character added by the mod, Jason.

`
v1323c4b692f74fda8bad6a96b8ddbc73_h580e6615c3364b05843d7575309ad942e568.wem
`

His character UUID is 1323c4b6-92f7-4fda-8bad-6a96b8ddbc73, and his voicebank ID is 1323c4b692f74fda8bad6a96b8ddbc73. The text handle in the mod localization file and his DialogsBinary file is h580e6615c3364b05843d7575309ad942e568, which is also used as the MapKey ID for the line.

The mocap and lipsyncing for this line follow the same file name format, with MC_ and FX_ appended to the start of them, like so:

Mocap:
`
MC_v1323c4b692f74fda8bad6a96b8ddbc73_h580e6615c3364b05843d7575309ad942e568.GR2
`

Lipsync:
`
FX_v1323c4b692f74fda8bad6a96b8ddbc73_h580e6615c3364b05843d7575309ad942e568.ffxanim
`

#### A note about mocap and lipsync:

Any animation .GR2s from other lines can be used as animations for your lines! They don't have to match your character's bodytype. I actually pulled a mocap animation from Mattis for one of Jason's lines, and it looks just fine. All you need to do is make sure the file name matches the pattern above.

Lipsync is a bit trickier. For one, it of course needs to match your dialog; you can't pull any lipsync file and have it work!

A bigger issue is that the game uses .ffxanim files, which are made using FaceFX, a $900 program that does not let you save in the free trial. I'm guessing most modders won't have access, or be able to afford this program—I certainly can't. But there are workarounds! I'll get to them in a moment. First, you'll want to know the proper file paths for everything.

The folder path for the .wem audio file and the character's soundbank file should be this!:

`
\\Mods\[Your mod folder name]\Localization\English\Soundbanks\
`

And the file path for the mocap and lipsync files should be this:

`
\\Mods\[Your mod folder name]\Localization\English\Animation\
`

(Unfortunately, I'm not sure if the game supports voice lines other than English, but it's definitely worth looking into! For now, put your files in the English Localization folder.)

You can add new lines both for existing characters, and for custom characters this way.

Now, let's get into lipsync.

#### Adding lipsync to the game:

One workaround is actually via the AnimationSlot attribute of TLAnimation in the dialog timeline files. Setting the AnimationSlot to 1 will allow you to override facial expressions with your own animation, which can be used for lipsync that matches your lines exactly. But this will come at the expense of the emotion system, which lets you configure character expressions on the fly without having to redo lipsync. It's a really handy system, and it'd be a shame to lose it!

Thankfully (kinda), there's another option. It's also not...*exactly* ideal, but it'll let you keep the benefits of the game's emotion system.

And it's that you can clone lipsync from other characters, and use it for your own!

To do so, you'll first need to pick a character. If you're adding lines for an existing character, you can skip this step! They already have their own .ffxactor and .ffxbones files, which you shouldn't replace.

Custom characters won't have .ffxactor and .ffxbones files, though, so you'll either need to make them, or, for anyone who doesn't have access to a $900 proprietary program, you'll need to grab them from another character. This should be a character that has a decent amount of lines, that might match parts of your own dialog. This is because lipsync is bound to the .ffxactor and .ffxbones files they were originally made for, and can *only* be used by characters using those files.

This is usually just one character; the .ffxactor and .ffxbones files are unique to each character in the game. But you can clone them and use them for your own characters, without affecting the original!

I cloned Alfira's .ffxactor and .ffxbones files for Jason, because she had a decent amount of lines matching parts of the dialog I wrote for him. To do so, I duplicated her files into my mod folder, at this file path:

`
\\Mods\MGNTN_JasonDialogDemo\Localization\English\Animation\FaceFXActors\
`

Then, I renamed those files to match his character UUID, resulting in these file names:

`
\\1323c4b6-92f7-4fda-8bad-6a96b8ddbc73.ffxactor
`
`
\\1323c4b6-92f7-4fda-8bad-6a96b8ddbc73.ffxbones
`

He could then use her lipsync files.

(When doing this yourself, put your mod folder name instead of MGNTN_JasonDialogDemo.)

...Make sure you're also pulling the .ffxactor and .ffxbones files from the same character. Mixing and matching them will result in horrors beyond imagination. (When I tried, he only had eyes when he spoke. Only eyes. And teeth... And nothing else,)

I then went through her dialog, and used CTRL+F to try and find parts of her lines that matched his. The [dialog parser](https://www.tumblr.com/roksik-dnd/727481314781102080/bg3-datamined-dialogue-google-drive) shared by roksik-dnd on tumblr is *invaluable* for this.

When I found a match, I extracted the audio file, and brought it into an audio editor program. I use Adobe Audition for work, so I stuck with that, but you can use an audio editor of your choice. Davinci Resolve's [Fairlight editor](https://www.blackmagicdesign.com/products/davinciresolve/fairlight) is one free alternative, but there are others out there.

To make sure the lines I recorded for him would match the lipsync, I lined up Alfira's audio with his, and adjusted them until they were in sync.

Keep in mind that the start of your file needs to match that of the original audio file for the lipsync! This might require padding the start of your line with empty audio or room tone (room tone is recorded "silence" that captures the ambient noise in a room; no room is ever truly silent, and it's usually apparent when it's missing in a recording! Make sure to capture about a minute of silence every time you record.)

You can't change when the lipsync will start playing—it'll start alongside the audio file, and not adding padding at the start when you need to can cause misalignments with the lipsync. Your line doesn't have to match the length of the original audio file, though! You can cut it short, and the lipsync will cut with it. Longer files will be missing lipsync at the end, but you can change the camera angles in the dialog timeline file to hide any misaligned or missing lipsync.

Once you've got your audio file lined up properly, mute the original line, and then make sure you check the audio levels for it. It's important to match the audio levels for the game itself! Audio levels for voices in other media are usually around -6 to -9db, but the voice lines in BG3 hover around -16/-18db. You'll want to make sure you match that, or you'll either blast your ears off, or it'll be way too quiet.

Keep in mind that you can't really trust your ears for this! You'll want to check the audio meter in the program you're using. Everyone has a different speaker setup, and something that sounds fine on your speakers might not on someone else's. Checking the audio meter itself will help produce more consistent results between sound systems!

Once you've done that, export your line as a .wav file. Then, convert the file to a .wem audio file using Wwise. Tendirty has a [really helpful guide](https://www.nexusmods.com/baldursgate3/mods/2801) on how to do so!

Now, rename your .wem file to match the pattern for voice lines, and place it in the folder I listed above. Then, grab the lipsync .ffxanim file for the original line, and rename it to match your audio file, before placing it in the folder I listed above for .ffxanim files, too.

Your character should now be able to use that lipsync!

## How do you add new dialog to the game?

This section is a *heavy* WIP atm. I've provided a collection of annotated files in a sample mod, [A New Voice In Town](https://www.nexusmods.com/baldursgate3/mods/10086), which will show you an example of the file structure for new dialog, and also breaks down a lot of the files related to dialog and voice lines, as well as custom game flags and character RootTemplates. It'll probably help a ton to look at those files while you go through this guide!

Adding new dialog really just requires matching the file structure of the game's dialog, which you can see in the folders for that sample mod.

To create new dialog, you can duplicate existing dialog files, and edit them according to your needs.

The files you'll need to set up are as follows:

- A Localization .loca file, for text handles and captions, like I described above
- A DialogsBinary .lsf file
- A Dialog Timeline .lsf file
- A Dialog Scene .lsf file
- An entry in a GeneratedDialogTimelines .lsf file
- A Dialog Resource entry in a Dialog Assets .lsf file

You can find more about what all these files do, and what file paths you can find them in in my longer dialog guide, [here](https://wiki.bg3.community/Tutorials/dialogue-files-tutorial).

The process for adding onto existing dialog files is remarkably similar to making them from scratch! Which is covered in that guide.

Start with duplicating a set of existing DialogsBinary, Dialog Timeline, and Dialog Scene files. Rename them to whatever you'd like, but make sure they all have the same file name, with the Dialog Scene file just appending \_Scene onto the end of it.

Place them in the proper \\\Story\DialogsBinary\ and \\\Timeline\Generated\ folders. You can find an example of the proper file structure in the sample mod I provided, by checking existing game dialog, or by looking at my longer dialog guide.

We won't be editing these yet! First, we'll need to make sure the game can reference them.

Make a Dialog Resource entry in a Dialog Assets file, using either my sample mod or existing dialog files as a guide. This file will tell the game where to look for your DialogsBinary file.

If you look at existing Dialog Resource entries, you'll see them referencing the Dialog .lsj files in their file paths. You don't need to make a Dialog .lsj file, though. These files are deprecated, and don't do anything in the game! Dialog made entirely from scratch, with no corresponding Dialog .lsj in the game's files works just fine. You'll still want to specify a Dialog .lsj file path in the Dialog Resource entry, though, but you can do that by changing the folder name of your DialogsBinary folder in the listed path to Dialogs, and your file extension to .lsj.

Generate a new UUID for your Dialog Resource. This is your DialogResourceId, which is used to refer to your DialogsBinary file. Then, make an entry for your dialog in a GeneratedDialogTimelines file, again using either my sample mod or existing game dialog as a guide.

Input the UUID you just generated for your Dialog Resource as the DialogResourceId in the GeneratedDialogTimelines entry, and generate a new UUID for your GeneratedDialogTimelines entry, and put it as the ID for the entry. Specify the file path for your timeline file in the SourceFile section. You'll see an EditorSourceFile listed, referring to a .tml file. You don't need to make a .tml file! It's likely just used for Larian's engine. I don't even think these files are available to players. I still updated the file path to mirror my dialog timeline file, though.

Take the UUID you just generated for your timeline file, and put it as the TimelineID in your DialogsBinary file, then generate a new UUID for the file itself, and substitute it in the UUID entry at the top of the file.

Generate a new UUID for your Scene file as well, and put it in the "Identifier" section of the Scene file.

Generate new SpeakerIDs for your dialog in the DialogsBinary file, and make sure to copy those same SpeakerIDs into your Dialog Timeline file.

This should help the game should properly reference your files, and the characters in them. You can now start adding to your scenes! You can find more instructions on how to do so in my longer guide on editing dialog files.

Now, to make sure your dialog can play in the game, you can either list your DialogResourceID as a DefaultDialog for a new character in their Global or RootTemplate, or you can link to it from existing dialog using the Nested Dialog node!

I've explained more about this both in the annotated sample mod files, and in my longer dialog guide.


(...I'm going to cut this guide here for now; a lot of this information can be found in the sample mods! I'll probably be filling out this page more, later, though. Take care!)
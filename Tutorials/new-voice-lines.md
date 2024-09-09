---
title: Adding New Voice Lines And Dialog
description: A guide to adding new voice lines to the game, and how the game utilizes them in dialogue.
published: false
date: 2024-09-09T20:27:09.339Z
tags: 
editor: markdown
dateCreated: 2024-07-09T21:40:21.205Z
---

# Adding New Voice Lines And Dialog - WIP

Hi! Welcome to another guide on dialogue files, made by Milo Magnetuning. This guide will cover voice lines, how the game is able to reference them within dialogue files, and how to add new ones without overriding any existing ones! (It's still currently a WIP, though, so keep that in mind!)

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

The sky's almost the limit, but don't be rude. And don't destroy the planet with energy-intensive AI!
 
...Now, let's get into the tutorial.

## How do you add new voice lines to Baldur's Gate 3?

It turns out that voice lines function a bit differently than other sounds used by the game. Things like music, ambient noise, and sound effects are handled within a specific file type, soundbank files, which use the file extension .bnk. These files can be made via the program [Wwise,](https://www.audiokinetic.com/en/wwise/overview/), and I believe they might now be able to be made by the BG3 Modding Tools, but I've not looked into that much!

Voice lines don't use these files, don't use .bnk files, though.

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

Adding voice lines to the game is pretty straightforward! You'll need to start by find the proper voicebank file for a character. This can be done by grabbing the text handle for a line of dialogue from the character, and searching for that via the BG3 Modder's Multitool index.

This text handle will usually pull up the voicebank .lsf file for the character the line belongs to. The name of the voicebank file is usually the UUID of the global/root template for the character, with all hyphens removed! You can double-check to make sure you've got the right character via the UUID listed at the top of the voicebank, which will be under VoiceSpeakerMetaData. If that UUID refers to the character you're looking for, congrats!! You've got the right voicebank file!

Once you've found the proper voicebank file, you'll need to copy the format for an existing voice line resource, and edit the information to match your audio file. The easiest way to do this is just by copying and pasting a duplicate of an existing voice line node, which are referred to as VoiceTextMetaData nodes.

If you're restoring a line from early access, make sure the text handle you're using isn't referenced in the full release version of game before you add it! (Once again, you can check via the indexing function with BG3MM.) It might be good practice to generate a new text handle regardless, though!

Once you've got your unique dialogue text handle, you'll then want to format your filenames like so:

For the audio

## How do you add new dialog to the game?



This section of the guide is still a bit of a WIP otherwise.
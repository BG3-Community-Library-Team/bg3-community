---
title: Adding New Voice Lines And Dialog
description: A guide to adding new voice lines to the game, and how the game utilizes them in dialogue.
published: false
date: 2024-09-09T19:54:20.669Z
tags: 
editor: markdown
dateCreated: 2024-07-09T21:40:21.205Z
---

# Adding New Voice Lines And Dialog - WIP

Hi! Welcome to another guide on dialogue files, made by Milo Magnetuning. This guide will cover voice lines, how the game is able to reference them within dialogue files, and how to add new ones without overriding any existing ones!

One thing to note before we start, though—in making this tutorial, I do ask that you respect the wishes and work of voice actors, and *don't* use AI voices for your mods! There's a number of ways to get voice acting for your mods, even if you're on a budget. You don't need AI Voices to do so.

Some ways  
  
The sky's almost the limit, but don't be rude.  
 

It turns out that voice lines function a bit differently than other sounds used by the game. Things like music, ambient noise, and sound effects are handled within a specific file type, soundbank files, which use the file extension .bnk. These files can be made via the program [Wwise,](https://www.audiokinetic.com/en/wwise/overview/) but making functional soundbank files does require matching the file structure BG3 uses for their own files. This also involves learning how to use Wwise itself, which I *will* be covering briefly as part of this guide, but only to convert your own audio files to the .wem format the game uses. I'll be honest, soundbank files are still a bit of a mystery to me!

…Lucky for us, though, is that voice lines don't use these files.

Instead, character voice lines are handled via these four files:

-   A character voicebank .lsf file
-   A .wem audio file
-   A .GR2 animation file for the character's gestures during the line
-   And a .ffxanim file for lipsyncing.

All of these are referenced within the DialogBinary files via a text handle, which is also used to call to the captions in the localization files! This both means that you can find a specific line of dialogue you're looking for within a DialogBinary file by searching for that text handle, and will usually find the .wem, .GR2, and .ffxanim files belonging to a certain line of dialogue that way, too. There are rare exceptions to this, though! In these cases, that text handle will be referenced in the voicebank file, followed by the actual .wem filename for the line, which will then lead you to the .GR2 and .ffxanim files as well.

…and this also means you can follow this format to add your own new dialogue to the game!

## So, how do you add new voice lines?

It's actually pretty straightforward! You'll need to find the proper voicebank file for a character, but this can be done by grabbing the text handle for a line of dialogue from the character, and searching for that via the BG3 Modder's Multitool index (you can find instructions on how to do so here! \[link\]).

This text handle will usually pull up the voicebank .lsf file for the character the line belongs to. The name of the voicebank file is generally the UUID of the global template for the character, with all hyphens removed! (For more information on character GlobalTemplates and UUIDs, check here \[link\]!) You can double-check to make sure you've got the right character via the UUID listed at the top of the voicebank, which will be under VoiceSpeakerMetaData. If that UUID refers to the character you're looking for, congrats!! You've got the right voicebank file!

Once you've found the proper voicebank file, you'll need to copy the format for an existing voice line resource, and edit the information in the following screenshot. The easiest way to do this is just by copying and pasting a duplicate of an existing voice line node, which are referred to as VoiceTextMetaData nodes.

The example shown here adds a new voice line for Wyll! It's a line I grabbed from early access.

If you're restoring a line from early access, make sure the text handle you're using isn't referenced in the full release version of game before you add it! (Once again, you can check via the indexing function with BG3MM.) It might be good practice to generate a new text handle regardless, though!

Once you've got your unique dialogue text handle, you'll then want to format your filenames like so:
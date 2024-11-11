---
title: Adding New Music And Sound Effects With Automated Dialog
description: A guide to using automated dialog to add custom sound effects and music to the game, without overriding existing files.
published: true
date: 2024-11-11T08:59:48.275Z
tags: 
editor: markdown
dateCreated: 2024-11-11T08:59:48.275Z
---

# Adding New Music And Sound Effects - WIP

This guide requires a basic understanding of the Baldur's Gate 3 dialog system! You can find my guides to the dialog system on the following pages, and I recommend looking over them before proceeding.

[Editing Dialog Files](https://wiki.bg3.community/en/Tutorials/dialogue-files-tutorial)

[Adding New Voice Lines And Dialog](https://wiki.bg3.community/en/Tutorials/new-voice-lines)


### Soundbanks, Wwise, and the Trouble With New Audio Files

If you've taken a look at the other guides to sound files on the wiki, like [this guide](https://wiki.bg3.community/Tutorials/Sound/Replace-Sound) to replacing the existing sound files from the game, you likely already know that adding new soundbanks to the game is not possible, and neither is editing or adding to existing soundbanks.

This is because Wwise, the sound engine BG3 uses, runs on a hierarchy system that is made within a single project file—as far as I'm aware, there can be only one Wwise project file per game. And because modders don't have access to Larian's original Wwise project file, there's currently no way to add our own soundbanks.

This is a bit of an issue when it comes to audio modding—soundbanks control a majority of the game's audio files, with one exception:

Voice lines!

As explained in the guide to adding new voice lines linked above, **voice lines do not go through soundbank files, making it possible to add our own original voice lines and dialog.**

But, technically, *any* audio file can be included in a voicebank!

...And that's where this guide comes in.

This is a guide to using automated dialog to add new sound effects and music, bypassing the soundbank system entirely!

So, let's get started, shall we?

### What is Automated Dialog?

*(While having a basic understanding of dialog files is recommended for this guide, I will be covering some of the basics here!)*

Automated dialog is one of the types of "overworld" dialog used outside of cutscenes. And it's used in a variety of ways, from the narrator lines that play when interacting with tombstones, to party banter, to the insults the characters give when using Vicious Mockery, and more. Automated dialog can be tied to events like spellcasting, interacting with objects, and more via Osiris scripting—and we can tie our own audio to these events through that automated dialog!
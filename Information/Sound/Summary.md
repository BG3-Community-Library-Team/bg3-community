---
title: BG3 Sound System Summary
description: Breaking down audio structure, software, and events
published: true
date: 2024-05-17T23:25:06.261Z
tags: audio, sound, wwise, events
editor: markdown
dateCreated: 2024-05-07T04:18:43.686Z
---

# Understanding BG3 Sound System
This article aims to bring some clarity to the BG3 audio system by breaking down the structure, software, and the events system.

## Audio Breakdown
Stefan Randelshofer (Audio Director, Larian Studios) and Matheus Vilano (Senior Technical Sound Designer, Larian Studios) joined an Audiokinetic [live stream](https://www.youtube.com/watch?v=LlaRuoT15kc&t=3351s) on Mar 13, 2024 for a technical discussion on mixing Baldur's Gate 3. Matheus talks in depth about the **complex** structure of system buses (they have almost 400!!!) and demonstrates how different audio is mixed in Wwise.

A quick summary based on that video is as follows.

Audio in the game can be passed to the player through both 2D and 3D spaces. 
2D sounds get sent to a "*passthrough*" bus, which bypasses the 3D spatial audio system. These are typically the less important sounds.
3D sounds either get sent through the "*main bus*", which is broken into a series of embedded virtual buses, or gets passed through an audio "*object*". 
Very important 3D sounds that require a high degree of precision get routed to an object, instead of the main bus.


#### 2D sounds (Passthrough):
- Music
- Ambience (Background)
- Interface (UI / HUD)
- Map voice lines (When you click to move and the character says a line like:"these boots have seen everything")

#### 3D sounds (Main):
- Status effects
- Movement (footsteps, folley sounds) 
- Item uses (consuming a potion, destroying a barrel)

#### 3D sounds (Objects):
- Cinematic specific sounds
- Spells & Actions (Combat sounds)
- Voice lines
- Voice components
- Instrument components

![bus_structure.png](/information/sound/bus_structure.png)

## Wwise
Wwise is software for editing interactive media in video games, developed by Audiokinetic. This is the software that Larian uses for mixing audio in BG3. 

Wwise can be downloaded [here](https://www.audiokinetic.com/download/) for free. You must create an Audiokinetic account, and install their launcher.
> The Free Trial version of Wwise allows you to create a project for non-commercial use only and is limited to 200 media assets in the Wwise SoundBanks.
{.is-info}

## Audio Events
In Wwise, Larian sound engineers have created **events** to play one or many sound files in a specific order, through specific buses, at specific volumes, with specific effects or transitions. These events can be viewed as data in lsf(x) files. Since these events originate from Wwise with a very specific (and hidden) set of instructions for which sound files to play, at what duration, with which triggers, etc, we are currently unable to edit these audio events through normal data editing means.

There is some information you can derive from looking at the data for audio events, but since you cannot replace the fields it isn't much help to modders that are looking to edit those sounds or create new ones.


## Adding sounds to BG3
Currently (as of May 6, 2024) there is not a way to add new soundbanks or audio files to BG3. 
The only option is to replace existing sound files (.wew format) so that an event plays your replaced track in place of the original. 
See [this](/Tutorials/Sound/Replace-Sound) guide for extracting and identifying sound files.

## Future for Audio Modding
We are hopeful that official Larian mod tools:tm: will add support for adding audio files/events.

## Resources
[Wwise Up On Air | Mixing Baldur’s Gate 3 with Wwise](https://www.youtube.com/watch?v=LlaRuoT15kc&t=3351s) 
[Baldur's Gate 3: An Audio Technical Deep Dive | GDC 2024](https://www.youtube.com/watch?v=hr8zuW_z7-A)
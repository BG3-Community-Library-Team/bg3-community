---
title: Custom Origin Creation
description: Make your own custom origin.
published: false
date: 2025-08-21T15:01:35.856Z
tags: origin
editor: markdown
dateCreated: 2025-08-20T20:20:04.633Z
---

# Overview
This is a tutorial for adding a custom origin into Baldur's Gate 3. This tutorial is considered **moderate difficulty**--you are expected to already be familiar with code editing and searching BG3's files for the info you need.

> This method is the "manual" method--it doesn't involve using the official toolkit. If someone else has a method of doing this in the toolkit, feel free to add to the page.
{.is-info}

## So why would I want to make a custom origin?

The simplest answer is that you just play the same character a lot, and are tired of going through character creation over and over to make the exact same choices. By making a custom origin, you select your character, make changes if necessary, and boom, done. If your character has special clothes or items, you can give them those by default instead of having to spawn them in. You can even give them unique skills or spells that Tavs wouldn't get. (Minsc has an example of this with his ability to Summon Boo.)

It also helps avoid pitfalls with editing things that also edit generic Tav. For example, if one of your characters has a custom body that replaces Body Type 1, and another character who is vanilla BT1... it's not possible to have both at once, because the bodies overwrite each other. Until custom origins, where you can make your custom origin with a unique body, while still keeping the vanilla body available for regular Tav.

Of course, a custom origin *can* also have things like custom dialogue, cutscenes, and plot lines. But that's a bit beyond the scope of this tutorial. What this tutorial will create is basically just a Tav (or Durge) that's already preset with your character's options.

## Recommended Tools

- Visual Studio Code
	- **BG3-GUIDinfos** VS Code Extension
	- **UUID Generator** VS Code Extension
- BG3 Modder's Multitool and/or NorbSearch (https://bg3.norbyte.dev/)

## Le Template

Download the template files from here: https://github.com/EmeraldTechnopath/Em_Custom_Origin_Template

It's a completely working custom origin, so you can pack it and put it into the game to see how it works. My recommendation is to make changes in **small batches**, testing every so often. If something breaks, you'll have a better idea of what went wrong. You can also use a version control service like GitHub to allow you to roll back your changes if something goes terribly wrong.

Also, you'll find many times where I left a note saying "Regenerate this!" When you see this, I recommend using VS Code's **Replace in Files** function to replace every occurance of the UUID in the template. This will help avoid issues with UUIDs that don't link up, which can cause crashes.

I put a lot of notes in there, so I'm not going to restate everything that's in there. However, I'll add extra context in here where it may be unclear in the template.

## Origins.lsx

This is the main file that tells the game, "Hey, here's a new origin. Show it in the origin list!"

The default tags should be fine for a Tav-like origin. If you want a Durge origin, you'll have to swap in the REALLY_DARK_URGE tag. Heck, you could even put in another origin's tag if you wanted, but it probably wouldn't make a lot of narrative sense.

> Swapping the body type or race in CC doesn't seem to work right with this setup. You get things like floating heads. I'd have to look more into how to fix this.
{.is-warning}

## Globals

This is a file that defines the character in the world itself. I'm not totally sure why this is necessary for an origin, but my game crashed when I didn't have it.

## RootTemplates

This is the base template for your origin.

## CharacterVisuals

This file defines the appearance of your origin: animations, body mesh, other meshes, colors, etc.

> 
> I noticed that if you made your origin editable in CC, any scar you set up here will get reset to default (no scar) and the user will have to select it again. I don't know why it's like this, but I didn't find any way around it. Scars are fine if you keep the appearance locked. (There could be other things like this, too. I didn't test every CC option.)
{.is-warning}

## Equipment.txt

This file defines the starting equipment for your custom origin. You can give them custom armor, camp clothes, and other items. To hunt down the file names, you can use the BG3 wiki as a starting point, and then paste the UID into Multitool or NorbSearch to find the actual stats name.

## Voices.lsx

Here's where you would define a custom voice table. For example, if you want your custom origin to always have Voice 4, you can make a custom table with only that voice.

> Here are the UUIDs for the vanilla Tav voices:
> 
> voice 1: 24247531-c432-4f0f-8f35-6c90c4844aa8
> voice 2: 869248f0-468a-4747-82d7-e8efc3bbcacf
> voice 3: 4df6dba0-8574-4704-a9fb-a500da38e1e1
> voice 4: 3347e417-d7ad-4088-bdd6-d5565efcd815
> voice 5: f5b335b2-9cd9-4b38-a4c1-458b846ab499
> voice 6: b9b26a44-943b-4427-9890-d81c7e81a75b
> voice 7: 2d206fda-0d4f-457f-b4ea-0fc18866f5dd
> voice 8: fb6b5353-8d14-4507-9222-ceaec990fce9
>
> (thanks milo for compiling this!)
{.is-info}

Just put the proper UUID into the SpeakerUUID field and assign the table back in your Origins.lsx.

If you want the voice to be pickable, just set the voice table in Origins.lsx back to **5ee56242-d07c-482e-9260-24529d1473a3**.

## Levels/Portraits

If you want a custom portrait for your origin, you can make a custom trigger that will fire on game start and level up. The way I did this was downloading the EasyCheat mod, teleporting into the SYS_PortraitPlayerRace_A level, and using the WASD mod to walk around until my character was standing in front of a background I liked. Then I used photo mode to take a screenshot and edited it in GIMP to the right size. This only affects the icon you'd see in the origins selection, however, so I also used the SE command `_P(Osi.GetPosition(GetHostCharacter()))` to get the coordinates of where my character was standing in the level. Then I used those coordinates to set up a new trigger and camera trigger. You'll probably have to adjust values a bit to get things in the right places, but once that's set up, you should get a new generated icon every time you start the game or level up.

> I don't know how to change the pose that's used for the generated icon, yet. It's probably going to end up using the default one for your origin's race/bodytype.
{.is-warning}

## Tags

This won't really affect anything, besides giving your custom origin a tag in their Character Sheet like other origins do. Of course, you could set up new dialogue that looks for this custom tag, but that's beyond the scope of this tutorial.

## Adding Mod Dependencies

If your custom origin relies on any other mods, you can add dependencies. This is especially important if you'd be releasing your custom origin, but still helpful if it's just for you. There's a tutorial for adding dependencies here: https://wiki.bg3.community/en/Tutorials/General/Basic/adding-mod-dependencies

## Help! I'm having an issue with this!

If you read all of this and you're having an issue with something I didn't cover, you can probably find me at the CMTY discord: https://discord.gg/bg3mods

## Credits

Thanks to Milo/Magnetuning for answering some of my questions about making this.
Thanks to Death for part of John Larian's description.

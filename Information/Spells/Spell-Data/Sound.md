---
title: Sound
description: List and definition of Sound data entries
published: true
date: 2024-05-10T20:28:51.269Z
tags: 
editor: markdown
dateCreated: 2024-05-10T20:28:51.269Z
---

# Sound
These entries will tell the spell what sounds to play at specific points of the spell, if they are not dictaed elsewhere. They are usually in the string id format found in their respective [RootTemplate](Link)'s.

## PrepareSound
This sound will play at the initial preperation of a spell.

Example: `data "PrepareSound" "Spell_Prepare_Damage_Necrotic_Gen_L1to3"`

## PrepareLoopSound
This sound will play continuously while you idle the preparation of a spell, during target selection, and after the initial `PrepareSound`.

Example: `data "PrepareLoopSound" "Action_Loop_Item_SummonHusband"`

## CastSound
This sound is played the moment the spell is cast.

Example: `data "CastSound" "Action_Cast_LightningAura"`

## TargetSound
This sound is played the moment the spell connects with it's intended target.

Example: `data "TargetSound" "Action_Impact_Item_GiantBlade"`

## VocalComponentSound
This is usually a soundbit that is played during the overall casting of the player, intended as a specialized sound, paired with the spell flag "HasVerbalComponent".

Example: `data "VocalComponentSound" "Vocal_Component_Disadvantage"`
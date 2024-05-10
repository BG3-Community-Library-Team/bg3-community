---
title: Visual Effects
description: List of Visual Effect data entries
published: true
date: 2024-05-10T20:39:19.501Z
tags: 
editor: markdown
dateCreated: 2024-05-10T20:39:19.501Z
---

# Visual Effects
This section will go over the various spell visual effects you can find in spell data files. These effects will usually be in UUID format, that link to MultiEffectInfos, or `MEI`s. You can find more information on `MEI`s [here](Link Here). Note, not all visual effect types will apply to all spell types.

## PrepareEffect
For the PrepareEffect, this is the initial visual effect and idling visual effect played by the spell during target selection. There are some cases, and conditions that will negate a prepare effect, causing the visuals to skip straight to the next effect in the sequence.

Example: `data "PrepareEffect" "3044bca0-7b0e-4d65-9b15-f586f5d58388"`

## CastEffect
CastEffect is the visual effects that will occur once the target has been confirmed.

Example: `data "CastEffect" "2ca60442-a034-4da4-ac6d-52954c231b20"`

## HitEffect
This is the visual effect that will occur when the spell connects to the target. It can sometimes be confused for TargetEffect, however, these effects are often meant to simply register impact effects with the visuals themselves.

Example: `data "HitEffect" "2ca60442-a034-4da4-ac6d-52954c231b20"`

## TargetEffect
This will be the visual effects that occur at the target of the spell, whether it be an object or character.

Example: `data "TargetEffect" "2ca60442-a034-4da4-ac6d-52954c231b20"`

## PositionEffect
This is the visual effect that happens to the area around the target of the spell.

Example: `data "PositionEffect" "2ca60442-a034-4da4-ac6d-52954c231b20"`

## BeamEffect
This particular visual effect is only used by spells that have beam effects attached to the primary particle of the spell.

Example: `data "BeamEffect" "2ca60442-a034-4da4-ac6d-52954c231b20"`

## Additional Effects
I will include a brief summary of some additional visual effect components [here](/Information/Spells/Spell-Data/Visual-Effects/Additional-Effects).
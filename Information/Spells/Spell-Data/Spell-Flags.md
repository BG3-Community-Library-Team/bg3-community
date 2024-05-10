---
title: Spell Flags
description: Definition and list of SpellFlag entries.
published: true
date: 2024-05-10T20:32:25.650Z
tags: 
editor: markdown
dateCreated: 2024-05-10T20:32:25.650Z
---

# Spell Flags
These are fine tuned conditions of the Spell data, stating more specifically what the individual spell can and cannot do. Not all conditions work for all spell types, but you can find some cursory data [here](/Information/Spells/Spell-Data/Spell-Flags/List).

Example: `data "SpellFlags" "NoCameraMove;HasSomaticComponent;NoCooldownOnMiss;HasVerbalComponent;IsSpell;HasHighGroundRangeExtension;RangeIgnoreVerticalThreshold;IsHarmful"`

This example would tell the game:
- NoCameraMove: Do not recenter the camera on the caster or target.
- HasSomaticComponent: Has body movement which will be dictated in the Spell Animations, as well, character will be required not being under any control effects to cast.
- NoCooldownOnMiss: If the spell roll fails, it will not put the spell on cooldown.
- HasVerbalComponent: Vocal sound will be played on preperation and/or cast of the spell, as well, character will require being able to speak to cast.
- IsSpell: This is specifically a spell, and not just an action, like crouch or jump.
- HasHighGroundExtension: This spell gets a range bonus if you have the high ground.
- RangeIgnoreVerticalThreshold: This spell does not have a range penalty if the target has the high ground.
- IsHarmful: This spell has negative effects. More specifically, even if you apply a positive status to the spell, if cast on an NPC that is not hostile, they will become hostile.
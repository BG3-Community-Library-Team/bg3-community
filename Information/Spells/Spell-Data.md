---
title: Spell Data
description: Information on the components of a Spell Data block.
published: true
date: 2024-05-10T19:52:12.846Z
tags: 
editor: markdown
dateCreated: 2024-05-10T17:43:59.384Z
---

# Spell Data
This article will break down the components found in the spell files. These files can be found in `Public\ModOrGame\Stats\Generated\Data\filename.txt`. It will always be a `.txt` file.

## Pages
- [New Entry](/Information/Spells/Spell-Data/New-Entry)
- [Type](/Information/Spells/Spell-Data/Type)
- [Spell Type](/Information/Spells/Spell-Data/Spell-Type)
- [AI Flags](/Information/Spells/Spell-Data/AI-Flags)
- [Container Spells](/Information/Spells/Spell-Data/Container-Spells)
- [Cooldown](/Information/Spells/Spell-Data/Cooldown)
- [Spell Rolls](/Information/Spells/Spell-Data/Spell-Rolls)
- [Target Conditions](/Information/Spells/Spell-Data/Target-Conditions)
- [Trajectories](/Information/Spells/Spell-Data/Trajectories)
- [Icon](/Information/Spells/Spell-Data/Icons)
- [Name & Description](/Information/Spells/Spell-Data/Name-Description)
{.links-list}









## Target Conditions
This data is intended for spells meant to have additional conditions for the target of the spell. 

Example: `data "TargetConditions" "Character() and not Dead()"`

In this case, the target must be a "Living" target, and not dead. More information on Target conditions can be found [here](Link Here).

## Trajectories
This particular information is referencing spells that often contain moving parts, whether it be the character, target, or visual effects. More information on the application of Trajectories can be found [here](Link Here).

Example: `data "Trajectories" "3d34f1ca-7e7e-4ee7-ad2b-704079f4a19f"`

The GUID in the information refers to a Root Template entry, which will dictate both the path of the spell and in some cases, the visual effects as well.

## Icon
This tells the game the icon to use for this spell. More information about icons can be found [here](https://wiki.bg3.community/en/Information/Icons).

Example: `data "Icon" "GenericIcon_Intent_Utility"`

## Display Name
This information will reference a handle id or `hid`, and it's version, which can be found in the [Localization](link here) file. This is intended to give the spell a visual name in the tooltip when hovered over in game.

Example: `data "DisplayName" "h95ec602eg6ae5g48ebg9fefge3d164860911;2"`

## Description
This is the same format and purpose as the Display Name section, usually used to give a more detailed description along with the display name, of the spell. You can find additional information on descriptions and extra parameters [Here](Link Here).

Example: `data "Description" "h3eb67ecegab30g4ce5g9f9fg1686128828b0;4"`

## Tooltip Damage List/Attack Save/Status Apply/ et al.
This data is usually a list of entries to add to the tooltip when hovered, that often give a visual breakdown of spell saving throws and success roll outcomes.

Examples:
`data "TooltipDamageList" "DealDamage(1d4),Force)"`
`data "TooltipAttackSave" "RangedSpellAttack"`
`data "TooltipStatusApply" "ApplyStatus(FRIGHTENED, 100, 1)"`

You can find a more detailed list of the tooltip entries and descriptions [here](Link Here).

## Sound
These entries will tell the spell what sounds to play at specific points of the spell, if they are not dictaed elsewhere. They are usually in the string id format. These will come in five types:

- PrepareSound: This sound will play at the initial preperation of a spell.
- PrepareLoopSound: This sound will play continuously while you idle the preparation of a spell, during target selection.
- CastSound: This sound is played the moment the spell is cast.
- TargetSound: This sound is played the moment the spell connects with it's intended target.
- VocalComponentSound: This is usually a soundbit that is played during the overall casting of the player, intended as a specialized sound, paired with the spell flag "HasVerbalComponent".

Example: `data "CastSound" "Action_Cast_VampireBite"`

In this case, this is the sound that would be played when a character flagged as a vampire casts the Vampire Bite on a target.

## Use Costs
This tells the game what the spell should cost, in terms of resources, when cast, such as an Action Point, Bonus Action or even a custom resource.

Example: `data "UseCosts" "ActionPoint:1;Elemental_Essence:1"`

In this example, to cast the spell, the player would need to have at least 1 default action point, and 1 custom resource, Elemental Essence, which will be expended on cast.

## Spell Animation
This information is usually a uuid, or string of uuids in a specific format that dictate a few things, but primarily the motions the character will take when casting the spell. This is not to be confused with visual effects. This is what the character will do with their body as they prepare and/or cast the spell.

Example: `data "SpellAnimation" "3ff87abf-1ea1-4c32-aadf-c822d74c7dc0,,;,,;38cdb41c-2eec-4e03-bb31-83cff0346c35,,;85414f5f-b448-4dda-9370-1b6c4b38b561,,;d8925ce4-d6d9-400c-92f5-ad772ef7f178,,;,,;eadedcce-d01b-4fbb-a1ae-d218f13aa5d6,,;,,;,,"`

These multiple strings will dictate the movement based on character height, race, gender, among other things.

## Spell Flags
These are fine tuned conditions of the Spell data, stating more specifically what the individual spell can and cannot do. Not all conditions work for all spell types, but you can find some cursory data [here](Link here).

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

## Spell Visual Effects
This section will go over the various spell visual effects you can find in spell data files. These effects will usually be in UUID format, that link to MultiEffectInfos, or `MEI`s. You can find more information on `MEI`s [here](Link Here). Note, not all visual effect types will apply to all spell types.

### PrepareEffect
For the PrepareEffect, this is the initial visual effect and idling visual effect played by the spell during target selection. There are some cases, and conditions that will negate a prepare effect, causing the visuals to skip straight to the next effect in the sequence.

Example: `data "PrepareEffect" "3044bca0-7b0e-4d65-9b15-f586f5d58388"`

### CastEffect
CastEffect is the visual effects that will occur once the target has been confirmed.

Example: `data "CastEffect" "2ca60442-a034-4da4-ac6d-52954c231b20"`

### HitEffect
This is the visual effect that will occur when the spell connects to the target. It can sometimes be confused for TargetEffect, however, these effects are often meant to simply register impact effects with the visuals themselves.

Example: `Example Here`

### TargetEffect
This will be the visual effects that occur at the target of the spell, whether it be an object or character.

Example: `Example Here`

### PositionEffect
This is the visual effect that happens to the area around the target of the spell.

Example: `Example Here`

### BeamEffect
This particular visual effect is only used by spells that have beam effects attached to the primary particle of the spell.

Example: `Example Here`

### Additional Effects
I will include a brief summary of some additional visual effect components here.



#### ToggleOnEffect
This is for toggles, and the visual that will play when the ability or spell is toggled on.

#### ToggleOffEffect
Same as above, except it will play this visual when the spell is toggled off, either by meeting the condition, or manually.

#### ApplyEffect
This is specifically for Status Effects and passives. When a spell applies these to a target, this is the visual that will play on application.

#### StatusEffect
Similar to above, this visual will continue to play as long as the target has the applied status.

#### EndEffect
This is the visual that will play at the end of a statuseffect, if applicable.


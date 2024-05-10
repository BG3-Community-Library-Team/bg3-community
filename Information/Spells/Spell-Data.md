---
title: Spell Data
description: Information on the components of a Spell Data block.
published: true
date: 2024-05-10T17:43:59.384Z
tags: 
editor: markdown
dateCreated: 2024-05-10T17:43:59.384Z
---

# Spell Data
This article will break down the components found in the spell files. These files can be found in `Public\ModOrGame\Stats\Generated\Data\filename.txt`. It will always be a `.txt` file.

## New Entry
This is the ID of the spell itself, which is referred to by progressions, class descriptions or other methods.
Example: `new entry "Projectile_Fireball_4"`

## Type
This data is referred to by the game engine to determine what preset information the new entry will have access to.

Example: `type "SpellData"`

## Spell Type
This entry dictates the type of spell data to use, from the Type section. There are varying types, which can be found here(Insert hyperlink here).

Example: `data "SpellType" "Projectile"`

## AI Flags
This determines specific factors on what the AI can and cannot do if an NPC has this spell.

Example: `data "AIFlags" "CanNotUse"`
In this example, the AI, even if it had this spell, cannot use it.

## Container Spells
This line dictates the spells contained in a container spell. Which means it is the master spell that holds it's nested spells. This line is only needed for the master spell container.

Example: `data "ContainerSpells" "Target_EnhanceAbility_BearsEndurance_3;Target_EnhanceAbility_BullsStrength_3;Target_EnhanceAbility_CatsGrace_3;Target_EnhanceAbility_EaglesSplendor_3;Target_EnhanceAbility_FoxsCunning_3;Target_EnhanceAbility_OwlsWisdom_3"`

## Spell Container ID
This data is only meant for spells contained in a container spell. It dictates what spell your spell is nested in. It will never have more than one layer. This line is needed for any spell nested within a container.

Example: `data "SpellContainerID" "Target_EnhanceAbility"`

## Cooldown
This will tell the spell how often it can be used.

Example: `data "Cooldown" "OncePerShortRest"`

In the example, the spell would only be usable once per short rest. You can find the cooldown types here (Insert hyperlink here).

## Spell Roll
This tells the game what stats of the caster or target to use when the dice are officially rolled, as well as that stat's minimum requirement to succeed. The caster will often have to roll higher (with modifiers) than the minimum  requirement, to succeed.

Example: `data "SpellRoll" "SkillCheck(Skill.Performance, 15)"`

## Spell Success
This will tell the game what happens when the caster succeeds the random dice roll.

Example: `data "SpellSuccess" "ApplyStatus(FRIGHTENED,100,2)"`

In this example, if the caster succeeds in the dice roll, the target of the spell will have the Frightened Status applied to them for 2 turns.

## Spell Fail
Similar to SpellSuccess, this tells the game what will happen if the dice roll is failed. It is not always included, as many spells have no effect if the dice roll fails. However, in some cases, half the value of the spell is still applied even if the roll fails, except in the case of a critical failure (Rolling a 1).

Example: `data "SpellFail" "DealDamage((2d6)/2, Necrotic,Magical)"`

In this case, if the caster fails the roll, they will still do "2d6 divided by 2" damage to the target.




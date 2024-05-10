---
title: Spell Rolls
description: Defining spell rolls and types
published: true
date: 2024-05-10T19:48:20.309Z
tags: 
editor: markdown
dateCreated: 2024-05-10T19:48:20.309Z
---

# Spell Rolls
Here, you can find the the definition of `SpellRoll` and the types of spell rolls.

## SpellRoll
This tells the game what stats of the caster or target to use when the dice are officially rolled, as well as that stat's minimum requirement to succeed. The caster will often have to roll higher (with modifiers) than the minimum  requirement, to succeed.

Example: `data "SpellRoll" "SkillCheck(Skill.Performance, 15)"`

## SpellSuccess
This will tell the game what happens when the caster succeeds the random dice roll.

Example: `data "SpellSuccess" "ApplyStatus(FRIGHTENED,100,2)"`

In this example, if the caster succeeds in the dice roll, the target of the spell will have the Frightened Status applied to them for 2 turns.

## SpellFail
Similar to SpellSuccess, this tells the game what will happen if the dice roll is failed. It is not always included, as many spells have no effect if the dice roll fails. However, in some cases, half the value of the spell is still applied even if the roll fails, except in the case of a critical failure (Rolling a 1).

Example: `data "SpellFail" "DealDamage((2d6)/2, Necrotic,Magical)"`

In this case, if the caster fails the roll, they will still do "2d6 divided by 2" damage to the target.
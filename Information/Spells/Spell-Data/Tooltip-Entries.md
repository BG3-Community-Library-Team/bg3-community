---
title: Tooltip Entries
description: List and definitions of tooltip related entries
published: true
date: 2024-05-10T20:18:56.358Z
tags: 
editor: markdown
dateCreated: 2024-05-10T20:18:56.358Z
---

# Tooltip Entries
This page is a list and summary of the types of data entries regarding tooltip display. The information contained is usally found in the [SpellSuccess](/Information/Spells/Spell-Data/Spell-Rolls) section, broken down for a better display in the tooltip.

## TooltipDamageList
This entry will display the input damage defined by the spell.

Example: `data "TooltipDamageList" "DealDamage(1d4),Force)"`

## TooltipAttackSave
This entry will display the information defined in the [SpellRoll](/Information/Spells/Spell-Data/Spell-Rolls) section of the spell entry.

Example: `data "TooltipAttackSave" "RangedSpellAttack"`

## TooltipStatusApply
This entry will display any status effects applied by the spell, if any.

Example: `data "TooltipStatusApply" "ApplyStatus(FRIGHTENED, 100, 1)"`

## AdditionalTooltipEntries
Coming soon.
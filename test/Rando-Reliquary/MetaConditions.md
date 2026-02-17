---
title: MetaConditions
description: 
published: true
date: 2026-02-17T22:35:54.700Z
tags: 
editor: markdown
dateCreated: 2026-02-17T22:35:54.700Z
---

# MetaConditions
Condition(s) that alter the properties of a spell or group of spells without having to alter individual spells

**AdditionalConditions**: the actual additional conditions you add to the ConditionType (below) - can be basically anything you’d put in TargetConditions/RequirementConditions/etc based on ConditionType

**ConditionType**: which property of the spell are you altering?
* Roll
* OriginRoll
* ThrowableRoll
* AoE
* Target
* ThrowableTarget
* Forking
* Cycle
* Requirements
* OriginTarget
* Highlight
* ProjectileTarget

Idk what most of these do, only used Target and Requirements personally

**Filter**: which spells will be affected? Can filter by most things you can find in CommonConditions - `IsSpellOfSchool(), HasSpellFlag(), HasUseCosts(), HasFunctor()`, etc.
Can also filter single spells, groups of spells, can substitute a khn function
IMPORTANT: when filtering single spells, formatting is like this:
`SpellId(&apos;SpellName&apos;)`

**Name**: unique name for this meta condition, name it whatever

**OverrideOriginalCondition**: do you want this meta condition to replace the normal conditions for the spells and conditions you filtered? (Not recommended)

**UUID**: generate a new one
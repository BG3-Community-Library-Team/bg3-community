---
title: Container Spells
description: Defining Container Spells
published: true
date: 2024-05-10T19:41:48.282Z
tags: 
editor: markdown
dateCreated: 2024-05-10T19:41:48.282Z
---

# Container Spells
This information will define container spells as well as spells in the container.

## ContainerSpells
This line dictates the spells contained in a container spell. Which means it is the master spell that holds it's nested spells. This line is only needed for the master spell container.

Example: `data "ContainerSpells" "Target_EnhanceAbility_BearsEndurance_3;Target_EnhanceAbility_BullsStrength_3;Target_EnhanceAbility_CatsGrace_3;Target_EnhanceAbility_EaglesSplendor_3;Target_EnhanceAbility_FoxsCunning_3;Target_EnhanceAbility_OwlsWisdom_3"`

## SpellContainerID
This data is only meant for spells contained in a container spell. It dictates what spell your spell is nested in. It will never have more than one layer. This line is needed for any spell nested within a container.

Example: `data "SpellContainerID" "Target_EnhanceAbility"`
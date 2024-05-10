---
title: Use Costs
description: Defining UseCost data entry and list of potential resource costs.
published: true
date: 2024-05-10T20:29:56.705Z
tags: 
editor: markdown
dateCreated: 2024-05-10T20:29:56.705Z
---

# Use Costs
This tells the game what the spell should cost, in terms of resources, when cast, such as an Action Point, Bonus Action or even a custom resource.

Example: `data "UseCosts" "ActionPoint:1;Elemental_Essence:1"`

In this example, to cast the spell, the player would need to have at least 1 default action point, and 1 custom resource, Elemental Essence, which will be expended on cast.
---
title: Spell Animations
description: Defining SpellAnimations data entry.
published: true
date: 2024-05-10T20:30:44.006Z
tags: 
editor: markdown
dateCreated: 2024-05-10T20:30:44.006Z
---

# Spell Animation
This information is usually a uuid, or string of uuids in a specific format that dictate a few things, but primarily the motions the character will take when casting the spell. This is not to be confused with visual effects. This is what the character will do with their body as they prepare and/or cast the spell.

Example: `data "SpellAnimation" "3ff87abf-1ea1-4c32-aadf-c822d74c7dc0,,;,,;38cdb41c-2eec-4e03-bb31-83cff0346c35,,;85414f5f-b448-4dda-9370-1b6c4b38b561,,;d8925ce4-d6d9-400c-92f5-ad772ef7f178,,;,,;eadedcce-d01b-4fbb-a1ae-d218f13aa5d6,,;,,;,,"`

These multiple strings will dictate the movement based on character height, race, gender, among other things.
---
title: Spells and Status Sounds Reference
description: Helper reference to explain sound data on spells and statuses
published: true
date: 2024-05-17T23:27:17.308Z
tags: data, audio, sound, spells, statuses
editor: markdown
dateCreated: 2024-05-17T23:27:17.308Z
---

# Spells Sound System
The four phases of spell casting (when it comes to sounds) are "prepare", "loop", "cast", "impact". 
Prepare and Loop go together, as they are played prior to the spell being cast.
Cast is when the spell actually happens.
Impact is when the spell makes contact with the target (ally, enemy, ground, object, etc)

![spells_breakdown.png](/information/sound/spells_breakdown.png)

Data for sounds in Spells
```c
data "PrepareSound" "Spell_Prepare_Buff_Gen_L1to3" // Initially played at beginning of Prepare phase
data "PrepareLoopSound" "Spell_Prepare_Buff_Gen_L1to3_01_Loop" // Loops after PrepareSound, continues looping until CastSound
data "CastSound" "Spell_Cast_Buff_Blur_L1to3" // Plays when the spell is cast
data "TargetSound" "Spell_Impact_Buff_Blur_L1to3" // Plays when the spell impacts an object, character, ally etc
```

There is also a Vocal Component to go with `VerbalIntent`
```c
data "VocalComponentSound" "Vocal_Component_Disadvantage"
data "VerbalIntent" "Buff" // Not 100% sure if this affects the actual speech
data "SpellFlags" "HasVerbalComponent" // Make sure this flag is on your spell if you want the verbal sound with it
```

[Vocal Component Sounds](https://bg3.norbyte.dev/search?q=Vocal_Component_*+type%3Asound)
[Verbal Intent Options](https://bg3.norbyte.dev/search?q=VerbalIntent+type%3Aenumeration)

And finally a control for the loudness
```c
data "SpellSoundMagnitude" "Big" // Small, Normal, Big, None
```

# Status Sound System
Data sounds in a status
```c
data "SoundStart" "Misc_Status_AbsorbElementsActive_Start" // Plays when the status is first applied.
data "SoundLoop" "Misc_Status_AbsorbElementsActive_MO" // Plays on a loop throughout the status
data "SoundStop" "Misc_Status_AbsorbElementsActive_End" // Plays when the status is removed.
```

There is also a Vocal component for statuses. 
```c
data "SoundVocalStart" "NONE" // Plays when the status is first applied.
data "SoundVocalLoop" "LAUGHTERMANIACAL" // Plays on a loop throughout the status
data "SoundVocalEnd" "RECOVER" // Plays when the status is removed.
```
[Types of Vocal Start](https://bg3.norbyte.dev/search?q=SoundVocalType+type%3Aenumeration)
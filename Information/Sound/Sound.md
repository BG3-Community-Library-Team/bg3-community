---
title: Localization Voicelines
description: Explains the Voicelines in Localization
published: true
date: 2024-09-08T19:28:25.324Z
tags: audio, sound, localization
editor: markdown
dateCreated: 2024-09-08T19:27:00.922Z
---

# Localization Voicelines
While most sounds exist under SharedSounds.pak, there's a large portion of voicelines stored in a separate location in the game files. These voicelines, which are located in Data\Mods\Gustav\Localization\English\Soundbanks\, are lines used in cutscenes and in the overworld when the party comes across specific locations or during certain events.

While some of these lines exist in SharedSounds and vice-versa, the lines in Data\Mods\Gustav\Localization\English\Soundbanks\ do not affect any point and click dialogue, and changing any dialogue from cutscenes or the overworld which may appear in SharedSounds does not change the line actually played in game unless it's altered under Localization.

## Extracting Voicelines
These voicelines can be extracted by dropping the appropriate .pak into [ShinyHobo's BG3 Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool), extracting specific lines by prefix using the Multitool's search index, or by using [VGMStream/Foobar2000](https://vgmstream.org/)

## File Characteristics

Once extracted the voiceline files will read as having a prefix (unique to each voice actor/character), and a unique handle as a suffix.

For example:

```v2c76687d93a2477b8b188a14b549304c_h109f706dg36cfg4089ga269gbe33b34cc981.wem```

is the filename for Karlach's line: "*Mm - hello, love. Did you have a bad dream?*"

The prefix *'v2c76687d93a2477b8b188a14b549304c'* appears as the beginning of every one of Karlach's lines. The suffix is unique for each line.

Just like the rest of the audio files in the game, its a .wem file with the VORBIS format. This is important for if you decide you want to record your own voicelines. You can record them in whatever format you want (.wav is typically easiest), then convert it to a .wem using [wwise](https://www.audiokinetic.com/en/wwise/overview/). A more comprehensive tutorial for how to use wwise to edit in-game sounds can be found [here.](https://wiki.bg3.community/Tutorials/Sound/Replace-Sound)

When editing voice lines that specifically appear in cutscenes and conversations, it is extremely important that the voicelines remain the same duration as they appear in the vanilla game. This does not matter for overworld chatter.

## Packing Voiceline Replacers
In BG3's current state, their is no way to add voicelines or other sounds as the bank files (.bnk) cannot be edited and the game does not support custom bank files. However, voicelines can be changed by loading a .wem file with the same filename as the one you want to replace.

In order to pack the mods, replicate the file structure below and place it using the BG3 Multitool.

```MyNewVoicelines\Mods\Gustav\Localization\English\Soundbanks\```

Place your mod meta.lsx folder in the same directory as the Gustav folder above. Place your meta.lsx in that folder.

Alternatively, you can place the loose files into your data folder.

```Data\Mods\Gustav\Localization\English\Soundbanks\```

## List of Character Voice Prefixes

- Astarion: ```vc7c13742bacd460a8f65f864fe41f255```
- Gale: ```vad9af97d75da406aae137071c563f604```
- Halsin: ```v7628bc0e52b842a7856a13a6fd413323```
- Jaheira: ```v91b6b2007d004d628dc999e8339dfa1a```
- Lae'zel: ```v58a6933340bf83581d17fff240d7fb12```
- Karlach: ```v2c76687d93a2477b8b188a14b549304c```
- Minsc: ```v0de603c542e248119dadf652de080eba```
- Minthara: ```v257213130c15493581769f134385451b```
- Shadowheart: ```v3ed74f063c6042dc83f6f034cb47c679```
- Wyll: ```vc774d7644a1748dcb47032ace9ce447d```
- Tav voice 1: ```v24247531c4324f0f8f356c90c4844aa8```
- Tav voice 2: ```v2d206fda0d4f457fb4ea0fc18866f5dd```
- Tav voice 3: ```v3347e417d7ad4088bdd6d5565efcd815```
- Tav voice 4: ```v4df6dba085744704a9fba500da38e1e1```
- Tav voice 5 (Default Dark Urge): ```v869248f0468a474782d7e8efc3bbcacf```
- Tav voice 6: ```vb9b26a44943b44279890d81c7e81a75b```
- Tav voice 7: ```vf5b335b29cd94b38a4c1458b846ab499```
- Tav voice 8 [(Siggi)](https://www.nexusmods.com/baldursgate3/mods/9499): ```vfb6b53538d1445079222ceaec990fce9```

## Useful Localization Voiceline Tools
Simosas created the [Voiceline Tool](https://www.nexusmods.com/baldursgate3/mods/11810) which can generate a list of voiceline transcriptions and their corresponding wem filenames when you enter the character name into the terminal.




---
title: Toolkit FAQ
description: FAQ about the Larian Toolkit
published: false
date: 2024-09-15T05:45:07.932Z
tags: toolkit
editor: markdown
dateCreated: 2024-09-13T04:50:44.079Z
---

# Toolkit FAQ
<br />

- The following page covers the frequentyl asked questions about the toolkit.
- Huge thanks to Lunisole for compiling the majority of this knowledge.
- Thank you Arrow and jerinski for adding their own expertise.

<br />

- Feel free to add to this FAQ. Information about how to become a contributor are linked in the sidebar. 

<br />

### General Usage
<br />

_"Where can I find tutorials ?"_
- You can find tutorials for the toolkit on [mod.io or Larian's website under "Guides"](https://baldursgate3.game/mods#/r)

<br />

_"I want to leave some cells empty after overriding but it keeps filling in"_
- Right click &#8594; Tick 'Disable parent stat's field inheritance'.
<br />

### Converting your mods to the toolkit and uploading them to mod.io
<br />

_"How do I import old mods into the toolkit ?"_ 
- There is no way to simply import them, but you can follow the [converting our existing mods to toolkit](https://mod.io/g/baldursgate3/r/converting-our-existing-mods-to-toolkit) guide.

<br />


_"How do I publish my mod ?"_ 
- Project settings &#8594; Publish
- There also is a [guide](https://mod.io/g/baldursgate3/r/publishing-a-mod)
<br />

### Game Files
<br />

_"What is the difference between Shared/SharedDev and Gustav/GustavDev ?"_

- Shared and Gustav contain the Early Access content of the game. 
- SharedDev and GustavDev include everything else. 
- Shared folders are usually for player-related stats
- Gustavs are usually for NPC, items and such.


<br />

### Stats (Spells, Passives and Statuses) 
<br />

_"I can't find this spell in stats editor !"_

- Look for it in all Shared/SharedDev/Gustav and GustavDev.
- Or you can narrow it down with the answer above.

<br />

_"Why do my spells not get added with AddSpells() ?"_ 
- The stats editor doesn't display the *actual* name of spells. 
- Spell names will have a prefix, depending on their type. 
- For instance, the cantrip *FireBolt* is actually called *"Projectile_FireBolt"* and must be referenced as such in your SpellLists.

<br />

_"Is there a list of all functions and arguments for spells, passives and statuses ?"_ 

- Not really, but there are community made resources about it such as [LSLibDefinitions.xml](https://github.com/Norbyte/lslib/blob/master/LSLibDefinitions.xml)
- And another guide [coming soon](insert-JuuMs-guide-when-released-here).

<br />

_"How do I test spells, passives and statuses in the editor ?"_
- The  [debug console](https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips) ! .

<br />

### VFX

<br />

_"How do I do trajectories ?"_
- You're a nerd and you don't exist, nobody cares about trajectories.


<br />

### Visuals

<br />

_"How to export GR2 files into blender ?"_ 

- There is an [addon](https://github.com/Norbyte/dos2de_collada_exporter) for blender you can use 
- You can also just use [lslib](https://github.com/Norbyte/lslib) to convert gr2 into a blender format.
- For a more in-depth guide click [here](https://wiki.bg3.community/en/Tutorials/Visual/getting-started-with-3d-modding)

<br />


_"Do I need to create mesh entries for all races?"_
- No. The human body type for example covers all elf races.


<br />

_"Why can't I find armor/clothing textures/meshes by name?"_

- Textures for armors/clothing a lot of the times have the `HUM_M`  prefix.
- If you cannot find your resource by searching for `HUM_F_Insert_Armor_Name_Here`, try adding the `HUM_M` prefix:   `HUM_M_Insert_Armor_Name_Here` 
- You can also use UndefinedScribble's Resource [here](https://docs.google.com/document/d/1otN5cz-mpxg4NCOGOwvGM17fJQR_Sm7lOwS50ReHtEg/edit)
- Internally the game calls body type 2 the *Strong body type* or adds *S* to the body type, so *FS* for *Femme Strong* or *MS* for *Masc Strong*.
- Strong body type body meshes are usually shared across races, unlike body type 1. So the `HUM_FS`, `TIF_FS`, `ORC_F`, all might share the same top and bottom meshes for a given armor.


<br />

### Classes
<br />

_"How do I add classes or subclasses in the toolkit ?"_ 

- You can follow the [Adding new classes or subclasses guide](https://mod.io/g/baldursgate3/r/adding-new-classes)

<br />

### Races

<br />

_"How to do races in the toolkit ?"_ 
- Answer coming  <img src="/test/alithea/soon_tm.webp" alt="soon_tm.webp" width="40"/>


<br />

### Levels

<br />

_"How to I trigger CC in the toolkit ?"_ 
- Load the CC level
- Or use the debug console and the command *ccStartNew*.


<br />

_"How do I place my custom Item in the world ?"_ 
- You can't really "place" them in the world
- But you can put them inside containers by changing those container's TreasureTable(s).

<br />

### Localization

<br />

_"Are tooltips in description different in the toolkit ?"_ 
- Yes, the formatting changed a bit. For instance,
- `&lt;LSTag Tooltip="ArmourClass"&gt;Armour Class&lt;/LSTag&gt;` 
- is now: 
- `<LSTag Tooltip="ArmourClass"><em>Armour</em> </LSTag>`.

<br />

### Scripting

<br />

_"Is there any Osiris Documentation or guide ?"_
- The only documentation we have is from [dos2](https://docs.larian.game/Osiris_Overview)
- But there are also guides uploaded by [Larian](https://mod.io/g/baldursgate3/r/introduction-to-osiris).

<br />

_"How do I make custom khns in the toolkit ?"_
- They are not handled through the toolkit
- You will have to [add the files and write them on a text editor outside the toolkit.](https://mod.io/g/baldursgate3/r/adding-khonsu-khn-condition-scripts)

<br />


### Testing

<br />

_"How do I test my mod in the game ?"_ 
- Project settings &#8594; Publish Local 
- Save it into `Drive:\Users\Username\AppData\Local\Larian Studios\Baldur's Gate 3\Mods`
<br />

_"How do I respec in the toolkit ?"_ 
- Debug console and the command ccStartRespec.

<br />

<br />




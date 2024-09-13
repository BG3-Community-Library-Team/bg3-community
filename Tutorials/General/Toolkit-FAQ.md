---
title: Toolkit FAQ
description: FAQ about the Larian Toolkit
published: false
date: 2024-09-13T05:54:39.957Z
tags: toolkit
editor: markdown
dateCreated: 2024-09-13T04:50:44.079Z
---

# Toolkit FAQ



The following page covers the frequentyl asked questions about the toolkit.

## General Usage


#### "Where can I find tutorials !"
- Add link sto Larian tutorials here

#### How can I convert my mod to the toolkit/mod.io
- You cannot just add it, but have to convert it.
- Link Padmes guide here
#### "What is the difference between Shared/SharedDev and Gustav/GustavDev ?"

- Shared and Gustav contain what was in  the EA of the game. SharedDev and GustavDev include everything else. Usually, Shared folders are for player-related stats, when Gustavs are for NPC, items and such.


#### "I can't find this spell in stats editor !"

- Look for it in all Shared/SharedDev/Gustav and GustavDev. Or you can narrow it down with the answer above.


#### "Is there a list of all functions and arguments for spells, passives and statuses ?" 

- Not really, sadly, but there are community-made resources about it such as <https://github.com/Norbyte/lslib/blob/master/LSLibDefinitions.xml> [insert JuuM's guide when it's released].


#### "How to export GR2 files into blender ?" 

There's an addon for blender : <https://github.com/Norbyte/dos2de_collada_exporter>. 
- You can also just use <https://github.com/Norbyte/lslib> to convert gr2 into a blender format.


#### "How do I test spells, passives and statuses in the editor ?"
- The debug console ! <https://mod.io/g/baldursgate3/r/editor-shortcuts-and-tips>.

#### "How to I trigger CC in the toolkit ?" 
- Load CC level, or use debug console and the command ccStartNew.
#### "How do I respec in the toolkit ?" 
- Debug console and the command ccStartRespec.
#### "How do I import old mods into the toolkit ?" 
- Not "very easy" way, but you can follow <https://mod.io/g/baldursgate3/r/converting-our-existing-mods-to-toolkit> this guide.
#### "How do I place my custom Item in the world ?" 
-> You can't really "place" them in the world, but you can put them inside containers by changing those container's TreasureTable(s).
#### "How do I publish my mod ? " 
- Project settings -> Publish <https://mod.io/g/baldursgate3/r/publishing-a-mod>
#### "How do I test my mod in the game ?" 
- Project settings -> Publish Local and save it into Drive:\Users\Username\AppData\Local\Larian Studios\Baldur's Gate 3\Mods
#### "How do I do trajectories ?"
- You're a nerd and you don't exist, nobody cares about trajectories.
#### "How to do classes in the toolkit ?" 
- <https://mod.io/g/baldursgate3/r/adding-new-classes>
#### "I want to leave some cells empty after overriding but it keeps filling in"
- Right click -> Tick 'Disable parent stat's field inheritance'.
#### "Is there any Osiris Documentation or guide ?"
- The only documentation we have is from dos2 <https://docs.larian.game/Osiris_Overview> but there are also guides uploaded by Larian <https://mod.io/g/baldursgate3/r/introduction-to-osiris>.
#### "How do I make custom khns in the toolkit ?" 
- Not handled through the toolkit, you'll have to add the files and write them on a text editor outside the toolkit. <https://mod.io/g/baldursgate3/r/adding-khonsu-khn-condition-scripts>.
#### "Why do my spells not get added with AddSpells() ?" 
- The stats editor doesn't display the *actual* name of spells. Spell names will have a prefix, depending on their type. For instance, the cantrip FireBolt is actually called "Projectile_FireBolt" and must be referenced as such in your SpellLists.
#### "Are tooltips in description different in the toolkit ?" 
- Yes, the formatting changed a bit. For instance, `&lt;LSTag Tooltip="ArmourClass"&gt;Armour Class&lt;/LSTag&gt;` is now `<LSTag Tooltip="ArmourClass"><em>Armour</em> </LSTag>`.

#### "How to do races in the toolkit ?" 
- Add answer here
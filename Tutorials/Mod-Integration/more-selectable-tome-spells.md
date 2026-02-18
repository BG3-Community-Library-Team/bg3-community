---
title: Patching in More Spells to Selectable Tome Spells
description: How to patch more spells into the Selectable Tome Spells mod using the toolkit.
published: true
date: 2026-02-18T22:04:56.449Z
tags: spells, toolkit, mod integration, selectable tome spells
editor: markdown
dateCreated: 2025-12-09T23:14:42.527Z
---

[Mod-Integration](/Tutorials/Mod-Integration)# Patching in More Spells to Selectable Tome Spells
Guide written by EvilSnail0fDestruktion! 

This is a guide on patching more spells into the Selectable Tome Spells mod ([Nexus](https://www.nexusmods.com/baldursgate3/mods/16889), [mod.io](https://mod.io/g/baldursgate3/m/pactofthetome#description)), using the BG3 Modding Toolkit. 

> If you are patching spells from mod that isn't yours, make sure you get permission to patch them first!{.is-warning}

1. Make sure both mods are installed that you are patching (Selectable Tome Spells, and the mod you'd like to add spells from). You may need to use Eclip5e's Toolkit Project Converter ([Nexus](https://www.nexusmods.com/baldursgate3/mods/15515?tab=description), [GitHub](https://github.com/Eclip5eLP/bg3-convert2toolkit)) in order to unpack and import the mods to see the spells.
2. Open toolkit, create new mod. just use Basic_Level_A
3. in the upper left, go to project settings and add both mods as a dependency, then restart the toolkit
4. in the Roottemplates section, find a book (if you can see mine thats better otherwise i first started with `BOOK_Wizards_Tome_Ornate_D`, after you have one you can copy that one)
5. when you copy the roottemplate, rename the book to match the spell, and change the description (theres the display name and the internal name, rename both, internal has no spaces)
6. in the sidebar, search Use:
          A) Open and clear this out
          B) Add the SpellBook option
          C) add the spell you want
          D) add `StatusDurationMoreThan(context.Source, "SELECT_TOME_SPELLS", 0)` to use conditions (for deepened pact its `"SELECT_DP_SPELLS"` instead)
          E) save and close the popup window
7. open stats editor
8. add a new object stat, use `CPS_PactOfTheTome` as the parent, and your new book as the roottemplate
9. save object stats
10. add a treasure table. set the name to `CantripPactSpells` and set the appendnotoverride column to `yes`, put `I_<your book name from stats>` in the treasure column, frequency of 1 and drop count of 1,1 (see screenshot) - once the table exists just add substat dont create new tables each time - make sure to save after editing
11. back in the roottemplate, reselect the book and in the sidebar search stat
12. switch it to the stat you just added
13. search icon
14. find the icon for the spell
15. save roottemplates or all
16. open the story editor
17. create a new goal (only need to do this once not for each,the rest can just be added to the list like the treasure tables)
18. in the KB section, add `IF LevelGameplayReady(_,_) THEN DB_PactofTomeBooks(<your book name>_<your book uuid>, "<technical spell name>");` (see screenshot)
19. File -> build and reload
20. repeat steps 4-19 for each cantrip you are adding
21. For the level 3 spells for deepended pact, do the same except in stats for step 10:
          A) create a new spell - you will need to match the type (ie shout, target, etc) of the original, but use a different name
          B) set the original spell as the parent
          C) remove spell slots from the use cost
          D) add a cooldown of `onceperrest`
          E) save, make sure the new spell you just made is the one used by the DB and the book!!
          F) use `DeepenedPactSpells` instead of `CantripPactSpells`
and for step 18, the DB is ```DB_DeepenedPactBooks(<your book name>_<your book uuid>, "<technical spell name>");```
22. When you are done adding books, go to Project settings -> publish mod (maybe. test it works first, if you want)

I also added a tag so you can only use the books as a warlock and turned off the is pickpocketable so they can't be transferred in inventories, both of those are settings in the sidebar of the roottemplate. once you set them on the first one if you just copy it you don't need to set it for each

![evilsnail_selectabletomespellpatches_image01.png](/tutorials/patching_selectable_tome_spells/evilsnail_selectabletomespellpatches_image01.png)
![evilsnail_selectabletomespellpatches_image02.png](/tutorials/patching_selectable_tome_spells/evilsnail_selectabletomespellpatches_image02.png)

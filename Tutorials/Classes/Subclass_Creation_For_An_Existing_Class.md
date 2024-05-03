---
title: Subclass Creation For An Existing Class
description: 
published: true
date: 2024-05-03T05:51:58.504Z
tags: tutorial, subclasses
editor: markdown
dateCreated: 2024-05-03T05:26:42.090Z
---

# Introduction
When we create a class, most of what we do is new. A new parent classdescription entry, a new subclass entry for the new class, and new progressiontable,etc. In many cases we may just want to modify things that exist in the game already, like say give a class a new spell or maybe even a new subclass. This often requires us to reference UUID's, handles, etc to their corresponding part in the base game files. I've seen alot of people add subclasses for paladins so let's take a look at the paladin class and learn how we can modify it and add our own subclass.

# Goals
<details>
<summary><a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#disclaimer%EF%B8%8F">Disclaimer</a></summary>
</details>

<details>
<summary><a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#setup-for-modding%EF%B8%8F">Setup For Modding</a></summary>
<ul>
      <li><a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#mod-folder-setup">Mod Folder Setup</a></li>
      <li><a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#holder">Holder</a></li>
</ul>
</details>

<details>
<summary><a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#make-a-new-subclass-for-an-existing-class%EF%B8%8F">Make a new subclass for an existing class</a></summary>
<ul>
    <li><a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#classdescriptionslsx">ClassDescriptions.lsx</a></li>
    <li>
        <a href="https://wiki.bg3.community/en/Tutorials/Classes/Subclass_Creation_For_An_Existing_Class#progressionslsx">Progressions.lsx</a>
    </li>
</ul>
</details>

# Disclaimer[⬆️](#goals)
If you create a class, everything you do will be new. You wouldnt have to worry about your class mod having clashing progressions or anything like that with other mods. But this clearly wont apply to subclasses for existing ingame classes. If you create a subclass for the paladin and another person creates a different subclass for the paladin as well, those two mods will be in conflict. Think of it like this, when you make a new subclass you need to edit the classes progression, but if someone else has another mod affecting the same class, its not like either of you could account for the other persons subclass additions in their progressions. Two mods can not alter the same progression in this way without crashing (I think?). If you intend to share your mod, it is advised you take a look at [NellsRelo's BG3-Compatibility-Framework](https://github.com/BG3-Community-Library-Team/BG3-Compatibility-Framework) and learn how to integrate it with your mod. The [github wiki](https://github.com/BG3-Community-Library-Team/BG3-Compatibility-Framework/wiki) for it would be a good place to start.
# Setup For Modding[⬆️](#goals)
Lets set up our initial folder for our mod. All of our mod files and folders will go in here. We will cover it when we get to it, but this folder will essentially be packed by our multitool to be used as our .pak file which we place in the mods folder for your game. We will only need a few folders and files to get a simple item mod running. The bulk of the files we will deal with are .lsx files which are basically xml files. As your mod gets more intricate, you will need to add more folders/files but the following should be all we need to get started editing an item. Note the indentation on entries to indicate the file tree structure, ie. Localization folder has the English folder in it and so forth.

## Mod folder setup
* Localization : Starting off, we can make a folder called Localization inside your mod folder, in my case my folder called PaladinOfTheCosmicOrder. This folder/subfolder will deal with your ingame text. For example, we will later edit the name and description of the item we make, so it appears as so on the character creation screen.
   * English : Should be the language of your ingame text. If you are reading this, I'm guessing yours should also be English.
      * PaladinOfTheCosmicOrder.loca : The actual file that has the text you will see in the game for your mod. It is not properly readable so when we do start to add any text, we will adding it to the xml file below. We dont need to make this file but once we convert out PaladinOfTheCosmicOrder.xml file below with the multitool, we will get out PaladinOfTheCosmicOrder.loca file
      * PaladinOfTheCosmicOrder.xml : The readable version of the localization file for our mod. We will use the multitool to convert this to the .loca file.
* Mods : This will let the multitool know the folder it is housed in is an unpacked mod. When you pack your mod, a new folder will appear here with your mod name and inside it, a meta.lsx. This is very important, and we may need to make some changes to it if your mod isn't working right away when we load up the game.
* Public : The bulk of the work we do will be in this folder and its subfolders.
   * PaladinOfTheCosmicOrder : This folder name should be the name of your mod. (Capitalize the first letter)
      * ClassDescriptions : Will house your ClassDescriptions.lsx
         * ClassDescriptions.lsx : Where we will add the base information about our new sub class (note i didnt say edit the Paladin base class at all here.)
      *  Progressions : Will house your class progression information files
         * Progressions.lsx : Where you will create your progression table for your subclass as well as modify the paladin class progression table to add your subclass on progression


*<sub>If you are unsure about how to make the xml or lsx files, just open a text document and click save as. On the save as menu, change the "Save as type" option to "All types" and change the file name to your mod name. When you convert via the converter app, make sure you specify the file name and extension</sub>

# Make a new subclass for an existing class[⬆️](#goals)
While not required, it would be helpful to read the [Basic Class Creation](https://wiki.bg3.community/en/Tutorials/Classes/Basic-Class-Creation) guide to have some background. This guide will try to keep it simple but if something isnt clicking I may have glossed over something that is already covered in that guide. Anyways, if you did read it, you will remember that when we made our class Quickster, we worked heavily with the file ClassDescriptions.lsx and Progressions.lsx. As you may have guessed, we will be doing the same here albeit a bit differently since we are modify something that exists, not creating from scratch.
## ClassDescriptions.lsx
When making the quickster mod, you may remember that we added an entire new entry in ClassDescriptions.lsx. We actually dont need to do that for this. You would think that since we are editing the Paladin class, we need to add in the Paladin classdescription entry. We actually don't! There is nothing in the base ClassDescription that relates to subclasses for that class. However, there is one thing we do need to grab, the UUID for the Paladin class. I will include it here for simplicity but obviously you will need to get the UUID of whatever class you are editing. The Paladin class UUID is ff4d9497-023c-434a-bd14-82fc367e991c. We will need this for the entry we plan on adding into our ClassDescription file, this entry being the actual subclass node.
The major difference between the class entries and subclasses is that subclasses have a parentguid attribute that refers back to the main class of the subclass, which is why we needed the paladin one. Lets make a ClassDescription node for the subclass using the Paladin uuid as a parent guid.

PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\ClassDescriptions\ClassDescriptions.lsx
```
...
<?xml version="1.0" encoding="utf-8"?>
<save>
  <version major="4" minor="4" revision="0" build="444"/>
  <region id="ClassDescriptions">
    <node id="root">
      <children>
        <node id="ClassDescription">
          <attribute id="CharacterCreationPose" type="guid" value="0f07ec6e-4ef0-434e-9a51-1353260ccff8"/>
          <attribute id="Description" type="TranslatedString" handle="h45ac7894a2254291976ccbd206ad20139783" version="1"/>
          <attribute id="DisplayName" type="TranslatedString" handle="h3954714727074b3fac8c2654befb2010f0c0" version="1"/>
          <attribute id="LearningStrategy" type="uint8" value="1"/>
          <attribute id="MustPrepareSpells" type="bool" value="false"/>
          <attribute id="Name" type="FixedString" value="PaladinOfTheCosmicOrder"/>
          <attribute id="ParentGuid" type="guid" value="ff4d9497-023c-434a-bd14-82fc367e991c"/>
          <attribute id="PrimaryAbility" type="uint8" value="6"/>
          <attribute id="ProgressionTableUUID" type="guid" value="d7f05d6e-a3df-4a68-8438-db3edca3f7bf"/>
          <attribute id="ShortName" type="TranslatedString" handle="h8f1ad6cdb5cd430aa56c8bfb33e8c31042a9" version="1"/>
          <attribute id="SoundClassType" type="FixedString" value="Paladin"/>
          <attribute id="SpellCastingAbility" type="uint8" value="6"/>
          <attribute id="UUID" type="guid" value="ba092169-d736-49e5-b599-2385de6d6069"/>
        </node>
      </children>
    </node>
  </region>
</save>
...
```

The most important thing here is that I used the Paladin UUID for the ParentGuid and made sure to add the corresponding new uuids for the subclasses uuid and its progressiontable, as well as new handles. I mostly included this part in the guide so you can see that even though we are modifying the Paladin class, we don't need to port over the entire Paladin entry. We only bring over to our mod whatever is new (this subclass entry) and whatever we intend to alter (which you will see in Progressions below).

## Progressions.lsx
Progressions are essentially whatever our class (or subclass) gets on Character Creation and level ups. Remember how I said we didn't need to add the node for the Paladin in ClassDescriptions.lsx? I said the reason was because we aren't changing anything in that entry, i.e. nothing in the node refers to subclasses for the class. However, progression entries do refer to subclasses, specifically at the levels the class gets the subclass option. Lets look at the base level 1 progression (CC) for the Paladin since thats when the paladin class chooses subclasses.
```
...
<node id="Progression">
    <attribute id="Boosts" type="LSString" value="ProficiencyBonus(SavingThrow,Wisdom);ProficiencyBonus(SavingThrow,Charisma);Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(HeavyArmor);Proficiency(Shields);Proficiency(SimpleWeapons);Proficiency(MartialWeapons);ActionResource(LayOnHandsCharge,3,0);ActionResource(ChannelOath,1,0)"/>
    <attribute id="Level" type="uint8" value="1"/>
    <attribute id="Name" type="LSString" value="Paladin"/>
    <attribute id="ProgressionType" type="uint8" value="0"/>
    <attribute id="Selectors" type="LSString" value="SelectSkills(627af380-2bbb-4a9f-9571-5ec781a6daf4,2);AddSpells(fb407d81-3a05-46f1-9153-0fb27dce95b6,,,,AlwaysPrepared)"/>
    <attribute id="TableUUID" type="guid" value="ba2afe85-acba-4ea1-a238-2b4543f47821"/>
    <attribute id="UUID" type="guid" value="b60618d1-c262-42b5-9fdd-2c0f7aa5e5af"/>
    <children>
        <node id="SubClasses">
            <children>
                <node id="SubClass">
                    <attribute id="Object" type="guid" value="b36d247e-d39f-4ae9-9476-3ec315c55789"/>
                </node>
                <node id="SubClass">
                    <attribute id="Object" type="guid" value="1c761ad0-6f5f-409e-ac1d-ddf6f85c1fc4"/>
                </node>
            </children>
        </node>
    </children>
</node>
...
```

Since we want to add a subclass to the Paladin class, this is where we would do it. This means modifying this entry to include our subclass. We will have to copy the exact node as is first, this is very important. For example, if you were to forget to include `Proficiency(HeavyArmor)` in `Boosts`, you would have overwritten the base games Paladin file and it wouldn't have proficiency in heavy armor anymore! If we edit something that exists in the game, we should still be retaining all the other information in the node aside from what we are changing to avoid altering unnecessary things when we try to modify something. Lets carefully add a new subclass node in the progression node.

PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Progressions\Progressions.lsx
```
...
<node id="Progression">
    <attribute id="Boosts" type="LSString" value="ProficiencyBonus(SavingThrow,Wisdom);ProficiencyBonus(SavingThrow,Charisma);Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(HeavyArmor);Proficiency(Shields);Proficiency(SimpleWeapons);Proficiency(MartialWeapons);ActionResource(LayOnHandsCharge,3,0);ActionResource(ChannelOath,1,0)"/>
    <attribute id="Level" type="uint8" value="1"/>
    <attribute id="Name" type="LSString" value="Paladin"/>
    <attribute id="ProgressionType" type="uint8" value="0"/>
    <attribute id="Selectors" type="LSString" value="SelectSkills(627af380-2bbb-4a9f-9571-5ec781a6daf4,2);AddSpells(fb407d81-3a05-46f1-9153-0fb27dce95b6,,,,AlwaysPrepared)"/>
    <attribute id="TableUUID" type="guid" value="ba2afe85-acba-4ea1-a238-2b4543f47821"/>
    <attribute id="UUID" type="guid" value="b60618d1-c262-42b5-9fdd-2c0f7aa5e5af"/>
    <children>
        <node id="SubClasses">
            <children>
                <node id="SubClass">
                    <attribute id="Object" type="guid" value="b36d247e-d39f-4ae9-9476-3ec315c55789"/>
                </node>
                <node id="SubClass">
                    <attribute id="Object" type="guid" value="1c761ad0-6f5f-409e-ac1d-ddf6f85c1fc4"/>
                </node>
                <node id="SubClass">
                    <attribute id="Object" type="guid" value="ba092169-d736-49e5-b599-2385de6d6069"/>
                </node>
            </children>
        </node>
    </children>
</node>
...
```

Remember the uuid that goes here the one I generated for uuid in my classdescriptions node for the subclass. Note that I retained all the other information in the file, including the subclasses that exist already. Lets not forget to add our actual progression node for our subclass. Quick and easy, dont forget to use the progressiontableid you generated in classdescriptions. Here is the whole file.

PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Progressions\Progressions.lsx
```
<?xml version="1.0" encoding="utf-8"?>
<save>
  <version major="4" minor="0" revision="4" build="444"/>
  <region id="Progressions">
    <node id="root">
      <children>
        <node id="Progression">
            <attribute id="Boosts" type="LSString" value="ProficiencyBonus(SavingThrow,Wisdom);ProficiencyBonus(SavingThrow,Charisma);Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(HeavyArmor);Proficiency(Shields);Proficiency(SimpleWeapons);Proficiency(MartialWeapons);ActionResource(LayOnHandsCharge,3,0);ActionResource(ChannelOath,1,0)"/>
            <attribute id="Level" type="uint8" value="1"/>
            <attribute id="Name" type="LSString" value="Paladin"/>
            <attribute id="ProgressionType" type="uint8" value="0"/>
            <attribute id="Selectors" type="LSString" value="SelectSkills(627af380-2bbb-4a9f-9571-5ec781a6daf4,2);AddSpells(fb407d81-3a05-46f1-9153-0fb27dce95b6,,,,AlwaysPrepared)"/>
            <attribute id="TableUUID" type="guid" value="ba2afe85-acba-4ea1-a238-2b4543f47821"/>
            <attribute id="UUID" type="guid" value="b60618d1-c262-42b5-9fdd-2c0f7aa5e5af"/>
            <children>
                <node id="SubClasses">
                    <children>
                        <node id="SubClass">
                            <attribute id="Object" type="guid" value="b36d247e-d39f-4ae9-9476-3ec315c55789"/>
                        </node>
                        <node id="SubClass">
                            <attribute id="Object" type="guid" value="1c761ad0-6f5f-409e-ac1d-ddf6f85c1fc4"/>
                        </node>
                        <node id="SubClass">
                            <attribute id="Object" type="guid" value="ba092169-d736-49e5-b599-2385de6d6069"/>
                        </node>
                    </children>
                </node>
            </children>
        </node>
        <node id="Progression">
          <attribute id="Level" type="uint8" value="1"/>
          <attribute id="Name" type="LSString" value="PaladinOfTheCosmicOrder"/>
          <attribute id="ProgressionType" type="uint8" value="1"/>
          <attribute id="Selectors" type="LSString" value=""/>
          <attribute id="TableUUID" type="guid" value="d7f05d6e-a3df-4a68-8438-db3edca3f7bf"/>
          <attribute id="UUID" type="guid" value="69ed8e46-6896-45f9-a2e8-abda4dc0350c"/>
        </node>
      </children>
    </node>
  </region>
</save>
```

And that's really it. If you load up your game and select paladin, you will now see the Paladin Of The Cosmic Order appear as a subclass for the paladin!
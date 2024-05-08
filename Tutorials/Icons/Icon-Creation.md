---
title: Icon Creation
description: Apply icons to your items, passives, skills, spells, etc. (Does not include class/subclass icons)
published: true
date: 2024-05-08T06:57:38.478Z
tags: tutorial, icons, icon, atlas
editor: markdown
dateCreated: 2024-05-08T06:50:52.688Z
---

# Introduction
This guide is intended to help you create and work with different types of icons in the game. Alot of this was learned from [Loz's guide that he posted on discord](https://discord.com/channels/98922182746329088/1161812332721209354) and is a much more concise and quick way to learn about icons then here so I suggest you check it out. Loz also includes not only file templates to use for this but background pngs thats match standard ones in the game that will help with your icon creation journey. This tutorial will show you how to add icons by following along as I apply icons to various skills/spells/passives for the class Paladin Of The Cosmic Order. 

# Goals
<details>
<summary><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#setup-for-modding%EF%B8%8F">Setup For Modding</a></summary>
<ul>
      <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#mod-folder-setup">Mod Folder Setup</a></li>
      <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#flesh-out-paladinofthecosmicorder-for-icon-addition">Flesh out PaladinOfTheCosmicOrder for icon addition</a></li>
</ul>
</details>

<details>
<summary><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#apply-icons%EF%B8%8F">Apply Icons</a></summary>
<ul>
    <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#tooltip-icons">Tooltip Icons</a></li>
    <li>
        <a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#controller-icons">Controller Icons</a>
    </li>
</ul>
</details>

<details>
<summary><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#add-a-controller-icon%EF%B8%8F">Add a controller icon</a></summary>
<ul>
    <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#skill-icons">Skill Icons</a></li>
    <li>
        <a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#item-icons">Item Icons</a>
    </li>
</ul>
</details>

<details>
<summary><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#add-a-hotbar-icon%EF%B8%8F">Add a hotbar icon</a></summary>
<ul>
    <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#icon-atlas">Icon Atlas</a></li>
    <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#icon-atlas-map">Icon Atlas Map</a></li>
    <li><a href="https://wiki.bg3.community/Tutorials/Icons/Icon-Creation#_mergedlsx">_merged.lsx</a></li>
</ul>
</details>

# Setup For Modding[⬆️](#goals)
Lets set up our initial folder for our mod. I will be creating a generic class mod with  some spells/passives so I have something to apply my icons to. Note the indentation on entries to indicate the file tree structure, ie. Localization folder has the English folder in it and so forth.

## Mod folder setup
* Localization : Starting off, we can make a folder called Localization inside your mod folder, in my case my folder called PaladinOfTheCosmicOrder. This folder/subfolder will deal with your ingame text. For example, we will later edit the name and description of the skill we use for the icon, so it appears as so on the character creation screen. (I guess for icons you don't need this folder but its good to just keep things standard, most mods should contain a localization folder.)
   * English : Should be the language of your ingame text. If you are reading this, I'm guessing yours should also be English.
      * PaladinOfTheCosmicOrder.loca : The actual file that has the text you will see in the game for your mod. It is not properly readable so when we do start to add any text, we will adding it to the xml file below. We dont need to make this file but once we convert out PaladinOfTheCosmicOrder.xml file below with the multitool, we will get out PaladinOfTheCosmicOrder.loca file
      * PaladinOfTheCosmicOrder.xml : The readable version of the localization file for our mod. We will use the multitool to convert this to the .loca file.
* Mods : This will let the multitool know the folder it is housed in is an unpacked mod. When you pack your mod, a new folder will appear here with your mod name and inside it, a meta.lsx. This is very important, and we may need to make some changes to it if your mod isn't working right away when we load up the game.
* Public : The bulk of the work we do will be in this folder and its subfolders.
   * PaladinOfTheCosmicOrder : This folder name should be the name of your mod. (Capitalize the first letter)
      * ClassDescriptions : Will house your ClassDescriptions.lsx
         * ClassDescriptions.lsx : The class we are making to test our icons and junk will be added in here
      * Progressions : Will house your class progression information files
         * Progressions.lsx : Gotta have a level 1 progression, ya know the drill
      * Assets :
         * Textures : 
            * Icons :
               * Icons_PaladinOfTheCosmicOrder.dds :
      * GUI :
         * Icons_Skills.lsx :
      * Content :
         * UI :
            * [PAK]_UI :
               * _merged.lsx (i think merged.lsx works as well?) : 
   * Game :
      * GUI :
         * Assets :
            * Tooltips :
               * Icons :
               * ItemIcons :
            * ControllerUIIcons : 
               * skills_png : 
               * items_png :

*<sub>If you are unsure about how to make the xml or lsx files, just open a text document and click save as. On the save as menu, change the "Save as type" option to "All types" and change the file name to your mod name. When you convert via the converter app, make sure you specify the file name and extension</sub>

## Flesh out PaladinOfTheCosmicOrder for icon addition
In order to add icons, we need to have things that could have icons attached to them! Let's quickly add in some base spells, passives, etc so we can add icons to them. Its more of a setup step so going to go through this quickly. Understanding the stuff outside of icon related matters isn't important here. Essentially, what I did to get things ready for icon addition is take the level 1 passive and spell the oath of ancients subclass gets and changed the names and handles to better fit my subclass. I didnt actually change what the spells and passives do, I dont care about that here like I said. Icons only.

### Progressions.lsx
Here is my newly updated progressions entry node for my subclass. Note the added passives and spell as well as the new name.
PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Progressions\Progressions.lsx
```
...
<node id="Progression">
  <attribute id="Level" type="uint8" value="1"/>
  <attribute id="Name" type="LSString" value="PaladinOfTheCosmicOrder"/>
  <attribute id="PassivesAdded" type="LSString" value="Oath_Cosmics_Tenents;Cosmics_The_Scale_Of_Everything"/>
  <attribute id="ProgressionType" type="uint8" value="1"/>
  <attribute id="Selectors" type="LSString" value="AddSpells(0895375b-2f7a-48dd-8318-619ddfc0f8db,,,,AlwaysPrepared)"/>
  <attribute id="TableUUID" type="guid" value="d7f05d6e-a3df-4a68-8438-db3edca3f7bf"/>
  <attribute id="UUID" type="guid" value="69ed8e46-6896-45f9-a2e8-abda4dc0350c"/>
</node>
...
```

### Passive.txt
I added the Oath_Ancients_Tenents passive like I said and simply changed the handles and entry name. I also added my passive that I want to actually change, Cosmics_The_Scale_Of_Everything.
PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Stats\Generated\Data\Passive.txt
```
new entry "Oath_Cosmics_Tenents"
type "PassiveData"
data "DisplayName" "h3165b913b2044509b6371cf19e9a3ae32g22"
data "Description" "ha70437670a164c4c9c9442af60639723155e"
data "ExtraDescription" "h875a4e75g1623g490agbe57g1f7c561b4989;2"
data "Icon" "Action_DivineIntervention_Weapon"
data "Properties" "Highlighted"

new entry "Cosmics_The_Scale_Of_Everything"
type "PassiveData"
data "DisplayName" "h9c2f5a247fc54f87b8fde47c5ea8af5b60f8"
data "Description" "h5eec7660ad2c45b5bf4045b168cd90f7c360"
data "ExtraDescription" "h875a4e75g1623g490agbe57g1f7c561b4989;2"
data "Icon" "Action_DivineIntervention_Weapon"
data "Properties" "Highlighted"
```

### SpellLists.lsx
Like for my Passive.txt, I grabbed the related spell the ancients subclass gets and changed the comment, the spell name, and the uuid.
PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Lists\SpellLists.lsx
```
<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="3" revision="0" build="300"/>
    <region id="SpellLists">
        <node id="root">
            <children>
                <node id="SpellList">
                    <attribute id="Comment" type="LSString" value="Paladin Cosmics Spells level 1"/>
                    <attribute id="Spells" type="LSString" value="Shout_UpholdBalance"/>
                    <attribute id="UUID" type="guid" value="0895375b-2f7a-48dd-8318-619ddfc0f8db"/>
                </node>
            </children>
        </node>
    </region>
</save>
```

### Spell_Shout.txt
And finally let's make the spell that we just put in the spell list. I use the spell that oath of ancients has at level 1, Healing Radiance, and change the entry anme and handles for my use case for my cosmic subclass.
PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Stats\Generated\Data\Spell_Shout.txt
```
new entry "Shout_UpholdBalance"
type "SpellData"
data "SpellType" "Shout"
data "SpellProperties" "RegainHitPoints(ClassLevel(Paladin)+Cause.CharismaModifier+ProficiencyBonus);ApplyStatus(SELF,HEALING_RADIANCE,100,1)"
data "AreaRadius" "3"
data "TargetConditions" "not Enemy() and not Dead() and not Tagged('UNDEAD') and not Tagged('CONSTRUCT') and Character() "
data "Icon" "Action_Paladin_HealingRadiance"
data "DisplayName" "h350ba5243dbb4b3aabfcd6ad0acc1645a523"
data "Description" "hfef1fb8574c34137945a9a0e1891b3938bee"
data "DescriptionParams" "RegainHitPoints(ClassLevel(Paladin)+Cause.CharismaModifier+ProficiencyBonus);"
data "TooltipDamageList" "RegainHitPoints(ClassLevel(Paladin)+Cause.CharismaModifier+ProficiencyBonus)"
data "TooltipStatusApply" "ApplyStatus(HEALING_RADIANCE,100,1)"
data "TooltipPermanentWarnings" "662e013d-e5cb-4669-9a4b-771636b24aa2"
data "CastSound" "Action_Cast_Paladin_HealingRadiance"
data "TargetSound" "Action_Impact_Paladin_HealingRadiance"
data "CastTextEvent" "Cast"
data "UseCosts" "BonusActionPoint:1;ChannelOath:1"
data "SpellAnimation" "83fb0115-57dd-4cce-ac40-87182b2865e2,,;,,;eb4f3d5f-6815-4ad5-a5af-870942af0863,,;ba5068a2-ed31-4b9a-87cc-be28edb9ad25,,;42014429-21fb-412d-bba6-0f8216f5e502,,;,,;43fa5e31-ad7e-47a9-9ca2-f6d40ba8e1cf,,;,,;,,"
data "VerbalIntent" "Healing"
data "SpellStyleGroup" "Class"
data "HitAnimationType" "MagicalNonDamage"
data "PrepareEffect" "f719faf1-83e7-4407-a2f2-0880e26f9ca5"
data "CastEffect" "a851aded-d542-482c-81ea-aa807d8b630f"
data "TargetEffect" "1dcca477-79be-4e15-bb70-8680a6dc49e5"
```

*Dont forget to link your uuids and handles folks!

I did these 4 files really fast but if you followed my other guides it shouldn't be too confusing. I don't want to cover it anyways since this guide focuses on icons, not spells or passives to a class. If you want to see that, go view the class guide I have uploaded. Anyways, we now passives/spells that we can attach an icon to. At the moment since I copied everything from oath of ancients and just changed handles, uuids, and names, we still have the oath of ancients icons for those things. Let's finally get started with altering icons.


# Apply Icons[⬆️](#goals)
We have the groundwork for our icon but we haven't actually made an icon to use yet. If you are so artistically inclined, you can always make your own. Plenty of good free editing software to use for it, ranging in simplicity from MS paint to gimp. I suck at art so I'm going to make an icon using Dall-e. Let's quickly use it to generate an icon related to my subclass. Lets work with the passive icon first, Cosmics_The_Scale_Of_Everything. (Oath_Cosmics_Tenents I added because all the paladin subclasses have an oath tenets passive, I figured I should keep it consistent a bit. They all share the same icon so I won't be changing this one). I have already generated one via Dall-e, so I will quickly convert it to a more usable file since Dall-e gives me a webm. I simply opened the webm in paint and saved as a png. Then I opened the image in paint 3d. Using the magic eraser in paint 3d, I basically cut out my icon from the original so I can get rid of the extra background stuff. We want a transparent background so by cutting out the icon itself and copying it, delete everything, make the canvas transparent and then paste the cut icon. Save the new image but make sure to alter the ratio of the png (380x380 for tooltips, 144x144 for controller, 64x64 for hotbar) before you save. Now we need to convert the png to a .DDS (uppercase), you can do this using an online converter. Like before, multiple way to do this, I use my vscode extension to do this for me but if you don't want to use it, you could try this png converter site, https://convertio.co/png-dds/. 

## Tooltip Icons
In case you didn't know already, tooltips are what you see when you hover over something in game to get more info, i.e. display the tooltip. The tooltip that pops up will have the icon that is referenced in the data/Passive.txt file. So let's take look at our Passive.txt file, specifically the data icon entry for `Cosmics_The_Scale_Of_Everything`. Like I said, I just copied the ancients information to make this data entry, so our icon is the icon for ancients. Lets change this now. The value inside here should be the name of the .DDS file you made, so in my case scale_of_everything.DDS. Here is my entry now after the change to point to my icon. 
PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Stats\Generated\Data\Passive.txt
```
...
new entry "Cosmics_The_Scale_Of_Everything"
type "PassiveData"
data "DisplayName" "h9c2f5a247fc54f87b8fde47c5ea8af5b60f8"
data "Description" "h5eec7660ad2c45b5bf4045b168cd90f7c360"
data "ExtraDescription" "h875a4e75g1623g490agbe57g1f7c561b4989;2"
data "Icon" "scale_of_everything"
data "Properties" "Highlighted"
```

We are now pointing to the correct icon as you can see from `data "Icon" "scale_of_everything"`. However, we haven't actually placed our icon in the correct location for it to be used for tooltips. In our setup for modding earlier, we made a folder PaladinOfTheCosmicOrder\Public\Game\GUI\Assets\Tooltips\Icons. We will be placing our .DDS file in here (don't mistake for \ItemIcons). We should also put our png in here as well. I don't know if it matters but it's good for reference at least.

Tooltip icons are pretty straightforward. We can launch the game now and should be able to see out icon when viewing the tooltip for our passive.
Here it is! Wow much beauty, such style!
![image](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/7171633e-78fe-49b4-a4e9-d7d3470cb6d3)

But hang on! You can see that the icon shows on the tooltip but it doesn't show on the part I'm hovering to display the tooltip. Similarly, on CC you may have noticed where your passive is shown, shows the same icon:
![image](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/218fca11-bce3-46be-b420-b9aa5a9d9326)

As you can see, the passive The Scale Of Everything does appear but there is a weird icon there. That is a default icon the game puts if you have an error with your current one and it can't be read. We need to add our icon to other locations for them to appear in these locations.

## Controller Icons
*I'm going to level with you here, I don't know what a controller icon is. But this should be the right way to set it up.<br>
Remember how I suggested you make a 144x144 png on top of the 380x380 for tooltip icons? Controller icons require 144x144 ratio. Assuming you made it when I mentioned it, all we need to do here is drag it to the correct folder, which we already made earlier in our setup for modding above. The folder we need to drop our .DDS and png into is PaladinOfTheCosmicOrder\Public\Game\GUI\Assets\ControllerUIIcons\skills_png.

## Hotbar Icons
The most important icons to add as well as being the most difficult. You are going to need a 64x64 version of your icon which you should have made earlier when I mentioned it. To get hotbar icons working, 3 files need to be create/adjusted:
1) Icon Atlas: PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Assets\Textures\Icons\Icons_PaladinOfTheCosmicOrder.dds
2) Icon Atlas Map: PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\GUI\Icons_Skills.lsx
3) _merged.lsx: PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Content\UI\[PAK]_UI\_merged.lsx

Lets go over each one, one by one.

### Icon Atlas
Your icon atlas will be a sheet of all your sprites/icons you are using. Basically, it's like putting them in a row so another file (the icon atlas map) can then find it and use it. There are a few ways to apply your icon to an atlas. When I first started, I used [Loz's guide that he posted on discord](https://discord.com/channels/98922182746329088/1161812332721209354) to learn and used the blank atlas he provided on his initial discord post/guide so I will show that method first here. This is also valuable because Loz has posted generic background the game uses for icons so if you want to get more indepth you can add these to your icons with a bit of image editing to have a more authentic look. I suggest you vist the link and get the blank atlas from him at least to follow along and make your own icon atlas from it. Anyways, I downloaded the empty icon atlas Loz provided and converted it to a png using a converter again. Then I used paint 3d to open it as well as my icon. I copied and pasted my icon to the top left of the icon atlas. It looks a bit like this for reference (did you remember to make them 64x64, they don't always need to be but for the atlas we are using from Loz, 64 is the way. Your hotbar icon size scales with your atlas size):
![image](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/1ba0d818-a16c-441d-862e-07a87ab458b1)

Once this is complete, we will want to convert our png atlas back to .dds, the casing matters so make sure its not upper case like the other .DDS files we have made. The proper name should be Icons_{ModName}.dds so in my case its Icons_PaladinOfTheCosmicOrder.dds. Like I mentioned above, move this file to PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Assets\Textures\Icons\Icons_PaladinOfTheCosmicOrder.dds.

### Icon Atlas Map
The icon atlas map is meant to identify/map the locations of your icons on the atlas. We have one icon on our Icons_PaladinOfTheCosmicOrder.dds and we need to define its location for the game to find it. Let's take a look at a generic icon atlas map.

```
<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="6" build="5" />
    <region id="TextureAtlasInfo">
        <node id="root">
            <children>
                <node id="TextureAtlasIconSize">
                    <attribute id="Height" type="int64" value=""/>
                    <attribute id="Width" type="int64" value=""/>
                </node>
                <node id="TextureAtlasPath">
                    <attribute id="Path" type="LSString" value=""/>
                    <attribute id="UUID" type="FixedString" value=""/>
                </node>
                <node id="TextureAtlasTextureSize">
                    <attribute id="Height" type="int64" value=""/>
                    <attribute id="Width" type="int64" value=""/>
                </node>
            </children>
        </node>
    </region>
    <region id="IconUVList">
        <node id="root">
            <children>
                <node id="IconUV">
                    <attribute id="MapKey" type="FixedString" value=""/>
                    <attribute id="U1" type="float" value=""/>
                    <attribute id="U2" type="float" value=""/>
                    <attribute id="V1" type="float" value=""/>
                    <attribute id="V2" type="float" value=""/>
                </node>	
                <node id="IconUV">
                    <attribute id="MapKey" type="FixedString" value=""/>
                    <attribute id="U1" type="float" value=""/>
                    <attribute id="U2" type="float" value=""/>
                    <attribute id="V1" type="float" value=""/>
                    <attribute id="V2" type="float" value=""/>
                </node>
            </children>
        </node>
    </region>
</save>
```

The top part of the atlas map describes the atlas size, its icon sizes, as well as its path. 64x64 for our icons like I mentioned. If you downloaded the atlas from Loz, your atlas as a whole is 2048x2048. We also know the location of our atlas, Assets/Textures/Icons/Icons_PaladinOfTheCosmicOrder.dds. The section below that `<region id="IconUVList">` describes the actual location of icons on the atlas. This all scales based of what you set as your atlas size and your icon size but I'm going to assume you did as I did (64x64 and 2048x2048). Anyways, lets look at that first node, `<node id="IconUV">`. Inside it, we see U1, U2, V1, and V2. These are basically the edges of your icons location on the atlas. These values are determined by the size of your icon and your atlas size as a whole. If you followed 64x64 and 2048x2048 you shouldn't have a problem copying the U1,U2,V1, and V2 that I use here without having to do the math to figure out what you should place for them. Let's fill out the values we need and go over them:

PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\GUI\Icons_Skills.lsx
```
<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="6" build="5" />
    <region id="TextureAtlasInfo">
        <node id="root">
            <children>
                <node id="TextureAtlasIconSize">
                    <attribute id="Height" type="int64" value="64"/>
                    <attribute id="Width" type="int64" value="64"/>
                </node>
                <node id="TextureAtlasPath">
                    <attribute id="Path" type="LSString" value="Assets/Textures/Icons/Icons_PaladinOfTheCosmicOrder.dds"/>
                    <attribute id="UUID" type="FixedString" value="5099f782-7207-403e-8914-1c2efc836a06"/>
                </node>
                <node id="TextureAtlasTextureSize">
                    <attribute id="Height" type="int64" value="2048"/>
                    <attribute id="Width" type="int64" value="2048"/>
                </node>
            </children>
        </node>
    </region>
    <region id="IconUVList">
        <node id="root">
            <children>
                <node id="IconUV">
                    <attribute id="MapKey" type="FixedString" value="scale_of_everything"/>
                    <attribute id="U1" type="float" value="0.0"/>
                    <attribute id="U2" type="float" value="0.03125"/>
                    <attribute id="V1" type="float" value="0.0"/>
                    <attribute id="V2" type="float" value="0.03125"/>
                </node>	
                <node id="IconUV">
                    <attribute id="MapKey" type="FixedString" value=""/>
                    <attribute id="U1" type="float" value="0.03125"/>
                    <attribute id="U2" type="float" value="0.0625"/>
                    <attribute id="V1" type="float" value="0.0"/>
                    <attribute id="V2" type="float" value="0.03125"/>
                </node>
            </children>
        </node>
    </region>
</save>
```

Lets go over the attributes I added.

* **Height/Width (TextureAtlasIconSize)** : What the size of your icons are. You shouldn't be getting tricky with this, make your atlas 2048x2048 so you can simply have your icon sizes as 64. Its rare you would ever use anything other then 64 for height and width

* **Path** : The path to the atlas. It should typically look like `Assets/Textures/Icons/Icons_MODNAME.dds`, so in my case mine will be `Icons_PaladinOfTheCosmicOrder.dds`

* **UUID** : Generate a new uuid for this. This uuid will also be used in your _merged file later so save enter your new uuid and save it for later. I generated 5099f782-7207-403e-8914-1c2efc836a06.

* **Height/Width (TextureAtlasTextureSize)** : As long as you downloaded Kaz's blank .dds file, it should be 2048x2048.

* **MapKey** : This is your reference to the icon. It should match the value you have for your entry in your data icon field in your Passive.txt (or whatever data file you have named your icon in. If you remember, I had min as `data "Icon" "scale_of_everything"` so i used scale_of_everything for my mapkey.

* **U1/V1/U2/V2** : Like I mentioned above, these are the edges of your icon in relation to the atlas. You could use math and figure out each one or if you followed what I said and did 64 x 64 icons and 2048 x 2048 atlas, you can copy and paste most peoples since your bounds should be the same.

* We only are adding one icon here, but I have two entries for IconUV. I can leave that alone for now without any issues. Id rather it be there for future use then now.

### _merged.lsx
If you have been modding other bg3 files you have probably seen a _merged file already. This one isn't as large thankfully. Here is an example of the file but with the changes for my mod.

PaladinOfTheCosmicOrder\Public\PaladinOfTheCosmicOrder\Content\UI\[PAK]_UI\_merged.lsx
```
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="4" revision="4" build="602" />
	<region id="TextureBank">
		<node id="TextureBank">
			<children>
				<node id="Resource">
					<attribute id="ID" type="FixedString" value="5099f782-7207-403e-8914-1c2efc836a06" />
					<attribute id="Localized" type="bool" value="False" />
					<attribute id="Name" type="LSString" value="PaladinOfTheCosmicOrder" />
					<attribute id="SRGB" type="bool" value="True" />
					<attribute id="SourceFile" type="LSString" value="Public/PaladinOfTheCosmicOrder/Assets/Textures/Icons/Icons_PaladinOfTheCosmicOrder.dds" />
					<attribute id="Streaming" type="bool" value="True" />
					<attribute id="Template" type="FixedString" value="Icons_Items" />
					<attribute id="Type" type="int32" value="0" />
					<attribute id="_OriginalFileVersion_" type="int64" value="144115188075855873" />
				</node>
			</children>
		</node>
	</region>
</save>
```
You will keep a few of these attributes the same but let's go over what I changed.

* **ID** : Rememeber that uuid I mentioned to save from the atlas map? We will place that here for id. 

* **Name** : Change this to the name of your mod.

* **SourceFile** : This will be the path to your dds atlas. It should start from Public. Mentioning that because in our atlas map when we described out atlas path we started from Assets.


and just like that, we can now see out icon in CC and ingame locations that arent the tooltip!
![image](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/94bc918f-b237-4de8-b6f9-baa940015c6d)

![image](https://github.com/ghostboats/bg3_modders_guide/assets/106226990/6de99891-f0de-4193-80f2-026ce802c983)



*I've simplified the atlas creation process in my vs code extension which really helps make the icon process at bit easier. If you download it [here](https://www.nexusmods.com/baldursgate3/mods/6574/) from nexus or searching it in views->extensions->bg3, you will be able to convert pngs to dds and vice versa, resize pngs/dds images to correct sizes required for the game, as well as autogenerate your atlas with your icons on them and its corresponding atlas map for it.
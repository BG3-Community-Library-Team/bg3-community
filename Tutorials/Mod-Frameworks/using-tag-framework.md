---
title: Tag Framework Usage
description: A Guide on making use of Tag Framework
published: true
date: 2024-04-25T22:51:03.317Z
tags: se, script-extender, frameworks, tags
editor: markdown
dateCreated: 2024-04-25T22:49:40.411Z
---

# Header
The Tag Framework(TF) is an API designed to allow mods to leverage some of the behind-the-scenes tag functionality, primarilly aimed at Race (REALLY) tags, Meta Race tags, and Exclusion Tags. Certain tags are forced onto new characters - particularly Baldurian and Illithid. When creating an Outlander character, or, as an example, a character of a custom race that would clearly never have been considered Baldurian, this becomes less than ideal. REALLY tags also don't apply for custom races, as they're set in the Osiris code. Tag Framework allows Mod Authors to register their tags with a JSON configuration file in order to mimic what Larian does behind-the-scenes for vanilla races.

In short, TF makes it possible for Mod Authors to easily register custom Race REALLY tags to their racial tag, as well as manage Tag Exclusion rules and Meta Tags.

## Mod Set-Up
First thing's first, we need to set up our mod. Chances are, by the time you're looking Tag Framework, you have your mod set-up already, but you'll want to ensure you have these files:
1. Relevant REALLY tags.
2. Any desired custom Meta tags

Both of these would live under `Public/ModName/Tags/uuid.lsx` (replacing `uuid` with the UUID value for the tag), and would look like a regular tag. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="0" build="58" lslib_meta="v1,bswap_guids" />
	<region id="Tags">
		<node id="Tags">
			<attribute id="Description" type="LSString" value="|Drow Half-Elf, shapeshifted or not|" />
			<attribute id="DisplayDescription" type="TranslatedString" handle="hcb0e4a17g6ed5g48begb610g4e7d3af1ad82" version="1" />
			<attribute id="DisplayName" type="TranslatedString" handle="h7fd943bbge764g47b2gb6c5g2ad3bd9c44d2" version="2" />
			<attribute id="Icon" type="FixedString" value="" />
			<attribute id="Name" type="FixedString" value="REALLY_DROWHALFELF" />
			<attribute id="UUID" type="guid" value="3dbe23e0-2c9f-4a81-b586-ec6e50f720e1" />
			<children>
				<node id="Categories">
					<children>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Code" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Dialog" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Race" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="PlayerRace" />
						</node>
					</children>
				</node>
			</children>
		</node>
	</region>
</save>
```

## Configuration
Whether you're adding new Races, or new exclusion tags or meta tags for existing races, you'll need to supply a `TagFrameworkConfig.json` file. This file is what allows Tag Framework to register these tags into the game. A [Sample Config](https://github.com/BG3-Community-Library-Team/TagFramework/blob/main/TagFrameworkConfig.sample.json) is provided in the repo.

Your file will look something like this:
In `Mods/ModName/ScriptExtender/TagFrameworkConfig.json`:
```json
{
  "FileVersion": 1,
  "Tags": [
    {
      "modGuids": ["(optional) UUID-of-required-mod"]
      "Type": "Race, Background, or Deity",
      "Tag": "TAG_NAME_tag-uuid-value",
      "ReallyTag": "TAG_NAME_tag-uuid-value",
      "TagsToExclude": ["reference to undesired tag"],
      "RaceMetaTags": ["reference to desired meta tags"],
      "DeityCleric": "Cleric Deity tag",
      "DeityPaladin": "Paladin Deity tag",
      "DeityAlignment": "Good, Evil or Neutral"
    }
  ]
}
```
Example:
```json
{
  "FileVersion": 1,
  "Tags": [
    {
      "modGuids": ["bfc31d95-8fd5-4bdc-a92b-ec3bfce13f86"],
      "Type": "Race",
      "Tag": "Ghouls_Dunmer_f34cadf5-ccfb-4e56-9596-356619569108",
      "ReallyTag": "REALLY_Ghouls_Dunmer_6a018dee-2f04-4bda-93c4-958422c3ed0a",
      "TagsToExclude": ["Baldurian"],
      "RaceMetaTags": ["Planar"]
    },
    {
      "Type": "Deity",
      "Tag": "Tyr",
      "DeityCleric": "TyrCleric",
      "DeityPaladin": "PALADIN_TYR_b8aec881-85fe-4e6e-8a28-7052ecd88899",
      "DeityAlignment": "Good"
    }
  ]
}
```

The values of TagsToExclude and RaceMetaTags can be set up as either the UUIDs of the relevant tags, or in a format like `TAG_NAME_tag-uuid` as seen in the Tag and ReallyTag fields, or in simple text. A list of the supported simple text options can be found in our [Tag Dictionary](https://github.com/BG3-Community-Library-Team/TagFramework/wiki/Tag-Dictionary)
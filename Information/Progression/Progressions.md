---
title: Progressions
description: Progression nodes for races and classes
published: true
date: 2025-08-09T14:47:04.076Z
tags: classes, subclasses, races
editor: markdown
dateCreated: 2025-08-09T14:47:04.076Z
---

# Header
Progression tables are used to assign various resources to a race, subrace, class, or subclass. These can be things like Action Resources, spells, passives, and more.

Each Progression table has 2 UUIDs associated with it:

* <code>UUID</code>
	* This is the unique identifier for this single Progression table, known as a <code>node</code>.
  * If you reference this UUID, you are referencing *only* this node.
  * Each node has its own UUID, different from every other node.
* <code>TableUUID</code>
	* This is the unique identifier that associates all individual Progression nodes together.
  * The TableUUID is the same in every Progression node because it is tied directly into the parent race/subrace or class/subclass.

### Example Progression Table
```
<node id="Progression">
	<attribute id="Boosts" type="LSString" value="ProficiencyBonus(SavingThrow,Wisdom);ProficiencyBonus(SavingThrow,Charisma);Proficiency(LightArmor);Proficiency(MediumArmor);Proficiency(HeavyArmor);Proficiency(Shields);Proficiency(SimpleWeapons);Proficiency(MartialWeapons);ActionResource(LayOnHandsCharge,3,0);ActionResource(ChannelOath,1,0)" />
	<attribute id="Level" type="uint8" value="1" />
	<attribute id="Name" type="LSString" value="Paladin" />
	<attribute id="ProgressionType" type="uint8" value="0" />
	<attribute id="Selectors" type="LSString" value="SelectSkills(627af380-2bbb-4a9f-9571-5ec781a6daf4,2);AddSpells(fb407d81-3a05-46f1-9153-0fb27dce95b6,,,,AlwaysPrepared);SelectAbilityBonus(b9149c8e-52c8-46e5-9cb6-fc39301c05fe,AbilityBonus,2,1)" />
	<attribute id="TableUUID" type="guid" value="ba2afe85-acba-4ea1-a238-2b4543f47821" />
	<attribute id="UUID" type="guid" value="b60618d1-c262-42b5-9fdd-2c0f7aa5e5af" />
	<children>
		<node id="SubClasses">
			<children>
				<node id="SubClass">
					<attribute id="Object" type="guid" value="b36d247e-d39f-4ae9-9476-3ec315c55789" />
				</node>
				<node id="SubClass">
					<attribute id="Object" type="guid" value="1c761ad0-6f5f-409e-ac1d-ddf6f85c1fc4" />
				</node>
				<node id="SubClass">
					<attribute id="Object" type="guid" value="3cc3d397-c47d-4966-87ae-88827f73f645" />
				</node>
			</children>
		</node>
	</children>
</node>
<node id="Progression">
	<attribute id="AllowImprovement" type="bool" value="True" />
	<attribute id="Boosts" type="LSString" value="ActionResource(LayOnHandsCharge,1,0)" />
	<attribute id="Level" type="uint8" value="4" />
	<attribute id="Name" type="LSString" value="Paladin" />
	<attribute id="ProgressionType" type="uint8" value="0" />
	<attribute id="TableUUID" type="guid" value="ba2afe85-acba-4ea1-a238-2b4543f47821" />
	<attribute id="UUID" type="guid" value="4f2c7b4e-2f91-4105-a136-9387a8cfed4f" />
</node>

```

The UUID <code>b60618d1-c262-42b5-9fdd-2c0f7aa5e5af</code> is exclusively used to reference the non-multiclass Level 1 Paladin Progression node. UUID <code>4f2c7b4e-2f91-4105-a136-9387a8cfed4f</code>, on the otherhand, references the Level 4 Paladin node.

The TableUUID <code>ba2afe85-acba-4ea1-a238-2b4543f47821</code> references **EVERY** base class Paladin Progression node. It is used in the Multiclass Level 1 node, Level 4 node, Level 12 node, etc.
---
title: Item Level Positioning
description: This is a data reference for Levels\Level_Name\Items and positioning of said items
published: true
date: 2024-05-11T07:49:30.858Z
tags: items, add items, data, levels, positioning, rotation, quaternion
editor: markdown
dateCreated: 2024-05-11T07:42:34.585Z
---

## Item Data File

Example of the `_merged.lsf.lsx` data file that would be in the level directory
```xml
<!-- MySweetMod\Mods\MySweetMod\Levels\WLD_Main_A\Items\_merged.lsf.lsx -->

<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="9" build="0" lslib_meta="v1,bswap_guids" />
	<region id="Templates">
		<node id="Templates">
			<children>
				<node id="GameObjects">
					<attribute id="Flag" type="int32" value="1" />
					<attribute id="LevelName" type="FixedString" value="WLD_Main_A" /> // Matches the parent directory
					<attribute id="MapKey" type="FixedString" value="47f37c11-098b-48ee-a908-61cab8a64d69" /> // Generate a UUID for this
					<attribute id="Name" type="LSString" value="WLD_Main_Camp_Box_A" /> // Add a name for the created object
					<attribute id="TemplateName" type="FixedString" value="3a6bf1fb-2785-406a-85d4-6bd247714591" /> // This is the MapKey of the object you are copying
					<attribute id="Type" type="FixedString" value="item" />
					<attribute id="_OriginalFileVersion_" type="int64" value="144537400540922158" />
					<children>
						<node id="LayerList">
							<children>
								<node id="Layers">
									<children>
										<node id="Object">
											<attribute id="MapKey" type="FixedString" value="WLD_Main_A" /> // Same as LevelName
										</node>
									</children>
								</node>
							</children>
						</node>
						<node id="Transform">
							<attribute id="Position" type="fvec3" value="-661.3397 0.5986 -199.6469" /> // X Y Z coords, no commas, single spaces
							<attribute id="RotationQuat" type="fvec4" value="0 0.7071068 0 0.7071068" /> // See conversion instructions below
							<attribute id="Scale" type="float" value="1" /> // Scale the item larger or smaller with this too
						</node>
					</children>
				</node>
			</children>
		</node>
	</region>
</save>
```

LevelName: This is the Region (`_P(Osi.GetRegion(GetHostCharacter()))`)
MapKey: UUID for the created object
Name: Name for the created object
TemplateName: MapKey of the item you are copying from
Position: X Y Z coordinates where the item is getting inserted. Can use (`_P(Osi.GetPosition(GetHostCharacter()))`) to get POS info
RotationQuat: Math Stuff (see below)
Scale: 1 = 100%, 0.5 = 50% (half as big as original), 2.0 = 200% (twice as big as original) etc.


## Converting Rotation to RotationQuat
The RotationQuat (Quaternions) attribute, needs to have a quaternion instead of a rotation angle. Unfortunately, there isn't a command in game to give you that, so you have to convert it externally.

You could use a site like [this](https://www.andre-gaschler.com/rotationconverter/), which allows you to enter degrees along the Y axis on the left and outputs it to quat on the right.

![quat.png](/tutorials/item-positioning/quat.png)

> Be sure to change the input on the left to degrees
{.is-warning}


Here are some pre-converted angles for convenience.
```c
0: "0 0 0 1"
30: "0 0.258819 0 0.9659258"
60: "0 0.5 0 0.8660254"
90: "0 0.7071068 0 0.7071068"
120: "0 0.8660254 0 0.5"
150: "0 0.9659258 0 0.258819"
180: "0 1 0 0"
210: "0 0.9659258 0 -0.258819"
240: "0 0.8660254 0 -0.5"
270: "0 0.7071068 0 -0.7071068"
300: "0 0.5 0 -0.8660254"
330: "0 0.258819 0 -0.9659258"
```

For example, 90 degrees converts out to `0 0.7071068 0 0.7071068`. so if the rotation is 90 degrees then the value we would enter for **RotationQuat** would be: `0 0.7071068 0 0.7071068`
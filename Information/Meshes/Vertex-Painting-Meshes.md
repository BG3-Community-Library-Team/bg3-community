---
title: Vertex Painting Meshes
description: 
published: true
date: 2025-10-28T12:36:43.704Z
tags: meshes
editor: markdown
dateCreated: 2024-04-28T17:39:51.157Z
---

# Vertex Paint Colors
| MapKey | Hex | Blender Hex|
|----------|----------|----------|
|"ModestyLeaf"|#000500|#010501|
|"Sleeves"|#000A00|#010A01|
|"knees"|#000F00|#010F01|
|"Pants"|#001400|#011401|
|"Dragonborn Attachments"|#001900|#011901|
|"Shoulders"|#001E00|#011E01|
|"shins"|#002400|#012401|
|"Private_Parts"|#002800|#012801|
|"Nipple Covers"|#002D00|#012D01|
|"Torso"|#003200|#013201|
|"wrists"|#003A00|#013A01|
|"upperarm"|#004100|#014101|
|"lowerarm"|#005000|#015001|
|"hands"|#005F00|#015F01|
|"decolletage_01"|#006E00|#016E01|
|"decolletage_02"|#008200|#018201|
|"feet"|#009600|#019601|
|"Underwear_Bra"|#00A000|#01A001|
|"Underwear_Panties"|#00AA00|#01AA01|
|"Thighs"|#00B900|#01B901|
|"Underwear_Panties_Tail"|#00C300|#01C301|

> 
>Blender gamma corrects the values by setting the values of the R and B components to 01. You can use either hex value in the table as only the green channel is used by the vertcut shaders. Red and Blue affect cloth physics.
{.is-info}

# Vertex Paint Transfer

You'll need an object with colors, and the object without colors that you want to transfer to.

You'll need to select your color mesh first and then the non color mesh, then press F3 and search Transfer Mesh Data.
Then select face corner colors.
You should now see a new color attribute on the non color mesh with the vertex colors.
Then there should be two entries in Color Attributes, the old one with nothing (delete it), and the new one.

![transfervertcol.gif](/information/meshes/transfervertcol.gif)

> 
> If the two meshes you are transferring between are significantly different, you will probably need to clean up the vertex paint manually, as any blurred edges will end up sticking to the ground in game.
{.is-info}

# Manually Applying Vertex Paint (Or Cleaning It Up)

First, enter edit mode, enable X-Ray mode, and select all of the faces you wish to apply vertex paint to.

![vertexpaintingmeshes_editmode.png](/information/meshes/vertex-painting-meshes/vertexpaintingmeshes_editmode.png)

Then switch to vertex paint mode. After selecting your color, enable Paint Mask on the top left, and then open the Paint menu and hit Set Vertex Colors.

![vertexpaintingmeshes_vertexpaint.png](/information/meshes/vertex-painting-meshes/vertexpaintingmeshes_vertexpaint.png)

The faces you selected will now be colored cleanly. You can turn on Flat shading to see it more clearly.

![vertexpaintingmeshes_endresult.png](/information/meshes/vertex-painting-meshes/vertexpaintingmeshes_endresult.png)

# Troubleshooting

If your vertex paint still doesn't work in game...

- Make sure you are using a VertCut compatible shader. Usually, compatible shaders will have `VertCut` in the name.
- Make sure the `SupportsVertexColorMask` line in your VisualBank mesh definition is set to `True`.
- Make sure you copied the correct hex code from this article and then flood-filled it in Blender. Color picking from other painted meshes doesn't seem to work.
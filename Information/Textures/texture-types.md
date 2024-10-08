---
title: Bg3 Engine Texture Variants
description: An explanation of the various styles of texture Bg3 uses and where it uses them
published: true
date: 2024-08-10T15:07:59.067Z
tags: textures
editor: markdown
dateCreated: 2024-05-03T01:28:21.117Z
---

# Important to note:

The engine Baldur's Gate 3 uses various texture 'formats' while utilizing a wide range of 'compression types'. This can be confusing because there are lots of moving parts and nowhere is it explained *how* exactly the game handles these texture 'formats' and 'compression types'.

First and foremost it is important to disclose the difference between 'format' and the *actual* file type that the textures are saved as - *all* textures outside of **Virtual Textures** are various types of .DDS (DirectDrawSurface) files. When we say format, we mean exclusively to refer to how the game *engine* interprets the data stored in the .DDS file. This is usually denoted in the name of the file (EX: '_HMVY.DDS' or '_NM.DDS') however it is possible to determine by other methods. 

Secondly it is important to note that the types of compression are different (usually*) dependant on what the texture is being used for. ([Insert link to Compression writeup here :)](/Information/Textures/compression))
<sup>*I say 'usually' as many textures share the same compression type but this is not guaranteed</sup>

## Texture Formats:

Bg3 has ultimately two 'styles' of rendering - 'Skin' and 'Hardsurface' for lack of better wording

The formats are as follows:

---

## Skin
 <table>
  <tr>
    <th>Map Syntax</th>
    <th>Red Channel</th>
    <th>Green Channel</th>
    <th>Blue Channel</th>
    <th>Alpha Channel</th>
    <th>DDS Compression</th>
  </tr>
  <tr>
    <td>CLEA</td>
    <td>Cavity Map</td>
    <td>Hair</td>
    <td>Makeup(lipstick)</td>
    <td>Ambient Occlusion</td>
    <td>BC3/DXT5 Linear</td>
  </tr>
  <tr>
    <td>HMVY</td>
    <td>Hemoglobin</td>
    <td>Melanin</td>
    <td>Vein</td>
    <td>Yellowing</td>
    <td>BC3/DXT5 Linear</td>
  </tr>
    <tr>
    <td>NM</td>
    <td>Not used</td>
    <td>Y Axis Normals</td>
    <td>Z Axis Normals</td>
    <td>X Axis Normals</td>
    <td>BC3/DXT5 Linear</td>
  </tr>
    <tr>
    <td>MSK</td>
    <td>Non-Skin</td>
    <td>Melanin Removal</td>
    <td>Mucous Map</td>
    <td>Not Used</td>
    <td>BC1/DXT1 Linear</td>
  </tr>
</table> 



---



## Dgb
- For Dragonborn Skin


	1. CLEA

	*~Format:~* *~BC3/DXT5~ ~Linear~*
	C - Curvature/Cavity map - RED channel
  L - Lips  - GRN channel
	E - Eyebrows - BLU channel
  A - Ambient occlusion - ALPHA channel
  
	2. NM

	*~Format:~* *~BC3/DXT5~ ~Linear~*
	RED channel - UNUSED BY BG3 ENGINE STORED IN ALPHA
  GRN channel - Y Axis Normals
  BLU channel - Z Axis Normals
  ALPHA channel - X Axis Normals
  
	3. HMVY

	*~Format:~* *~BC3/DXT5~ ~Linear~*
	H - Hemoglobin - RED channel
  M - Melanin - GRN channel
  V - Veins - BLU channel
  Y - Yellowing - ALPHA channel

	4. MSK (DMSK)
   
	5. MSK (AccentMSK)
    
      
---
## Objects
- For Hard Surface Objects

	1. BM (Either full color *or* B/W)

	*~Format:~* *~BC3/DXT5~ ~Linear~?*
	RED channel - Intensity of Red
  GRN channel - Intensity of Green
  BLU channel - Intensity of Blue
  ALPHA channel - EMPTY

	2. NM

	*~Format:~* *~BC3/DXT5~ ~Linear~?*
	RED channel - UNUSED BY BG3 ENGINE STORED IN ALPHA
  GRN channel - Y Axis Normals
  BLU channel - Z Axis Normals
  ALPHA channel - X Axis Normals

	3. PM

	*~Format:~* *~BC3/DXT5~ ~Linear~?*
	RED channel - Metallic Intensity
  GRN channel - Roughness Amount
  BLU channel - Ambient Occlusion (Baked in shadows)


	4. MSK (MSKColor/MSKcloth)

	*~Format:~* *~BC3/DXT5~ ~Linear~?*
	Channel makeup is largely irrelevant, Colored mask for segments of different material colors

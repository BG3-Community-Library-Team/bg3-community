---
title: Bg3 Engine Texture Variants
description: An explanation of the various styles of texture Bg3 uses and where it uses them
published: true
date: 2025-11-25T14:51:23.413Z
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



## DGB 
- For Dragonborn Skin


	1. **CTLO** (Called CLEA in Shader, CLEA texture itself for Dragonborn is rudiment and not used for anything!)

	*~Format:~* *~BC3/DXT5~ ~Linear~*
	C - Cavity map - RED channel
  T - Thickness  - GRN channel
	L - Lips - BLU channel
  O - Ambient occlusion - ALPHA channel
  **Note:**
  Thickness - it's inverted compared to one from Marmoset and much lighter
  AO - it's much whiter then one you will bake in Marmoset or Substance, so adjust them if you want to mix with yours
  
	2. **NM**

	*~Format:~* *~BC3/DXT5~ ~Linear~*
	RED channel - UNUSED BY BG3 ENGINE STORED IN ALPHA
  GRN channel - Y Axis Normals
  BLU channel - Z Axis Normals
  ALPHA channel - X Axis Normals
  **Note:**
  To convert a "regular" tangent DX normal map to BG3, put the Red channel into Alpha channel and set Red channel to black
  
	3. **HMVY**

	*~Format:~* *~BC3/DXT5~ ~Linear~*
	H - Hemoglobin - RED channel
  M - Melanin (pigment amount) - GRN channel
  V - Veins - BLU channel
  Y - Yellowing - ALPHA channel
  ![1200px-dgb_hmvy1.png](/engine_texture_variants/1200px-dgb_hmvy1.png)

	4. **MSK** (Called Cancel MSK in Shader)
  
	*~Format:~* *~BC3/DXT5~ ~Linear~*
  RED channel - Non-skin (horns, scales, any keratin parts is white, soft skin - black)
  GRN channel - Convexity map 
  BLU channel - Emty black for heads ( white used for nails in body textures)
  ALPHA channel - Not Exist
  ![1200px-dgb_msk_1.png](/engine_texture_variants/1200px-dgb_msk_1.png)
  ![1200px-dgb_msk_2.png](/engine_texture_variants/1200px-dgb_msk_2.png)
   
	5. **DMSK (Accent Mask)**
  
  *~Format:~* *~BC3/DXT5~ ~Linear~*
  RGB - every channel is decorative mask (trough them you make guilded mask, add details, aka accent masks)
  ![1200px-dgb_dmsk_rgb1.png](/engine_texture_variants/1200px-dgb_dmsk_rgb1.png)
  In the picture you could see DMSK blue channel as yellow guilding:
  ![1200px-dgb_dmsk_b_examle.png](/engine_texture_variants/1200px-dgb_dmsk_b_examle.png)
   
	5. **Draconic Bloodline DMSK (Accent Mask)**
  
  *~Format:~* *~BC3/DXT5~ ~Linear~*
  RGB - every channel is draconic bloodline decorative mask - they will replace DMSK if gamer choose the DB subclass, keep it in mind
  ![1200px-dgb_draconic_bloodline_dmsk1.png](/engine_texture_variants/1200px-dgb_draconic_bloodline_dmsk1.png)

	6. **Illithid MSK**
  
  *~Format:~* *~BC3/DXT5~ ~Linear~*
	RED channel - X Axis Normals
  GRN channel - Y Axis Normals
  BLU channel - Mask
  ALPHA channel - Not Exist
  **Note:**
  For head it is 1x1 ratio image, for body it is 1x2. If you have any UV parts out of 1x1 bot by 1, this parts will take info from 2nd part of texture
  ![illithid_msk.png](/engine_texture_variants/illithid_msk.png)
    
   [Here example](https://www.nexusmods.com/baldursgate3/mods/11111) how you could use DGB textures in Substance Painter with [Volno's Substance Skin Shader](https://www.nexusmods.com/baldursgate3/mods/9045)Volno's Substance Skin Shader
    
    
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

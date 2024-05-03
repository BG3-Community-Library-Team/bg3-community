---
title: Bg3 Engine Texture Variants
description: An explanation of the various styles of texture Bg3 uses and where it uses them
published: true
date: 2024-05-03T01:47:42.830Z
tags: textures
editor: markdown
dateCreated: 2024-05-03T01:28:21.117Z
---

# Important to note:

The engine Baldur's Gate 3 runs on uses various texture 'formats' while utilizing a wide range of 'compression types'. This can be confusing because there are lots of moving parts and nowhere is it explained *how* exactly the game handles these texture 'formats' and 'compression types'.

First and foremost it is important to disclose the difference between 'format' and the *actual* file type that the textures are saved as - *all* textures outside of **Virtual Textures** are various types of .DDS (DirectDrawSurface) files. When we say format, we mean exclusively to refer to how the game *engine* interprets the data stored in the .DDS file. This is usually denoted in the name of the file (EX: '_HMVY.DDS' or '_NM.DDS') however it is possible to determine by other methods. 

Secondly it is important to note that the types of compression are different (usually*) dependant on what the texture is being used for. (Insert link to Compression writeup here :) )


## Texture Formats:

Bg3 has ultimately two 'styles' of rendering - 'Skin' and 'Hardsurface' for lack of better wording

The formats are as follows:

---

- For Non-Dragonborn Skin

	1. CLEA 

	*~BC3/DXT5~ ~Linear~*
	C - Curvature/Cavity map - RED channel
  L - Lips  - GRN channel
	E - Eyebrows - BLU channel
  A - Ambient occlusion - ALPHA channel

	2. NM 

	*~BC3/DXT5~ ~Linear~*
	RED channel - UNUSED BY BG3 ENGINE STORED IN ALPHA
  GRN channel - Y Axis Normals
  BLU channel - Z Axis Normals
  ALPHA channel - X Axis Normals

	3. HMVY

	*~BC1/DXT1~ ~Linear~*
	H - Hemoglobin - RED channel
  M - Melanin - GRN channel
  V - Veins - BLU channel
  Y - Yellowing - ALPHA channel

	4. MSK (CancelMSK)

	*~BC1/DXT1~ ~Linear~*
	RED channel - Non-Skin amount (Nails/Horns usually)
  GRN channel - Skin melanin intensity
  BLU channel - Mucous (Lips/tear lines)


---




- For Dragonborn Skin


	1. CLEA

	*~BC3/DXT5~ ~Linear~*
	C - Curvature/Cavity map - RED channel
  L - Lips  - GRN channel
	E - Eyebrows - BLU channel
  A - Ambient occlusion - ALPHA channel
  
	2. NM

	*~BC3/DXT5~ ~Linear~*
	RED channel - UNUSED BY BG3 ENGINE STORED IN ALPHA
  GRN channel - Y Axis Normals
  BLU channel - Z Axis Normals
  ALPHA channel - X Axis Normals
  
	3. HMVY

	*~BC3/DXT5~ ~Linear~*
	H - Hemoglobin - RED channel
  M - Melanin - GRN channel
  V - Veins - BLU channel
  Y - Yellowing - ALPHA channel

	4. MSK (DMSK)
   
	5. MSK (AccentMSK)
    
      
---

- For Hard Surface Objects

	1. BM (Either full color *or* B/W)

	~BC3/DXT5~ ~Linear~?
	RED channel - Intensity of Red
  GRN channel - Intensity of Green
  BLU channel - Intensity of Blue
  ALPHA channel - EMPTY

	2. NM

	~BC3/DXT5~ ~Linear~?
	RED channel - UNUSED BY BG3 ENGINE STORED IN ALPHA
  GRN channel - Y Axis Normals
  BLU channel - Z Axis Normals
  ALPHA channel - X Axis Normals

	3. PM

	~BC3/DXT5~ ~Linear~?
	RED channel - Metallic Intensity
  GRN channel - Roughness Amount
  BLU channel - Ambient Occlusion (Baked in shadows)


	4. MSK (MSKColor/MSKcloth)

	~BC3/DXT5~ ~Linear~?
	Channel makeup is largely irrelevant, Colored mask for segments of different material colors

---
title: Creating Makeup and Face / Body tattoos
description: Guide to create tattoo/makeup textures and get them in game
published: true
date: 2025-05-22T15:38:42.627Z
tags: tattoo, makeup, texture painting, kavt
editor: markdown
dateCreated: 2025-05-22T15:00:51.844Z
---

# Creating Tattoos
This guide will primarily cover creating face tattoos using Blender (to paint) and Photoshop (to compile into an atlas). 

Alternatively, Substance Painter can be used instead of Blender, as can GIMP/Paint.net/etc. for atlas work.


## The Basics
The tattoos and makeup are all located respectively on a single atlas file, utilizing a grid and channels to determine number and order of the individual options.

- These are each a 4x4 grid with a resolution of: 4096x4096, meaning each individual option is 1024x1024
 - It is possible to use upscaled atlases with a resolution of 8192x8192, with individual options being 2048x2048 (recommended as you have more to work with)
- Kazstra Virtual Tav (KAVT) has extended this further, utilizing a tattoo atlas size of 8192x16384 and a makeup atlas of 4096x8192 - both doubling the ammount of options you can have in CC
- The tattoo atlases in all cases are set up by editing each RGB channel independently (either by decomposing in GIMP, or directly editing channels in PS)
- The makeup atlases are edited in the same way, but only have the red channel to work with. Green is used by the game for gith spots

They look like this:
![vanilla-atlases-preview.png](/tutorials/tattoos_makeup/vanilla-atlases-preview.png)

### The vanilla files can be found here:
`..\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\Characters\_Models\_SharedAssets\SHARED_Atlas\Resources`
- Tattoos `Skin_Atlas_Head_SHR_Tattoo_A_MSK1.DDS`
- Makeup `Skin_Atlas_Head_SHR_Makeup_A_MSK2.DDS`

### If using Unique Tav or Kazstra Virtual Tav, they will be located here:
`E:\Games\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\FACE`
- Tattoos UT `Skin_Atlas_Head_SHR_Tattoo_A_MSK.DDS`
- Tattoos KAVT `KVT_Head_Atlas_Tattoo.DDS`
- Makeup UT `Skin_Atlas_Head_SHR_Makeup_A_MSK.DDS`
- Makeup KAVT `KVT_Head_Atlas_Makeup.DDS`

## Creating a tattoo in Blender

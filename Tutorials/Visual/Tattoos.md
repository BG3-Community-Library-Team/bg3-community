---
title: Creating Makeup and Face / Body tattoos
description: Guide to create tattoo/makeup textures and get them in game
published: true
date: 2025-05-22T16:30:30.839Z
tags: tattoo, makeup, texture painting, kavt
editor: markdown
dateCreated: 2025-05-22T15:00:51.844Z
---

# Creating Tattoos and Makeup
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
`..\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\FACE`
- Tattoos UT `Skin_Atlas_Head_SHR_Tattoo_A_MSK.DDS`
- Tattoos KAVT `KVT_Head_Atlas_Tattoo.DDS`
- Makeup UT `Skin_Atlas_Head_SHR_Makeup_A_MSK.DDS`
- Makeup KAVT `KVT_Head_Atlas_Makeup.DDS`

### Body tattoos are effectively only usable for the player character if using mods like UT or KAVT
Location for UT and KAVT is 
`..\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\BODY\TATTOO`
- as `Skin_Atlas_Body_UNI_Tattoo_A_MSK.DDS`

> This tutorial focuses on simply creating face tattoos (or makeup) and then putting them on a vanilla atlas. For specifics regarding KAVT it is recommended to check out the articles and resources found [here on the Nexus page](https://www.nexusmods.com/baldursgate3/mods/16325?tab=articles)
{.is-info}


## Creating a tattoo in Blender

> There is a Youtube video (silent with captions) going over this part for those who prefer it:
> https://youtu.be/sHszyXyko0Q
{.is-success}

While we can directly paint onto a head model without textures, it is recommended to use [Volno's Texture Toolbox](https://www.nexusmods.com/baldursgate3/mods/4310). For this purposes the setup is easy as the blend file already contains a vanilla head hooked up to the shaders, we can use this.

### Initial setup of meshes

First, hide everything aside from the head meshes and lights. Now we want to join the ears to the head mesh - this will allow us to paint over both as one mesh.

To do that, rename the UV maps of the ears mesh so they are identical to those of the head mesh. The UV maps of the ears should look like this:

![joinears.png](/tutorials/tattoos_makeup/joinears.png)

Now select the ears, then head and Ctrl+J to merge them.

### Setup of shaders

Head over to the Shading tab, select the head and zoom in to find the tattoos/makeup nodes, expand the Tattoo Atlas part. If we wish we can change the colour which shows in Blender (in this case we're just using Tattoo A so will set it to black and with a strength of 1 - fully visible):

![findtattoonodes.png](/tutorials/tattoos_makeup/findtattoonodes.png)

Now, create a new image texture by clicking anywhere outside of the nodes, right click -> Add -> Texture -> Image Texture

![newimage1.png](/tutorials/tattoos_makeup/newimage1.png)

Rename it (this will be the name of our tattoo png which we will later place on our atlas), and resize to 2048 if using the upscaled atlases:

![hookup.png](/tutorials/tattoos_makeup/hookup.png)

Now hook the two up:

![newimage2.png](/tutorials/tattoos_makeup/newimage2.png)

### Setup of Texture Paint workspace



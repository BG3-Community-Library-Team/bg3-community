---
title: A Guide to UV Mapping
description: Everything you need to know about UV mapping
published: false
date: 2026-03-22T18:00:09.650Z
tags: uv, uv mapping, uvs, udim
editor: markdown
dateCreated: 2026-03-22T15:21:46.094Z
---

# A Guide to UV Mapping
## Overview
To texture a 3D model, it requires a UV map. A UV map is the 2D texture coordinates for a 3D mesh. In other words, the UV map determines how the 2D textures will be placed on the mesh. UV mapping is the process of creating the 2D map of the mesh. 

The individual pieces that make up the UV map are called *shells* or *islands*. Shells are packed/arranged into a *tile*, most often in the 0-1 space. 

### What is the 0-1 space?
As mentioned above, UVs are texture *coordinates* and behave like coordinates on a Cartesian plane except they use U and V instead of X and Y. This is better shown in Maya than Blender as you can actually see the scale of the axes. 

![tilespacemaya.png](/tutorials/visual/uv-mapping/tilespacemaya.png) 

Blender only clearly displays one tile. This tile is the 0-1 tile. The U and V axes and the origin point are annotated in the image.

![blendertile.png](/tutorials/visual/uv-mapping/blendertile.png)

The 0-1 space would equate to quadrant 1 in the Cartesian system. In most cases this is where you want your UVs to be packed. If you are a beginner, you can safely assume that this is *always* where you want your UVs to be packed. 

![tilespacemaya_cartesian.png](/tutorials/visual/uv-mapping/tilespacemaya_cartesian.png)

The image below shows an unwrapped mesh with its shells filling the 0-1 tile space. Notice that the shells do not overlap nor do they extend beyond the boundaries of 0-1. 

![01_space.png](/tutorials/visual/uv-mapping/01_space.png)

### What is a UDIM?
>UDIMs are **not supported** in BG3.[^1]
{.is-warning}

[^1]: There is **one** shader in the game that by name appears to use UDIMs:  CHAR_AlphaBlend_GM_Udim_Flowmap. This shader does not behave the way a shader that truly supports UDIMs would. True UDIM workflow is unsupported in BG3.

A UDIM, short for U-Dimension, is a way of UV mapping that allows you to place shells across multiple tiles and create separate textures for each tile. This setup is more commonly used for meshes created for use in 3D animations than in games. 

Since UDIMs are not supported in BG3, I will not go into detail explaining them.

When importing game meshes, you may come across UVs outside of the 0-1 tile space. Shown below is the UV arrangement of the TIF_F_NKD_Tail_A mesh when imported into Blender. Note that in the example below that the shells are identical, both in shape and in position within their respective tiles. If the shell outside of the 0-1 tile is selected and moved to the left by one unit (done by selecting the shell and pressing `G → X → -1` on the keyboard), you can see that it stacks perfectly on top of the shell already in the tile. This is **not** a UDIM. This is done to optimize baking results. See the section on Baking below.

![movedshells.png](/tutorials/visual/uv-mapping/movedshells.png) ![identicalshells.png](/tutorials/visual/uv-mapping/identicalshells.png)


### Why it matters
Is CMTY member baeator sending messages to you that look like this?[^2] Do you wonder why she bothers to point it out? Why isn't a moderator stepping in to handle this bullying? 

[^2]: I, the author of this page, am baeator. I can call myself out.

![baeatorcomment.png](/tutorials/visual/uv-mapping/baeatorcomment.png)

Good UVs, both in regards to shape and arrangement, will make things easier when texturing. There's many reasons for this so I'll list a handful:
- Less artifacts on your bakes
- Better results when using materials/masks that are procedural based on UVs
- Consistent texel density
- Better results when using UV projection projection type
- Easier to line up patterns across multiple shells
- Avoid patterns looking stretched or warped in areas
- etc... just trust me, bro.

![plsbrouvs.jpg](/tutorials/visual/uv-mapping/plsbrouvs.jpg)

### Checkerboard Visualizer
To better illustrate my point above of why good UVs matter, allow me to introduce you to using a checkerboard material. 

Why the checkerboard is great:
- Shows texel density
- Shows flow/stretching

## Unwrapping Methods
### Seams

## Packing Islands
### Optimal Arrangements
### To stack or not to stack?

## Textures and Baking
Your content here

## Merging Meshes
---
title: A Guide to UV Mapping
description: Everything you need to know about UV mapping
published: false
date: 2026-03-22T16:33:47.282Z
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

Blender only clearly displays one tile. This tile is the 0-1 tile.

![blendertile.png](/tutorials/visual/uv-mapping/blendertile.png)

The 0-1 space would equate to quadrant 1 in the Cartesian system. In most cases this is where you want your UVs to be packed. If you are a beginner, you can safely assume that this is *always* where you want your UVs to be packed. 

![tilespacemaya_cartesian.png](/tutorials/visual/uv-mapping/tilespacemaya_cartesian.png)

The image below shows an unwrapped mesh with its shells filling the 0-1 tile space. Notice that the shells do not overlap nor do they extend beyond the boundaries of 0-1. 

![01_space.png](/tutorials/visual/uv-mapping/01_space.png)

### What is a UDIM
When importing game meshes, you may come across UVs outside of the 0-1 tile space. Note that in the example below that the shells are identical, both in shape and in position within their respective tiles. This is **not** a UDIM. This is done to optimize baking results. See the section on Baking below.


### Why it matters
### Checkerboard Visualizer

## Unwrapping Methods
### Seams

## Packing Islands
### Optimal Arrangements
### To stack or not to stack?

## Baking
Your content here

## Merging Meshes
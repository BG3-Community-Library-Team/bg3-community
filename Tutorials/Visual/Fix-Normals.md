---
title: Fix Broken Normals on Imported Meshes
description: Short guide to fix meshes with borked normals (random invisible triangles)
published: true
date: 2025-02-09T21:21:34.952Z
tags: meshes, normals
editor: markdown
dateCreated: 2025-02-09T20:14:36.245Z
---

# Fixing Broken Normals on Imported Meshes
Are your meshes looking a bit cut-out like this after they've been through Blender?

![borkednormals-example.png](/tutorials/fix_normals_meshes/borkednormals-example.png)

That weirdness down there is somehow linked with importing meshes into Blender via the BG3 plugin and it's caused by the mesh normals getting a bit messed up. Luckily, it's usually easy to fix!

> **Quick Reference Guide for the speedy:**
> ‣ Visualize Normals with Overlays -> Face Orientation
> ‣ Select parts of meshes with borked normals using "L" in edit mode
> ‣ Mesh -> Normals -> Recalculate Outside (this should fix most of it)
> ‣ Mesh -> Normals -> Set From Faces (if the mesh is still looking strangely lumpy)
{.is-success}

For an explanation and walkthrough of the above, keep reading :)


## Visualizing Normals
The first thing to do is to go up to Overlays in the top right of the viewport and tick the box for Face Orientation, this will show you which parts of the mesh are "outside" and which are "inside" (marked by blue and red respectively). Generally speaking, everything which is blue will be visible, so to speak, and all which is red will not be.

For the robe example above, this is how the Face Orientation will look when imported (left), vs fixed (right):

![borkednormals-example2.png](/tutorials/fix_normals_meshes/borkednormals-example2.png)

All of those red faces outside on the left image are actually designated as "inside" faces and therefore invisible in game.

## Sharps
These should usually be along edges of a mesh you want more defined and they usually import strangely (including edges of faces that are not actually edges). Keeping them like this will often have a negative influence on how this fix will work so there are two options: 
- go through and remove the Sharps which aren't along the mesh edge and add them where they are missing
- simply select the affected areas of your mesh using "L", then remove them all 

Usually it's fine/not noticeable to just remove them so in the interest of brevity here we'll be doing that in the gif below:

![fixingnormals-clearsharps.gif](/tutorials/fix_normals_meshes/fixingnormals-clearsharps.gif)

## Recalculate Normals Outside
Selecting the parts of your mesh which need to be fixed (for example if it's a skirt with borked normals, select a vertex on it and press "L" to select the whole skirt).

Go up to Mesh -> Normals -> Recalculate Outside

![fixingnormals-recalcoutside.gif](/tutorials/fix_normals_meshes/fixingnormals-recalcoutside.gif)

and we see that pretty much fixes it.

## Finishing Touches
Sometimes the mesh can still look a bit lumpy after doing this, and one way to usually fix it is to set custom normals for this area.

Mesh -> Normals -> Set from Faces

![fixingnormals-setfromfaces.gif](/tutorials/fix_normals_meshes/fixingnormals-setfromfaces.gif)

and that's it!

> **Is it still looking wrong for your mesh?**
> Annoyingly, there are some meshes whose normals are borked for a more complicated reason (usually they are two sided meshes and have fused vertices upon import). This can require a more involved fix and I'd recommend checking out the discord server and asking there, the link can be found on the left sidebar of the wiki <3
{.is-success}

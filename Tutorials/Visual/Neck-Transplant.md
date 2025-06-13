---
title: Fixing Neck Seam via Transplant
description: one way to fix both a mesh normals seam + weights
published: false
date: 2025-06-13T18:36:40.279Z
tags: blender, head, neck, seam
editor: markdown
dateCreated: 2025-06-13T17:15:31.973Z
---

# Fixing Neck Seams
> Neck seams are often due to:
> - the mesh normals on the bottom of the head not matching those of the body it should go on
>   - this usually looks like a line where the light seems to reflect differently on each side
> - the weights on the bottom of the head not matching those of the body it should go on
>   - this will appear in game (often cutscenes) where it looks like it is pulling apart slightly
> - the textures on the bottom of the head not matching those of the body it should go on
>   - if the above two are fine, then it may be a texture seam - more on this at the end
{.is-success}


The main focus of this tutorial will be on the first two points. 

## The Neck Transplant

In the blend file with your modded head, import both a vanilla head of the same race/body type, as well as the body for it. The Vanilla head will be donating its lower ring of faces, and the body will just be there to visual everything better.

###### Big thanks to Alahria for letting me use their head as an example

Now that we have everything in our blend, it helps to turn on wireframe display for the head meshes:
![1-wireframe.png](/tutorials/visual/1-wireframe.png)

Next, select the modded head and go to Edit Mode.
Use Alt+click any of the bottom edges to select the whole vertices ring.
Ctrl+numpad+ to select the vertices ring above it as well.
Now X to delete Faces, this will leave us with a space to put our transplant in:

![2-mod-del-ring.png](/tutorials/visual/2-mod-del-ring.png)

Head back to Object Mode and select the vanilla head. Go into Edit Mode.
Select the bottom 2 rings of vertices as we did for the modded head.
Now: Shift+D to duplicate them, Esc to let go of it, then P -> Separate.

When we go back into Object Mode, go ahead and hide the vanilla head but leave the ring visible like so:

![4-mod-neck-and-vanilla-ring.png](/tutorials/visual/4-mod-neck-and-vanilla-ring.png)
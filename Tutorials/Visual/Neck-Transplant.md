---
title: Fixing Neck Seam via Transplant
description: one way to fix both a mesh normals seam + weights
published: false
date: 2025-06-13T19:49:24.567Z
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

At this point, we do not touch the vanilla neck ring mesh, all refitting and snapping will be done from the modded head's side.

In some cases, we will see that our modded head does not quite match up well with the vanilla neck ring. If it is more extreme, when we later snap the vertices together is may look a bit awkward and jagged. In our example it is nearly flush so one could probably just head to the next part where we snap the vertices.

![6-not-fitting.png](/tutorials/visual/6-not-fitting.png)

However, for the purpose of the tutorial, we will do so anyway.
With the modded head selected, go into Sculpt Mode. Use Elastic Grab tool with X-Symmetry on.
Now we just go around and make a nice smooth fit of our modded head to the neck ring:

![necktransplant-sculpt-clip.gif](/tutorials/visual/necktransplant-sculpt-clip.gif)

Once we like the look of it, we can go into Edit Mode again for the modded head.
Turn on Snap (the Magnet) and select Vertex.
Now with the move tool we can snap all vertices to the corresponding ones on the neck ring.
With X-Symmetry on, theoretically only one side is needed, but depending on the symmetry of the mesh itself if may not work entirely (we can fix this later)

![necktransplant-snap-clip.gif](/tutorials/visual/necktransplant-snap-clip.gif)

## Joining them up

> BEFORE JOINING, it is important that both meshes have the same UV Maps names, it does not matter which, but the must match. If they don't, it will result in funny half-invisible meshes in game.
{.is-warning}


In our example, the modded head has a UV Map of: `HEL_F_NKD_Head_Shadowheart_Mesh-uvs0`
And the neck ring mesh has a UV Map of: `TIF_F_NKD_Head_A_Mesh-uvs0` and `TIF_F_NKD_Head_A_Mesh-uvs1`

So in this case we simply rename the neck ring mesh (double click on the UV Map, then copy and paste). Now they have identical UV Maps names.

![5-rename-ring.png](/tutorials/visual/5-rename-ring.png)

Now, select only the bottom ring of vertices on the modded head using Alt+select an edge.
Switch to the neck ring mesh and select the top ring of vertices in the same way.

![11-select-bottomverts.png](/tutorials/visual/11-select-bottomverts.png)
![10-select-topverts.png](/tutorials/visual/10-select-topverts.png)

Go back to Object Mode.
Select the neck ring mesh, then Shift+select the modded head mesh

![12-select-both-meshes.png](/tutorials/visual/12-select-both-meshes.png)

Ctrl+J to join them together.
They are now one mesh, but the neck ring is still technically not attached to the rest. So we need to merge the vertices.

Back in Edit Mode, you will see that our rings we selected previously are still selected. These are the vertices we will merge.

Go to Mesh -> Clean up -> Merge by Distance.

![14-merge.png](/tutorials/visual/14-merge.png)

If all vertices were previously snapped well, you should see a notification in the bottom centre that 40 vertices have been merged. If it is less, that means some were farther apart than the set distance. You can change it here if needed (very small increments! The default value is 0.0001m):

![15-mergevalue.png](/tutorials/visual/15-mergevalue.png)

Done! 

![16-finish.png](/tutorials/visual/16-finish.png)

## Texture Seams

wip :)

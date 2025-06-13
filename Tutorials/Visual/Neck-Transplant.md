---
title: Fixing Neck Seam via Transplant
description: one way to fix both a mesh normals seam + weights
published: false
date: 2025-06-13T17:26:38.027Z
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


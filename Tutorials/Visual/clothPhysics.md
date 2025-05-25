---
title: Cloth Physics
description: A guide to add cloth physics to your mesh
published: false
date: 2025-05-25T17:06:25.520Z
tags: tutorial, cloth, cloth physics, physics
editor: markdown
dateCreated: 2025-05-23T18:21:12.555Z
---

# Cloth Physics

## Video Tutorial

The lovely **Lynia** has created a tutorial on how to add cloth physics without using the toolkit.

[See her video here](https://www.youtube.com/watch?v=-dXZ11lBXH4&list=PLy0yNPbdX35HvxgIuDE-oI9br25SoWtOk)

[![Cloth Physics](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D-dXZ11lBXH4%26list%3DPLy0yNPbdX35HvxgIuDE-oI9br25SoWtOk)](https://www.youtube.com/watch?v=-dXZ11lBXH4&list=PLy0yNPbdX35HvxgIuDE-oI9br25SoWtOk)

## Things You'll Need

- [This fork](https://github.com/nicoco007/lslib) of lslib
- [Blender](https://www.blender.org/download/)
- [Vertex Color Master Add-On](https://github.com/andyp123/blender_vertex_color_master/releases) (optional, but recommended)

# Steps

## Setting up your mesh

### Weight Painting

Your mesh should already be weight painted before you begin. To learn about weight painting your mesh, see the guide for [Weight Painting Armor and Clothes](https://wiki.bg3.community/en/Tutorials/Visual/Weight-Painting-Armor)

### Vertex Count

The mesh that will have the cloth physics applied to it needs to be under **10,000 vertices** otherwise it will likely crash the game and/or not work. 

To see the vertex count:
- Click on the **Viewport Overlays** icon in the top right of the 3D viewport
- Check the box for **Statistics**

> In **Edit Mode** this will show you the object, vertex, face, edge, and triangle counts for the selected mesh(es). In **Object Mode** the values will be the counts for all **visible** objects.
{.is-info}

![Screenshot 2025 05 25 124521](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-124521.png) ![Screenshot 2025 05 25 124604](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-124604.png)

The values on the right of the slash are the totals. The ones on the left are for the active selection.

Another way to see the vertex count (and other statistics) is using the **Preferences** window. 

- In the top menu bar, click **Edit** → **Preferences...**
- Select the **Interface** tab
- Open the **Status Bar** dropdown menu
- Check the box for **Scene Statistics**

This will show the information in the bottom right corner of the Blender window. 

> Like the previous method, in **Edit Mode** the values will be for the selected mesh(es). In **Object Mode** the values will be the counts for all **visible** objects, but the name you see is that of the active object.
{.is-info}

![Screenshot 2025 05 25 124657](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-124657.png)
![Screenshot 2025 05 25 124729](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-124729.png)


If your mesh has over 10,000 vertices, reduce it or separate the mesh into different pieces so that the piece that needs the cloth physics is less than 10,000 vertices.

## Creating the cloth mesh
## Vertex Painting

## Exporting from Blender

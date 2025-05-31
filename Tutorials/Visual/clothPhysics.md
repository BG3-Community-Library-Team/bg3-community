---
title: Cloth Physics
description: A guide to add cloth physics to your mesh
published: false
date: 2025-05-31T18:25:37.688Z
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
- [Blender](https://www.blender.org/download/) (any version 3.6 or above)[^1]
- [Vertex Color Master Add-On](https://github.com/andyp123/blender_vertex_color_master/releases) (optional, but recommended)

[^1]: Lynia uses version 4.1 in the video tutorial. The steps documented in this guide use version 3.6
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


If your mesh has over 10,000 vertices, reduce it or separate the mesh into different pieces so that the piece that needs the cloth physics has less than 10,000 vertices.

## Creating the cloth mesh

The best way to create the cloth mesh will depend on the shape of the mesh you're applying the physics to. 

- For something like a skirt, a dress, a robe, etc. that wraps around the body, we'll use the method of **duplicating the mesh**. 
- For things that dangle like ribbons, chains, tassles, etc. we'll follow the method of **creating a plane**.

### Duplicated mesh method

> Note that this method assumes that the mesh is **not** solidified/extruded to create faces on the inside. You do not want to create a solidified cloth mesh. It should always be a plane/two-dimensional.
{.is-warning}

In **Object Mode**, select the mesh object you'll be applying the physics to from the **Outliner**
Hit `Shift + D` to duplicate the mesh, then press the `Esc` key before clicking elsewhere to return it to the same position as the original.
- If the duplicated mesh is not in the same position as the original mesh, you can manually set the transform location values to 0 (or whatever the values are if you haven't applied transforms yet) in the **Object Properties** tab.

> Duplicate is __not the same__ as copy and paste
{.is-warning}

If your mesh looks like the cape shown in the image below and has normals facing outwards on both sides of the mesh, when you duplicate the mesh you'll have to make sure only **one side** of faces are selected. 

[![Screenshot 2025 05 25 142236](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-142236.md.png)](https://tinypic.host/image/Screenshot-2025-05-25-142236.3YEaVz)

Selecting the faces from the **UV Editing** tab is helpful here. Only the outside faces of the cape are selected. Not the faces that point in towards the character.

In this case, we would duplicate these faces from **Edit Mode**, then separate them into their own object by pressing `P` then the **Selection** option from the pop-up.

![Screenshot 2025 05 25 142635](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-142635.png)

Your cloth mesh does not need to have all same fold and wrinkle details as the original mesh, it just needs to roughly follow the same shape. Remove these details by smoothing out the cloth mesh. 

With your cloth mesh selected, switch to **Sculpt Mode** via the mode dropdown or by holding `Ctrl +  Tab` then with the option wheel open, press `2`, or use your mouse to hover over Sculpt Mode before releasing the keys.

![Screenshot 2025 05 25 133040](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-133040.png) [![Screenshot 2025 05 25 133606](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-133606.md.png)](https://tinypic.host/image/Screenshot-2025-05-25-133606.3YolL4)

Use the **Smooth** tool to smooth out the mesh.
![Screenshot 2025 05 25 133944](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-133944.png)
- Some tips to help:
	- Toggle isolating your mesh by pressing the `/` key
	- If your mesh is symmetrical, turn on **x-axis symmetry** in the upper right hand corner of the 3D viewport before you begin sculpting
	![Screenshot 2025 05 25 134017](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-134017.png)
	- Use the keys `[` and `]` to change the size of your brush
	- Start low and slow. Use a big brush with a low strength and build the up smoothness with it

Check to make sure the body isn't clipping through the cloth. It is okay if the original mesh clips through.
- If the body *is* clipping, go back to Sculpt Mode and adjust your cloth mesh. The **Elastic Grab** tool is good for this. 

In the image on the left, we can see that the body does not clip through. On the right, we see that the cloth mesh does clip through the original mesh. This is acceptable.

[![nobodyclipping](https://tinypic.host/images/2025/05/25/nobodyclipping.md.png)](https://tinypic.host/image/nobodyclipping.3Yo0PE) [![meshclipping](https://tinypic.host/images/2025/05/25/meshclipping.md.png)](https://tinypic.host/image/meshclipping.3Yo6M5)

For solidified/thick meshes like the cape shown in the example at the beginning of this article, positioning the cloth mesh to sit in the middle of the two sides will give you the best results. Clipping will be inevitable (provided your mesh is a reasonable thickness), so position the cloth mesh to *clip more* on the side that will be *seen less*.

![capeClipping](https://tinypic.host/images/2025/05/26/capeClipping.png)

The cloth mesh is ready to vertex paint.

### Create a new plane method

Something like this bow is a good example of when to use the plane method to create the cloth mesh as it is meant to hang down off the body, not conform to it. 

[![Screenshot 2025 05 25 141320](https://tinypic.host/images/2025/05/25/Screenshot-2025-05-25-141320.md.png)](https://tinypic.host/image/Screenshot-2025-05-25-141320.3YoFJ9)

Before creating the cloth mesh, we must first think about *how* we want this object to move. This bow has **4** parts that make sense to move with physics. They are numbered 1, 2, 3, 4 in the image below. 

There are multiple ways we could set up the cloth mesh for this:
- All four pieces move **together** under one cloth mesh
- All four pieces move **independently**, each with a unique cloth mesh[^2]
- Group the pieces by side; **1 & 2 move together** and share a cloth mesh, **3 & 4 move together** and share a cloth mesh

> The options with "multiple cloth meshes" do **not** mean we will have multiple cloth mesh objects. Everything will still be one mesh object in Blender, even if divided into separate parts. We will cover this in more detail in section **Exporting From Blender**
{.is-info}

[^2]: "Unique cloth mesh" does **not** mean 4 separate cloth mesh objects. See section Exporting from Blender for more details.

[![bowPieces](https://tinypic.host/images/2025/05/26/bowPieces.md.png)](https://tinypic.host/image/bowPieces.3Y7o3e)

This guide will use the third option, "Group the pieces by side; 1 & 2 move together and share a cloth mesh, 3 & 4 move together and share a cloth mesh". The steps can be adapted to suit the other two cases. 

In **Object Mode**, create a new plane and rotate it by **-90° on the x axis**. Scale it down and roughly position it. 

In **Edit Mode**, we can tweak the shape of the plane to better match the object it will be simulating. In the example below, the plane is now a trapezoid shape rather than a rectangle to better fit the pieces of the bow. It is still a single face at the moment.

[![Screenshot 2025 05 31 133503](https://tinypic.host/images/2025/05/31/Screenshot-2025-05-31-133503.md.png)](https://tinypic.host/image/Screenshot-2025-05-31-133503.3qUHYm)

Using the **Loop Cut** tool, start adding edge loops to create more faces. Tweak the edges and vertices as you go to minimize clipping. The more faces the cloth mesh has, the smoother the physics simulation will be, however it will also be more resource intensive. 
- Your cloth mesh shoudn't have more faces than the mesh it is simulating. 
- The density should be similar to or less than that of the mesh it will be simulating. 

The plane on the left has good density for this mesh. The plane on the right is too dense for this mesh. 

[![density](https://tinypic.host/images/2025/05/31/density.png)](https://tinypic.host/image/density.3qUFSe)

After repeating the process for the other side of the bow, I now have two separate cloth mesh objects in the scene. I've adjusted them so that they do not clip into each other. Leave them as separate mesh objects until the vertex painting is finished. You can apply transforms now. 

[![Screenshot 2025 05 31 140911](https://tinypic.host/images/2025/05/31/Screenshot-2025-05-31-140911.md.png)](https://tinypic.host/image/Screenshot-2025-05-31-140911.3qorUw)

The cloth mesh is ready to vertex paint.

## Vertex Painting
> The vertex colour master add-on mentioned above is optional. It is recommended because it will easily create gradients between vertex colours. 
{.is-info}

Both the mesh and it's cloth mesh need to be vertex painted. 

There are three colours that are used when vertex painting for cloth physics. 


| Colour | sRGB | Hex | Swatch
|----------|----------|----------|----------|
|Black|1 0.5 0|#FF8000|{.blackPhys}|
|Red|1 0 0|#FF0000|{.redPhys}|
|Blue|1 0.5 0.5|#FF8080|{.bluePhys}|
||||


If you have the add-on installed, **Vertex Paint** mode there will be a tab labelled **VCM** in the N-menu. 
- Press the `N` key to see the menu if it is not already there.
- Select the VCM tab.


## Exporting from Blender

## LSlib

---
title: Cloth Physics
description: A guide to add cloth physics to your mesh
published: true
date: 2025-07-04T16:54:57.799Z
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

![Screenshot 2025 05 25 124521](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-124521.png)) ![Screenshot 2025 05 25 124604](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-124604.png)


The values on the right of the slash are the totals. The ones on the left are for the active selection.

Another way to see the vertex count (and other statistics) is using the **Preferences** window. 

- In the top menu bar, click **Edit** → **Preferences...**
- Select the **Interface** tab
- Open the **Status Bar** dropdown menu
- Check the box for **Scene Statistics**

This will show the information in the bottom right corner of the Blender window. 

> Like the previous method, in **Edit Mode** the values will be for the selected mesh(es). In **Object Mode** the values will be the counts for all **visible** objects, but the name you see is that of the active object.
{.is-info}

![Screenshot 2025 05 25 124657](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-124657.png)
![Screenshot 2025 05 25 124729](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-124729.png)


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

[![Screenshot 2025 05 25 142236](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-142236.md.png)](https://tinypic.host/image/Screenshot-2025-05-25-142236.DcdeH)

Selecting the faces from the **UV Editing** tab is helpful here. Only the outside faces of the cape are selected. Not the faces that point in towards the character.

In this case, we would duplicate these faces from **Edit Mode**, then separate them into their own object by pressing `P` then the **Selection** option from the pop-up.

![Screenshot 2025 05 25 142635](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-142635.png)

Your cloth mesh does not need to have all same fold and wrinkle details as the original mesh, it just needs to roughly follow the same shape. Remove these details by smoothing out the cloth mesh. 

With your cloth mesh selected, switch to **Sculpt Mode** via the mode dropdown or by holding `Ctrl +  Tab` then with the option wheel open, press `2`, or use your mouse to hover over Sculpt Mode before releasing the keys.

![Screenshot 2025 05 25 133040](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-133040.png) [![Screenshot 2025 05 25 133606](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-133606.md.png)](https://tinypic.host/image/Screenshot-2025-05-25-133606.DcK2X)

Use the **Smooth** tool to smooth out the mesh.
![Screenshot 2025 05 25 133944](https://tinypic.host/images/2025/07/04/Screenshot-2025-05-25-133944.png)
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

There are **three colours** that are used when vertex painting for cloth physics. 

| Colour | Swatch | Hex |Purpose
|----------|----------|----------|----------|
|Black|{.blackPhys}|#000000|Excludes vertices from simulation|
|Red|{.redPhys}|#FF0000|Activates physics|
|Blue|{.bluePhys}|#0000FF|Slows physics[^3]|
||||
[^3]: Blue vertex paint rarely appears as pure blue. It'll be mixed with the red to create pink/purple hues.

If you have the add-on installed, **Vertex Paint** mode there will be a tab labelled **VCM** in the N-menu. 
- Press the `N` key to see the menu if it is not already there.
- Select the VCM tab.


**At least one black vertex is required**. The cloth needs to be pinned somewhere by a black vertex, even if it's as little as a singular corner vertex. The image below shows an example of a flag asset in game that makes use of cloth physics with the four corner vertices painted black.

![clothFlag](https://tinypic.host/images/2025/06/02/clothFlag.png)

Both the mesh and it's cloth mesh need to have vertex paint. We will start by painting the object mesh then transfering the colours to the cloth mesh. 

The different pieces that will make up the cloth mesh can be made to behave differently by using different blue values to give them an overall different colour. 

You can use any colour for your physics paint that has an **RGB colour** with a **red** value in the range **[0, 1]** and a **blue** value in the range **[0, 1]**. Make sure the **green** channel is **0**. Having a value in the green channel may interfere with vertex colour mask paints. Read about vertex colour masks [here](https://wiki.bg3.community/Information/Meshes/Vertex-Painting-Meshes).

![annotatedphysPaintRange](https://tinypic.host/images/2025/06/02/annotatedphysPaintRange.png)

In the **Properties** panel under the **Data** tab, make sure there isn't already any colour attributes. The game engine shaders can only read the active colour attribute set, so delete any others or be prepared to overwrite them. Don't worry about using the plus button to create a new set. A colour attribute set will be automatically created when following the steps. 

![Screenshot 2025 06 02 122635](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-122635.png)

Begin by filling your entire object mesh with black vertex paint. 
- Go to **Vertex Paint** mode
- Set both of the colour options to pure black (RGB 0 0 0 or Hex #000000)
- Press `Shift + K` to flood the entire mesh with black
	- This step is the same both with and without the VCM add-on.
  - You can also select **Paint** → **Set Vertex Colors** from the dropdown menu or the **Fill With Color** button from the add-on's N-menu.

For meshes that have large areas that won't be affected by the physics, mask them out before filling with any red or blue. 
- Go to **Edit Mode**
- Press key `1` or `3` to select by faces or vertices respectively
- Select the geometry to exclude
	- Press `Alt + Z` to toggle x-ray mode then `W` to cycle through to box selection
  - Select the areas
  - You can also use `L` to select by seams or UVs if your object is mapped and those areas are on separate UV islands/shells from those that will be using cloth physics. 
  
- Switch back to **Vertex Paint** mode
- Click the icon in the toolbar to mask the selection by vertices or faces
![Screenshot 2025 06 02 124638](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-124638.png)
- Since we selected the areas we do **not** want to paint, press `Ctrl + I` to invert the selection.
See the image below for the comparison between the selected areas in Edit Mode and the inverted area in Vertex Paint mode. The area with the vertices highlighted is the area that will be painted. 
![selection](https://tinypic.host/images/2025/06/02/selection.png)

As Lynia explains in the video linked at the beginning of this guide, when working with skirts and dresses, the best results are achieved if you start the cloth physics paint gradient below the widest part of the hips.
- Where the curve switches from increasing to decreasing
- Where ƒ''(x) = 0; the point of inflection for those of you who remember calculus.

If you're not using VCM, you'll have to manually paint and blur and smear to make a gradient.

If you are using VCM:
- Leave the first colour option as pure black. 
- Set the second colour option to a value within the ranges defined above.
	- I like making sure x-axis symmetry is enabled here, but that isn't always necessary depending on the shape of your mesh. 
- Click the **Linear Gradient** button at the bottom of the N-menu
- Hold down the `Left Mouse` button and drag a line down towards the bottom of the mesh

You can fine tune by manually painting. If you set the first colour to blue and the second to black, and change the blending mode to **Add** you can add blue to create pinks and slow the physics. Blend out these areas after painting.

![Screenshot 2025 06 02 132105](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-132105.png)

Once the mesh is painted, transfer the vertex paint colours to the cloth mesh.
- Select the unpainted cloth mesh
- `Shift` select the painted mesh in the viewport
	- If selecting from the Outliner, use `Ctrl` select instead of Shift
- Press `F3` and search for **"Transfer Mesh Data"**
- Select the option under **Face Corner Data** → **Colors** to transfer. This is not the same as the one under Vertex Data.
![Screenshot 2025 06 02 132827](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-132827.png)

For pieces like the bow from earlier, when transfering the colours over it is easier to split the bow into the same pieces as will be used by the cloth mesh, then merge everything back together.

## Exporting from Blender

### Naming and Number

You can only have **one cloth mesh object per exported object** (excluding LODs of the same cloth mesh), though you can assign multiple submeshes to use the same cloth mesh in LSlib. We'll get to that later.

The mesh used as an example throughout this guide currently has three cloth meshes: the robe, and two for the bow. 

[![Screenshot 2025 06 02 145126](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-145126.md.png)](https://tinypic.host/image/Screenshot-2025-06-02-145126.3qeV2Z)

This can be resolved in two ways:
- Merge **all** of the cloth meshes into one object
- Break apart the items into separate pieces to export so that they each only have one cloth mesh.

I'll use both methods. The robe and it's cloth mesh will be one GR2 file, and the belt, bow, and the bow's cloth meshes will be a second GR2 file.

If merging any cloth mesh objects together, make sure they have the name for their colour attribute set, just like you would do with UV map names before merging meshes together. The colour attribute name can be anything. It won't be seen again outside of Blender. 

- Merge the cloth mesh objects together by selecting them both either in the viewport or the outliner
- Press `Ctrl + J` to join them
- Rename the object and the mesh
	- You can call it whatever you want as long as you can differenciate it from other meshes
  - Mine are usually named *whateverItemNameIs_**Cloth_Mesh*** because I'm a stickler for naming conventions but you do you

### Checkboxes

In the **Properties** panel in the **Object** tab, assign LOD info and export order as usual.

Before exporting, there's some boxes that will have to be checked in the **Mesh Type** box.

- For the object that will be assigned the cloth physics, check the box for **Cloth**
[![Screenshot 2025 06 02 150719](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-150719.md.png)](https://tinypic.host/image/Screenshot-2025-06-02-150719.3qeKww)
- For the **cloth mesh**, check **Cloth** and **Cloth Physics**
[![Screenshot 2025 06 02 150710](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-150710.md.png)](https://tinypic.host/image/Screenshot-2025-06-02-150710.3qeEmv)

Your cloth mesh should be parented under the armature and have the correct armature like you would for any other mesh. It does not need to be UV mapped.

Export as usual. 

> If you use BG3EquipmentGenerator, note that it tends to lose these parameters along the way. You can still use it to generate all the files for your mod, but you'll need to reexport and overwrite the GR2s it outputs with ones directly exported from Blender.
{.is-warning}

## LSlib

In the forked version of LSlib linked above, open **ConverterApp.exe** and switch to the **Cloth Tools** tab

- Locate your exported GR2 to fill in the field for **GR2 File Path**
- Click **Load**

The **Resource Name**, **Physics Mesh**, and **Target Meshes** fields should autofill based on what submeshes had the boxes for **Cloth** and **Cloth Physics** checked. You can un/check submeshes if needed. 

![Screenshot 2025 06 02 151503](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-151503.png)

- Click **Generate**
- Copy `Ctrl + C` all of the XML it outputs

![Screenshot 2025 06 02 151757](https://tinypic.host/images/2025/06/02/Screenshot-2025-06-02-151757.png)

In your **meshes.lsf.lsx** file, paste in the [code block Lynia has linked](https://pastebin.com/4peJ4dkn) from her video. Paste it **underneath** `<node id="Base" />`, not inside of that node. This block contains all of the parameters of the cloth physics. Feel free to adjust them. 

Under the node `<node id="ClothParams">`, replace the value of the attribute **UUID** with the name of your cloth mesh. 
- The name will be in GR2FileName.SubmeshName format

Inside of the **children** node within `<node id="ClothProxyMapping">`, paste in the output from LSlib. 

> If you make any changes to the mesh and then reexport, it is a good idea to regenerate the output from LSlib in case vertices changed. 
{.is-info}


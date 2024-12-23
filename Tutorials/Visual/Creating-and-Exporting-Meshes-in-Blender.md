---
title: Creating and Exporting Meshes in Blender
description: How to create and export meshes in blender.
published: false
date: 2024-12-23T13:49:45.768Z
tags: visual, tutorial, blender, wip
editor: markdown
dateCreated: 2024-12-23T13:49:45.768Z
---

# Creating and Exporting Meshes in Blender

### this article was written by commanderstrawberry and is currently ported and edited by Alithea - please be patient.

In this tutorial, we assume you are generally familiar with using 3D software. Therefore, the focus will be on aspects specific to the Baldur’s Gate 3 exporter made by Norbyte. Remember, there are many general YouTube tutorials available on weight painting and editing meshes in Blender.

## Table of Contents

- [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [BG3 Tutorials and Resources](#BG3-Tutorials-and-Resources)
  - [Setup](#Setup)
  - [Extracting a Model to Work With](#Extracting-a-Model-to-Work-With)
  - [Importing](#Importing)
  - [Editing Meshes](#Editing-Meshes)
  	- [Vertex Paint](#Vertex-Paint)
  - [How to Vertex Paint Sleeves and Pant Legs](#How-to-Vertex-Paint-Sleeves-and-Pant-Legs)
  - [Fixing meshes that import in wrong](#Fixing-meshes-that-import-in-wrong)
  - [Physics](#Physics)
  - [LODs and Load Order](#LODs-and-Load-Order)
  	- [Using No LODs](#Using-No-LODs)
  - [Weight Painting](#Weight-Painting)
  - [Exporting](#Exporting)
  - [Testing in Game](#Testing-in-Game)
  - [Hotloading](#Hotloading)
  - [General Blender Tutorials](#General-Blender-Tutorials)

  
## Requirements
- Be sure to watch [this video tutorial series](https://www.youtube.com/watch?v=IbivHL2lPrc&list=PLG6GyipNkD2ptAp16VXs8BiTNEaMlgKhO&index=1) by Druu using the BG3 Blender plugin and follow along. It is older but still very relevant and helpful.

## Setup

[Check here for a list of tools.](https://modding.wiki/tools)

Here we are using Modder's Multitool, Blender 3.6, and [Norbyte’s Blender installer](https://github.com/Norbyte/dos2de_collada_exporter). Until the update specifically says it has been updated to work with Blender 4.0, we recommend sticking with Blender 3.6 currently.

Make sure you install it correctly—[this video](https://www.youtube.com/watch?v=yQSqRF7dLB8) should give you an example of how to install it.

You should also install [Padme’s Addon, ‘Create LODs’](https://www.nexusmods.com/baldursgate3/mods/346). You may also find use of the 'Reset Transforms' tools as they are helpful when weight painting a model.

## Extracting a Model to Work With

![Imported meshes.](NewBodyBlenderScreenshotImported.webp)

Now open your modder’s multitool. Click ‘Search Index’. Filter by `.GR2`. Search something like `HUM_F_ARM_` and browse the in-game meshes available to regular size humanlike females.

You should at least extract [HUM_F_NKD_Body_A](https://modding.wiki/Modding:Body%20Models) (or whatever nude you are basing your outfit on) to fit your new outfit around.

When you have found a model to your liking, click the extract file/open folder. You should find the mesh in `.GR2` and `.dae` form on your computer. Use the `.dae`—the Blender importer likes `.dae` format a lot more than `.gr2`. 

![A mesh importing. It has only 1 LOD.](MeshImportsWithLODSS.webp)

**Note:** You generally cannot import a modded-in mesh without the plugin crashing Blender. Save your work often and ensure you have permission to edit any modded items.

## Importing

It will be a fairly standard rig with an Armature modifier (see Modifier tab). Your armatures will import in at 90 degrees, which will cause it to export flat to the floor and follow a naked character around like a weird sad windsock. Fix it by applying transforms:

- **[Object Mode] Object > Apply > All Transforms** on the armature, until the coordinates for its location all read **0, 0, 0**. You may need to do the same for the meshes as well.

![Your mesh will likely import this way—note the 90-degree angle.](UrMeshImported90.webp)

The mesh will import with 1 or more LODs (Level of Detail meshes). Delete anything with "LOD" in the name except the highest-quality one. If the mesh has a skirt, you may see an undetailed boxy "Cloth Mesh," which has to do with Physics.

## Editing Meshes

If you wish to combine two meshes, ensure each mesh has the same name for the UV and color maps before combining them. BG3 meshes may not align with the UV square; you may need to scroll far to locate them.

![Your UV map and Colour maps, found in Object Data tab.](Screenshot_Uv_and_colour_map_imports.webp)

For a full-body mesh, consider parenting your mesh to a naked body armature, which includes all bones and can avoid weighting issues.

**Note:** Genitals are attached via LSX code and are not part of the body mesh.

## Vertex Paint

![This underwear has its green vertex paint, which tells it to vanish when a top is equipped.](BlenderVertexPaintUnderwearExample.webp)

The game’s armor system uses vertex paint to manage visibility. Use existing meshes as reference for vertex paint:

- **Black:** Visible elements.
- **Dark Green:** Elements intended to disappear (e.g., pant legs).
- **Red:** Physics regions.

For sleeves or pant legs, use these steps for painting vertex paint:

1. Enter Edit mode.
2. Select vertices to paint.
3. **Shift + D** to duplicate vertices (keep them in place).
4. Use Vertex Paint mode and the selected vertices icon to apply paint.

[Check here for reference Hex codes.](https://modding.wiki/Modding:VertexColorMaskSlots)

## Fixing Meshes That Import Wrong

![Fixing meshes that import in wrong.](BlenderTutAlfiraBustedNormals.webp)

Skirts and similar meshes may import with broken shading due to normals. To fix:

1. **[Edit Mode] Mesh > Clean Up > Merge By Distance**
2. Apply a solidify modifier (0.01 thickness).
3. **Alt+N > Recalculate Normals > Average Face Area.**

Alternatively:

- Select all and **Alt+N > Average Face Area.**
- If edges are blue, clear sharp edges and repeat.

## Physics

[Here is a physics tutorial by ReallyLazyIcarus.](https://www.nexusmods.com/baldursgate3/articles/311)

Physics are managed with red vertex paint, with counterbalance colors (hot pink, blue). Meshes entirely weighted to one bone may crash the game; weight static meshes to piercing bones.

![Example of red vertex paint for Physics.](ScreenyExampleOfPhysicsMesh.webp)

## LODs and Load Order

Generate LODs using Padme’s addon tool. 

- **LOD Level:** LOD0 is the best quality. 
- **LOD Distance:** Ensure LOD0 is visible up to ~15 meters; the final LOD must be set to 0.
- **Export Order:** All LOD0 meshes first, followed by LOD1, LOD2, etc.

![LOD order in BG3 settings.](Screenshot_LOD_Distance_level_Explained.webp)

## Exporting

Default export settings are fine. Remember:

- Capitalize `.GR2` in file names.
- Delete any nude body armature before exporting.

![Default export settings for Blender 3.6](BlenderTtut3.6ExportSettings.webp)

## Testing in Game

Test as a replacer for existing meshes before creating new items. [See here for coding items.](https://modding.wiki/Modding:Coding%20An%20Item)

Hotloading is highly recommended for testing. [See here for hotloading.](https://modding.wiki/Modding:Hotloading)

## General Blender Tutorials

- [BlenderGuru’s Donut tutorial.](https://www.youtube.com/@blenderguru)
- [TheRoyalSkies Blender tutorials.](https://www.youtube.com/@TheRoyalSkies/playlists)

## Modder Resources

- [High Heel Feet by LazyIcarus.](https://www.nexusmods.com/baldursgate3/mods/2973)
- [Outfit Builder by LazyIcarus.](https://www.nexusmods.com/baldursgate3/mods/3683)
- [Volno Texture Toolbox.](https://www.nexusmods.com/baldursgate3/mods/4310)

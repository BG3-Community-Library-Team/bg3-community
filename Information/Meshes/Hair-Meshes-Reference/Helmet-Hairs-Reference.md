---
title: Helmet Hair Meshes Reference
description: A reference for all helmet hair meshes in the game's files.
published: false
date: 2024-07-20T23:00:16.560Z
tags: hair, reference
editor: markdown
dateCreated: 2024-07-20T22:45:19.939Z
---

# Explanation

The “HairType” value in a standard hair's \_merged entry helps determine what mesh will be used when a character has equipped certain headwear, such as a hat or a helmet.

Helmet hair meshes do not have physics and are not made to autosnap, so there are meshes for each unique body type. You can find the meshes in “Models\\Generated\\Public\\Shared\\Assets\\Characters\\\_Models\\\_Hair\\Helmet\_Hair\\Resources”.

The \_merged file containing the entries for each helmet hair mesh can be found in "Shared\\Public\\Shared\\Content\\Assets\\Characters\\\[PAK\]\_Helmet\_Hair".

Note that there is no mesh or \_merged entry for value 0. A hairstyle with a "0" HairType will only show the scalp, rather than a helmet hair.

The helmet hair version that a headwear will use is set in the headwear's RootTemplate, but if none is set then it will use the same version assigned to the ParentTemplate item.

-   Version A is typically used by helmets, to which the base ParentTemplateID is c58a1f91-ec1b-49c8-96ab-d94d4be4b584 (aka "ARM\_Helmet\_Leather" or "ARM\_Headwear\_Leather\_A").
-   Version B is not currently used by vanilla headwear.
-   Version C is typically used by hats, to which the base ParentTemplateID is 4d2e0931-3a01-4759-834b-8ae36749daab (aka "ARM\_Hat" or "CLT\_Headwear\_H").

### Table

-   HairType: The identifier for the mesh the hair uses when wearing a hat.
-   Filename: The name of the mesh in the game files. Note: Only the HUM\_M mesh names are listed here.
-   Version A: An image of the “A” version of the hair.
-   Version B: An image of the “B” version of the hair.
-   Version C: An image of the “C” version of the hair.

# Helmet Hairs

### Version A

| HairType | Hair Texture & Length | Version A | Version B | Version C |
| --- | --- | --- | --- | --- |
| 1   | Straight\_Long | ![](/information/meshes/helmet-hairs/straight_long_a.png) |     | ![](/information/meshes/helmet-hairs/straight_long_c.png) |
| 2   | Straight\_Short | ![](/information/meshes/helmet-hairs/straight_short_a.png) | ![](/information/meshes/helmet-hairs/straight_short_b.png) | ![](/information/meshes/helmet-hairs/straight_short_c.png) |
| 3   | Wavy\_Long | ![](/information/meshes/helmet-hairs/wavy_long_a.png) | ![](/information/meshes/helmet-hairs/wavy_long_b.png) | ![](/information/meshes/helmet-hairs/wavy_long_c.png) |
| 4   | Wavy\_Short | ![](/information/meshes/helmet-hairs/wavy_short_a.png) | ![](/information/meshes/helmet-hairs/wavy_short_b.png) | ![](/information/meshes/helmet-hairs/wavy_short_c.png) |
| 5   | Curly\_Long | ![](/information/meshes/helmet-hairs/curly_long_a.png) | ![](/information/meshes/helmet-hairs/curly_long_b.png) | ![](/information/meshes/helmet-hairs/curly_long_c.png) |
| 6   | Curly\_Short | ![](/information/meshes/helmet-hairs/curly_short_a.png) | ![](/information/meshes/helmet-hairs/curly_short_b.png) | ![](/information/meshes/helmet-hairs/curly_short_c.png) |
| 7   | Dreads\_Long | ![](/information/meshes/helmet-hairs/dreads_long_a.png) | ![](/information/meshes/helmet-hairs/dreads_long_b.png) | ![](/information/meshes/helmet-hairs/dreads_long_c.png) |
| 8   | Dreads\_Short | ![](/information/meshes/helmet-hairs/dreads_short_a.png) | ![](/information/meshes/helmet-hairs/dreads_short_b.png) | ![](/information/meshes/helmet-hairs/dreads_short_c.png) |
| 9   | Afro\_Long | ![](/information/meshes/helmet-hairs/afro_long_a.png) | ![](/information/meshes/helmet-hairs/afro_long_b.png) | ![](/information/meshes/helmet-hairs/afro_long_c.png) |
| 10  | Afro\_Short | ![](/information/meshes/helmet-hairs/afro_short_a.png) | ![](/information/meshes/helmet-hairs/afro_short_b.png) | ![](/information/meshes/helmet-hairs/afro_short_c.png) |
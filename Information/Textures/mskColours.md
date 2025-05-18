---
title: MSK Colours
description: MSK Colour Parameters
published: true
date: 2025-05-18T18:58:30.576Z
tags: msk, mskcloth, mskcolor
editor: markdown
dateCreated: 2025-05-12T19:59:51.080Z
---

# MSK Colours

For a mesh to be dyeable in game, it needs to have an MSK map. This texture map allows you to set which dye parameters different areas in your mesh use. 

There are **12** parameters used by the primary MSK armour shader(s).

| Parameter | sRGB | Hex | Swatch
|----------|----------|----------|----------|
|Cloth_Primary|1 0.5 0|#FF8000|{.clothPri}|
|Cloth_Secondary|1 0 0|#FF0000|{.clothSec}|
|Cloth_Tertiary|1 0.5 0.5|#FF8080|{.clothTer}|
|Leather_Primary|0.5 0 1|#8000FF|{.leatherPri}|
|Leather_Secondary|0 0 1|#0000FF|{.leatherSec}|
|Leather_Tertiary|0.5 0.5 1|#8080FF|{.leatherTer}|
|Metal_Primary|0 1 0.5|#00FF80|{.metalPri}|
|Metal_Secondary|0 1 0|#00FF00|{.metalSec}|
|Metal_Tertiary|0.5 1 0.5|#80FF80|{.metalTer}|
|Accent_Color|1 0 0.5|#FF0080|{.accentCol}|
|Custom_1|0 0.5 1|#0080FF|{.custom1}|
|Custom_2|0.5 1 0|#80FF00|{.custom2}|
|||||

For less complex meshes, the MSK map can use **3** parameters: Color_01, Color_02, and Color_03. You cannot combine these on the same MSK map as the parameters above, as you may notice they use the same values as Cloth_Secondary, Metal_Secondary, and Leather_Secondary respectively. You can define values for both sets in a colour preset or dye, though which value gets used will depend on the material shader. Read more about shaders [here.](https://wiki.bg3.community/Information/Textures/Shaders)


| Parameter | sRGB | Hex | Swatch
|----------|----------|----------|----------|
|Color_01|1 0 0|#FF0000|{.color1}|
|Color_02|0 1 0|#00FF00|{.color2}|
|Color_03|0 0 1|#0000FF|{.color3}|
||||


## Solid Colour MSK

If your MSK map is a solid colour, you can use the UUID of the Engine_MSK colour map in your material instead of creating a new solid map.

| Parameter |UUID
|----------|----------|
|Cloth_Primary|01e0ce88-b357-fd26-323a-5a3577fcc35a|
|Cloth_Secondary|a175d259-c903-43c3-afc7-8149cafaa693|
|Cloth_Tertiary|083b46e4-bc81-c9f7-fb3f-04f51d723aa9|
|Leather_Primary|afea41e0-169c-efd2-008e-b6ac3174a180|
|Leather_Secondary|cb176f64-9cc7-44ee-b575-d96e2aa7b431|
|Leather_Tertiary|unknown|
|Metal_Primary|40daac11-00dc-de43-7dcc-7cb7206fd298|
|Metal_Secondary|41f0e870-0cc8-1293-6b72-36dab4026617|
|Metal_Tertiary|c1776e67-672d-7a87-18c5-bb97acf5264a|
|Accent_Color|773df1ad-1d72-474d-6568-75ba26e79fac|
|Custom_1|f717b846-57ff-f211-a7e9-2da363bfb8f5|
|Custom_2|4ee46b58-caf0-e98a-a235-1375b43f5dca|

## Compression

For clothing and armour, MSK maps use the same compression settings as the base colour map: **BC1 DTX1** with mipmaps enabled. You can read more about compression settings [here.](https://wiki.bg3.community/Information/Textures/texture-types)


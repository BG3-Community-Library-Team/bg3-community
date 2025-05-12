---
title: MSK Colours
description: MSK Colour Parameters
published: false
date: 2025-05-12T20:16:19.659Z
tags: 
editor: markdown
dateCreated: 2025-05-12T19:59:51.080Z
---

# MSK Colours
For a mesh to be dyeable in game, it needs to have an MSK map. This texture map allows you to set which dye parameters different areas in your mesh use. 

There are **12** parameters used by the MSK armour shader(s).

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
|Accent_Color|1 0 0.5|##FF0080|{.accentCol}|
|Custom_1|0 0.5 1|##0080FF|{.custom1}|
|Custom_2|0.5 1 0|#80FF00|{.custom2}|
|||||


## Solid Colour MSK
If your MSK map is a solid colour, you can use the UUID of the Engine_MSK colour map in your material instead of creating a new solid map.

Cloth_Primary 	1 0.5 0 	#FF8000
Cloth_Secondary 	1 0 0 	#FF0000
Cloth_Tertiary 	1 0.5 0.5 	#FF8080
Leather_Primary 	0.5 0 1 	#8000FF
Leather_Secondary 	0 0 1 	#0000FF
Leather_Tertiary 	0.5 0.5 1 	#8080FF
Metal_Primary 	0 1 0.5 	#00FF80
Metal_Secondary 	0 1 0 	#00FF00
Metal_Tertiary 	0.5 1 0.5 	#80FF80
Accent_Color 	1 0 0.5 	#FF0080
Custom_1 	0 0.5 1 	#0080FF
Custom_2 	0.5 1 0 	#80FF00

## Compression




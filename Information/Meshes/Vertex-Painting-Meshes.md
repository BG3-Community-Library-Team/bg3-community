---
title: Vertex Painting Meshes
description: 
published: true
date: 2024-05-12T00:48:27.587Z
tags: meshes
editor: markdown
dateCreated: 2024-04-28T17:39:51.157Z
---

# Vertex Paint Colors

# Vertex Paint Transfer

You'll need an object with colors, and the object without colors that you want to transfer to.

You'll need to select your color mesh first and then the non color mesh, then press F3 and search Transfer Mesh Data.
Then select face corner colors.
You should now see a new color attribute on the non color mesh with the vertex colors.
Then there should be two entries in Color Attributes, the old one with nothing (delete it), and the new one.

![transfervertcol.gif](/information/meshes/transfervertcol.gif)

> 
> If the two meshes you are transferring between are significantly different, you will probably need to clean up the vertex paint manually, as any blurred edges will end up sticking to the ground in game.
{.is-info}


[TODO: Pictures]
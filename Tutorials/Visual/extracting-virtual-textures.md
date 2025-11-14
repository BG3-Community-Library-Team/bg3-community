---
title: Extracting Virtual Textures with LSLIB
description: how to find and extract virtual textures
published: false
date: 2025-11-14T16:49:35.291Z
tags: textures, lslib, virtual textures
editor: markdown
dateCreated: 2025-11-14T16:49:35.291Z
---

# Extracting Virtual Textures with LSLIB
Many/most equipment and skin textures are stored as virtual textures and will require extraction if we wish to edit them.

This tutorial will use the skin textures for the BT1 elf/human/halfelf body (HUM_F_/NKD_Body_A). The principle is the same for equipment as well.

## Find the material assigned to that mesh

Easiest is to use [Norbyte's BG3 search](https://bg3.norbyte.dev/search)

We will follow a patch of breadcrumbs from mesh name to the virtual texture name, starting with our mesh name
`HUM_F_NKD_Body_A`
There will be some results and for the purpose of this tutorial we are looking for the one labeled "VISUAL"

Scroll down to where the materials are assigned and click on the UUID -> View object to open in a new tab:
![1-norbsearch.png](/tutorials/extract_vt/1-norbsearch.png)

## Find the virtualtexture

So now we have the MaterialResource opened, and usually the virtual texture entry is at the very bottom, under `<VirtualTextureParameters>`:
![2-norbsearch.png](/tutorials/extract_vt/2-norbsearch.png)

again, click the UUID and open in a new tab.

## Make note of the important info


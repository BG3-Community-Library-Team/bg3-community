---
title: Temp fix for head armature export via glTF
description: stop the export from baking (non-existant) animations
published: false
date: 2025-08-29T22:11:13.433Z
tags: blender, skeleton, armature, gltf
editor: markdown
dateCreated: 2025-08-29T22:11:13.433Z
---

# Temp fix for head armature export via glTF
The necessity of this is subject to change, should the plugin be updated.

At the time of this writing, the latest version of the [BG3/DOS2 gltf/dae/gr2 plugin](https://github.com/Norbyte/dos2de_collada_exporter) for Blender (commit 270c975) has a bake animation setting set to True by default - this appears to be problematic when exporting custom skeletons. If using the toolkit, the import will likely fail with an error that it finds no skeleton but instead an animation. If forced in anyway, trying to use it will result in an invisible head.

## Fix
Find the io_scene_dos2de folder where the plugin installed to in Appdata\Roaming\Blender Foundation, example here:

![new-14_exportgltf3-operators1.png](/tutorials/custom_head_armatures/new-14_exportgltf3-operators1.png)

Open the file operators_gltf.py in a text editor, Ctrl+F to find "bake" which finds this line:

![new-14_exportgltf3-operators2.png](/tutorials/custom_head_armatures/new-14_exportgltf3-operators2.png)

By default it will be set to True. This will need to be set to False as seen above. Now save and close the file.
---
title: Virtual Textures Explained
description: 
published: false
date: 2026-01-18T10:56:51.056Z
tags: 
editor: markdown
dateCreated: 2026-01-18T10:55:00.292Z
---

# Virtual Textures - The Basics
## What are Virtual Textures? 

Virtual textures are a rendering technique used in modern video games like Baldur's Gate 3 to efficiently manage and display high-resolution textures across large, detailed environments. Instead of loading entire high-resolution textures into memory at once, virtual texturing streams only the necessary portions of textures based on what’s visible to the player at any given time. This helps to avoid overwhelming the GPU's memory and thus improves game performance. 

Here’s how it works:

- Texture Atlas: A massive texture (or set of textures) is created. This texture is too large to fit in GPU memory all at once.
- Tiling and Streaming: The texture is divided into smaller tiles. Only the tiles needed for the current camera view (based on the player’s position and perspective) are loaded into memory and rendered. As the player moves, new tiles are streamed in, and unused ones are discarded.
- Mipmapping and LOD: Virtual textures use mipmaps (progressively lower-resolution versions of textures) to ensure smooth transitions and efficient rendering at varying distances (levels of detail). For example, distant objects use lower-resolution tiles, while close-up objects use higher-resolution ones.
- Page Table: A "page table" maps which texture tiles are needed for each part of the scene, allowing the engine to dynamically fetch the right data from disk or memory.

VTs are typically used alongside traditional textures in game development, which is the case in BG3. Modders can choose to use virtual textures or traditional textures.  


**[Notes: Adding visuals for the above would be ideal]**

## TBA
Ideas: 
- How to locate and extract VTs using multittol (finding gtex file name) and toolkit (noting that they extract from the toolkit a bit differently, and NM is often blank until decomposed)
- How to unpack VTs using LSLIB (since some are not included in multitool)
- Advanced section? 
- Links to external resources / writeups? 
- Then, click "here" to see how to build your own Virtual Textures etc etc
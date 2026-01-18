---
title: Misconceptions About Virtual Textures
description: 
published: false
date: 2026-01-18T11:22:16.415Z
tags: 
editor: markdown
dateCreated: 2026-01-18T11:22:16.415Z
---

# Misconceptions About Virtual Textures
Due to knowledge of VTs not being intuitive, there can be misconceptions surrounding them. We address some common ones below:  
## “Virtual Textures stop the game from loading up, particularly in Honour Mode.”

Virtual Textures do not prevent the game from loading and are not uniquely tied to Honour Mode. VTs are designed to stream as a background process during real-time during gameplay. Therefore, any issues with VTs are likely to present during gameplay (e.g missing or low resolution textures) and not when starting the game. 

If Baldur’s Gate 3 fails to load (e.g., freezes on a loading screen or crashes at startup), the issue is more likely related to other factors, such as:
- Corrupted game files
- Hardware limitations
- Software conflicts (such as issues with drivers, mods, or background processes)
- Save file issues (such as corrupted saves or overly complex game states, like saving in the middle of a hundred barrels exploding.)
    
If the game fails to load, it’s usually because of issues with initializing the game state, not because virtual textures are “stopping” it. 

## “Virtual textures have broken my mods.” 
Virtual textures do not break mods. 

Virtual textures operate on engine level rather than mod level. Therefore, a mod adding a new armor set might include custom virtual textures, but these are processed by the same virtual texturing system as the base game’s assets. The system itself doesn’t “break” mods; it simply renders the textures provided, whether they’re from Larian or a modder. 

Therefore, any issues narrowed down to a specific mod are unlikely to be caused by its virtual textures.

## “Virtual textures are causing my game to have performance issues.”

Some mod users notice performance issues (e.g., lag or stuttering) when using texture-heavy mods and assume virtual textures are to blame. However, these issues are more likely caused by:
- High-Resolution Mod Textures: Mods with 4K or 8K textures can strain VRAM or disk streaming, especially on lower-end systems. Virtual texturing tries to mitigate this by streaming only necessary tiles, but poorly optimized mod textures can still cause performance hits.
- Mod Bloat: Installing many mods, especially those adding new assets, can increase memory demands or cause conflicts, slowing down the game. This is a mod management issue, not a virtual texture problem.
    
Mod authors can help prevent this by using the lowest resolution texture that suits their needs. For Baldur’s Gate 3, 2k textures are usually sufficient. 

Mod users should make sure to safely remove mods between playthroughs when they do not intend to use them to minimize performance issues.  

# Common Mod Issues Mistaken for Virtual Texture Problems
Here are some specific issues mod users might encounter that could be misattributed to virtual textures, along with their actual causes. This list is also helpful for mod authors to consider when troubleshooting their own mods:

## Missing or Blurry Textures
**Symptom:** A modded item or character appears with missing textures (e.g., pink or black surfaces) or low-resolution visuals.

**Cause:** The mod’s texture files might be incorrectly formatted, missing mipmaps, or not properly referenced in the mod’s configuration. For example, a mod might point to a texture file that doesn’t exist or is in the wrong folder. Alternatively, the VT limit has been exceeded – view the following section for more details!

**Not Virtual Textures:** Virtual texturing simply renders what it’s given. If the mod’s texture data is faulty, the system can’t display it correctly.

> **What Happens When VTs Fail to Load?** 
> Fortunately, this is not game-breaking! The game engine will typically fall back to a lower-resolution version of the texture (called a mipmap). This may cause visual issues like blurriness or missing details but won’t prevent the game from working or loading. If a VT in a mod isn’t loading in at all, the textures will simply be absent and the material will show as black. 
{.is-info}

## Game Crashes or Freezes
**Symptom:** The game crashes when loading an area or character.

**Cause:** Crashes are often due to mod conflicts, outdated mods after a game patch, or corrupted mod files.

**Not Virtual Textures:** Virtual texturing operates after the game is loaded and don’t initiate crashes. Crashes are more likely tied to the above issues. Make sure to avoid conflicts in your mod load order and keep your mods updated. Mod authors can test their .pak files to confirm no corruption occurred when pak-ing the mod together.  

## Texture Pop-In or Slow Loading

**Symptom:** Modded textures take time to load, appearing blurry before sharpening.

**Cause:** This can happen if the mod’s textures are very large (e.g., 4K) and/or the user’s system struggles to stream them quickly. It could also result from improper mipmap generation in the mod.

**Not Virtual Textures:** The virtual texturing system is doing its job by streaming tiles as needed. The delay comes from hardware limitations or mod optimization issues.

## Mod Not Appearing In-Game

**Symptom:** A modded texture or asset doesn’t show up at all.
**Cause:** This is often due to incorrect mod installation, missing dependencies, or a load order issue. For example, an armour mod might require a specific texture from a second mod to function and, without it, the textures won’t load.
**Not Virtual Textures:** Virtual texturing doesn’t control whether a mod’s assets are loaded; that’s handled by the game’s modding framework and file structure.


**[Note: This above section is a bit repetitive of the one before. Might be worth combining them, edited wording a bit etc]**

# How Modder Users and Creators Can Avoid Issues

To prevent issues that might be mistaken for virtual texture problems, mod users and creators can take these steps.

## For Mod Users
- Use a Mod Manager to ensure proper load order and help detect conflicts.
- Verify that mods are updated for the latest game patch. Outdated mods are a common source of issues.
- Monitor your system resources, especially when using texture-heavy mods. Check system specs if performance issues arise.
- Read mod documentation. Some mods require specific installation steps or dependencies. They may need to be placed in a specific position in your load order. Follow the modder’s instructions carefully.

## For Mod Creators
- Optimize Textures: Ensure textures are correctly formatted and compressed, include mipmaps, and are not unnecessarily high-resolution. 
- Test mods in the game environment to ensure textures load correctly and don’t conflict with existing assets.
- Test your mod in the game after pak-ing to ensure no file corruption occurred. 
- Provide clear instructions. Specify any dependencies or load order requirements to help users avoid setup errors.
- Create a VT Library to reduce the number of VTs adding to the VT limit. This can be done for mods made in the toolkit and manually. Consider using Script Extender to build your VTs to avoid the limit altogether. 
- Include in your mod description if your mod will contribute to the VT limit (i.e your VTs were made using the official toolkit) – this helps users keep track of how many VT mods they are installing. 
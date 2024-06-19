---
title: Armour Meshes Reference
description: A reference for all wearable meshes in the game
published: false
date: 2024-06-19T04:58:03.197Z
tags: reference, meshes, armor, armour
editor: markdown
dateCreated: 2024-06-17T23:33:06.802Z
---

# Description
## Summary
This is a collection of the wearable meshes in the game files, including some which are not utilised within the game itself. They are split between ARM (armour) and CLT (clothing). "Armour files" will be used here to refer to all ARM and CLT files.

Armour files begin with an abbreviated race name and body type, followed by the type of equipment it is - for instance `HUM_M_ARM`.

> Sometimes an item within the game will use ARM files for a piece of camp clothing and vice versa. On rare occasions, neither ARM nor CLT will be used.
{.is-info}

## Glossary
- Mesh: Meshes are the models that make up all physical objects in the game, be they people, items, or buildings. 
- Item: An item, as defined here, is something which can be obtained in game. It is something that can exist in your inventory. An item can be comprised of a single or multiple meshes [(more on that here)](/Information/Items/Item-RootTemplate)
- Body: In the case of armour files, a body mesh is typically the piece which contains the torso. Body can refer to a shirt, breastplate, or even full top-to-bottom outfit.
- Skirt: A skirt often refers to the bottom, looser part of a piece of armour (or even a shirt). If an armour has physics, it is typically on the skirt.
- Physics: Physics are the way the game attempts to simulate how an object in game should move. In armour, we are typically dealing with cloth physics, which attempt to mimic the movement of fabric. This is accomplished through [vertex painting](/Information/Meshes/Vertex-Painting-Meshes).
- Cloth mesh: When an armour file submesh ends with `_Cloth_Mesh`, this is (with very rare exceptions) the cloth mesh, which is an invisible submesh that gives the game information on how to simulate the cloth physics for the other parts of that armour file.


# Pages

---
### Armour (ARM)
- [Body, Clothing](ARM_Body-Clothing)
- [Body, Light](ARM_Body-Light)
- [Body, Medium](ARM_Body-Medium)
- [Body, Heavy](ARM_Body-Heavy)
- More...

{.links-list}
### Clothing (CLT)
- [Body](CLT_Body)
- [Pants](CLT_Pants)
- [Shoes](CLT_Accessories)
{.links-list}
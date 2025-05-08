---
title: Races
description: Race UUIDs
published: true
date: 2025-05-08T17:10:51.911Z
tags: charactervisuals, races, race, equipmentraces
editor: markdown
dateCreated: 2025-05-08T15:24:52.235Z
---

# Races

## Equipment UUIDs

UUIDs used when assigning equipment in the RootTemplates

# Tabset

## Vanilla Races

| Race | Prefix | UUID | Parent Race |
| --- | --- | --- | --- |
| Dragonborn Female | DGB\_F | 6d38f246-15cb-48b5-9b85-378016a7a78e | HUM\_FS |
| Dragonborn Male | DGB\_M | 9a8bbeba-850c-402f-bac5-ff15696e6497 | HUM\_M |
| Dwarf Female | DWR\_F | b4a34ce7-41be-44d9-8486-938fe1472149 |
| Dwarf Male | DWR\_M | abf674d2-2ea4-4a74-ade0-125429f69f83 |
| Elf/Drow Female | ELF\_F | ad21d837-2db5-4e46-8393-7d875dd71287 | HUM\_F |
| Elf/Drow Female Strong | ELF\_FS | N/A^[\[1\]](#fn1)^ |
| Elf/Drow Male | ELF\_M | 7dd0aa66-5177-4f65-b7d7-187c02531b0b | HUM\_M |
| Elf/Drow Male Strong | ELF\_MS | N/A^[\[1:1\]](#fn1)^ |
| Githyanki Female | GTY\_F | 06aaae02-bb9e-4fa3-ac00-b08e13a5b0fa | HUM\_F |
| Githyanki Male | GTY\_M | f07faafa-0c6f-4f79-a049-70e96b23d51b | HUM\_M |
| Gnome Female | GNO\_F | c491d027-4332-4fda-948f-4a3df6772baa |
| Gnome Male | GNO\_M | 5640e766-aa53-428d-815b-6a0b4ef95aca |
| Half-Elf Female | HEL\_F | 541473b3-0bf3-4e68-b1ab-d85894d96d3e | HUM\_F |
| Half-Elf Female Strong | HEL\_FS | N/A^[\[1:2\]](#fn1)^ |
| Half-Elf Male | HEL\_M | a0737289-ca84-4fde-bd52-25bae4fe8dea | HUM\_M |
| Half-Elf Male Strong | HEL\_MS | N/A^[\[1:3\]](#fn1)^ |
| Half-Orc Female | HRC\_F | eb81b1de-985e-4e3a-8573-5717dc1fa15c | HUM\_FS |
| Half-Orc Male | HRC\_M | 6dd3db4f-e2db-4097-b82e-12f379f94c2e | HUM\_MS |
| Halfling Female | HFL\_F | 8f00cf38-4588-433a-8175-8acdbbf33f33 |
| Halfling Male | HFL\_M | a933e2a8-aee1-4ecb-80d2-8f47b706f024 |
| Human Female | HUM\_F | 71180b76-5752-4a97-b71f-911a69197f58 |
| Human Female Strong | HUM\_FS | 47c0315c-7dc6-4862-b39b-8bf3a10f8b54 |
| Human Male | HUM\_M | 7d73f501-f65e-46af-a13b-2cacf3985d05 |
| Human Male Strong | HUM\_MS | e39505f7-f576-4e70-a99e-8e29cd381a11 |
| Tiefling Female | TIF\_F | cf421f4e-107b-4ae6-86aa-090419c624a5 | HUM\_F |
| Tiefling Female Strong | TIF\_FS | a5789cd3-ecd6-411b-a53a-368b659bc04a | HUM\_FS |
| Tiefling Male | TIF\_M | 6503c830-9200-409a-bd26-895738587a4a | HUM\_M |
| Tiefling Male Strong | TIF\_MS | f625476d-29ec-4a6d-9086-42209af0cf6f | HUM\_MS |

## Custom Races

| Race | Prefix | UUID | Parent Race | Link to Mod |
| --- | --- | --- | --- | --- |
| Hobgoblin Female | HOB\_F | eb81b1de-985e-4e3a-8573-5717dc1fa15c **\*** uses HRC\_F | HRC\_F | [Warlords of the Coast - The Hobgoblin Race](https://www.nexusmods.com/baldursgate3/mods/11530) |
| Hobgolbin Male | HOB\_M | 6dd3db4f-e2db-4097-b82e-12f379f94c2e **\*** uses HRC\_F | HRC\_M | [Warlords of the Coast - The Hobgoblin Race](https://www.nexusmods.com/baldursgate3/mods/11530) |

> **Want your custom race added here?**  
> Send a message [here](https://discord.com/channels/1211056047784198186/1370077003621077154)

## Karlach

| Race | Prefix | UUID | Parent Race |
| --- | --- | --- | --- |
| Tiefling Karlach | \_Karlach^[\[2\]](#fn2)^ | 6326d417-315c-4605-964e-d0fad73d719b | TIF\_FS |

> **Why does Karlach have her own tab?**  
> Karlach has her own unique race UUID, though it only has a few uses in the game^[\[3\]](#fn3)^.
> 
> Some mesh items include replacing areas of skin. Since her skin is different than that of other characters, it requires a different material to be applied to the mesh, so a new object needs to be created for that, and thus she requires her own race UUID.

## Parent Races

WIP

## CharacterVisuals

UUIDs used to assign character creation elements such as heads, horns, hair, etc

# Tabset

## Vanilla Races

| Race | CharacterVisual UUID |
| --- | --- |

## Custom Races

| Race | Prefix | UUID | Parent Race | Link to Mod |
| --- | --- | --- | --- | --- |

---

1.  This race does not have a UUID. The prefix is used for naming heads. [↩︎](#fnref1) [↩︎](#fnref1:1) [↩︎](#fnref1:2) [↩︎](#fnref1:3)
    
2.  `_Karlach` is typically used as a **suffix** on associated meshes. [↩︎](#fnref2)
    
3.  *Reason’s Grasp*, *Bonespike Gloves* and her *Epilogue Camp Outfit* are the only uses of her race UUID. [↩︎](#fnref3)
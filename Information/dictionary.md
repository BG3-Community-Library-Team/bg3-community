---
title: Dictionary
description: test page for a potential bg3 modding dictionary
published: true
date: 2024-08-09T11:25:31.485Z
tags: test
editor: markdown
dateCreated: 2024-06-20T08:31:54.801Z
---

![myconid-cmty-curvy.webp](/test/myconid-cmty-curvy.webp)

[Follow up to this conversation.](https://discord.com/channels/1211056047784198186/1252694850097385472/1252955321887096893)

Intended as a temporary hub for terms that may need to be explained in our work-in-progress dictionary. Very inclined by [this layout](https://eternity.obsidian.net/game-data-formats/concepts), but no decisions were made yet.

BG3 Modding Dictionary
======================

A
-

*   **Anubis** - Larian scripting language.
*   **Attribute (Character Stats)** - Attributes refer to character statistics such as Charisma, Strength, Constitution, etc. These can be modified through various means, including templates, classes, and stats.
*   **Attribute (Template)** - An Attribute in the context of a template defines its characteristics and functionality. For example, `WalkOn = true` allows characters to walk on it, `CanShootThrough = false` makes it impenetrable, and `VisualEntry = "A UUID"` links a VisualBank to a template.

B
-

*   **BG3MM** - [LaughingLeader's Baldur's Gate 3 Mod Manager](https://github.com/LaughingLeader/BG3ModManager).
*   **Boost** - Boosts are similar to buffs or debuffs in other games. They can modify an entity in various ways or be re-utilized to trigger other things with Script Extender.
*   **BootstrapClient** - A script or set of scripts that initialize on the client side when the game starts.
*   **BootstrapServer** - A script or set of scripts that initialize on the server side when the game starts.

C
-

*   **CCAV** - CharacterCreationAppearanceVisuals - A file that assigns visuals to slots in Character Creation such as heads, hairs, horns, etc. Visuals are assigned to particular races, body shapes, and body types.
*   **CCSV** - Character creation shared visuals
*   **CF** - Compatibility Framework.
*   **Client** - The game instance running on a player's machine, handling local rendering and input.
*   **CL** - Community Library.
*   **Class (Coding)** - In coding, a class is a blueprint for creating objects within Object-Oriented Programming (OOP). It defines shared properties and methods of an object you create. For example, a class dedicated to an element/object would outline its properties and the functions available for it.
*   **Class (Game)** - In-game classes determine the abilities and stats a character gains throughout the game. [Here is a guide to creating a custom class](https://wiki.bg3.community/en/Tutorials/Classes/Basic-Class-Creation).
*   **CLEA** - DDS file, stores Curvature, Lips, Eyebrows, and Ambient Occlusion (AO)
*   **CMTY** - Community / BG3 Modding Community.

D
-

*   **Dump** - Extracting game data for analysis or modification.

E
-

*   **Enumeration (Enum)** - Enumerations, or Enums, are lists of named constants representing component types, such as WeaponType. Each type can also be associated with a number, allowing it to be referenced by name or number, e.g., (None, 0), (Sword, 1), (Club, 2). [(Here is a list of possible Enumerations available to us via Script Extender)](https://github.com/Norbyte/bg3se/blob/1b96b0824bd541933219226d48279c89635dba44/BG3Extender/GameDefinitions/Enumerations.inl).
*   **Entity** - Any object in the game world, including characters, items, and environmental objects.
*   **Entity Dump** - A comprehensive list of all properties and attributes of an entity, useful for debugging and modding.

F
-

*   **Framework** - A structured foundation for developing mods, often providing essential functions and utilities.

G
-

*   **GUID** - Globally Unique Identifier, a unique reference number used as an identifier in software.

H
-

*   **Handle** - A reference to an object or entity in the game, often used in scripting.
*   **HMVY** - DDS file, stores the Hemoglobin, Melanin, Veins, and Yellowing

I
-

*   **IDE** - Integrated Development Environment, a software application that provides comprehensive facilities to computer programmers for software development.
*   **IF** - Inspiration Framework.

J
-

*   **JSON** - JavaScript Object Notation, a lightweight data interchange format that's easy for humans to read and write and easy for machines to parse and generate.

K
-

*   **Keybind** - A keyboard shortcut that allows a player to perform a specific action in the game.

L
-

*   **Load order** - The sequence in which mods are placed in BG3MM and Vortex.
*   **Loca** - Localization files containing translations for different languages.
*   **Lua** - Programming language used for Script Extender.
*   **Lsf** - Larian's proprietary file format for various game data.
*   **Lsx** - Larian's XML-based file format for game data.

M
-

*   **Meta** - Metadata or data about data, often used to refer to information about a mod or file.

N
-

*   **NM** - Normal Map, DDS file, stores directional data used to fake depth on objects
*   **Norbsearch** - [BG3 Search Engine](https://bg3.norbyte.dev/) by Norbyte.
*   **Notepad++** - Open source code editor and replacement for Notepad, commonly used by the community.

O
-

*   **OF** - Oath Framework.
*   **OOP (Object-Oriented Programming)** - Object-Oriented Programming is a programming paradigm that structures code using objects, which are instances of classes. It defines elements/objects, their properties, and functions. [Here is a brief introduction to OOP with more information](https://wiki.bg3.community/en/Tutorials/ScriptExtender/the_basics_of_lua).
*   **Osiris** - Larian scripting language.

P
-

*   **Passive** - A passive ability provides a continuous effect (Boost) as long as it is activated on the passive hotbar.

Q
-

*   **Quest** - A task or series of tasks that a player completes for rewards.

R
-

*   **REL** - Random Equipment Loot.

S
-

*   **Shared folder** - Folder that contains your Localization, Mods, and Public folder.
*   **Server** - The game instance that manages the game world and game state, often running on a remote machine.
*   **Stats** - Various attributes linked to a GameObject-Template, typically defined in a text file. Examples include the attributes an item grants, its weight, and the slot it occupies (e.g., Gloves).

T
-

*   **Template** - A template is a fundamental building block in the game, composed of various attributes. It can also inherit attributes from a parent template, building on its properties or overriding a specific attribute if the child has a new value for it.
*   **TreasureTable** - Determines what items a container or vendor might have. A TreasureTable would be registered in the container/entity's GameObject-Template as a new child node "InventoryList". (Use Norbsearch to look up an existing container to find out how.)

U
-

*   **UUID** - Universally Unique Identifier, a 128-bit value used in the game files to identify an object or entity by its unique 36-character format. Example: `000cfc9f-b973-48e7-a5c8-f2992a47a943`.

V
-

*   **Vortex** - Nexusmods' Mod Manager.
*   **Visual bank entry** - A reference to a visual asset in the game.
*   **Visual Studio Code (VSCode)** - Free code editor created by Microsoft. Commonly used in the community, with several extensions available specifically for BG3 modding.
*   **Visual Studio Codium (VSCodium)** - An open source version of VSCode.

W
-

*   **Workspace** - A project setup in a development environment that includes all files and settings related to a specific mod or group of mods.

X
-

*   **Xml** - Extensible Markup Language, markup language and file format for storing, transmitting, and reconstructing arbitrary data, both human-readable and machine-readable.

Y
-

*   **YAML** - Yet Another Markup Language, a human-readable data serialization format.

Z
-

*   **Zip** - A compressed file format used to package mod files for distribution.

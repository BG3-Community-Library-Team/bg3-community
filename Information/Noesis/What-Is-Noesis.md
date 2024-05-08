---
title: What is Noesis
description: An explanation to what Noesis is for the uninitiated
published: false
date: 2024-05-08T19:15:44.788Z
tags: 
editor: markdown
dateCreated: 2024-05-08T19:15:44.788Z
---

# What is Noesis?
Noesis, or noesisGUI, is a middleware solution that provides a highly customisable User Interface (UI) using XAML files written in a XML-based language. The language is structually similar to WPF, but implements unique methods to implement new features for gameplay, rather than a Windows environment.

Now, if most of that didn't make sense - take a look at this lovely diagram:
![overview3.png](/overview3.png)
Add/edit visual assets, layouts, interactions and animations into the game - it's all loaded into the Game Engine at runtime, taking roughly <2ms.
## What is possible in Noesis?
The user interface sits in its own "layer" above the game, between the player and the game engine. If you want to turn the game into one big photo of Astarion/your favourite companion, you *can* - but we can do a lot more:
<img src=https://staticdelivery.nexusmods.com/mods/3474/images/7428/7428-1709504693-1605183470.jpeg>
Example from [UI Dialogue Framework](https://www.nexusmods.com/baldursgate3/mods/7428) - Hidden UI buttons, increased text size, different colours, white border for text. Also - the font can be changed, the text appearing can be animated, and additional text can be added!

## What is not possible in Noesis?
- Some of the Engine data is made available to the UI via Data context - either via a one-way or two-way street. This means that some parts of the game can be amended in the UI (appearance options), some parts of the game can be shown in the UI but not directly amendable (current health) and some parts are not available to interact with at all (character animations).
- *Currently*, there is no communication between the UI and scripting - you can't add a button to the game, that fires a lua script.
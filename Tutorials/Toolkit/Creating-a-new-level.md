---
title: Creating a new level
description: Small guide that covers basics of level creation
published: true
date: 2025-10-22T20:41:07.401Z
tags: 
editor: markdown
dateCreated: 2025-10-17T12:50:22.826Z
---

# WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP WIP 
## Overview 

This level creation guide aims to cover all the basic knowledge that you need to know to be able to create some basic levels. It was written for Virtual photography/Screenarchery in mind. It doesn't cover things that you need to know to create actual gameplay levels

Please let me know if there are useful tips, keybinds,and other simplifications

## Project setup

First you `Create` a new project,

![placeholder](image-2.png)

name it however you want, and then press `Create`. I'm going for LevelGuide

![placeholder](image-5.png)

After some time, the toolkit will finally open `Level browser`, where you also press `Create` to create a new level

![placeholder](image-4.png)

Name the new level. As a good habit you should follow some sort of a naming convention. Me personally uses Larian one, but instead of Region name (like WLD_Main_A, SCL_..., BGO_...) in the begining, I use `ProjectName_LevelName`, so it would `LG_MyNewPrettyLevel`

![placeholder](image-6.png)

And press `Create` one more time

## Placeholder

In this guide, I'm going to use this UI layout

![placeholder](image-13.png)


Hide or close `Message log` [1] and open `Resource Manager` [2]

![placeholder](image-7.png)

Drag `Root Templates` to the bottom

![placeholder](image-11.png)

Drag `Resource Manager` next to `Root Templates` 

![placeholder](image-12.png)

And save it 

![placeholder](image-14.png)

This one does make sense for me, but of course, you can use your layout
![placeholder](image-13.png)


If you closed a window by accident, you can eiter `Reset Layout` or go to `View`

![placeholder](image-16.png)

## Settings

Maybe 



## Controls

There are some important keybinds:
1. `WASD` for the camera movement
1. `QE` for moving the camera up or down
1. `Scroll up/down` to move the camera forward/backward
1. `Shift`/`Ctrl` speeds up/slows down the camera
1. `1` for the Pointer, `2` to Translate, `3` to Rotate, `4` to Scale objects
1. `C` to deselect object
1. `Ctrl + Alt + S` to Save everything
1. And of course basic keybinds like `Ctrl + C/V`, `Delete`, etc

To change initial camera speed, go to `Editor Camera Settong`

![placeholder](image-15.png)
                            
Small tip: you can use `Scroll` keybind with `Shift` + `WS` to "speed up" the camera even more without changing intial camera speed


## UI

### Top bar

![placeholder](image-18.png)

I'm not going to cover all the basic buttons (you can hover over them to see the tooltips) and Editor buttons; the options you need are

1. `Terrain panel` - to create or paint terrain
1. `AI Grid` - to create walkeable areas
1. `Instances` - to paint with vegitation and other objects
1. `Atmospehere panel` - to edit Lighting and Atmosphere

### The windows
1. `Resource Manager` is where all game meshes/textures/sounds/materials are located

    ![](2025-10-17-15-26-26.png)

1. `Root Templates` and its `Preview` is where all "interactable" objcets are located
    
    ![](2025-10-17-15-28-06.png)

    Basically, the difference between `Resource Manager` resources and `Root Templates` ones is that before you can place an object on the level, you need to create a `RootTemplate` for it; you create your level using `RootTemplates`. You can't just drag and drop an object from `Resource Manager`

    Further in the guide I will refer to `RootTemplate` as `Object` or vice versa



2. `Sidebar` is where all selected object's parameters are

    ![](2025-10-17-15-29-30.png)


2. `Outliner` is a list with all placed objects on the level

    ![](2025-10-17-15-30-28.png)


### Additional objcet controls

At the bottom you can also see: `Pos: x y z`, `Rot: x y z`, `Scale XYZ`, and their differen modes. These also allow you to manipulate over selected object. Hover over the modes to see the tooltips
![placeholder](image-19.png)



## Root Templates
There are some `RootTemplate` types. The only ones you need:

`item` (orange barrel)
`scenery` (green tree)
`lightProbe` (shiny sphere)
`TileConstruction` (two red bricked walls)
`Prefab` (P)
`Trigger` (blue oulined box)
`fogVolume` (misty spehere)
`light` (bulb)
`character` (purple Astarion)

Resource Manager
    Types

Creating objects
    Item/scenery/prefab - chair - position - sidebar
    Fog volume

Terrain
    Size
    Brush - Parameters
    TerrainTextures
    TerrainTextures mixing

Instances
    Brush - Parameters
    IPs

Atmosphere panel
    Triggers
    Modes
    Lighting
    Atmosphere
    LightProbe
    LightyLights support

Other triggers
    Start point
    AiSeeder

Interaction mode options 


AI grid


"Recolor" of RootTemplates/VisualResources
    VisualResource
    Material
    RootTemplate

VisualResources as RootTemplates
    Batch convert with the tool

New IPs, TTs

How to delete the level






---
title: Creating a new level
description: Small guide that covers basics of level creation
published: true
date: 2025-11-02T22:20:32.234Z
tags: 
editor: markdown
dateCreated: 2025-10-17T12:50:22.826Z
---

# WIP
## Overview

This level creation guide aims to cover all the basic knowledge that you need to know to be able to create some basic levels. It was written for Virtual photography/Screenarchery in mind. It doesn't cover things that you need to know to create actual gameplay levels

Please let me know if there are useful tips, keybinds,and other simplifications


Some sections were copied from Larian's wiki https://docs.larian.game/ because they have a better explanation

## Project setup

First you `Create` a new project,


![creating-a-new-level-create-project.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-create-project.webp)

name it however you want, and then press `Create`. I'm going for LevelGuide


![creating-a-new-level-5-project-name.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-5-project-name.webp)

After some time, the toolkit will finally open `Level browser`, where you also press `Create` to create a new level

![creating-a-new-level-6-create-level.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-6-create-level.webp)

Name the new level. As a good habit you should follow some sort of a naming convention. Me personally uses Larian one, but instead of Region name (like WLD_Main_A, SCL_..., BGO_...) in the begining, I use `ProjectName_LevelName`, so it would `LG_MyNewPrettyLevel`
And press `Create` one more time

![creating-a-new-level-7-name-level.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-7-name-level.webp)



## UI

In this guide, I'm going to use this UI layout
It makes sense for me, but of course, you can use your own

Drag `Root Templates` to the bottom on `Message log` 
Open `Resource Manager` and drag it near the `Root Templates` window

![creating-a-new-level-13-ui.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-13-ui.webp)

Save it

![creating-a-new-level-14-save-ui-2.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-14-save-ui-2.webp)

If you closed a window by accident, you can eiter `Load Layout`, `Reset Layout` or go to `View` and re-open it there

## Settings

Maybe 



## Controls

There are some important keybinds:
1. `WASD` for the camera movement
1. `QE` for moving the camera up or down
1. `Scroll up/down` to move the camera forward/backward
1. `Shift`/`Ctrl` speeds up/slows down the camera
1. `1` for the Pointer, `2` to Translate, `3` to Rotate, `4` to Scale objects, '5' to enable Create object on click
1. `C` to deselect object
1. `Ctrl + Alt + S` to Save everything
1. And of course basic keybinds like `Ctrl + C/V`, `Delete`, etc

There are a loooooot more kebinds that you can use, they are located in `Preferences`. I highly suggest utilizing them




To change initial camera speed, go to `Editor Camera Settong`

![creating-a-new-level-15-camera-speed.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-15-camera-speed.webp)

                            
Small tip: you can use `Scroll` keybind with `Shift` + `WS` to "speed up" the camera even more without changing intial camera speed


## UI

### Top bar

![creating-a-new-level-18-top-bat.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-18-top-bat.webp)

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


![creating-a-new-level-19-add-controls.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-19-add-controls.webp)




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

### item
Basically it's an object you can interact with: shells, plates, food, gems, etc. It's not completely true, but it's just easier to explain (some sceneries and items can intersect)

### scenery
It's an object you can't interact with: rocks, plants, trees, shelves, etc. (some sceneries and items can intersect)

### lightProbe
The game doesn't have any form of dynamic global Illumination, so Larian use LightProbe to capture hdri map around it self and then calculate inderect lighting

There are 2 types of light probes:

1. Distant probes are used to account for far away lighting information: the sun and sky.
It uses the information of the surrounding atmosphere to apply an approximation of sun and sky light bouncing and color to everything in that atmosphere.
Since the probe contains lighting information, it applies to everything in that LightingResources. You only need one distant probe per Lighting trigger.
2. Local probes are used to simulate color and reflections related to nearby lights and objects.
Local probes only gather information within a defined area around them and thus, only apply to objects in that same area.
Contrary to distant probes, you can place as many local probes as you want. Even probes inside other probe areas are allowed.
The lighting of the smallest probes always gets priority over the lighting of a larger probe that covers the same area. With local probes, you fine-tune illumination and reflections where the distant probe, or a larger local probe proves to be insufficient.

Since I make levels mostly for one picture, I always use `Distant` one and then move it around to tune the lighting for my needs

Whenever you make changes with a probe, you need to save your level in order for the `LightProbe` to save the rendered `"HDRi"` maps
!!! If you have a lot of `LightProbes`, *EACH* `LightProbe` will render the map for *EACH* `LightingResources` in the trigger, so rendering will take some time !!!
You should mainly focus on 1-4 `LightingResources`, and when you are finished with the level, only then add additional `LightingResources`, and make the final render

### TileConstruction
You build walls, roofs, floors, and other repetitve things with this thing

### Prefab
A saved group of objects. You can create and decorated a furnace using different objects and then save it as Prefab to reuse the whole thing again

### Trigger
In our case we only need two:
1. `LightingTrigger` sets `LightingResources` for current trigger area
1. `AtmosphereTrigger` sets `AtmosphereResources` for current trigger area
1. `StartPoint` sets starting point when you appear on the level
1. Maybe `` #crowd
1. Maybe 

### fogVolume
You can create fog areas with this thing

### light
Just a light
Most of you probably using Lighty Lights, but you can place then to preview the lighting

### character
I only use Astarion for size reference

#### Sources                           
https://docs.larian.game/Entity_types
https://docs.larian.game/My_first:_Item
https://docs.larian.game/Light_probes (In BG3 Larian split Atmosphere to Atsmosphere and Lighting)

## Resource Manager
There are a lot of types. The only ones you need:
`Visual` (utah teapot)
`Texture` (missing texture sphere)
`Material` (blue spehere)
`Effect` (sparkles)
`Lighting` (bulb)
`Atmospehere` (sun with face)
`Terrain Brush` (a brush and a mountain)

### Visual
Meshes and stuff

### Texture
Textures

### Material
Materials

### Lighting
A resource that contains Lighting parameters: sun/moon position, sun/moon color, fog, etc

### Atmospehere
A resource that contains Atmospehere parameters: overall color correction, light shafts, different effectrs environmental effects (like rain, ashes, etc), etc

### Terrain Brush
A resource, "similar" to a material, that you use to paint terrain


## The tools

There are 5 main tools:
1. `Pointer/Cursor` - you select things with it
1. `Translate` - you move things with it
1. `Rotation` - you rotate things with it
1. `Scale` - you scale things with it
1. `Create` - you create/place things with it

Each tool has a lot of different parameters, you can access them by right clicking on a tool
For example, you can eanble `Snap to grid` for `Translate`, enable random rotation or scale for `Create`, and so on

## Finally placing objects to unleash your abstract vision

Enable `Create` tool, which allows you to create objects on click (`5` keybind), without dragging them from the `Root Temlates` window

![creating-a-new-level-12-place-tool.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-12-place-tool.webp)

Then find an object in `Root Templates` and place it by clicking on terrain
You can also hold left mouse button to rotate the object before placing it

![creating-a-new-level-place-object.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-place-object.webp)

Now you can move it however you want by selecting it and using the keybinds I mentioned earlier
![creating-a-new-level-place-object.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-move-object.webp)



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






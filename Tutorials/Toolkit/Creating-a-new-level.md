---
title: Creating a new level
description: Small guide that covers basics of level creation
published: true
date: 2025-12-01T16:19:48.899Z
tags: 
editor: markdown
dateCreated: 2025-10-17T12:50:22.826Z
---

# WIP
## Overview

This level creation guide aims to cover all the basic knowledge that you need to know to be able to create some basic levels. It was written for Virtual photography/Screenarchery in mind. It doesn't cover things that you need to know to create actual gameplay levels.

Please let me know if there are useful tips, keybinds,and other simplifications.


Some sections were copied from Larian's wiki https://docs.larian.game/ because they have a better explanation.

## Project setup

First you `Create` a new project,


![creating-a-new-level-create-project.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-create-project.webp)

Name it whatever you want, and then press `Create`. I'm going for LevelGuide.


![creating-a-new-level-5-project-name.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-5-project-name.webp)

After some time, the toolkit will finally open `Level browser`, where you also press `Create` to create a new level.

![creating-a-new-level-6-create-level.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-6-create-level.webp)

Name the new level. As a good habit you should follow some sort of a naming convention. I personally use Larian's, but instead of Region name (e.g. WLD_Main_A, SCL_, BGO_) in the begining, I use `ProjectName_LevelName`, or something like `LG_MyNewPrettyLevel`. 

Once you name your level, press `Create` one more time.

![creating-a-new-level-7-name-level.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-7-name-level.webp)



## UI

In this guide, I'm going to use this UI layout.
It makes sense for me, but of course, you can use your own.

Drag `Root Templates` to the bottom on `Message log`, open `Resource Manager`, and drag it near the `Root Templates` window

![creating-a-new-level-13-ui.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-13-ui.webp)

Save it

![creating-a-new-level-14-save-ui-2.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-14-save-ui-2.webp)

If you closed a window by accident, you can eiter `Load Layout`, `Reset Layout` or go to `View` and re-open it there.

You can also drag windows outside of the toolkit (this might make it easier to see things if you have multiple screens). However, they will end up re-docked when you reopen the toolkit. 

## Settings

Maybe 



## Controls

There are some important keybinds:
1. `WASD` for the camera movement.
1. `QE` for moving the camera up or down.
1. `Scroll up/down` to move the camera forward/backward.
1. `Shift`/`Ctrl` speeds up/slows down the camera.
1. `1` for the Pointer, `2` to Translate (move), `3` to Rotate, `4` to Scale objects, '5' to enable Create object on click.
1. `C` to deselect object.
1. `Ctrl + Alt + S` to Save everything.
1. And of course basic keybinds like `Ctrl + C/V`, `Delete`, etc.

There are a loooooot more keybinds that you can use, they are located in `Preferences`. I highly suggest utilizing them.




To change initial camera speed, go to `Editor Camera Setting`.

![creating-a-new-level-15-camera-speed.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-15-camera-speed.webp)
Different camera modes

*You can use `Scroll` keybind with `Shift` + `W/S` to "speed up" the camera even more without changing intial camera speed*.

## UI

### Top bar

![creating-a-new-level-18-top-bat.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-18-top-bat.webp)

I'm not going to cover all the basic buttons (you can hover over them to see the tooltips) and Editor buttons; the options you need are:

1. `Terrain panel` - to create or paint terrain.
1. `AI Grid` - to create walkeable areas.
1. `Instances` - to paint with vegitation and other objects.
1. `Atmospehere panel` - to edit Lighting and Atmosphere.

### Windows
1. `Resource Manager` is where all game meshes/textures/sounds/materials are located.

	![creating-a-new-level-22-ui-resource-manager.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-22-ui-resource-manager.webp)

1. `Root Templates` and its `Preview` is where all "interactable" objcets are located.

    ![creating-a-new-level-22-ui-root-templates.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-22-ui-root-templates.webp)


	Basically, the difference between `Resource Manager` resources and `Root Templates` ones is that before you can place an object on the level, you need to create a `RootTemplate` for it; you create your level using `RootTemplates`. You can't just drag and drop an object from `Resource Manager`.

    Further in the guide I will refer to `RootTemplate` as `Object` or vice versa.



1. `Sidebar` is where all selected object's parameters are.

	You can see parameters for selected `RootTemplate` in either the `Root Template` window or in the level/`World Outliner` window. Changing parameters for selected `RootTemplate` in the window will change them globaly for all `RootTemplates` on the level; changing parameters for selected `RootTemplate` on the level or `World Outliner` will change them for selected `RootTemplate` only.

	![creating-a-new-level-23-ui-sidebar.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-23-ui-sidebar.webp)

1. `World Outliner` is a list with all placed objects on the level.

	![creating-a-new-level-24-ui-outliner.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-24-ui-outliner.webp)


### Additional object controls

In the bottom right corner, you'll also see more ways to manipulate selected objects with `Pos: X Y Z`, `Rot: X Y Z`, and `Scale XYZ`, plus toggles for different modes (hover over them to see tooltips). You can use these tools to manipulate selected objects more precisely: for example, you can easily rotate an object by typing the new angle (e.g. 90 for 90 degree) in the `Rot: Y` box.


![creating-a-new-level-19-add-controls.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-19-add-controls.webp)




## Root Templates
There are several `RootTemplate` types. The ones you need to know:

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
Basically an object you can interact with: shells, plates, food, gems, etc. It's not completely true, but it's just easier to explain (some sceneries and items can intersect).

### scenery
An object you can't interact with: rocks, plants, trees, shelves, etc. (some sceneries and items can intersect).

### lightProbe
The game doesn't have any form of dynamic global Illumination, so Larian uses `LightProbe` to capture `HDRI` map around itself and then calculate and "bake" indirect lighting.

There are 2 types of light probes:

1. Distant probes are used to account for far away lighting information: the sun and sky.
It uses the information of the surrounding atmosphere to apply an approximation of sun and sky light bouncing and color to everything in that atmosphere.
Since the probe contains lighting information, it applies to everything in that LightingResources. You only need one distant probe per Lighting trigger.
2. Local probes are used to simulate color and reflections related to nearby lights and objects.
Local probes only gather information within a defined area around them and thus, only apply to objects in that same area.
Contrary to distant probes, you can place as many local probes as you want. Even probes inside other probe areas are allowed.
The lighting of the smallest probes always gets priority over the lighting of a larger probe that covers the same area. With local probes, you fine-tune illumination and reflections where the distant probe, or a larger local probe proves to be insufficient.


Since I make levels mostly for one picture, I always use `Distant` one and then move it around to tune the lighting for my needs.
You should use `Local` for interiors and stuff, or to adjust some specific parts.

> A level has to have at least one `Distant` one
{.is-warning}

Not going to explain each parameter, they all have a tooltip in the `Sidebar`, just read them.

> Do not edit `Intensity`. I think it does nothing in the actual game, haven't really tested though
{.is-warning}

Don't forget that you can also change its size using `Edit shape bounds tool` (square with dots with a rhombus shaped square inside) in the tool bar

To render them, you need to select `LightProbe` and toggle forth and back `Inifinite Capture` or `Enabled` (I haven't figure out a better consistent way) to update the lighting; you should see the changes immediately, and then you just save your level.



The difference between level with correctly rendered `LightProbes` and one with incorrectly rendered:

> Incorrect
![creating-a-new-level-21-light-probe-diff.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-21-light-probe-diff.webp)
{.is-danger}

> Correct
![creating-a-new-level-21-light-probe-diff.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-20-light-probe-diff.webp)
{.is-success}

You can see that on incorrect one, there's no indirect lighting (harsh shadows).

> Whenever you make changes with a probe, you need to save your level in order for the `LightProbe` to save the rendered `HDRI` maps
!!! If you have a lot of `LightProbes`, *EACH* `LightProbe` will render the map for *EACH* `LightingResources` in the `LightingTrigger`, so rendering will take some time !!!
You should mainly focus on 1-4 `LightingResources`, and when you are finished with the level, only then add additional `LightingResources`, and make the final render.
{.is-warning}

https://docs.larian.game/Light_probes (In BG3 Larian split Atmosphere to Atmosphere and Lighting)

### TileConstruction
You build walls, roofs, floors, and other repetitive things with this thing.

### Prefab
A saved group of objects. You can create and decorate a furnace using different objects and then save it as Prefab to reuse the whole thing again.

### Trigger
In our case we only need two:
1. `LightingTrigger` sets `LightingResources` for current trigger area.
1. `AtmosphereTrigger` sets `AtmosphereResources` for current trigger area.
1. `StartPoint` sets starting point when you appear on the level.
1. Maybe `` #crowd.
1. Maybe .

### fogVolume
You can create fog areas with this thing.

### light
Just a light.
Most of you probably use Lighty Lights, but you can place then to preview the lighting.

### character
I only use Astarion for size reference.

### LevelTemplate

Saves the whole level as a `RootTemplate` that you can paste on any other levels

### Important
> Each of these `RootTemplate` types has different additional tools.
For example: if you click on a trigger that has its `Physics Shape` set to Sphere or Box, you can change size of it using `Edit shape bounds tool`. Or if you click on a `LevelTemplate` it will show you `Edit LevelTemplate` button
{.is-info}



#### Sources                           
https://docs.larian.game/Entity_types
https://docs.larian.game/My_first:_Item


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
Meshes and stuff.

### Texture
Textures.

### Material
Materials.

### Lighting
A resource that contains Lighting parameters: sun/moon position, sun/moon color, fog, etc.

### Atmosphere
A resource that contains Atmospehere parameters: overall color correction, light shafts, different effectrs environmental effects (like rain, ashes, etc), etc.

### Terrain Brush
A resource, "similar" to a material, that you use to paint terrain.


## The tools

There are 5 main tools:
1. `Pointer/Cursor` - you select things with it.
1. `Translate` - you move things with it.
1. `Rotation` - you rotate things with it.
1. `Scale` - you scale things with it.
1. `Create` - you create/place things with it.

Each tool has a lot of different parameters, you can access them by right clicking on a tool.
For example, you can eanble `Snap to grid` for `Translate`, enable random rotation or scale for `Create`, and so on.

## Finally placing objects to unleash your abstract vision

Enable `Create` tool, which allows you to create objects on click (`5` keybind), without dragging them from the `Root Temlates` window.

![creating-a-new-level-12-place-tool.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-12-place-tool.webp)

Then find an object in `Root Templates` and place it by clicking on terrain.


*You can also hold left click to rotate the object before placing it*.

![creating-a-new-level-place-object.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-place-object.webp)

Now you can move it however you want by selecting it and using the keybinds I mentioned earlier.
![creating-a-new-level-place-object.webp](/tutorials/toolkit/creating-a-new-level/creating-a-new-level-move-object.webp)

*You can make `Sidebar` inactive by opening a different window (I always open `Atmosphere panel`), so you can scroll through the list of objects with arrow keys faster.
(Basically whenever you select an object, you also load all its parameters in `Sidebar`, by making `Sidebar` inactive, you stop 	loading the parameters)*.


## Terrain
Size
Brush - Parameters
TerrainTextures
TerrainTextures mixing

## Instances
Brush - Parameters
IPs

## Atmosphere panel
Triggers
Modes
Lighting
Atmosphere
LightProbe
LightyLights support

## Other triggers
Start point
AiSeeder

## Interaction mode options 


## AI grid


## "Recolor" of RootTemplates/VisualResources
VisualResource
Material
RootTemplate

## VisualResources as RootTemplates
Batch convert with the tool

## New IPs, TTs

## How to delete the level






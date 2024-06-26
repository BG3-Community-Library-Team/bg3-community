---
title: Technical skills I
description: Exploring Otis’ camera tool and ReShade to enhance your captures. (Beginner)
published: false
date: 2024-06-26T23:28:51.500Z
tags: guide, wip, screen archery
editor: markdown
dateCreated: 2024-06-24T20:54:56.738Z
---

## Exploring Otis camera tool and ReShade to enhance your captures. (Beginner)

![soon_tm.webp](/test/alithea/soon_tm.webp)
INTRO

### Overview
> - **What to Install**
> 	- Download and setup of main tools needed to start
> - **Depth of Field**
> 	- What is DOF
>   - Disable default DOF
>   - Using IgcsDOF
> - **DisplayDepth & DepthDarkness**
> 	- How to setup DisplayDepth first
> 	- Using Depthdarkness



### What to install
- Otis_inf Camera tool: https://www.patreon.com/Otis_Inf/posts
- Reshade: https://reshade.me/
	- Download version reshade with full add-on support
		- Install reshade, choose the bg3 exe you're using (vulcan or directx)
		- Select the shaders to start with, I suggest the following to start:
    (insert image)
- IGCS DOF Plugin: https://www.patreon.com/posts/igcs-depth-of-87670650 and unpack
	- Place the Igcsconnector.addon64 in the same folder as bg3.exe is located
	- Place Shaders\IgcsDof.fx in the folder reshade-shaders\Shaders
	- Place Textures\monochrome_gaussnoise.png in the folder reshade-shaders\Textures
--> I'll prob leave out all the install info, because that info is available at download locations and can change

### Depth of Field
--> introduction to depth of field? maybe in previous steps so can be linked?
- Disable In game DOF: If the in game DOF is still enabled, you will not be able to take all your shots as certain angles will appear blurry
-> insert example
- To prevent this set Depth of Field to None
- And set Anti-aliasing to TAA to prevent issues later on when using shaders
-> screenshot game menu

### Using IgcsDOF --> prob place this under Depth of Field
- Because DOF in game has been disabled, you will now have to setup your own depth of field when taking screenshots
- Open the reshade overlay by pressing the home button -> change the default key in the settings tab because home is also used by the camera tool to block camera movement
- You'll see a list of shaders that can be selected
- For now search for igcsDOF and select it
--> insert screenshot of reshade window

- Now setup a shot, lock the camera with home and pause the game
- Go to Add-Ons tab and open IGCS Connector
--> screenshot add-ons tab

- Use this guide https://opm.fransbouma.com/igcsdof.htm to setup your DOF for the shot
	- There's now an extra option 'frame wait type' -> if you use FAST make sure Number of frames to wait is set to 1 or everything will appear blurry. I still use Classic mostly.


- If you like the shot, you can screenshot it with PrtScn 
--> this can be changed - maybe I'll use 'screenshot hotkey'
- Folder settings for screenshot can be changed in the settings tab

--> add example without IgcsDOF and example screenshot with IgcsDOF







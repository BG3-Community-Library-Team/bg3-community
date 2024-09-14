---
title: Creating a Custom Head and Preset - For Beginners 
description: In this tutorial I will show you how to create your own head and preset for the BG3 Character Creator.
published: false
date: 2024-09-14T11:50:29.519Z
tags: tutorial, head, preset
editor: markdown
dateCreated: 2024-09-14T11:50:29.519Z
---

# Introduction
Hello everyone, I created this tutorial because I wished I had something like this when I 
started out.

It is primarily aimed at those who have no experience with modding tools or Blender, but 
still want to create their own head with the corresponding preset.
All the tools and files, whose names you probably don't know yet, might seem quite 
intimidating at first glance, but don’t worry—I’ll try to explain everything as clearly as 
possible.

I also only discovered 3D modding through Baldur's Gate 3 and had zero experience with 
Blender before that. If I managed to do it, you can too.
This tutorial will include both text and video segments. I will usually describe a specific 
process in writing first and provide some screenshots, and at the end, there will be a brief 
video summary.

I hope this approach will reach as many people as possible, as some prefer PDF tutorials 
and others prefer video tutorials.
The video sections are marked with a little playbutton symbol so keep an eye out for it. However, 
I recommend reading everything first and then watching the video. The video does not 
include any spoken words or text overlays explaining everything again; it simply shows what 
I have already explained in writing.

Additionally, I want to mention that English is not my native language. Nevertheless, I hope 
you understand everything. I had some paragraphs reviewed by ChatGPT, but even AI isn't 
always reliable.
# Tools – Where to get them and how to install them
Note: 
- please install Modders-Multitool and Lslib before Blender


Baldur’s Gate 3 Toolkit (on Steam)
---

What do we need this for? We need it to..
- get our head, preset into the game 
You can find instructions for installing the kit here: https://mod.io/g/baldursgate3/r/installing-the-toolkit.

Lslib
---

What do we need it for? We need it to … 
- we don’t need the tool itself, but the divine.exe. This exe allows us to use a specific 
plugin for Blender. 

Modders-Multitool
---

What do we need it for? We need it to … 
- unpack the game files 
Here is a video that shows you how to install the Modders-Multitool 
AND Lslib: https://www.youtube.com/embed/b1a_LO5tDnQ?feature=oembed


Blender 3.6
---

“Blender is the free and open source 3D creation suite.”
What do we need it for? We need it to ...
- edit our head mesh 

Blender Addons we need: 
BG3/DOS2 Collada Exporter for Blender 3.6 by Norbyte 
Normal Map Transfer by Padme4000
BG3 Head Order by Padme4000

Here is a video that shows you how to install Blender and the associated addons:
https://www.youtube.com/embed/GVonU07kecE?feature=oembed

Here is a video that shows you how to set up the previously installed BG3/DOS2 Collada 
Exporter for Blender 3.6: https://www.youtube.com/embed/b1a_LO5tDnQ?feature=oembed
# Resources
Before we begin editing, we first need to gather our resources, which can be located using the Modder's Multitool. But what resources do we actually need? 

We’ll need: 
•	our head mesh (.GR2 file format)
•	our head’s skeleton (.GR2 file format) 
•	a body mesh (.GR2 file format) 
•	our heads textures (.dds file format)

To access all of these files, please do the following:
1. Open the Modder’s-Multitool 
2. Click on Utilities -> Index -> Index Game Files 
3. The program should now start indexing the game files
4. Let the program finish indexing 
5. Now you need to search for a head mesh you want to edit. Here you'll find all head presets listed with their file names:
https://wiki.bg3.community/Information/Meshes/Head-Meshes-Reference


BT1 and BT2 refer to body type 1 and 2, meaning the standard female and male bodies. BT4 and BT3 are the muscular body types, respectively.

Choose one that you like and copy the file name. For this tutorial, I will use HUM_M_NKD_Head_H.

6. go back to the Modders-Multitool, click on search index 
7. A new windows, named Index Search, will open. Paste your file name into the search bar 
8. Open the dropdown menu next to the search file button and select “gr2” only. This way, we ensure that textures and other files are not displayed. 
9. Now click on “Search Files”. You’ll see this:
![bild1.png](/bild1.png)
10. Now you might be wondering, which of the two files do we need? We actually need both. The file located in the "Generated" folder is our head mesh, which we will edit later. The file in the "Public" folder, with "Base" at the end of its name, serves as the "skeleton" of our head. Don't worry, we won't need to edit this one; we'll simply import it later.
11. Now hover over the first entry until a model appears on the right-hand side.
![bild2.png](/bild2.png)
12. Right next to the file path, you'll see a small folder icon. Please click on it.
13. A folder named “Resources” will open containing our .GR2 file. Copy this file to your desktop or any folder of your choice. I’ll be placing mine in my tutorial folder.
14. Now go back to the Index Search window and do step 11 - 13 for the second entry (our head’s skeleton). 

Note: This time, no mesh will appear on the side. Instead, you'll see the message "1: No lines found; search returned filename only."

Now we still need the textures and the body mesh. Since the textures and our head have the same name, we’ll start by locating the textures.

15. So, go back to your Index Search. This time, instead of searching for .gr2 files, look for .dds files.
16. You should now see either 3 or 4 entries, depending on the head.

These are the textures we can edit later... but it’s not mandatory. 
For now, we’ll extract them in the same way as we did with the mesh and copy them to the desktop or any folder of your choice. The process is the same.

17. Since the textures are in the same folder, you can hover over each of the three files first. Then, click on the folder icon and copy them out.
![bild3.png](/bild3.png)
![bild4.png](/bild4.png)
![bild5.png](/bild5.png)
![bild6.png](/bild6.png)
![bild7.png](/bild7.png)

Now, we only need to find the right body mesh. Since it has a different name and different races use different body meshes, I recommend searching for the appropriate body here: 
https://wiki.bg3.community/Information/Meshes/Body-Meshes-Reference

In my case it would be HUM_M_NKD_Body_A, Body Type 2. 
![bild8.png](/tutorials/creating-a-head-mesh-and-a-custom-preset/bild8.png)

 

# Header
Your content here
# Header
Your content here
# Header
Your content here
# Header
Your content here
# Header
Your content here
# Header
Your content here
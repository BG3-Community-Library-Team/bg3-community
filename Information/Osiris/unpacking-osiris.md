---
title: Unpacking Osiris Code
description: Quick Overview on Unpacking Osiris Scripts
published: true
date: 2024-04-25T23:21:51.926Z
tags: osiris, scripting
editor: markdown
dateCreated: 2024-04-24T07:02:04.532Z
---

# Unpacking Osiris Code
The Osiris Scripts that handles just about everything relating to the game can be found in what is commonly referred to as the "Goal" files. These files are compressed in the `story.div.osi` file, which is found in a few locations:

- `Gustav/Mods/Gustav/Story/story.div.osi`
- `Gustav/Mods/GustavDev/Story/story.div.osi`
- `Gustav/Mods/Honour/Story/story.div.osi`

These files all have the same name, and are often changed in patches, so you'll want to check in any unpacked patch folders for their presence as well. To unpack these scripts, you'll need to utilize LSLib, going to the Story (OSI) tools section, and setting the Story/savegame and Goal Output path inputs.

![The Story (OSI) tools tab of LSLib](/osidiv-lslib-location.png)

1. Set the `Story/savegame file path` input field to the location of the story.div.osi file you wish to unpack.
2. Click "Load."
3. Set the `Goal output path` input field to the location you want the Osiris scripts to be unpacked into.
4. Click "Extract."

<div class="row">
  <div class="col col-4">

  If you navigate to that folder, you should see something like the folder on the right. It's recommended to open the folder in vscode, for a better understanding of how the files and their contents connect.


  </div>
	<div class="col col-8">  
    <img align="right" alt="A folder where the osiris script files have been extracted" src="/osidiv-extracted.png" />
  </div>
</div>

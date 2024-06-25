---
title: Legally Obtaining Old Builds of Baldur's Gate 3
description: This tutorial will go over how to legally obtain old Patches/Builds of Baldur's Gate 3 using Steam's console and download_depot command.
published: false
date: 2024-06-25T06:10:38.046Z
tags: early access, ea, old patch, download, steam, steam depot, steamdb, download_depot, old build
editor: markdown
dateCreated: 2024-06-25T05:39:45.425Z
---

# Legally Obtaining Old Builds of Baldur's Gate 3
Legally obtaining previous builds or patches of Baldur's Gate 3 is an easy process, which simply requires you to put one console command into the Steam Console.
## Requirements
- [Steam](https://store.steampowered.com/about/) - Steam must be installed and running on your computer, as well as a Steam account.
- [Baldur's Gate 3](https://store.steampowered.com/app/1086940/Baldurs_Gate_3/) - You must own a legal copy of Baldur's Gate 3 on Steam.
## SteamDB
[SteamDB](https://steamdb.info/) is a third-party Steam database tracker which documents both applications and packages maintained on Steam, and keeps a history of all change made to both applications and packages.

The [SteamDB page for Baldur's Gate 3](https://steamdb.info/app/1086940/) will contain three pieces of information which we require for downloading previous/old builds of the game:

- **App ID**: This is the ID associated with Baldur's Gate 3 on Steam, and is unique to each game found on the platform.
- **Depot ID**: This is the ID associated with the specific grouping of files that gets packaged and sent to users when they download a game on steam.
- **Manifest ID**: This is the ID associated with the specific build of the game you wish to download.

### General guide on how to obtain these IDs
1. **App ID**: This is easily found in the official store page link for BG3, and is `1086940`
2. **Depot ID**: Navigate to the ***Depots*** page on the SteamDB BG3 Page, and sort the depots by size. The main depot will typically have the highest file size, however, in this instance, we want to make sure we are finding the ***Windows*** build of the game, and not the ***macOS*** version of the game. This depot will be labeled as ***Gustav Content***, with the ID of `1086941`.
3. **Manifest ID**: Once you have found the correct ***Depot ID***, click on it, and then navigate to it's ***Manifests*** page. Here you will find the Manifest of every published build of the game.
From here, you want to look at the date each Manifest was published, and compare it to the date each [Patch Notes](https://steamdb.info/app/1086940/patchnotes/) was published. You should be able to triangulate which ***Manifest ID*** you require by doing this. 
For example, the very first Early Access build's ***Manifest ID*** is `891244578529757560`.

## Steam's Console
To 
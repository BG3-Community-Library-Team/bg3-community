---
title: Obtaining Old Builds/Patches of Baldur's Gate 3
description: This tutorial will go over how to legally obtain old Patches/Builds of Baldur's Gate 3 using the Steam Depot.
published: false
date: 2024-06-25T19:58:10.820Z
tags: early access, ea, old patch, download, steam, steam depot, steamdb, download_depot, old build
editor: markdown
dateCreated: 2024-06-25T05:39:45.425Z
---

# Obtaining Old Builds/Patches of Baldur's Gate 3
## Requirements
- [Steam](https://store.steampowered.com/about/) - Steam must be installed and running on your computer, as well as a Steam account.
- [Baldur's Gate 3](https://store.steampowered.com/app/1086940/Baldurs_Gate_3/) - You **MUST** own a legal copy of Baldur's Gate 3 on Steam, this guide will not work otherwise. Attempting to circumvent Steam's DRM is illegal, and is in no way supported by the BG3 Modding Community Wiki or it's contributors.
## SteamDB
[SteamDB](https://steamdb.info/) is a third-party Steam database tracker which documents both applications and packages maintained on Steam, and keeps a history of all changes made to both applications and packages.

The [SteamDB page for Baldur's Gate 3](https://steamdb.info/app/1086940/) will contain three pieces of information which we require for downloading previous/old builds of the game:

- **App ID**: This is the ID associated with an application on Steam, and is unique to each game found on the platform.
- **Depot ID**: This is the ID associated with the specific grouping of files that gets packaged and sent to users when they download a game on steam.
- **Manifest ID**: This is the ID associated with the specific build of the game you wish to download.

### General guide on how to obtain these IDs
1. **App ID**: This is easily found in the official store page link for BG3.
2. **Depot ID**: Navigate to the ***Depots*** page on the SteamDB BG3 Page, and sort the depots by size. The main depot will typically have the highest file size, however, in this instance, we want to make sure we are finding the ***Windows*** build of the game, and not the ***macOS*** version of the game. This depot will be labeled as ***Gustav Content***.
3. **Manifest ID**: Once you have found the correct ***Depot ID***, click on it, and then navigate to it's ***Manifests*** page. Here you will find the Manifest of every published build of the game. From here, you want to look at the date each Manifest was published, and compare it to the date each [Patch Notes](https://steamdb.info/app/1086940/patchnotes/) was published. You should be able to triangulate which ***Manifest ID*** you require by doing this.

For example, the **App ID** for BG3 is `1086940`, the main **Depot ID** is `1086941`, and the very first Early Access build's **Manifest ID** is `891244578529757560`.

## Steam's Console
Using the IDs found above, you'll need to use a console command in Steam to start downloading the build of the game you want.

To access this console, make sure Steam is currently running on your PC. Then paste the command found below into either the Windows Run utility, or into the address bar of your browser.

`steam://open/console`

At this point, steam will open a new tab called "CONSOLE", which will be a blank page with a text input box at the bottom.

## Downloading Your Chosen Build
> Later Early Access builds of Baldur's Gate 3 such as **Hotfix #32** use the same AppData folder as the current Patch of the game. Make sure to **BACK-UP** your `%LocalAppData%\Larian Studios\Baldur's Gate 3` folder before continuing.
>
> Data loss, including the loss of Save Data **CAN** occur if you do not back up this folder.
<!-- {blockquote:.is-danger} -->
You will not have the option to choose the installation location of the Depot. It will be placed into a default directory separate from your default game download location. Verify there is enough storage on the drive Steam is installed, so you do not have issues while downloading your chosen build.

Before entering any commands, verify that you have the correct App, Depot, and Manifest IDs for the version of the game you wish to download, and that you are only attempting to use Manifest IDs from their correlating Depots.

In the Steam Console, type the command `download_depot AppID DepotID ManifestID`. Replace the **AppID**, **DepotID**, and **ManifestID** values with the IDs that you found earlier.

**Example Command**: `download_depot 1086940 1086941 891244578529757560` - This command will tell Steam to start downloading very first early access build of the game.

Once you have entered the command, a line will appear in the console that looks something like this: 

`Downloading depot DepotID (file size in MB)`

There will not be a download percentage which tells you how much of the depot has been downloaded, or the speed at which you're downloading it. You will know when the download is finished once a new line appears in the console along the lines of:

`Depot download complete : "...\Steam\steamapps\content\app_AppID\depot_DepotID" (X files, manifest ManifestID) `

Once you receive this message, go to the file location listed, and you should find the contents of the build you chose to download.
> Later Early Access builds of Baldur's Gate 3 such as **Hotfix #32** require you to download the `Gustav Content - Bin` depot, in addition to the `Gustav Content` depot. You must place the contents of both depots into the same folder for the game to function.
>
> If the `Gustav Content` build you downloaded does not contain a `Bin` folder, you must additionally download the corresponding `Gustav Content - Bin` build.
<!-- {blockquote:.is-info} -->

At this point, you may unpack the downloaded game files.

## Launching The Game
When launching these older builds of Baldur's Gate 3, verify that Steam has been entirely closed, and that you are launching from the exe file. If you attempt to launch the game while Steam is open, it may prompt you to install the latest version of the game.

Older game versions should be used for asset mining, accquiring cut content, or anything else that might be useful for modding the latest version of the game. It is not recommended to actually play on these old patches/builds of BG3, as you will get a hampered, and buggy experience compared to the latest release of the game.
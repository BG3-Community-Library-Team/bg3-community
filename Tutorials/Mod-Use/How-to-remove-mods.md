---
title: How to remove mods from BG3
description: Using this guide, you will be able to remove ALL mod files from your game and have a vanilla version of BG3.
published: true
date: 2024-06-23T02:44:09.456Z
tags: bg3-mod-helper, bg3mm, moduse, mod use, loose-file-mods, mod, mod uninstall
editor: markdown
dateCreated: 2024-05-02T16:40:20.175Z
---

# <p style="text-align:center">*How to Remove All Mods from BG3*</p>

## <p style="text-align:center">**Created in collaboration with ResplendentArrow, Maze, DefinitiveToast, Norbyte, Surōand, a very special thanks to LaughingLeader and NellsRelo!**</p>
---

## **Before using this guide:**

-   This guide is written assuming you are using [_BG3MM_](https://github.com/LaughingLeader/BG3ModManager) and a PC with Microsoft Windows.
-   This guide focuses on removing all mods from your game, but it can also be used to remove individual mods for troubleshooting
-   This guide directs you to delete folders/files, but you can move the folders/files to another location instead of deleting if you want to reinstall the mods after following this guide
-   This guide uses screenshots of folder locations that may differ from what it is located on your computer
-   If you would like to respost this guide to another site, please contact ResplendentArrow on Discord

---

# **1. Delete all Mods in your AppData folder**

## **1.1 Navigate to your Mods folder at:**

C:\\Users\\YourName\\AppData\\Local\\Larian Studios\\Baldur's Gate 3\\Mods

![](<https://lh7-us.googleusercontent.com/sfc47gTFBtAgy0jdp-vdZUDtUHWdTf3V1pQs1a3pgUNM7dLI0mpVGE0OJoNloVsLvdpha0K7iWP5y9LhXBidJ-fI7odc2I3Hek3idI6odP_tKVLPt2FWHYpBlkD0B8Ln6xQSEfiAVMV2U5UTc_vPmA> "Example image of Mod folder located in the AppData of a users computer") <p style="text-align:center">*Example image of Mod folder located in the AppData of a users computer*</p>
To quickly find this folder, type "run" into the windows search bar at the bottom of your screen. A window should open that looks like the image below. Type or copy and paste the following into the run screen and press enter:

> %localAppData%/Larian Studios/Baldur's Gate 3/Mods

![rumcommandmodfolder.png](</mod-use/remove-mods/rumcommandmodfolder.png> "Example image of run window with the copy and pasted line of text")<p style="text-align:center">*Example image of run command window using the copy and pasted text from above*</p>

## **1.2 Delete ALL .pak files (mods) in the Mods Folder:**

![](https://lh7-us.googleusercontent.com/JZBIPV31xeidZR7sWowjcnQxfoAVtFDggLqEGQiOtM4Bclg24hSrkU0hGjGMbXMJZcQwnTxuIVyLxd9EFVGTOfndDWTo_poAnVRkeyG2ut6nFd3qpAtL4tOnVTGqdxZRoWUOVIWhGEm-6ofmNrIFTw "Example image of mod files to delete or move to another location")<p style="text-align:center">*Example image of mod files to delete or move to another location*</p>

---

# **2. Delete Folders in Installation Folders**

Some mods may have files in your BG3 Installation folder, such as UniqueTav or other replacer mods. These files and folders must be **deleted**.

## **2.1 Navigate to your Installation folder at:**

D:\\SteamLibrary\\steamapps\\common\\Baldurs Gate 3\\Data

![](https://lh7-us.googleusercontent.com/EOnBD3jTOQNUM2aRECE1jW6qfgjmlb-lhxwTX4h9sy_4hgZE1FW-gzcSZ1lDC-eJM5NspnhRG7JDSadP8SJzK8IFWmNziNJ_0CnAkMkVT_xmgWZMLbP2C3RLSIgDbNgxJOs4pVasqYDNrZpdxi6kHw "Example image of the Data folder in the BG3 installation folder")<p style="text-align:center">*Example image of the Data folder in the BG3 installation folder*</p>

If you are using the Steam version of BG3, you can access your Bin folder by right clicking the game in your game list, clicking Manage, then Browse Local Files.

![](https://lh7-us.googleusercontent.com/cQ7YI8Szh3ZEq_-CXY0ibUEAhtef5b1QyaxRVdliYySOXI270k9gPU7GXFnV-4Wl0T2YKkBhFQVqGQq5PEZeOdWzYNg350eU3UhXNY6xmge-wF3oZ8MRx5_8iPaE-pnzGvT1GCaCtSXvYz-byDEGBg "Example GIF of how to access Data folder through Steam")<p style="text-align:center">*Example GIF of how to access Data folder through Steam*</p>

## **2.2 Delete all folders in your Data folder, EXCEPT LOCALIZATION**

> **DO NOT DELETE .PAK FILES OR THE LOCALIZATION FOLDER, DOING SO MAY RESULT IN NEEDING A FULL REINSTALL OF BG3. ONLY DELETE THE FOLDERS HIGHLIGHTED IN THE SCREENSHOTS BELOW**
{.is-warning}

![](https://lh7-us.googleusercontent.com/ZfBGtdVsBWmUps9aWCA7uTvFu74_rhieWHod-OHPaENCqRLLVJp4BOypIwhUxAG8vUlvPS68KTFCix3LW2DyrKZTMSyWyhBOoGl7dEHeH18FHkPQly3R4MQrzD-VOOGvRgTgsQE1kQauHqkwFzCPBA "Example image of the specific files in the Data folder to delete or move to another location")<p style="text-align:center">*Example image of the specific files in the Data folder to delete or move to another location*</p>

If you installed any .pak(mod) file into your Localization folder, make sure to delete those .pak(mod) files.

> ### **Special Note - Translation Mods**
> If you are using a translation mod, the following must be done:
> -   If you installed a .pak(mod) file in the Localization folder, make sure to delete the .pak(mod) files
> -   If you replaced any of the .pak (mod) files in the Localization folder, simply delete those replaced .pak files and when you verify your game in _step 4_, the verification process will replace this file with a vanilla file.
> {.is-info}

---

# **2.1. Uninstall NativeMods/WASD/NativeCameraTweaks**

Use this step if you are using NativeMods/WASD/NativeCameraTweaks

## **2.1.1 Navigate to your Bin folder**
This folder is inside your game installation folder, refer to the steps taken in *2.1 Navigate to your Installation folder at*
![](https://lh7-us.googleusercontent.com/d3Va6wYlmclQmgol4ekMQS4WZzv3X2ELJGn_wsEjr459M3zzuBuSn0jvLnmfxL2vgoSXa9Z2ovKWiA5MsD0wjvFavbidv48pipAuHPCb4xrMVlbqMXC9Ke5nHI1a5oTMSPj47Qin5VFbDneR7M9yqw "Example image of the Bin folder in the game installation folder")<p style="text-align:center">*Example image of the Bin folder in the game installation folder*</p>

## 2.1.2 Delete the following in your Bin folder

-   Delete the “NativeMods” folder
-   Delete “bink2w64.dll”

![](https://lh7-us.googleusercontent.com/YjEEe33FgKNEXBz0Q-xroy9nuXqFUtKUMlNAUxFrw7Af5Hz6hZxbNmlZYNYbuTFMPW-8-IKfURejfJrPDROQ4L4SSLXisfGtB7yjTXR6jIt44DK9SSyOkK4ggneVHKodfYO22QQKHaOh-tCFPf6cCQ "Example image showing what to delete in the Bin folder")<p style="text-align:center">*Example image showing what to delete in the Bin folder*</p>

## **2.1.3 Rename “bink2w64\_original.dll” to “bink2w64.dll”**

The file “bink2w64\_original.dll” was created when NativeMods was installed.

![](https://lh7-us.googleusercontent.com/gigioMv1DPjqQHkBp65m_DOCqahGVaNXIyq8Ic22eEfDOOn5ThSxwqGYv0bmNgs7R9ouAxZ6FKbiC9L82OYRrljaslkR-L2nwL6lt92FCD1aj8poq-_6KUU1gGNwP8JW3z_Gnib-OcnWBHrG1aozqw "Example image showing the file to rename")<p style="text-align:center">*Example image showing the file to rename*</p>

---

# **2.2. Uninstall Script Extender**

Use these steps if you have Script Extender installed. 

Script Extender is installed in the Bin folder. Refer to the steps taken in *2.1 Navigate to your Installation folder at* to get to your Bin folder.

## **2.2.1 Delete the file “Dwrite.dll” in your Bin folder**

![](https://lh7-us.googleusercontent.com/m6W8Fyitzb2pDPHxiM1uxLX_oUcOz3ZaaC0MVX4vf9v9zrrzUK_aOB-iPnwtkqHukfl7mz9F0vpRRHFSSfXj8ATu5j4hSDr0Tv9Ew8DsfT9IjkkuJkQyf4C3y6Hjqg2uMzwV7sV8lwmmErLY1XIAsQ "Example image showing the file to delete")<p style="text-align:center">*Example image showing the file to delete*</p>s

## **2.2.2 Delete the files “ScriptExtenderSetting.json” and “ScriptextenderUpdater.json” (if you have them) in your Bin folder**

![](https://lh7-us.googleusercontent.com/J0vMTloBJqNsUTQ7RhzGUrC-YuIgX8lPhioujUm-0C-YcYdBhYJI12FogigdWPUOjamnM6EExe3iqQcg3FgWgQvMoBwjWIiLnW4lkoVmT-20x8rlalClRCGozRlf9KHRdT5EPnzJfBcfkzdV46FeTw "Example image showing the files to delete if you have them")<p style="text-align:center">*Example image showing the file to delete if you have them*</p>

## **2.2.3 Delete the folder “BG3ScriptExtender”**

Navigate to your local folder, as done in step *1.1 Navigate to your Mods folder* and delete the BG3ScriptExtender folder.

![](https://lh7-us.googleusercontent.com/A2CmAgCI5tR3HUWRcPNz2Cy80wkLW54Xllx16mQX1yGvJZWvdqDF67KfErvjkBeL19RL95t1ZBq98Te_krO32cppaSvtRIRiKSErWP0B_eVoZe-7-8rMRQkRXUXJGcX_BCNLf7kb_18RzK-4ZVt_EQ "Example image showing the file to delete")<p style="text-align:center">*Example image showing the file to delete*</p>

## **2.2.4 Delete the folder ”Script Extender” (if you have it)**

Navigate to your Baldur's Gate 3 folder in the your AppData. You can use the same "run" method as earlier but use the following text instead:

> %localAppData%/Larian Studios/Baldur's Gate 3

![runcommandbg3folder.png](/mod-use/remove-mods/runcommandbg3folder.png "Example image of run window with the copy and pasted line of text")<p style="text-align:center">*Example image of run window with the copy and pasted line of text*</p>

---

# **2.3 Uninstall Party Limit Begone Legacy Edition**

> **If you use the .pak version of this mod, skip this step.**
{.is-success}

If you had Party Limit Begone Legacy, then you need to delete your .exe files in your bin folder and the .exe backup.

The .exes do not get altered/reinstalled when you verify the game so this is a MUST!

---

# **3. Deleting the modsetting.lsx file**

Navigate to C:\\Users\\YourName\\AppData\\Local\\Larian Studios\\Baldur's Gate 3\\PlayerProfiles\\Public

You can use the same "run" method as earlier but use the following text instead:

> %localAppData%/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public

You can navigate to this folder using the same "run" command as done in step *2.2.4 Delete the folder ”Script Extender”*

![runcommandmodsetting.png](/mod-use/remove-mods/runcommandmodsetting.png "Example image of run window with the copy and pasted line of text")<p style="text-align:center">*Example image of run window with the copy and pasted line of text*</p>

In the Public folder, delete the modsetting.lsx file

![removemodsstep3.png](/mod-use/remove-mods/removemodsstep3.png "Example image showing the file to delete")<p style="text-align:center">*Example image showing the file to delete*</p>

---

# **4. Verify Game Files**

## **4.1 In steam, right click on BG3 in your game list and click properties.**

![](https://lh7-us.googleusercontent.com/gIV2yWZCHH_K6-QYvHMYhfM64MZXC4JsBNmlguvpcP9BN8o4O0Y6DCCCzDTa2EoibfmJ0vPvRLfUIM_IF9Z8vinjVve1PRU3S8zfpmuad-fyu5zEyll2VRb9_eXRshhAHvt39JSm4es1OyiDMC0GrA "Example GIF of how to verify files through Steam part 1")<p style="text-align:center">*Example GIF of how to verify files through Steam*</p>

## **4.2 In the properties window, click on the Installed files tab and click Verify Integrity of Game Files**

![](https://lh7-us.googleusercontent.com/nC7ObRzfxulKmG-UTsSmn0daeU6QOvr32q21t1i71zi9wiIc78NcNYeTzUBcT3XcOn-IgIqtOAn-fh6OIWEmOHxIcpaGpZKTVwHCQVH3TeHE-c23-FRC-_muzVmpLJ6jk0l2cOWY3Cn9yqIc1IUqlA "Example GIF of how to verify files through Steam part 2")<p style="text-align:center">*Example GIF of how to verify files through Steam*</p>

> This process may take some time. Verifying game files replaces missing files and files that have been overwritten by mods. It does not delete mod files, which is why all the above steps must be done.
{.is-info}

## **Special Note - GOG Users**

For GOG users, you can verify files in a similar way as Steam

(Screenshot coming soon)

---

# **5. Test your game**

- Run BG3 once without any mods (This will reset the modsetting file and tell the game SE is no longer installed)
- Test if you can reach character creation without issues and identify any bugs.
- If there are no issues, create a base tav and test if you can load into the ship (the tutorial area).

> If you have made it here, then congratulations, you have successfully returned your modded BG3 to a vanilla state! You can choose to continue without mods or use this as an opportunity to test mods.
> 
{.is-success}

![](https://lh7-us.googleusercontent.com/iI8GEYUqbLLxjJ3UG8dlDcGmU0jFl1DW5y3yUuLklQUxGhUN__Z0_sajucPxHmnMk-uzx9er_hxBmFMeSCpV_iHJGcw_mo_P4yX-2pTiTJpmxHfenCunnHGimyAsrgHIz1GksdK4ML1nQS1QrlANPg)
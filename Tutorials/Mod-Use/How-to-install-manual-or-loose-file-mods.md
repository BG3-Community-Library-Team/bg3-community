---
title: How to install manual/loose file mods
description: 
published: true
date: 2024-05-04T22:01:19.829Z
tags: installation, loose-file-mods, manual-mods, manual, non-pak, verify, mods, how-to, bin, generated, data, public, folders, folder
editor: markdown
dateCreated: 2024-05-01T01:34:11.948Z
---

# How to install manual/loose file mods

This is part 3 and the final part on how to install BG3MM, mods and loose file mods. 
- [Part 1: Installation Of BG3MM](/Tutorials/Mod-Use/Installation-Of-BG3MM)
- [Part 2: How to Install Pak Files](/Tutorials/Mod-Use/How-to-Install-Pak-Files)


## What is loose/manual mods? 

What is loose file mods? Loose file mods are mods that are not managed by a mod manager. This can for example be tattoo mods or make up mods. You can identify them with coming in a zip, 7zip or rar and when you extract them they typically have folders which can be named; "Data", "Bin", "Public", "Generated". 
When you open these folders, it will typically be a bunch of folders ending with different files such as DDS or other files. Meaning, these will not end in files that are ".pak" files. 

These folders shouold not be put in the mods folder (`%localAppData%/Larian Studios/Baldur's Gate 3/Mods`) but instead the data or the bin folder in your root installation folder (`\SteamLibrary\steamapps\common\Baldurs Gate 3`)

However Vortex can manage them, but it is not a good idea as there are potential risk such as Vortex putting the folders and files in a wrong place which can but is not limited to these bugs: 

BG3 crashing
BG3 not responding
BG3 not opening
Weird textures
Mods not working correctly
Mods not showing up
Mods having compatbility issues when there should be none etc. 

This is where this guides comes in to provide information with how to install these manually. 
For Unique Tav which also have a loose file aspect, look through this guide instead: (On To-Do)

> For GOG users, you will need to find the GOG equivalevant of the Steam folders and it may look different to what is shown in this guide
{.is-info}

## Find and download the mod you wish to install from Nexus

- [Nexus Website](https://www.nexusmods.com/baldursgate3)


For this guide, [CovenElf Tattoo and Makeup Mod](https://www.nexusmods.com/baldursgate3/mods/1684?tab=description) will be the example.


> You will need to press on "manual download" as highlighted below. Do not press "download with mod manager" if there is such an option. That is for vortex and through a mod manager, which is not recommended with loose file mods. 
{.is-warning}


![firstmanualinstallpng.png](/tutorials/install_manual_mods/firstmanualinstallpng.png =x300)

It should show up as a zip, 7zip or a rar file. In this case, it is a rar file. 

Now extract it in your downloads folder: 

![extract.png](/tutorials/install_manual_mods/extract.png =x250)

![extraction.png](/tutorials/install_manual_mods/extraction.png)

When you have done this, just delete the rar, zip or 7zip file. 

You should now end up with a folder called the exact same as the zip, rar or 7zip file. 
It may also come out called "Generate", "Bin", "Data" or "Public". 

If the folder is called the same thing as the file you just extracted, you need to go one folder deeper until you find either "Generated", "Public" or "Data" or "Bin". 

Like this: 
![onefolderdeeper.png](/tutorials/install_manual_mods/onefolderdeeper.png)
As you can see, I clicked into the "CovenElf - Tattoo and Makeup Collection-1684-v1-2-1-1694224111" and inside that folder, is the folder "Generated" which I need. 
Do not go deeper into the folder: you only need to move the first "Generated", "Public", "Bin" or "Data" folder you find. 

The difference between all of these are just where they go. 

> "Generated" and "Public" act the same and goes in the same folder. 
> "Data" and "Bin" act the same and goes into the same folder. 
{.is-info}


## "Generated" and "Public" folders - where do they go?

When you have extracted the zip, rar or 7zip file and found either a "Generated" or a "Public" folder, you will need to find your data folder in another window of your file explore. 

You will need to go on Steam, then to your Library and then right click on BG3, hover over "Manage" and click "Browse local files": 

![steam.png](/tutorials/steam.png)

File explore will open this folder: 

![bg3folder.png](/tutorials/install_manual_mods/bg3folder.png)


---


You will need to click into the "Data" folder. 

![datafolder.png](/tutorials/install_manual_mods/datafolder.png =x700)

> You should see a folder with a folder called "Localization" and a bunch of pak files. These pak files are game files and Localization is base game as well. 
> You may see a "Mods" folder as well in the data folder. That is normal. Do not confuse this mods folder with the real mods folder as it is not. The real mods folder is located here: `%localAppData%/Larian Studios/Baldur's Gate 3/Mods`. 
{.is-info}

Then you open the downloads folder again and drag the "Generated" or "Public" folder into the data folder, like this: 

![movegenerated.png](/tutorials/install_manual_mods/movegenerated.png)

To this: 

![movedintothedatafolder.png](/tutorials/install_manual_mods/movedintothedatafolder.png =x600)

If you have multiple mods, and some of them have been "Generated" and "Public" it can also look like this after: 

![bothdataandpublic.png](/tutorials/install_manual_mods/bothdataandpublic.png)

When you have done the above, you have installed the mod and can open the game to see the changes. 

> Tip: If you have multiple mods that has a folder named "Generated" or "Public" you just do the same as above. The folders and files will automatically merge with each other. Check the mod description for incompatibilities as you cannot have two "Tattoo" mods such as CovenElf Tattoo and then also for example Mari's tattoo mod. They will override each other. Same with makeup mods and so fourth. 
> However, if it is related to mods that adds items, such as "Camp clothes" there should not be any incompatibilities.
{.is-info}

## "Data" and "bin" folders - where do these go? 

Much like above, the process is the same however they go into a different place. 

You will again need to find the root installation folder which is this folder: `\SteamLibrary\steamapps\common\Baldurs Gate 3`

Open your steam, go to library and right click on BG3. Hover over the "Manage" and click on "Browse local files".

![steam.png](/tutorials/steam.png)

When you have done that, it will open a folder in your file explore: 

![bg3folder.png](/tutorials/install_manual_mods/bg3folder.png)

When you have found this folder, download the mod you wanted. 


---


This guide uses [The Native Mod Loader](https://www.nexusmods.com/baldursgate3/mods/944) as an example:

First click on the manual download: 

![downloadnativemod.png](/tutorials/install_manual_mods/downloadnativemod.png =x300)


When you have downloaded it, it will be downloaded as a zip file. 
Extract the zip file: 

![nativemodloader.png](/tutorials/install_manual_mods/nativemodloader.png)

![nativemodextract.png](/tutorials/install_manual_mods/nativemodextract.png)

When you have extracted it, you can delete the zip file. 

Again, the extracted folder may come out with the same name as the zip file so click into the folder: 

![onefolderdeepernativemod.png](/tutorials/install_manual_mods/onefolderdeepernativemod.png)

As seen above, you can see the "Bin" folder. If it is a "Data" folder, you need to do the exact same thing. 

Now you just need to move the downloaded "Bin" or "Data" folder from the mod into the root installation folder. Do not drag the "Bin" or "Data" folder on top of any folders but simply just place it in this folder: `\SteamLibrary\steamapps\common\Baldurs Gate 3`. 

![placethebin.png](/tutorials/install_manual_mods/placethebin.png)


> You will notice that there already is a "Bin" and a "Data" folder. This is normal, and to be expected. The downloaded "Data" or "Bin" folder will merge with the "Bin" and "Data" folder in your root installation folder. Explanation below.
{.is-info}

You may need to replace files and it will come up with this: 

![replace.png](/tutorials/install_manual_mods/replace.png)

That is normal, and it just replaces two files. You will need to say "Replace the files in the destination" otherwise the affect will not take place. It will not replace the entire "Bin" or "Data" folder but only the files it needs to replace so the rest of the bin folder is still there and unaffected. 

When all of this is done, you have now successfully installed the mod. 

## How to install WASD movement, Camerea Tweaks and other "Native mods"

This is the exact same process as above in '"Data" and "Bin" folders - where do they go?'

When you have installed all of them, and done the same process with placing the bin folder in the root installation folder (`\SteamLibrary\steamapps\common\Baldurs Gate 3`), you can control you have installed them correctly by looking for this folder: 

![nativemods.png](/tutorials/install_manual_mods/nativemods.png)

Simply just click into the bin folder, and check you have the "NativeMods" folder. 
You can click further into the "NativeMods" folder and see which NativeMods you have installed:

![nativemodfolder.png](/tutorials/install_manual_mods/nativemodfolder.png)


## How to uninstall loose file mods

Here is a guide for uninstalling all mods in your game (loose/manual file mods are also covered): [How to install manual or loose file mods](/Tutorials/Mod-Use/How-to-install-manual-or-loose-file-mods)

If you want to uninstall any loose file mods, you will need to find the corresponding files again. 

For example if you installed a tattoo mod, where you needed to move the "Generated" folder into the "Data" folder, go to your data folder and delete the "Generated" folder. 

![movedintothedatafolder.png](/tutorials/install_manual_mods/movedintothedatafolder.png)

If you have more mods inside the "Generated" folder, you will need to go on Nexus, find the mod and preview the files: 

![previewfile.png](/tutorials/install_manual_mods/previewfile.png)

![preview.png](/tutorials/install_manual_mods/preview.png)

As seen above, if I had more mods in "Generated", I should go down one folder deeper and delete the "Public" folder inside the "Generated" folder. (Not to be confused with the "Public" folder in your "Data" folder). If I have more mods that share the same "Public" folder inside the "Generated" folder, I just keep moving down the folders until I can delete the one folder that only leads to the mod I want to uninstall. 

Do not just delete the end files, as that can cause issues. It is recommend you delete the path down to the mod. 

Native mods have a special way to delete them: 

First you delete the "NativeMods" folder or the specific NativeMod file you wish to uninstall. 
Note: WASD Movement also replaces the SDL2.dll in your bin folder, which you will also need to delete and then you need to verify your game to replace the SDL2.dll file you just deleted, with a base game copy. 

If you wish to uninstall Native Mod Loader and Native Mods completely, you will also need to delete this file: 

![bink.png](/tutorials/install_manual_mods/bink.png)

And rename the "`bink2w64_original.dll`" to "`bink2w62.dll`"

If you had WASD movement as well, you will need to verify your game. 

## How to verify your game

Go to Steam, right click on BG3 and click on "Properties". 

![properties.png](/tutorials/install_manual_mods/properties.png =x250)

Then a new window will pop up. Click on "Installed files" and then "Verify integrity of game files". 

![verify.png](/tutorials/install_manual_mods/verify.png)

> When it is done, it will say "could not verify x files, redownloading the files" or something alike this. This is very normal, this just means you have played with mods and it needs to replace the amount of files it showed you. It will redownload the files, and validate in steam. You can follow the process in Steam Downloads. 
{.is-info}

When the process is done, you have verifed the game and the missing files has been replaced. 

## Other relevant guides and credits: 
How to install BG3MM, pak files and loose/manual mods series: 
- [Part 1: Installation Of BG3MM](/Tutorials/Mod-Use/Installation-Of-BG3MM)
- [Part 2: How to Install Pak Files](/Tutorials/Mod-Use/How-to-Install-Pak-Files)

Other relevant guides: 
- [General load order guide](/Tutorials/Mod-Use/general-load-order)
- [Unique Tav & Everything you need to know](/Tutorials/Mod-Use/Unique-Tav-Everything-you-need-to-know)
- [How to remove mods/troubleshooting guide](/Tutorials/Mod-Use/How-to-remove-mods)
- [How to install Script Extender](/Tutorials/Mod-Use/How-to-install-Script-Extender)
- SE Fresh Install (On-To-Do)

Made by: Maze
Credits: LaughingLeader, Norbyte, Kaz, NellsRelo, Arrow, DefinitiveToast


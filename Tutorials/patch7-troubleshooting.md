---
title: Patch 7 Troubleshooting
description: Will be updated as we discover more information
published: true
date: 2024-09-10T16:25:29.808Z
tags: patch 7, troubleshooting
editor: markdown
dateCreated: 2024-09-08T23:55:05.989Z
---

# Patch 7 Troubleshooting
- This page will be updated to add/change information as more is learned over time.
- Note, the in game mod manager that BG3 now has will be referred to as IGMM on this page.
- Thank you to everyone in the community, the mod support helpers, modders, and mod users!  Special thanks to SatanModding for putting this all together, Norbyte and LaughingLeader for their expert skills and knowledge that we would be lost without, Kaz for his KVT guide, ResplendentArrow for editing!
## General Troubleshooting

**How do I back up my saves and mods ?**
- Copy your `Mods` folder, `modsettings.lsx` file, `Story` folder, and `Generated` folder somewhere else, like your desktop. 
- The location of those files are a bit further down

#####

**How do I update my game to Patch 7 ?**
- To update to patch 7, we recommend backing up your mods and reverting to [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) first.
- After you do this, simply update the game on whatever game manager you are using (Steam, GOG, etc).

#####

**How do I downgrade my game to the Patch 6 beta ?**

> This method is not recommended as it causes almost as many issues as just upgrading to patch 7
{.is-warning}
- Larian made it possible to choose a patch 6 beta branch
- However this branch is more of a patch 7 "light"
- This means many mods that are broken on patch 7, are also broken on patch 6
- Specifically, mods that reset the `modsettings.lsx` file
- Regardless, if you want to join the patch 6 beta follow these steps:
- Before you do this, we recommend backing up your mods and reverting to [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) first. 
- Then, you can revert to Patch 6 like so:
_Right click on BG3 in your Steam Library > Properties > Betas
On Beta Participation select: release_patch6_hf9_
- Update BG3MM to the [patch 7 version](https://github.com/LaughingLeader/BG3ModManager/releases/tag/1.0.11.1)


#####

**How do I actually downgrade my game to Patch 6 ?**
- To actually downgrade your game to the "real" patch 6 follow these steps:
- Before you do this, we recommend backing up your mods and reverting to [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) first. 
- Then, you can follow this guide https://wiki.bg3.community/en/Tutorials/General/Legally-Obtaining-Old-Builds-Patches-Of-BG3

#####
**I downgraded to Patch 6 and now my mods don't work anymore**
- Back up your mods and revert to  [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) 
- Get the [Patch 6 version of BG3MM](https://github.com/LaughingLeader/BG3ModManager/releases/tag/1.0.10.0)
- If you use [Vortex](https://www.nexusmods.com/about/vortex/) no additional steps are necesssary.
- Delete your `modsettings.lsx` file
- Add your mods with BG3MM/Vortex as usual

> Please be aware that the Patch 6 beta is **not** the same as Patch 6  
> See __How do I downgrade my game to the Patch 6 beta ?__  for additional information
{.is-warning}

#####
**How do I revert back to Vanilla ?**
Follow [this](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) guide to revert to vanilla

#####

**Where can I find my Mods/Loose Files/modsettings/bin**
_For Windows_
Mod folder: `%LocalAppData%\Larian Studios\Baldur's Gate 3\Mods`

modsettings: `%LocalAppData%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public\modsettings.lsx`

saves: `%LocalAppData%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public\Savegames\Story`

Data folder: `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data`

#####

_For Linux/SteamDeck_ - _On SteamDeck your username is usually_ **deck** 
Mod folder: `/home/userName/.steam/steam/steamapps/compatdata/1086940/pfx/drive_c/users/steamuser/AppData/Local/Larian Studios/Baldur's Gate 3/Mods`

modsettings: `/home/userName/.steam/steam/steamapps/compatdata/1086940/pfx/drive_c/users/steamuser/AppData/Local/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/modsettings.lsx`

saves: `/home/userName/.steam/steam/steamapps/compatdata/1086940/pfx/drive_c/users/steamuser/AppData/Local/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/Savegames/Story`

Data folder: `/home/userName/.steam/steam/steamapps/common/Baldurs Gate 3/Data`

#####
**My Game crashes/ I get an error message**
- Back up your mods and revert to  [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) 


#####

**I keep seeing "Not Found"**
- If you are seeing NOT FOUND, you are using an outdated localization mod like Show Approval in Dialog Choices or OIO - Overexplained Interaction Options. Delete it.
- Those are just examples, it can be any other mod that changes the localization file
- Delete the file `C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Localozation\English\english.loca` and Verify file integrity on steam

#####

**I removed Mods and now I cannot load my save anymore**
- Most mods cannot be removed from a current save.
- Reinstall your mods and use [Mod Uninstaller](https://www.nexusmods.com/baldursgate3/mods/9701) by Volitio to uninstall your mods
- This does not work for all mods.
- We recommend you start a new save for patch 7




## BG3MM/Vortex and the IGMM (In Game Mod Manager)

**Should I use BG3MM, Vortex, or the in game mod manager ?** 
- We recommend that you use BG3MM or Vortex
- Please don't use BG3MM and Vortex together

#####

**BG3MM doesn't work anymore**
- Use the correct BG3MM version for your patch
- Click [here](https://github.com/LaughingLeader/BG3ModManager/releases/tag/1.0.11.1) for the patch 7 version
- Click [here](https://github.com/LaughingLeader/BG3ModManager/releases/tag/1.0.11.1) for the patch 6 beta version (same as for patch 7)
- Click [here](https://github.com/LaughingLeader/BG3ModManager/releases/tag/1.0.10.0) for the patch 6 version
- delete your `modsettings.lsx` file if you run into any issues like BG3MM being stuck loading or modsettings not working correctly.

#####

**Vortex doesn't work anymore**
- Vortex auto updates. If you have not received the new updates, restart the program.
- The newest Vortex version is compatible with Patch 6 and Patch 7
- You can import your patch 6 load orders and they will be converted to patch 7 load order.
- You can read more information [here](https://forums.nexusmods.com/topic/13498316-baldurs-gate-3-patch-7-support-for-vortex/)

#####

**My modsettings are always getting reset**
- You have one, or multiple mods that are "bad" and keep resetting the `modsettings.lsx` file
- Remove all your mods (**Just placing them in inactive is not enough! - Remove them from the folder!**)
- Add mods one by one until you find the one resetting your modsettings 

#####

**Is Modfixer broken?**
- No. Modfixer is not broken
- It is not needed anymore in Patch 7, but it does not cause issues.
- You can continue using mods that have ModFixer bundled

#####

**How does the in game mod manager handle load order ?**
- The in game Mod Manager does not allow you to change the load order 
- The load order in the IGMM is based on dependencies and order of subscription
- For this reasons, we recommend to use BG3MM/Vortex instead
- If you want to use the in game mod manager, we recommend you reenable the load order buttons with
   - [Mod Manager Fixes and Tweaks - Nexus](https://www.nexusmods.com/baldursgate3/mods/11954)
   - [Mod Manager Fixes and Tweaks - Mod.io](https://baldursgate3.game/mods#/m/mod-manager-fixes-and-tweaks)



## Third Party Mods and Supported mods  (Mod.io and IGMM)

**Does Script Extender work?**
- Yes. Script Extender works

#####

**Is Script Extender included in Patch 7?**
- No. You still need to [install](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender) it 

#####

**Why are mods that use Script Extender not on Mod.io?**

> The following text has been written when it was believed that Script Extender mods could never be on mod.io
> Recent discoveries have made it possible to host Script Extender mods on mod.io now.
{.is-warning}


- The official toolkits do not support SE, which means that no SE mods can be uploaded to Mod.io.
- To clarify, the only way modders can upload a mod to mod.io, is to use the official toolkit. Mods, such as ones on NexusMods, cannot be simply dragged and dropped to convert using the toolkit. Since SE is not supported on the toolkit, there is no way to convert SE mods using the tool and upload to mod.io.
- This is a Larian decision, not a modder one, modders cannot control what the tools allow and don't allow.


#####

**Will my mods work on patch 7 ?**
- Many mods work, some don't
- You have to try on a case to case basis.

#####

**Can I use in game and third party mods together ?**
- You can use supported and third party mods together.
- In this case, choose the supported mods from the IGMM
- Then close the game
- Export your load order with BG3MM/Vortex as usual
- Start your game but don't interact with the IGMM
- If you interact with the IGMM, your load order will be changed and you have to close the game, and export with BG3MM/Vortex again

#####

**What does the third party warning mean ?**
- This is a design decision by Larian and has no meaning
- Ignore it

#####

**In game all my third party mods have the same name**
- This seems to be a visual bug that has no other consequences
- Ignore it

#####

**How do I add mods safely?**
- To add mods safely, first revert to  [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods)
- Then add mods one by one, or in small batches to test if they work

## Mod Updates: 

**Does UTav work? Why should I switch to KazVT?**
- It seems like UTav works again, however we recommend switching to [KazVT](https://www.nexusmods.com/baldursgate3/mods/8912) 
- You can see a guide about how to use it [here](https://wiki.bg3.community/en/Tutorials/patch7-troubleshooting#kaz-virtual-tav)
- KazVT has multiple benefits:
  - It's console/mac compatible
  - It can support sweat
  - It doesnt depend on additional unsupported shaders


#####
**What mods are broken/Still work?**
- Many mods work, some don't
- You have to try on a case to case basis.


#####
**Is my favorite mod updated/When will my favorite mod be updated?**
- You can check for updates on Nexus
- Either check your download history and filter by **Updated**
- Or check the Nexus page of the mod you are interested in
- Be patient mod author's create mods in their free time. Updates might take a while
- Other mods don't need updates at all and work on patch 7


#####
**When will my favorite mod come to the in game mod manager ?**


> The following text has been written when it was believed that Script Extender mods could never be on mod.io
> Recent discoveries have made it possible to host Script Extender mods on mod.io now.
{.is-warning}


- Not every mod will be converted for upload on mod.io
- Converting a mod is not as simple as drag and drop. It takes time to convert mods and may takes weeks to months for mods to be converted if the mod author is willing to convert their mod, so be patient
- Not every mod author may want to put their mods on mod.io. Respect the mod authors choice and do not harass them
- Any mod that uses SE extensively will not be on mod.io because the toolkit is incompatible with Script Extender. SE mods still work! You just won’t see them uploaded on mod.io. SE mods will continue to be available on nexus mods.



## Multiplayer

**To play with another person for a modded game, you need the same**
- Mods
- Mod Versions
- Load order (modsettings)
- Game version

#####

**I have the same Mods, Mod versions, load order and game version but I still cannot connect**
- You made a mistake somewhere
- To make sure you really have the exact same files, do the following steps:
    - Everyone reverts to  [Vanilla](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-remove-mods) 
    - Everyone updates their game to the most recent version
	- One person downloads all mods
    - They create a load order (`modsettings.lsx`) file
    - This person zips their `Mods` folder and sends it, together with the `modsettings.lsx` to their friends
	- Everyone else deletes their `Mods` folder and `modsettings.lsx` file
	- Everyone unzips the `Mods` folder that has been sent and places it, and the `modsettings.lsx` file in the correct folder
- Afterwards you can compare the size of your folder and your `modsettings.lsx` file with  https://www.diffchecker.com/

#####

**I sent my Mods and modsettings to my friend, but we still cannot connect**

- There is a rare case where the host has to long rest before others can join
- Otherwise you have made a mistake somewhere and there is still a difference

## For Mod Developers / Aspiring Mod Developers

**What can the toolkit do?**
- For our toolkit FAQ, head over to #toolkit-faq 

#####

**Is the toolkit easier than the old way?**
- In some cases yes, in some cases no. 
- Have a look at our toolkit channels to get an idea #toolkit-general 

#####

**What can the toolkit not do?**
- The toolkit cannot import your old mods to upload them to mod.io. You will have to recreate them
- Script Extender is not compatible with the toolkit
- You cannot create or edit dialogs/quests or levels. These things migth still be possible with third party methods like Script Extender

- As usual, a mix of both the new and the old ways will give you the benefit of both
#####

**My mods are resetting modsettings**
- This is likely due to a bad `meta.lsx`
- The way `meta.lsx` files work changed in patch 7
- Previously it was a `FixedString`, but now it HAS to be a `UUID`. Meaning a uuid created by hand like
- "`1234567-b9e1-430e-8263-MyCoolMod"` is not valid anymore. Replace it with a generated UUID
- Additionally the published version changed from `int32` to `int64` All the way back in early access

#####

**My mod causes  the "failed to compile story" message to appear**
- While ModFixer has been disabled by Larian, this is only the case for ModFixers called `ForceRecompile.txt`
- If your Modfixer has any other name, it will cause this error
- Rename it to `ForceRecompile.txt` if you want your mod to stay comaptible with patch6
- Or remove it entirely if you only want to support Patch7 +

<img src="/mod-use/not_forcerecompile.png" alt="not_forcerecompile.png" width="700" height="200">



## Kaz Virtual Tav

Just like with regular UTav and its additional patches and assets place the files from the mod in the corresponding folder. **COMPATIBLE with any UTav asset AFTER IT HAS BEEN CONVERTED by either the author or yourself**
- WRITTEN CONVERSION GUIDE IS ON KVT [KazVT](https://www.nexusmods.com/baldursgate3/mods/8912) PAGE 
- LSLIB is required for conversion you can find it [here](https://github.com/Norbyte/lslib/releases/tag/v1.19.5) (1.19.5 is Current as of Sept 6 '24) - unzip and double click converter.exe

**For Tattoos:**
`Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\BODY\TATTOO\ named : Skin_Atlas_Body_UNI_Tattoo_A_MSK.DDS`

**For Glowy:**
`Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Generated\Public\Shared\Assets\unique_tav\BODY\GLOWY\ named : UVTT_KAZ_GlowMap_GM.DDS`

**Or, for virtual textures - those that end in  .gts/.gtp** 

If you do not have a folder, like `VirtualTextures` you can create one in here

`Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public\unique_tav\Assets\` 

**For CharacterVisuals Overrides**
`Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public\unique_tav\Content\[PAK]_CharacterVisuals\`

**For body textures:**
`Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public\unique_tav\Assets\VirtualTextures\YourDownloadedFile.gtp`

`Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public\unique_tav\Assets\VirtualTextures\YourDownloadedFile.gts`


If you are a mod author and require assistance porting your Body Textures (IE the HMVY, NM, CLEA), a video guide will be here soon, or head to The [Dev Thread](https://discord.com/channels/1211056047784198186/1231483295452233769) for help!


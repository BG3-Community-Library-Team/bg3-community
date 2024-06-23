---
title: Installing Script Extender
description: How to install Norbyte's Script Extender
published: true
date: 2024-06-23T12:53:44.360Z
tags: installation, moduse, script extender
editor: markdown
dateCreated: 2024-06-21T04:52:35.045Z
---

# <p style="text-align:center">*How to Install Script Extender*</p>

> **Do not Download Script Extender from Nexus. It is an unofficial reupload.**
> **Do not Download Script Extender from any other website except for Norbyte's official GitHub.**
{.is-danger}


## Compatiable Operating Systems

Script Extender is compatiable with the following systems:
- Script Extender works on Windows
- Script Extender works on Steam Deck *
- Script Extender works on Linux *

\* Additional actions necessary. See [4. Installing Script Extender Manually (Linux)](https://wiki.bg3.community/en/Tutorials/Mod-Use/Installing-Script-Extender#h-4-installing-script-extender-manually-linux)

> Mac OS has no official supprt for Script Extender
> Consoles (Playstation, Xbox) have no official supprt for Script Extender
{.is-danger}

## **1. Install Script Extender via BG3MM (Windows)**

The easiest way to install Script Extender (SE) is by using Baldur’s Gate 3 Mod Manager (BG3MM) 

[Click here](https://github.com/LaughingLeader/BG3ModManager/releases) to go to LaughingLeader's official GitHub to download BG3MM. You can use [this guide](/Tutorials/Mod-Use/Installation-Of-BG3MM) this guide to install BG3MM.

To install SE via BG3MM:
- Open BG3MM
- Click *Tools* on the top ribbon
- In the tools drop down menu, click *Download & Extract Script Extender*

<img src="https://lh7-us.googleusercontent.com/kh-PKn8ADbNExFHssRdN3ZwpuBdeFwFqHgDoP7LJZUZOilN0mnNKcOiE4jXbzyECBmAJdm01IFPi7noHuO0jhDZFkgmI8oRecyRfE7XXPYqtxpFCfAtEeSumLuDUm00XHZrhNau6ZNmJbiMaTBEstco" alt="description" width="600" height="auto" />

- After clicking, you will see the following message pop up on the bottom left of your screen.
- Once you see this message confirming the install, close BG3MM and reopen.
- Launch BG3 once and SE will install on its own.

> BG3MM will warn you with a red exclamation mark that SE is not installed **unless** you launch the game once and refresh the manager.
> If you see the yellow SE Symbol (Plunger) it means that BG3MM has recognized that SE is installed.
{.is-warning}

## **2. Install Script Extender Manually (Windows)**

If you do not use BG3MM, download SE directly from Norbyte's GitHub and follow the the steps below.

[Click here to download SE from Norbyte's official GitHub](https://github.com/Norbyte/bg3se/releases)

Simply drag the `DWrite.dll` in your bin folder. On windows this is usually located at 

`C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\bin` or
`C:\Users\yourname\steamapps\common\Baldurs Gate 3\bin` 

Afterwards, launch your game once, and SE should install itself.

> BG3MM will warn you with a red exclamation mark that SE is not installed **unless** you launch the game once and refresh the manager.
> If you see the yellow SE Symbol (Plunger) it means that BG3MM has recognized that SE is installed.
{.is-warning}

## **3. Install Script Extender on Linux/Steam Deck**

> The following instructions are for Linux/Steam Deck.
> Please ignore them if you use windows
{.is-warning}

Download SE directly from Norbyte's GitHub and follow the the steps below.

[Click here to download SE from Norbyte's official GitHub](https://github.com/Norbyte/bg3se/releases)

- Extract the file "Dwrite.dll" to the following locations (Linux or Steam Deck):
  - On **Linux** the path is usually
    - `\home\yourname\.steam\steam\steamapps\common\Baldurs Gate 3\bin` 
  - On **Steam Deck** yourname is usually 
    - `deck` 
    - `\home\deck\.steam\steam\steamapps\common\Baldurs Gate 3\bin` 

- Navigate to the launch options on steam, right click on BG3 in your game library and click `Properties`
![steam_properties.png](/tutorials/install_se/steam_properties.png)
- Add the following command to the launch options on steam (for both Linux/Steam Deck):
> `WINEDLLOVERRIDES="DWrite.dll=n,b" PROTON_NO_ESYNC=1 %command%`
![launch_options.png](/tutorials/install_se/launch_options.png)

- Launch your game once, and SE should install itself.

> BG3MM will warn you that SE is not installed **unless** you launch the game once and refresh the manager.
> BG3MM will sometimes fail to recognize an SE install on Linux/Steam Deck.
> The red exclamation mark and warnings might show even though SE is installed correctly.
{.is-warning}

To verify SE is installed, simply start the game and see if you can spot the Script Extender version on the bottom left in the main menu.

![se_manual_check.png](/tutorials/install_se/se_manual_check.png)

## **4. Activating Script Extender Console (BG3MM)**

To be able to spot errors, or debug your mod and test your functions, the debug console is very useful.

To activate the Script Extender console, you need a *ScriptExtenderSettings.json* file in your bin folder. 

The easiest way to get this file is with BG3MM.

In BG3MM click _Settings_ and _Open Preferences_. Another menu will open.

![](https://lh7-us.googleusercontent.com/06oM1eidUKDnFk-kBwhSC0Ql3_YZMQopntV-4peuFMCsiq02M84cmrjjKdFgOxcDq1sJYOQGHgh6_kZ37ly8aj5O1lcp9Zi7HS7VqPb3Lj685m2qHKJVotbek7j5qUh8Ic0nPKvKc9kLI9aOifTZyh0)

In this menu make sure to activate the setting “Create Console”.

![](https://lh7-us.googleusercontent.com/hMiFp1tEQLqTUEU6EWYCNrluAlZIm3pR9n73I3_r0_AAKZZLk46kiSgOr80cvsrnBRAKH8HsAtiVLbrMkEx-9S90Vjfig_IY9ZzPBVP9XFSQib8zVtXJq2FrG_Uiwd07fDN1WIYeUXhoSbTX1zINRdw)

## **6\. Activating the Script Extender Console (Manually)**

If you cannot use BG3MM, navigate to your *bin* folder.

![](https://lh7-us.googleusercontent.com/5tZaVx55jl3aylYBk3aFKYIhbrkJiAFw3mcRN7-6FOpCnaf3EfBRpcNwbz6DePeJa6K5ftQyUUzCfoK5aziJkkEh7_d9nM9zRjAS9auHw3abifXmatSQ8gSklTK-0zkNkpzSrBe51wEsF6XSKx-mIqk)

In your bin folder, create a file called *ScriptExtenderSettings.json*

![](https://lh7-us.googleusercontent.com/dwCBQnvPfEXIaYIrOSND9i4C28hC_AZn3mrRu3g84ICyPHdNX5NfRwm89FG8zCwTrDeSp41M1nZGI8qaP573KsLkTzMdROgrCUVCHIPzMVTGBbPzNtJB1EdfhEDhunaL584eYLI6fA5-S-tnkqvaUx0)


Paste the following content in the file

```plaintext
{  

"CreateConsole": true

}
```

The result should look like this:

![](https://lh7-us.googleusercontent.com/9yEb3ZrFUz04fYu7n8XBWrk-ANexXGe_hbp_49SPCPzNT6_RpYBLkso6PIeWFV39CQnac4Zmvslcx2G-egM8E2kki7bfZPETVsmMblDDXhBgEFTbfXBWh3Ru3vQIvmF765w4UTkgqcH9VGpyUgwRwVM)



## 7\. Ensure you have activated the Script Extender Console  


When you launch the game now, you should see a second window opening. This is the Script Extender console.


![](https://lh7-us.googleusercontent.com/LeswDxdXyI4gNc4bfLY4Hlz2i2dXnyb1ogSWFOQO25yidO8ol5U5x6vxt8nuWulxRej9CiJk3IQgM1Djh0z03cgT4mn-G45drTxY6qSKnooKZfE-34ahsfLOd3ZN1jlzJJR8VnfSaOYQmzBq46QCbps)


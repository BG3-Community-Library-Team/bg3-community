---
title: Installing Script Extender
description: 
published: false
date: 2024-06-21T04:53:19.912Z
tags: installation, moduse, script extender
editor: markdown
dateCreated: 2024-06-21T04:52:35.045Z
---

p>This tutorial assumes that you know how to install mods and create them. So please familiarize yourself with those topic on the relevant wiki pages:

This tutorial assumes that you know how to install mods and create them. So please familiarize yourself with those topic on the relevant wiki pages:

-   [How to install .pak files](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-Install-Pak-Files) 
-   [How to install .pak files](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-Install-Pak-Files) 
-   [Installing Script Extender and activating the console](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender)

For further information, follow the links in **Useful Resources** on the bottom of this page that this guide is based on**.**

For further information, follow the links in **Useful Resources** on the bottom of this page that this guide is based on**.**

After reading this guide, feel free to follow the tutorial: **Creating your First SE Mod (TBA)**

After reading this guide, feel free to follow the tutorial: **Creating your First SE Mod (TBA)**

## **0\. Installing Script Extender**

The easiest way to install Script extender (SE) is by using the Baldur’s Gate 3 Mod Manager (BG3MM)  

[_https://github.com/LaughingLeader/BG3ModManager/releases_](https://github.com/LaughingLeader/BG3ModManager/releases)

![](https://lh7-us.googleusercontent.com/kh-PKn8ADbNExFHssRdN3ZwpuBdeFwFqHgDoP7LJZUZOilN0mnNKcOiE4jXbzyECBmAJdm01IFPi7noHuO0jhDZFkgmI8oRecyRfE7XXPYqtxpFCfAtEeSumLuDUm00XHZrhNau6ZNmJbiMaTBEstco)

Figure 1: Installing Script Extender with the Baldurs's Gate 3 Mod Manager 

Click “Tools” and “Download & Extract the Script Extender” . 

Afterwards launch your game once and SE should install itself.

If you cannot use BG3MM, download SE directly from github and follow the install instructions

[_https://github.com/Norbyte/bg3se/releases_](https://github.com/Norbyte/bg3se/releases)

## **1\. Activating the Script Extender Console**

To be able to debug your mod and test your functions, the debug console is very useful.

To activate the Script Extender console, you need a *ScriptExtenderSettings.json* file in your bin folder. 

The easiest way to get this file is with BG3MM

![](https://lh7-us.googleusercontent.com/06oM1eidUKDnFk-kBwhSC0Ql3_YZMQopntV-4peuFMCsiq02M84cmrjjKdFgOxcDq1sJYOQGHgh6_kZ37ly8aj5O1lcp9Zi7HS7VqPb3Lj685m2qHKJVotbek7j5qUh8Ic0nPKvKc9kLI9aOifTZyh0)

Figure 2: Opening the settings for activating the Script Extender Console.

In BG3MM click “Settings” and “Open Preferences”. Another menu will open.

![](https://lh7-us.googleusercontent.com/hMiFp1tEQLqTUEU6EWYCNrluAlZIm3pR9n73I3_r0_AAKZZLk46kiSgOr80cvsrnBRAKH8HsAtiVLbrMkEx-9S90Vjfig_IY9ZzPBVP9XFSQib8zVtXJq2FrG_Uiwd07fDN1WIYeUXhoSbTX1zINRdw)

Figure 3: Activating the Script Extender Console with the Baldur's Gate 3 Mod Manager

In this menu make sure to activate the setting “Create Console”.

If you cannot use BG3MM, navigate to your *bin* folder 

![](https://lh7-us.googleusercontent.com/5tZaVx55jl3aylYBk3aFKYIhbrkJiAFw3mcRN7-6FOpCnaf3EfBRpcNwbz6DePeJa6K5ftQyUUzCfoK5aziJkkEh7_d9nM9zRjAS9auHw3abifXmatSQ8gSklTK-0zkNkpzSrBe51wEsF6XSKx-mIqk)

Figure 4: Navigating to the bin folder

![](https://lh7-us.googleusercontent.com/dwCBQnvPfEXIaYIrOSND9i4C28hC_AZn3mrRu3g84ICyPHdNX5NfRwm89FG8zCwTrDeSp41M1nZGI8qaP573KsLkTzMdROgrCUVCHIPzMVTGBbPzNtJB1EdfhEDhunaL584eYLI6fA5-S-tnkqvaUx0)

## 1\. Ensure you have activated the Script Extender Console  

Figure 5: Creating the ScriptExtenderSettings.json file

After following the guide  [How to install Script Extender](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender) and activating the console, ensure that the console is activated.  
When you launch the game now, you should see a second window opening. This is the Script Extender console.

In your bin folder, create a file called *ScriptExtenderSettings.json*

Paste the following content in the file

```plaintext
{  

"CreateConsole": true

}
```

![](https://lh7-us.googleusercontent.com/9yEb3ZrFUz04fYu7n8XBWrk-ANexXGe_hbp_49SPCPzNT6_RpYBLkso6PIeWFV39CQnac4Zmvslcx2G-egM8E2kki7bfZPETVsmMblDDXhBgEFTbfXBWh3Ru3vQIvmF765w4UTkgqcH9VGpyUgwRwVM)

Figure 6: Then content of ScriptExtenderSettings.json

When you launch the game now, you should see a second window opening. This is the Script Extender console.

![](https://lh7-us.googleusercontent.com/LeswDxdXyI4gNc4bfLY4Hlz2i2dXnyb1ogSWFOQO25yidO8ol5U5x6vxt8nuWulxRej9CiJk3IQgM1Djh0z03cgT4mn-G45drTxY6qSKnooKZfE-34ahsfLOd3ZN1jlzJJR8VnfSaOYQmzBq46QCbps)

![](https://lh7-us.googleusercontent.com/LeswDxdXyI4gNc4bfLY4Hlz2i2dXnyb1ogSWFOQO25yidO8ol5U5x6vxt8nuWulxRej9CiJk3IQgM1Djh0z03cgT4mn-G45drTxY6qSKnooKZfE-34ahsfLOd3ZN1jlzJJR8VnfSaOYQmzBq46QCbps)

Figure 7: The Script Extender cosole on game start.

Figure 7: The Script Extender cosole on game start.

If you see this window, it means you have successfully installed SE with console.

If you see this window, it means you have successfully installed SE with console.

## **2\. Familiarizing yourself with the Script Extender Console**

## **2\. Familiarizing yourself with the Script Extender Console**

To familiarize yourself with the usage of the SE console you can execute a few simple commands.

To familiarize yourself with the usage of the SE console you can execute a few simple commands.

These can all be found in the **Useful Resources** at the bottom of this tutorial.
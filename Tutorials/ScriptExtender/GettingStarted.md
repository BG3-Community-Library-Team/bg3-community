---
title: Getting Started with Script Extender
description: 
published: true
date: 2024-05-04T17:54:09.621Z
tags: tutorial, guide, script extender, lua
editor: markdown
dateCreated: 2024-04-30T08:23:34.674Z
---

# **Getting started with Script Extender**

This tutorial covers the absolute basics for modders to start writing mods with [Norbytes Script Extender](https://github.com/Norbyte/bg3se/tree/main). 

No prior knowledge about programming is required; however, please familiarize yourself with how to install mods and Script Extender:

-   [How to install .pak files](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-Install-Pak-Files) 
-   [Installing Script Extender and activating the console](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender)


After reading this guide, feel free to follow the tutorial: [**Creating your First SE Mod (TBA)**](https://wiki.bg3.community/en/Tutorials/ScriptExtender/creating_your_first_se_mod)


> If you are having trouble following this guide, feel free to join the DBTR discord linked [here](hhttps://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-9-useful-resources) for assistance
> DBTR is a community discord. Keep in mind that everyone that may help you is a volunteer. Please read and follow the server rules.
{.is-success}

You can find further information linked under [09. Useful Resources](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-9-useful-resources) on the bottom of this page.



## 1\. Ensure you have activated the Script Extender Console  

After following the guide  [How to install Script Extender](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender) and activating the console, ensure that the console works properly.  
When you launch the game now, you should see a second window opening. This is the Script Extender console.


![gswse_console_startup.png](/tutorials/getting_started_with_se/gswse_console_startup.png)

If you see this window, it means you have successfully installed SE with console.

## **2\. Familiarizing yourself with the Script Extender Console**

To familiarize yourself with the usage of the SE console you can execute a few simple commands.

These can all be found in the [09.Useful Resources](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-9-useful-resources) at the bottom of this tutorial as [Osi functions](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua) .

### **2.1\. Load a save**

You can either start a new game or load an existing save.

When the save is loaded you should see some output in your console, telling you that the session has loaded and other debug statements depending on what kind of mods you have installed:


![gswse_game_loaded.png](/tutorials/getting_started_with_se/gswse_game_loaded.png)


### **2.2\. Activate the input** 

To be able to input commands into the console press enter once.

If you have too much text on your console and you cannot see your input line, you can repeat this a few times until you can see the *S >>* 


![gswse_input_ready.png](/tutorials/getting_started_with_se/gswse_input_ready.png)

### **2.3\. Basic inputs**

Replicate the following steps to familiarize yourself with basic inputs into the SE console:

#### 2.3.1\. In the console enter the following command. This will print “Hello World” on the console:

`
_P(“Hello World”)
`

![](https://lh7-us.googleusercontent.com/ktFR5G6vYetJeqyVYLznc8tmizLM-JMHag7C4esUa-aunS3F9hQsMYGYf9taLyHrsekRm-eS6f6cGGpcXINdu3q4ml7oopyIWRobEqSygFEXZigJZ5TjH7_D9BWZ-bshPhNVE9gKX2DRtWajxHckLDU)


#### 2.3.2\. Add an item to your inventory - Here: 10 Bars of Soap:

` TemplateAddTo("d32a68ff-3b6a-4d83-b0c4-0a2c44b93ea9", GetHostCharacter(), 10) `


![gswse_tempateadd.png](/tutorials/getting_started_with_se/gswse_tempateadd.png)

> You will not see any print statement this time.
> Instead check your characters inventory
{.is-warning}


![gswse_pre_soap.png](/tutorials/getting_started_with_se/gswse_pre_soap.png =600x300)
<div style="margin-left: 250px;"> <span style="font-size: xx-large;">&darr;</span> </div>

![gswse_post_soap.png](/tutorials/getting_started_with_se/gswse_post_soap.png =600x300)


#### 2.3.3\. Get the HostCharacter uuid (the character whose portrait is activated - here: Astarion):

`
_P(Osi.GetHostCharacter())
`

This will print: *c7c13742-bacd-460a-8f65-f864fe41f255* to your console

You will need this command quite often to easily access your character so it's useful to keep it in mind!

![](https://lh7-us.googleusercontent.com/Ef3BwIjlS_T-hgQ3qzfhPUYihqQQoupRColMLaKHZHrTIasa2IBKtdXTBW-trPKG1xya76MIC6WPoAPPNKF4fCaWYO1oKyRC_Y9cut3Rp84lQWDmJYW19hpNEWoAFOCctj5QADY-NQKbgLX12PN30gw)


Now that you are familiar with entering commands in the console, it is time to create your workspace


> Only want to execute a few commands on the console and not interested in creating a mod?
> You can stop here if you are following another guide or jump to 
> [6.Osiris](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#h-6-osiris) for a few examples
{.is-warning}


## **3\. Creating your workspace**


>  For the next steps, please close your game.
{.is-info}


>This guide uses the example workspace found here: https://drive.google.com/file/d/1PP9i2oAI9NZQx4aTooTFIe6laotVvOop/view?usp=sharing
>Using it will make it easier to follow the tutorial.
{.is-warning}



You will also need an editor. I recommend VSCode or the Open Source alternative VSCodium:  
  -   VSCode: [_https://code.visualstudio.com/_](https://code.visualstudio.com/)
  -   VSCodium:[_https://vscodium.com/_](https://vscodium.com/)


Download the example workspace linked above and unpack/unzip it.

### 3.1 Opening your workspace


![](https://lh7-us.googleusercontent.com/y8Vrl86Pnz7b_oGasddrDJuk8zPeVnhq-xUO3FRRZUK5SeolwQOMQwoTOlCIEK9SLOsrV4YYnfSW7JbSBHvL6bmGNPsfn0zNqb3iRvxjPOFKa3BEEiN6LoiyVDF426_KsKdVXYFn0N1N_vpcu4uyTBg)


On Windows 11, right click the folder “MySEMod” after unzipping and click “Open with Code”.

> If you did not specify in the installation of VSCode that "Open with Code" 
> should be added to the context menu in windows, you will not see this option.
> In this case follow the steps below instead.
{.is-info}


If you do not see that option, launch VSCode and open the unzipped workspace as a folder
![gswse_open_file.png](/tutorials/getting_started_with_se/gswse_open_file.png)


Navigate to where  you saved the folder and select it

![gswe_open_file_2.png](/tutorials/getting_started_with_se/gswe_open_file_2.png)


Now you should see the `MYSEMOD` folder in your editor. This is your workspace.

![](https://lh7-us.googleusercontent.com/ZTy0cD3-wymnkpEj99udh1241KM3oJA2nYy0WmwXiIT-Rz6IxFbFdDLKwXsxWppM-MdtATFrNvCieQvlG8KijOWSV7Wyzw0klGSYZx5XVLvxbFkaeSG6JrGDPMYzeRvDKyb6Vg8u8S1BiepaZcitoBw)

### 3.2 Installing Extensions

We will now install a few `Extensions` which will make creating mods a lot easier.
For this click the `Extensions` button on the left. This will open a tab which allows you
to see your installed `Extensions` and install new ones.

![gswse_extensions.png](/tutorials/getting_started_with_se/gswse_extensions.png)

We will first install `BG3 Text Support`, `bg3_mod_helper` and `BG3-SE-Snippets`.
These can be installed by searching for them in the search bar.


![gswse_search_extension.png](/tutorials/getting_started_with_se/gswse_search_extension.png)

Click on the desired `Extension` and a new tab will open. Here click `install`.
Repeat this step for `bg3_mod_helper` and `BG3-SE-Snippets`

![gswse_install.png](/tutorials/getting_started_with_se/gswse_install.png)

If you were not able to find `BG3-SE-Snippets` in the `Extensions` follow the manual install below:
Visit : https://marketplace.visualstudio.com/items?itemName=FallenStar.bg3-se-snippets

Follow the commands listed under **installation**. You can also see specific instructions in the next images.
First, copy the text `ext install FallenStar.bg3-se-snippets`

![gswse_fallen.png](/tutorials/getting_started_with_se/gswse_fallen.png)

Then open VSCode again and press `Ctrl+P`
This will open a small search window on the top
![gswse_ctrlp.png](/tutorials/getting_started_with_se/gswse_ctrlp.png)

paste `ext install FallenStar.bg3-se-snippets` into this field and press enter.
This will automatically install this extension.


![gswse_install_fallen.png](/tutorials/getting_started_with_se/gswse_install_fallen.png)

>If you use VSCodium instead of VSCode you will have to manually install this extension
{.is-info}





### 3.3 Adding your first line

Now navigate back to your explorer by clicking `Explorer`.
You will find a few files here already. 

![gswse_explorer.png](/tutorials/getting_started_with_se/gswse_explorer.png)



Navigate to to `BootstrapServer.lua`

![gswse_bootstrapserver.png](/tutorials/getting_started_with_se/gswse_bootstrapserver.png)


To make sure your mod is active in the game, add a print statement that will execute when the game loads.

![gswse_first_print.png](/tutorials/getting_started_with_se/gswse_first_print.png =600x200)



Adding this print statement causes Script Extender to execute it upon loading the game, letting us know if the mod is active.



### 3.4 Packing your mod

Afterwards, Pak the mod with a tool of your choice.

-   LsLib: [_https://github.com/Norbyte/lslib/releases_](https://github.com/Norbyte/lslib/releases)
-   Modder’s Multitool: [_https://github.com/ShinyHobo/BG3-Modders-Multitool/releases_](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases)

Here we will use lslib. The packing tool is called `ConverterApp.exe`
Navigate to the correct tab `PAK/LSV Tools`


![gswse_lslib_censored.png](/tutorials/getting_started_with_se/gswse_lslib_censored.png =800x400)

Pak the folder with a tool of your choice in the sections `Create Package`



![](https://lh7-us.googleusercontent.com/OZIQx8Cg7rml-UhA0qm3dYzoxrqQWLewDGxch5Z-bLDqvj0_ZBof9MLn--r0wwDUahBy6ln-aR1evQ6Rgv6Nbu2qdPvODuU43w_8AfAoY72vxGM2nArZQDosjYJg79Upc9iC3a6oBNiFjLD93C4VljY)


Add the generated .pak file to your Mods folder and acitvate it and save the load order with your mod manager.

When you see your print statement on game startup, you have successfully loaded your mod.

![](https://cdn.discordapp.com/attachments/1233113869497667684/1233155556643176488/image.png?ex=6631ffdb&is=6630ae5b&hm=a1853663ef6f46b46af9416710ac247d31b4161577405f4b0b9ea1cf963dc462&=)


If you are not able to see this statement, you likely missed one of the steps.

## **4\. Symlinking**

Every time you make a change to your mod, you have to exit the game, repack your mod, and launch the game again to see the effect.
Symlinking is optional, although highly recommended, as it allows you conveniently avoid the aforementioned steps aka hot load your mod.

> If this sounds too complicated, you can also move your workspace into the `Mods` folder in `Data`. 
> For this follow  [4.2\. Alternative to symlinking: Move your project to the Mods folder](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-42-alternative-to-symlinking-move-your-project-to-the-mods-folder)
{.is-success}


### 4.1\. Setting up the Symlink


The following instructions are for Windows. On Linux, simply use `ln -s <workspace> <game files>`

>Due to wiki formatting, the commands had to be divided in separate lines. 
> When you input the commands, please make sure to write all in one line.
{.is-info}


This command is executed in the windows terminal. Type `cmd` in the search bar and execute the program as **administarator**

Type `cmd` in the windows search bar and execute the program as **administrator**
![gswse_admin.png](/tutorials/getting_started_with_se/gswse_admin.png)

Your console should open. This is where you will type your commands
![gswse_cmd2.png](/tutorials/getting_started_with_se/gswse_cmd2.png)



> Using `cmd` in **administrator** mode allows a lot of control over your system.
> Only execute commands here when you are certain what they will do
{.is-warning}


The commands for copying are found in the code block below. Please make sure to modify the commands, accordingly to your username, and direction of your workspace as well as your game. 
A text editor like `Notepad` is recommended to do this.

> The folders **Mods**, **Public** and **Localization** do not exist in a Vanilla game. They will be created by the symlink.
> If they already exist because you installed **loose files** mods, please delete them first, else the command will throw an error.
{.is-info}




```plaintext
// Public folder
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public" 
"C:\Users\YourUsername\path\to\YourModName\Public"

// For code 
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Mods" 
"C:\Users\YourUserName\path\to\YourModName\Mods"

// Loca
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Localization\English\yourLoca.loca" 
"C:\Users\YourUserName\path\to\YourModName\English\YourLoca.loca"
```




> Want to use a tool that creates the links for you? 
> Try [Link Shell Extension](https://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html)
{.is-info}


![gswe_focus_muffin.png](/tutorials/getting_started_with_se/gswe_focus_muffin.png =1100x900)
<div style="margin-left: 300px;"> <i>Image created by Focus and kindly provided by Muffin </i> </div>


> Still stuck? Here are some other resources that explain this step differently
> [Tutorial for Symlinking & Mass File Conversion for hot-testing your mods](https://github.com/ImmortalRDI/Tutorial-SymLink-Convert-HotTest/wiki/3.-Symlink)
{.is-warning}


> To delete the symlink simply delete the linked folder in 
> `\Steam\steamapps\common\Baldurs Gate 3\Data`
{.is-info}


> An automated way of setting up your symlink might be provided in the future
{.is-info}

### 4.2\. Alternative to symlinking: Move your project to the Mods folder


You can also move your project to the `Mods` folder in `Data` instead if you were not able to symlink your folders.


`C:\SteamLibrary\steamapps\common\Baldurs Gate 3\Data\Mods\MySEMod`

in the example below, where you can see the full path to the script it is:

`D:\SteamLibrary\steamapps\common\Baldurs Gate 3\Data\Mods\CBR_Hugs`


![gswse_mods_path.png](/tutorials/getting_started_with_se/gswse_mods_path.png)


> Note that this symlink is for your scripts. If you want to include **.loca** or **.txt** / **.gr2** files
> They need to be placed in a `Localization` and `Public` folder respectively.
> For this follow the guide [How to install manual/loose file mods](https://wiki.bg3.community/Tutorials/Mod-Use/How-to-install-manual-or-loose-file-mods)
{.is-info}


### 4.3\. Verifying the symlink

To verify whether the symlink has been created in the correct space, click your newly created symlink
in `Data`. This should lead you to your workspace folder. 


If you see an error instead or a link to a subfolder, please repeat the steps in [4. Symlinking](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#h-4-symlinking) and make sure your **paths** are correct.


### 4.4\. Testing the symlink

To test whether your symlink has been succesfully created, you can change the print line we have created earlier while having a save loaded.

![](https://lh7-us.googleusercontent.com/tqoF0Aj51oHiApBmLQmI573TEnmElxHsqRPqrVNBQp00vwEVQpRKsnBmBv3XqxdExOTTzJuzfPpD6YXJsenAUk0YODbxn3ab2LD96nROVlldWv8W5XqIydpt5myyIbyayWM2pemVZs8w-kKx_wuLbrs)


Change it to something else so you can recognize the change

![](/tutorials/getting_started_with_se/gswse_18.png)


Then, after activating your SE console again, type `reset` in the console and press enter

![](/tutorials/getting_started_with_se/gswse_19.png)


This will reset the console and all loaded scripts, allowing you to see instant changes of your code.

> Depending on your code, some changes will only apply when the Game session is loaded 
> In that case simply reload the game (F8)
{.is-info}

![](/tutorials/getting_started_with_se/gswse_20.png)


> It has been reported that [Modders Multitool](https://github.com/ShinyHobo/BG3-Modders-Multitool) might get stuck during the indexing step 
> in case symlinked folders are present. 
> If this is an issue for you, simply remove the symlink and create it again after the indexing is done.
{.is-info}


## **5\. Creating multiple files**

Whether you created a symlink or not, you can create multiple files in your workspace 
to help break down your project and for easier navigation.
Let us create a new file by right clicking on the folder "Server" and clicking "New File".
We will name this file `MySecondSEScript.lua`.


**Step 1:** Right click on "Server"
![gswse_21.png](/tutorials/getting_started_with_se/gswse_21.png =800x500)

**Step 2:** Click "New File"
![gswse_22.png](/tutorials/getting_started_with_se/gswse_22.png =800x500)

**Step 3:** Enter the name `MySecondSEScript.lua`

![gswse_24.png](/tutorials/getting_started_with_se/gswse_24.png =800x500)

> All Lua scripts you want to create need to have the ending *.lua*
{.is-info}


**Step 4:** Add the new file to `BootstrapServer.lua` by adding the line

`Ext.Require("Server/MySecondSEScript.lua")`

Only by adding this line will SE know to load the new file. Else it will be ignored.


![gswse_28.png](/tutorials/getting_started_with_se/gswse_28.png =900x400)


> If you do not add your new file to the BootstrapServer.lua it and its contents will not be recognized
{.is-warning}

**Step 5:** Enter some print statements to make sure you can see the difference


![gswse_26.png](/tutorials/getting_started_with_se/gswse_26.png)


**Step 6:** reset the console to see the difference


![gswse_both_loaded.png](/tutorials/getting_started_with_se/gswse_both_loaded.png)



## **6\. Osiris**

> The following section assumes that you have some basic programming and `Lua` knowledge
> If you do no, please follow [The Basics of Lua](https://wiki.bg3.community/Tutorials/ScriptExtender/the_basics_of_lua)
> Experienced programmers might still benefit from it as well since it introduces a few `Lua` quirks
{.is-warning}



Osiris is a programming language used by Larian Studios.[[1]](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#references). Using Norbyte's Script Extender we can interact with Baldur's Gate 3 and manipulate it in a tremendous manner.[[2]](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#references). Here we will have a look at a few simple examples. Specifically Osi.lua[[3]](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#references) and Osi.Events[[4]](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#references) provided by LaughingLeader[[5]](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#references). There are many more functions, but here we focus on the basics.   

### 6.1\. Functions

Here we will introduce a few functions from LaughingLeaders [Osi.lua](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua) file. We will go over how wo call the functions and how to use their output.

#### 6.1.1\. Osi.GetHostCharacter()

Here we will introduce one of the most important functions for testing.
```Osi.GetHostCharacter()``` will return the ```UUID``` of the currently selected character
```lua
---@return CHARACTER character
function Osi.GetHostCharacter() end
```

Here it is being called while Astarion is selected.
Since it returns a `UUID` we want to dump the return value with `_D` so we can see the output.

```lua
_D(Osi.GetHostCharacter())
```

`"c7c13742-bacd-460a-8f65-f864fe41f255"`

#### 6.1.2\. Osi.AddGold()

Our next example will be adding gold to a character

```
---@param inventoryHolder GUIDSTRING
---@param amount integer
function Osi.AddGold(inventoryHolder, amount) end
```

Here we can use `Osi.GetHostCharacter` for the `inventoryHolder` since we know that it returns a `UUID`. 
For the second argument we need an `integer` , that is a non-decimal number.

```lua
Osi.AddGold(Osi.GetHostCharacter(), 999)
```
![gswse_poor.png](/tutorials/getting_started_with_se/gswse_poor.png)

<div style="margin-left: 130px;"> <span style="font-size: xx-large;">&darr;</span> </div>


![gswse_rich.png](/tutorials/getting_started_with_se/gswse_rich.png)

#### 6.1.3\. Osi.GetApprovalRating()

We can not only execute functions that lead to changes in the game, we can also use them to get information.

```lua
---@param ratingOwner CHARACTER
---@param ratedCharacter CHARACTER
---@return integer rating
function Osi.GetApprovalRating(ratingOwner, ratedCharacter) end
```
Here we will select out Tav so they will be the `host character` for the `ratedCharacter`.
For the `ratingOwner` we will choose Astarion. His UUID is `"S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"` 

Since here we  `Get` a value we want to dump it again to see the output.

```lua

_D(Osi.GetApprovalRating("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255", Osi.GetHostCharacter())) 

```

`1` (standard approval)

#### 6.1.4\. Osi.UseSpell()

We can also do more proactive actions with these functions.
Here we will cast a spell.


```lua
---@overload fun(caster:GUIDSTRING, spellID:string, target:GUIDSTRING)
---@param caster GUIDSTRING
---@param spellID string
---@param target GUIDSTRING
---@param target2 GUIDSTRING
function Osi.UseSpell(caster, spellID, target, target2) end
```
This function can be `overloaded`. This means that we can execute it with another set of parameters than listed. We can either use `caster, spellID, target, target2` or `caster, spellID, target`.
We are only interested in hitting one target right now so we will use the second option.

We will use our `Tav` to hit `Astarion` with `Eldritch Blast`

```lua
Osi.UseSpell(Osi.GetHostCharacter(), "Projectile_EldritchBlast" , "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255")
```

![gswse_violence.png](/tutorials/getting_started_with_se/gswse_violence.png =500x300)

> Want to try out more spells? Use https://bg3.norbyte.dev/search?q=type%3Aspell
> to look up their names
{.is-info}



### 6.2\. Events and Listeners

><span style="font-size:24px;">Authors's note: This guide is still a work in progress. Please see <strong>[9. Useful Resources](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-10-useful-resources)</strong> for more information</span>
{.is-success}


> Work in Progress. For now refer to Osi Events: [_https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua_](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua)
{.is-info}


> Work in Progress. For now refer to SE API Documentation: [_https://github.com/Norbyte/bg3se/blob/main/Docs/API.md_](https://github.com/Norbyte/bg3se/blob/main/Docs/API.md)
{.is-info}

For more interactivity we can use `Listeners`. If you followed [3.2 Installing Extensions](https://wiki.bg3.community/Tutorials/ScriptExtender/GettingStarted#h-32-installing-extensions) then you should have `BG3-SE-Snippets` installed. This will allow you to autocomplete listeners. Else you can build them yourself.

## **7\. Script Extender Functions**


> Work in Progress. For now refer to SE IDE Helpers: [_https://github.com/Norbyte/bg3se/blob/main/BG3Extender/IdeHelpers/ExtIdeHelpers.lua_](https://github.com/Norbyte/bg3se/blob/main/BG3Extender/IdeHelpers/ExtIdeHelpers.lua)
{.is-info}

// TODO 
-   Dumping
-   Basically go over the API and heavily credit it
- 	List some useful Ext functions, like \_D(Ext.Entity.Get(GetHostCharacter()).CharacterCreationAppearance) - maybe even in a separate wiki page
- DB_Avatars, \_D(Osi.DB_Players:Get(nil))
- Ext Listeners
- link to imgui page here


// TODO: Explain : and . (Calling the function with itself as the first parameter) -> Maybe something for 8. Using Script Extender Functions instead?  Might fit in the metables section


https://discord.com/channels/98922182746329088/1228009824017453147 (ask for permission to post - original author is not clear)

## **8\. Advanced Information**

-   IMGUI / Devel stuff?


> Done reading? 
> [Create your first SE Mod with me](https://wiki.bg3.community/Tutorials/ScriptExtender/creating_your_first_se_mod) [TBA]
{.is-success}




## 9. Useful Resources

**_Norbyte_**

Norbytes search engine: [_https://bg3.norbyte.dev/_](https://bg3.norbyte.dev/)

Script Extender: [_https://github.com/Norbyte/bg3se/tree/main_](https://github.com/Norbyte/bg3se/tree/main)

SE API Documentation: [_https://github.com/Norbyte/bg3se/blob/main/Docs/API.md_](https://github.com/Norbyte/bg3se/blob/main/Docs/API.md)

SE IDE Helpers: [_https://github.com/Norbyte/bg3se/blob/main/BG3Extender/IdeHelpers/ExtIdeHelpers.lua_](https://github.com/Norbyte/bg3se/blob/main/BG3Extender/IdeHelpers/ExtIdeHelpers.lua)

LsLib: [_https://github.com/Norbyte/lslib_](https://github.com/Norbyte/lslib)

**_FallenStar_**

FallenStar’s VSCode extension: [_https://marketplace.visualstudio.com/items?itemName=FallenStar.bg3-se-snippets_](https://marketplace.visualstudio.com/items?itemName=FallenStar.bg3-se-snippets)

**_LaughingLeader_**

BG3MM: [_https://github.com/LaughingLeader/BG3ModManager_](https://github.com/LaughingLeader/BG3ModManager)

Osi functions: [_https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua_](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua)

Osi Events: [_https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua_](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua)

**_Larian Studios_**

Osiris: [_https://docs.larian.game/Osiris_](https://docs.larian.game/Osiris)

**_DBTR Discord_**

[Down by the river](https://discord.com/channels/766962323037749248/1233113869497667684/1235679160425381888)

**_Me_**

Utils file: 



Credits: 

*Alithea Ancunín* for screenshots, writing and proofreading 
*Cerberry* for screenshots, ideas and feedback
*Chip Chocolate, Legendary Muffin for a multitude* of resources and his knowledge
*ImmortalRD, Schroedingercat and Chip Chocolate, Legendary Muffin* for the [tutorial for Symlinking & Mass File Conversion for hot-testing your mods](https://github.com/ImmortalRDI/Tutorial-SymLink-Convert-HotTest/wiki)
*Padme4000* for reporting the conflict between MMT and symlinks
*simosas* for his millions of useful functions and good company.
*Skiz* for bravely enduring and suffering through this journey with me
*BG3 Modding Communiry Discord* for answering my questions

# References

[1] Osiris: A scripting language by Larian https://docs.larian.game/Osiris_Overview
[2] Norbyte's Script Extender: An API that allows Lua/Osiris scripting for Baldur's gate 3 https://github.com/Norbyte/bg3se
[3] Osi.lua: Osiris calls provided by LaughingLeader https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua
[4] Osi.Events: Osiris events provided by LaughingLeader https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.Events.lua
[5] LaughingLeader: Github link https://github.com/LaughingLeader


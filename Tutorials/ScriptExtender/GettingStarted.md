---
title: Getting Started with Script Extender
description: 
published: true
date: 2024-04-30T19:23:59.168Z
tags: script extender
editor: markdown
dateCreated: 2024-04-30T08:23:34.674Z
---

# **Getting started with Script Extender**

This tutorial covers the absolute basics for modders to start writing mods with Norbytes Script Extender. 

You can start this tutorial even with no knowledge about programming.

This tutorial assumes that you know how to install mods and create them. So please familiarize yourself with those topic on the relevant wiki pages:

-   [How to install .pak files](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-Install-Pak-Files) 
-   [Installing Script Extender and activating the console](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender)

For further information, follow the links in **Useful Resources** on the bottom of this page that this guide is based on**.**

After reading this guide, feel free to follow the tutorial: **Creating your First SE Mod (TBA)**

## 1\. Ensure you have activated the Script Extender Console  

After following the guide  [How to install Script Extender](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender) and activating the console, ensure that the console is activated.  
When you launch the game now, you should see a second window opening. This is the Script Extender console.

![](https://lh7-us.googleusercontent.com/LeswDxdXyI4gNc4bfLY4Hlz2i2dXnyb1ogSWFOQO25yidO8ol5U5x6vxt8nuWulxRej9CiJk3IQgM1Djh0z03cgT4mn-G45drTxY6qSKnooKZfE-34ahsfLOd3ZN1jlzJJR8VnfSaOYQmzBq46QCbps)

Figure 7: The Script Extender cosole on game start.

If you see this window, it means you have successfully installed SE with console.

## **2\. Familiarizing yourself with the Script Extender Console**

To familiarize yourself with the usage of the SE console you can execute a few simple commands.

These can all be found in the **Useful Resources** at the bottom of this tutorial.

### **1\. Load a save**

You can load either a new save or an existing one.

When the save is loaded you should see some output in your console, telling you that the session has loaded and other debug statements depending on what kind of mods you have installed:

![](https://lh7-us.googleusercontent.com/iR7etzru7qjtz99vhl43MuAvDLA6rMfl3hW2YTb-szUwM_mkMwCRW7ZFs-goNRw-LRDUZtA29WRr-qjT7E7UwnhZjQ0clNq36Z0qsEhmENRD9t27Ei_hMwOFBDUB0geN0Cdi1YnWrwyqPUhpEkQQWts)

Figure 8: An example of the Script Extender output when a save is loaded

### **2\. Activate the input** 

To be able to input commands into the console press enter once.

If you have too much text on your console and you cannot see your input line, you can repeat this a few times until you can see the *S >>* 

![](https://lh7-us.googleusercontent.com/QYtqY_84Nny8EeUPFTFzwi820yZ6LzxKsrUYgjnTUOMTcCVVdTcxgKqlYcKeeoQqh-DS7DJA7iwSm5UzYZ0Imj6zZJL4SW-tdXR_IfOj9kdphcgJVzGBKc0U608-PmNwpWZLO31cxUdSPndT_jo0y48)

Figure 9: An activated Script Extender console

### **3\. Basic inputs**

Replicate the following steps to familiarize yourself with basic inputs into the SE console:

**1\. In the console enter the following command. This will print “Hello World” on the console:**

```plaintext
_P(“Hello World”)
```

![](https://lh7-us.googleusercontent.com/ktFR5G6vYetJeqyVYLznc8tmizLM-JMHag7C4esUa-aunS3F9hQsMYGYf9taLyHrsekRm-eS6f6cGGpcXINdu3q4ml7oopyIWRobEqSygFEXZigJZ5TjH7_D9BWZ-bshPhNVE9gKX2DRtWajxHckLDU)

Figure 10: The output of \_P("Hello World")

**2\. Get the HostCharacter uuid (the character whose portrait is activated - here: Astarion):**

```plaintext
_P(Osi.GetHostCharacter())
```

This will print: *c7c13742-bacd-460a-8f65-f864fe41f255* to your console

![](https://lh7-us.googleusercontent.com/Ef3BwIjlS_T-hgQ3qzfhPUYihqQQoupRColMLaKHZHrTIasa2IBKtdXTBW-trPKG1xya76MIC6WPoAPPNKF4fCaWYO1oKyRC_Y9cut3Rp84lQWDmJYW19hpNEWoAFOCctj5QADY-NQKbgLX12PN30gw)

Figure 11: Printing Astarions uuid to the console when he is the active character

Now that you are familiar with entering commands in the console, it is time to create your workspace

## **3\. Creating your workspace**

Download the example workspace here: [https://drive.google.com/file/d/1PP9i2oAI9NZQx4aTooTFIe6laotVvOop/view?usp=sharing](https://drive.google.com/file/d/1PP9i2oAI9NZQx4aTooTFIe6laotVvOop/view?usp=sharing)

And unpack it. Place it where you want to develop your mods. For example in your *Documents* folder on windows.

You will also need an editor. I recommend VSCode or the Open Source alternative VSCodium:

-   VSCode: [_https://code.visualstudio.com/_](https://code.visualstudio.com/)
-   VSCodium:[_https://vscodium.com/_](https://vscodium.com/)

Now you want to open your project.

![](https://lh7-us.googleusercontent.com/y8Vrl86Pnz7b_oGasddrDJuk8zPeVnhq-xUO3FRRZUK5SeolwQOMQwoTOlCIEK9SLOsrV4YYnfSW7JbSBHvL6bmGNPsfn0zNqb3iRvxjPOFKa3BEEiN6LoiyVDF426_KsKdVXYFn0N1N_vpcu4uyTBg)

Figure 12: Opening a folder in VSCode

On Windows 11, right click the folder “MySEMod” after unzipping and click “Open with Code”.

![](https://lh7-us.googleusercontent.com/ZTy0cD3-wymnkpEj99udh1241KM3oJA2nYy0WmwXiIT-Rz6IxFbFdDLKwXsxWppM-MdtATFrNvCieQvlG8KijOWSV7Wyzw0klGSYZx5XVLvxbFkaeSG6JrGDPMYzeRvDKyb6Vg8u8S1BiepaZcitoBw)

Figure 13: The VSCode workspace 

This will open your folder in your editor. You will find a few files here already. 

Navigate to to *BootstrapServer.lua* 

![](https://lh7-us.googleusercontent.com/tqoF0Aj51oHiApBmLQmI573TEnmElxHsqRPqrVNBQp00vwEVQpRKsnBmBv3XqxdExOTTzJuzfPpD6YXJsenAUk0YODbxn3ab2LD96nROVlldWv8W5XqIydpt5myyIbyayWM2pemVZs8w-kKx_wuLbrs)

Figure 14: Adding a print statement to BootstrapServer.lua

To make sure your mod is active in the game, we will add a print statement that will execute when the game loads.

Afterwards, Pak the mod with a tool of your choice. Here we will use lslib.

-   LsLib: [_https://github.com/Norbyte/lslib/releases_](https://github.com/Norbyte/lslib/releases)
-   Modder’s Multitool: [_https://github.com/ShinyHobo/BG3-Modders-Multitool/releases_](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases)

Pak the folder with a tool of your choice

![](https://lh7-us.googleusercontent.com/OZIQx8Cg7rml-UhA0qm3dYzoxrqQWLewDGxch5Z-bLDqvj0_ZBof9MLn--r0wwDUahBy6ln-aR1evQ6Rgv6Nbu2qdPvODuU43w_8AfAoY72vxGM2nArZQDosjYJg79Upc9iC3a6oBNiFjLD93C4VljY)

Figure 15: Paking the workspace with lslib

Add the generated .pak file to your Mods folder and acitvate it and save the load order with your mod manager.

When you see your print statement on game startup, you have successfully loaded your mod.

![](https://cdn.discordapp.com/attachments/1233113869497667684/1233155556643176488/image.png?ex=6631ffdb&is=6630ae5b&hm=a1853663ef6f46b46af9416710ac247d31b4161577405f4b0b9ea1cf963dc462&=)

Figure 16: The print statement showing that your mod is active

If you are not able to see this statement, you likely missed one of the steps.

## **4\. Symlinking**

### 1\. Setting up the Symlink

For you to not have to repack your mod every time you make a change, you can symlink your folders.

The following instructions are for Windows. On Linux, simply use `ln -s <workspace> <game files>`

Because of the formatting of the wiki, the commands had to be placed on separate lines. When you input the commands, please make sure to write all in one line.

The commands for copying can be seen below the code block.  Please make sure to modify the commands for your username and place of your workspace and game.

```plaintext
// Public folder
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Public" 
"C:\Users\YourUsername\Desktop\BG3 Modding\YourModName\Public"

// For code 
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Mods" 
"C:\Users\YourUserName\Desktop\BG3 Modding\YourModName\Mods"

// Loca
mklink /D "C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data\Localization\English\yourLoca.loca" 
"C:\Users\YourUserName\Desktop\BG3 Modding\YourModName\English\YourLoca.loca"
```

mklink /D "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\Public" "C:\\Users\\YourUsername\\Desktop\\BG3 Modding\\YourModName\\Public"

mklink /D "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\Mods" "C:\\Users\\YourUserName\\Desktop\\BG3 Modding\\YourModName\\Mods"

mklink /D "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\Localization\\English\\yourLoca.loca" "C:\\Users\\YourUserName\\Desktop\\BG3 Modding\\YourModName\\English\\YourLoca.loca"

### 2\. Testing the symlink

To test whether your symlink has been succesfully created, you can change the print line we have created earlier while having a save loaded.

![](https://lh7-us.googleusercontent.com/tqoF0Aj51oHiApBmLQmI573TEnmElxHsqRPqrVNBQp00vwEVQpRKsnBmBv3XqxdExOTTzJuzfPpD6YXJsenAUk0YODbxn3ab2LD96nROVlldWv8W5XqIydpt5myyIbyayWM2pemVZs8w-kKx_wuLbrs)

Figure 17: The print statement you have added previously

Change it to something else so you can recognize the change

![](/tutorials/getting_started_with_se/gswse_18.png)

Figure 18: Changed text for the print message

Then, after activating your SE console again, type `reset` in the console and press enter

![](/tutorials/getting_started_with_se/gswse_19.png)

Figure 19: The reset command

This will reset the console and all loaded scripts, allowing you to see instant changes of your code.

> Depending on your code, some changes will only apply when the Game session is loaded 
> In that case simply reload the game (F8)
{.is-info}

![](/tutorials/getting_started_with_se/gswse_20.png)
## **5\. The Basics of Programming**

The following section is aimed towards people who have no programming knowledge.

If you don't know what a function is, you might want to read through this. If you have worked with other programmig languages before, feel free to skip this section but make sure to read up on Lua syntax.

> It is recommended to not only read this section but to follow along. 
> Also try typing some of these commands instead of using copy and paste
> to better familiarize yourself with them
{.is-info}

Use the example mod "MySEMod" to follow along by typing in "MyFirstSEScript.lua" and resetting the console to see the changes.

### 1\. Order of execution

Any script that you write will be executed from top to bottom.

```lua
print("Hello World")
print("My name is YourName")
```

`
Hello World`
`My name is YourName
`

This means that anything you define and want to refer to has to be declared before you will use it

```lua
local myName = "YourName"
print("My name is ", myName)
```
`My name is YourName`

When you use a variable before you have defined it, the program won't know what to do with it

```lua
print("My name is ", myName)
local myName = "YourName"
```

`My name is nil`


> *nil* in Lua means *nothing*
{.is-info}

### 2\. Variables 

You can use variables to refer to cerain values.
This has many applications. For example in BG3 we often use unique IDs (UUIDs) to refer to characters, objects, items and more. 
For you to not have to retype these same long strings and maybe make mistakes, we can use variables

```lua
local astarion = "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"
print("Astarions ID is ", astarion)
```


`Astarions ID is         S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255`

> By default a value in Lua is global if you do not use the *local* keyword
> In most cases you want your variables to be *local* 
{.is-info}

### 3\. A very special data structure: tables

You might have heard of some data strucutres like "arrays" or "lists" before.
In Lua we use a so called "table" for all of these instances.

> Paste the following function at the top of your *MyFirstSEScript.lua*  so you can use it
{.is-info}

```lua
local function printMyTable(table)
    for x,y in pairs(table) do
       print(x, " ", y)
    end
end

```

Example usage:
```lua
printMyTable(myTable)
```

> To see the changes in your tables, use the *printMyTable* function after every change!
{.is-info}

#### 1\. The basics

You can create a new table by instantiating an empty one

```lua
local myTable = {}
```

` ` (empty output)

You can also pre fill the table
```lua
local myTable = {"Cheese", "Bread", "Wine"}
```
`1 Cheese`
`2 Bread`
`3 Wine`

You can add items to a table
```lua
table.insert(myTable, "Grapes")
```

`1 Cheese`
`2 Bread`
`3 Wine`
`4 Grapes`

You can delete the last item from a table

```lua
table.remove(myTable)
```

`1 Cheese`
`2 Bread`
`3 Wine`

You can delete an item from a table based on its index (position)

```lua
table.remove(myTable, 1)
```

`1 Bread`
`2 Wine`

#### 2\. Iterating over a table

To be able to access all components, we want to iterate over the tables.
This is what we are doing in the *printMyTable *function.


```lua
for x,y in pairs(myTable) do
	 print(x, " ", y)
end
```


`1 Bread`
`2 Wine`


#### 3\. Different types of tables


##### 1\. Arrays

The tables in the example above can fir the description of an "array". They consist of an index and an entry


```lua
local myTable = {"Cheese", "Bread", "Wine"}
```
`1 Cheese`
`2 Bread`
`3 Wine`


```lua
print("The first entry in myTable is ", myTable[1])
```
`The first entry in myTable is   Cheese`

##### 1\. Maps


```lua
ORIGINS = {
    ["Wyll"] = "S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d",
    ["ShadowHeart"] = "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679",
    ["Laezel"] = "S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12",
    ["Astarion"] = "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255",
    ["Gale"] = "S_Player_Gale_ad9af97d-75da-406a-ae13-7071c563f604",
    ["Karlach"] = "S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c",
}
```


`Wyll            S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d`
`Karlach         S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c`
`Astarion                S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255`
`Laezel          S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12`
`ShadowHeart             S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679`
`Gale            S_Player_Gale_ad9af97d-75da-406a-ae13-7071c563f604`


```lua
print("Wylls UUID is ", ORIGINS["Wyll"])
```

`Wylls UUID is   S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d`



##### 1\. Sets


```lua
local creatures = {
    ["Goblin"] = true,
    ["Skeleton"] = true,
    ["Elf"] = true
    }
```


`Elf             true`
`Goblin          true`
`Skeleton         true`

```lua
print("Is Elf part of creatures? ", creatures["Elf"])
print("Is Dragonborn part of creatures? ", creatures["Dragonborn"])
``` 

`Is Elf part of creatures?       true`
`Is Dragonborn part of creatures?        nil`


> In a lot of cases *nil* will give you the same result as *false*
{.is-info}

#### 4\. Tables within tables

Tables are very 

###### Example 1

local spells = {
    ["fire"] = {
        "Fireball",
        "Flame Strike",
        "Wall of Fire"
    },
    ["ice"] = {
        "Ice Storm",
        "Cone of Cold",
        "Freeze"
    }
}



###### Example 2

- myEntry = {name = fijifjf, somethingElse = fhufhifh} 
- tzhen put that in a table


Please note that these are just some examples. Feel free to experiment and choose the type of table that fits your data


### 4\. Scope 

#### 4.1 Variables

#### 4.2 Functions

#### 4.3 A brief introduction to metatables

### 5\. Functions

### 6\. If statements

### 7\. Loops

### 8\. Debugging using print statements

## **6\. Osiris**

### 1\. Functions

### 2\. Events

### 3\. Using Listeners

## **7\. Script Extender Functions**

-   Dumping
-   Basically go over the API and heavily credit it

## **8\. Advanced Information**

-   IMGUI / Devel stuff?

## **9\. Useful Resources**

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
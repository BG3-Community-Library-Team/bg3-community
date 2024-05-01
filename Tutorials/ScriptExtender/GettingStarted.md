---
title: Getting Started with Script Extender
description: 
published: true
date: 2024-05-01T16:27:59.549Z
tags: tutorial, guide, script extender, lua
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

After reading this guide, feel free to follow the tutorial: [**Creating your First SE Mod (TBA)**](https://wiki.bg3.community/en/Tutorials/ScriptExtender/creating_your_first_se_mod)


## 1\. Ensure you have activated the Script Extender Console  

After following the guide  [How to install Script Extender](https://wiki.bg3.community/en/Tutorials/Mod-Use/How-to-install-Script-Extender) and activating the console, ensure that the console is activated.  
When you launch the game now, you should see a second window opening. This is the Script Extender console.

![](https://lh7-us.googleusercontent.com/LeswDxdXyI4gNc4bfLY4Hlz2i2dXnyb1ogSWFOQO25yidO8ol5U5x6vxt8nuWulxRej9CiJk3IQgM1Djh0z03cgT4mn-G45drTxY6qSKnooKZfE-34ahsfLOd3ZN1jlzJJR8VnfSaOYQmzBq46QCbps)


If you see this window, it means you have successfully installed SE with console.

## **2\. Familiarizing yourself with the Script Extender Console**

To familiarize yourself with the usage of the SE console you can execute a few simple commands.

These can all be found in the **Useful Resources** at the bottom of this tutorial.

### **1\. Load a save**

You can load either a new save or an existing one.

When the save is loaded you should see some output in your console, telling you that the session has loaded and other debug statements depending on what kind of mods you have installed:

![](https://lh7-us.googleusercontent.com/iR7etzru7qjtz99vhl43MuAvDLA6rMfl3hW2YTb-szUwM_mkMwCRW7ZFs-goNRw-LRDUZtA29WRr-qjT7E7UwnhZjQ0clNq36Z0qsEhmENRD9t27Ei_hMwOFBDUB0geN0Cdi1YnWrwyqPUhpEkQQWts)


### **2\. Activate the input** 

To be able to input commands into the console press enter once.

If you have too much text on your console and you cannot see your input line, you can repeat this a few times until you can see the *S >>* 

![](https://lh7-us.googleusercontent.com/QYtqY_84Nny8EeUPFTFzwi820yZ6LzxKsrUYgjnTUOMTcCVVdTcxgKqlYcKeeoQqh-DS7DJA7iwSm5UzYZ0Imj6zZJL4SW-tdXR_IfOj9kdphcgJVzGBKc0U608-PmNwpWZLO31cxUdSPndT_jo0y48)


### **3\. Basic inputs**

Replicate the following steps to familiarize yourself with basic inputs into the SE console:

**1\. In the console enter the following command. This will print “Hello World” on the console:**

```plaintext
_P(“Hello World”)
```

![](https://lh7-us.googleusercontent.com/ktFR5G6vYetJeqyVYLznc8tmizLM-JMHag7C4esUa-aunS3F9hQsMYGYf9taLyHrsekRm-eS6f6cGGpcXINdu3q4ml7oopyIWRobEqSygFEXZigJZ5TjH7_D9BWZ-bshPhNVE9gKX2DRtWajxHckLDU)

**2\. Get the HostCharacter uuid (the character whose portrait is activated - here: Astarion):**

```plaintext
_P(Osi.GetHostCharacter())
```

This will print: *c7c13742-bacd-460a-8f65-f864fe41f255* to your console

![](https://lh7-us.googleusercontent.com/Ef3BwIjlS_T-hgQ3qzfhPUYihqQQoupRColMLaKHZHrTIasa2IBKtdXTBW-trPKG1xya76MIC6WPoAPPNKF4fCaWYO1oKyRC_Y9cut3Rp84lQWDmJYW19hpNEWoAFOCctj5QADY-NQKbgLX12PN30gw)


Now that you are familiar with entering commands in the console, it is time to create your workspace

## **3\. Creating your workspace**

Download the example workspace here: [https://drive.google.com/file/d/1PP9i2oAI9NZQx4aTooTFIe6laotVvOop/view?usp=sharing](https://drive.google.com/file/d/1PP9i2oAI9NZQx4aTooTFIe6laotVvOop/view?usp=sharing)

And unpack it. Place it where you want to develop your mods. For example in your *Documents* folder on windows.

You will also need an editor. I recommend VSCode or the Open Source alternative VSCodium:

-   VSCode: [_https://code.visualstudio.com/_](https://code.visualstudio.com/)
-   VSCodium:[_https://vscodium.com/_](https://vscodium.com/)

Now you want to open your project.

![](https://lh7-us.googleusercontent.com/y8Vrl86Pnz7b_oGasddrDJuk8zPeVnhq-xUO3FRRZUK5SeolwQOMQwoTOlCIEK9SLOsrV4YYnfSW7JbSBHvL6bmGNPsfn0zNqb3iRvxjPOFKa3BEEiN6LoiyVDF426_KsKdVXYFn0N1N_vpcu4uyTBg)


On Windows 11, right click the folder “MySEMod” after unzipping and click “Open with Code”.

![](https://lh7-us.googleusercontent.com/ZTy0cD3-wymnkpEj99udh1241KM3oJA2nYy0WmwXiIT-Rz6IxFbFdDLKwXsxWppM-MdtATFrNvCieQvlG8KijOWSV7Wyzw0klGSYZx5XVLvxbFkaeSG6JrGDPMYzeRvDKyb6Vg8u8S1BiepaZcitoBw)

This will open your folder in your editor. You will find a few files here already. 

Navigate to to `BootstrapServer.lua`

![](https://lh7-us.googleusercontent.com/tqoF0Aj51oHiApBmLQmI573TEnmElxHsqRPqrVNBQp00vwEVQpRKsnBmBv3XqxdExOTTzJuzfPpD6YXJsenAUk0YODbxn3ab2LD96nROVlldWv8W5XqIydpt5myyIbyayWM2pemVZs8w-kKx_wuLbrs)


To make sure your mod is active in the game, we will add a print statement that will execute when the game loads.

Afterwards, Pak the mod with a tool of your choice. Here we will use lslib.

-   LsLib: [_https://github.com/Norbyte/lslib/releases_](https://github.com/Norbyte/lslib/releases)
-   Modder’s Multitool: [_https://github.com/ShinyHobo/BG3-Modders-Multitool/releases_](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases)

Pak the folder with a tool of your choice

![](https://lh7-us.googleusercontent.com/OZIQx8Cg7rml-UhA0qm3dYzoxrqQWLewDGxch5Z-bLDqvj0_ZBof9MLn--r0wwDUahBy6ln-aR1evQ6Rgv6Nbu2qdPvODuU43w_8AfAoY72vxGM2nArZQDosjYJg79Upc9iC3a6oBNiFjLD93C4VljY)


Add the generated .pak file to your Mods folder and acitvate it and save the load order with your mod manager.

When you see your print statement on game startup, you have successfully loaded your mod.

![](https://cdn.discordapp.com/attachments/1233113869497667684/1233155556643176488/image.png?ex=6631ffdb&is=6630ae5b&hm=a1853663ef6f46b46af9416710ac247d31b4161577405f4b0b9ea1cf963dc462&=)


If you are not able to see this statement, you likely missed one of the steps.

## **4\. Symlinking**

### 1\. Setting up the Symlink

For you to not have to repack your mod every time you make a change, you can symlink your folders.

The following instructions are for Windows. On Linux, simply use `ln -s <workspace> <game files>`

Because of the formatting of the wiki, the commands had to be placed on separate lines. When you input the commands, please make sure to write all in one line.

The commands for copying can be seen below the code block.  Please make sure to modify the commands for your username and place of your workspace and game.

> This command is executed in the windows terminal
>  in the search bar type `cmd` and execute the program as administarator
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

mklink /D "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\Public" "C:\\Users\\YourUsername\\path\\to\\YourModName\\Public"

mklink /D "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\Mods" "C:\\Users\\YourUserName\\path\\to\\YourModName\\Mods"

mklink /D "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data\\Localization\\English\\yourLoca.loca" "C:\\Users\\YourUserName\\path\\to\\YourModName\\English\\YourLoca.loca"

### 2\. Testing the symlink

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

## **5\. Creating multiple files**

You might have already noticed that you can create multiple files in your workspace.
This often helps to break down your project and make it easier to navigate. 
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


**Step 4:** Add the new file to `BootstrapServer.lua`


![gswse_28.png](/tutorials/getting_started_with_se/gswse_28.png =800x400)


> If you do not add your new file to the BootstrapServer.lua it and its contents will not be recognized
{.is-warning}

**Step 5:** Enter some print statements to make sure you can see the difference


![gswse_26.png](/tutorials/getting_started_with_se/gswse_26.png)


**Step 6:** reset the console to see the difference

![gswse_27.png](/tutorials/getting_started_with_se/gswse_27.png =800x100)



## **6\. The Basics of Programming**

**// TODO - This has to be moved to a separate wiki page**

The following section is aimed towards people who have no programming knowledge.

If you don't know what a function is, you might want to read through this. If you have worked with other programmig languages before, feel free to skip this section but make sure to read up on Lua syntax.

> It is recommended to not only read this section but to follow along. 
> Also try typing some of these commands instead of using copy and paste
> to better familiarize yourself with them
{.is-info}

Use the example mod "MySEMod" to follow along by typing in `MyFirstSEScript.lua` and resetting the console to see the changes.

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

> Paste the following function at the top of your `MyFirstSEScript.lua`  so you can use it
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

> To see the changes in your tables, use the `printMyTable` function after every change!
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
This is what we are doing in the `printMyTable` function.


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


> In most programming languages we start counting at 0, but in Lua we start at 1
{.is-info}

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

Tables are very flexible and allow varied structuring. Below you can see two more examples.
Note that because of the nested structure, our printMyTable function does not work anymore.
Instead we can use `_D` to "dump" the whole table and write special loops for them.

###### Example 1

```lua
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

_D(spells)
```


`{`
 &nbsp;    &nbsp; &nbsp; ` "fire" :`
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ` [`
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      `   "Fireball",`
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      ` "Flame Strike",`
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ` "Wall of Fire"`
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `    ],`
  &nbsp;    &nbsp; &nbsp; `      "ice" :`
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `     [`
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     `     "Ice Storm",`
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        `   "Cone of Cold",`
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ` "Freeze"`
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      `  ]`
`}`



```lua
for element, spellList in pairs(spells) do
    print(element, " spells:") 
    for _, spell in ipairs(spellList) do
        print(spell) 
    end
end
```

`ice      spells:`
`Ice Storm`
`Cone of Cold`
`Freeze`

`fire     spells:`
`Fireball`
`Flame Strike`
`Wall of Fire`


###### Example 2

```lua
local companion1 = {name = "Astarion", class = "Rogue"}
local companion2 = {name = "Gale", class = "Wizard"}
local companion3 = {name = "Karlach", class = "Barbarian"}

local myParty = {companion1, companion2, companion3}

_D(myParty)
```

`output`


`[`
     &nbsp;    &nbsp; &nbsp;  ` {`
           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `    "class" : "Rogue",`
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     `  "name" : "Astarion"`
   &nbsp;    &nbsp; &nbsp;   `  },`
 &nbsp;    &nbsp; &nbsp;     `  {`
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    `    "class" : "Wizard",`
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ` "name" : "Gale"`
  &nbsp;    &nbsp; &nbsp;    `  },`
 &nbsp;    &nbsp; &nbsp;   `    {`
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     `    "class" : "Barbarian",`
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       `  "name" : "Karlach"`
    &nbsp;    &nbsp; &nbsp;    `}`
`]`

```lua

for _,entry in pairs(myParty) do
 		print("Name = ", entry.name, " class = ", entry.class)
end
```

`Name =  Astarion         class =        Rogue`
`Name =  Gale     class =        Wizard`
`Name =  Karlach  class =        Barbarian`

Please note that these are just some examples. Feel free to experiment and choose the type of table that fits your data


### 4\. Scope 

As you have already learned in **1. Order of executions** your variables are not available everywhere in your program.
The order of execution is not the only thing that defines this.

#### 4.1 Scope within a file

Within one file, a variable might be declared above its usage but still not available.
This happens when it is declared in its own *scope*

```lua
-- returns Astarions UUID
local function getAstarion()
	local astarionUUID = "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"
  return astarionUUID
end

print(astarionUUID)

```

`nil`

In this case `astarionUUID` is not known outside of its scope.
If we want to access `astarionUUID` directly we can instantiate it outside of the scope of the function

```lua

local astarionUUID = "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"
print(astarionUUID)

```

`S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255`

This also means that when a variable is instantiated within one function, it is not known in any other functions

```lua
-- returns Shadowhearts UUID
local function getShart()
	local shartUUID = "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679"
  return shartUUID
end

-- prints Shadowhearts UUID
local function printShart()
	print(shartUUID)
end

printShart()

```

`nil`

It is accessible again when we declare it outside of the scope of the function


```lua
local shartUUID = "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679"

-- prints Shadowhearts UUID
local function printShart()
	print(shartUUID)
end

printShart()

```

`S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679`

This also means that we can reuse names as long as they exist in different scopes

```lua

-- returns Shadowhearts UUIS
local function getShart()
	local uuid = "S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679"
  return  uuid
end

-- returns Astarions UUID
local function getAstarion()
	local uuid = "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"
  return uuid
end


print(getShart())
print(getAstarion())

```

`S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c67`
`S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255`


If one variable is defined in the outer scope it will get overwritten if it is being reused.

```lua
local karlach =  "S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c"

local function switchKarlachWithLaezel()
	karlach = "S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12"
end

switchKarlachWithLaezel()

print(karlach)
```

`S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12`


#### 4.2 Scope across files

if you have followed **5. Creating multiple files** then you have two files in your "Server". `MyFirsSEScript.lua` and `MySecondSEScript.lua`

Not all variables and functions that you create in one file will be visible in the other one.


Create a variable in  `MyFirsSEScript.lua`

```lua
-- MyFirstSEScript.lua

local gale =  "S_Player_Gale_ad9af97d-75da-406a-ae13-7071c563f604"
```

Try to access it in  `MySecondSEScript.lua`

```lua
-- MySecondSEScript.lua

print(gale)
```

`nil`


Because of the `local` keyword, the variable is not accessible in other files.
For that we have to make it a global variable by omitting the `local` keyword.

Create a variable in  `MyFirsSEScript.lua`

```lua
-- MyFirstSEScript.lua

Gale =  "S_Player_Gale_ad9af97d-75da-406a-ae13-7071c563f604"
```

Try to access it in  `MySecondSEScript.lua`

```lua
-- MySecondSEScript.lua

print(Gale)
```

`S_Player_Gale_ad9af97d-75da-406a-ae13-7071c563f604`

> Global variables and functions usually start with an uppercase letter to distinguish them form local ones
{.is-info}

The same rules appy to functions


Create a function in  `MyFirsSEScript.lua`

```lua
-- MyFirstSEScript.lua

local function getWyll()
	return "S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d"
end
```

Try to access it in  `MySecondSEScript.lua`

```lua
-- MySecondSEScript.lua

print(getWyll())
```



`bg3se::lua::State::LoadScript(): Failed to execute script: [string "MySEMod/Server/MySecondSEScript.lua"]:1: attempt to call a nil value (global 'getWyll')`


Here we have to make the function global as well to access it from other files

Create a function in  `MyFirsSEScript.lua`

```lua
-- MyFirstSEScript.lua

function GetWyll()
	return "S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d"
end
```

Try to access it in  `MySecondSEScript.lua`

```lua
-- MySecondSEScript.lua

print(GetWyll())
```

`S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d`

> It is best practice to keep the content in your files separate most of the time.
> Some content that will never change, like the ORIGIN UUIDs  you might want to keep global in a separate *Data* folder
{.is-info}



### 4\. Functions

You can use fuctions when you have to execute the same code multiple times.
This allows you to reuse your code without having to copy and paste it.
You will be less likely to make mistakes and your code will be easier to maintain


A function can be declared by using the keyword `function`. Then its `name` and parenthesis `()`.
It always has to end with `end`


```lua

local function printAstarion()
	print("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255")
end

```

Optionally you can also add parameters to your function to make it more flexible.
In this case `companion`

```lua

local function printKarlachOrLaezel(companion)

	if companion == "Karlach" then
		print("S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c")
    
  elseif companion == "Laezel" then
 	 	print("S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12")
    
  else
  	print("Not Karlach or Laezel")
  end
end

```

You might want to add some descriptions to your functions so you and other people know what it does, what input it takes and what it returns.

```lua
-- prints Astarions uuid
local function printAstarion()
	print("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255")
end

-- prints Karlachs or Laezels uuid. Else prints an error message
---@param name string
local function printKarlachOrLaezel(companion)

	if companion == "Karlach" then
		print("S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c")
    
  elseif companion == "Laezel" then
 	 	print("S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12")
    
  else
  	print("Not Karlach or Laezel")
  end
end

```

To call a function, simply type its name with the parenthesis.

```lua

printAstarion()

```

`S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255`


If you have added parameters for your function, then make sure to also include those.

```lua

printKarlachOrLaezel("Karlach")
printKarlachOrLaezel("Laezel")
printKarlachOrLaezel("Gale")

```

`S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c`
`S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12`
`Not Karlach or Laezel`



Functions can also return values. You can save these return values in a variable to use later

```lua


-- returns Astarions uuid
---@return uuid string
local function getAstarion()
	return "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"
end
```

```lua
local astarion = getAstarion()

print(astarion)
```

` S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255 ` 

This also works for functions that take parameters


```lua

-- returns Karlachs or Laezels uuid. Else returns nil
---@param name string
local function getKarlachOrLaezel(companion)

	if companion == "Karlach" then
		return "S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c"
    
  elseif companion == "Laezel" then
 	 	return "S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12"

  end
end

```

```lua
local karlach = getKarlachOrLaezel("Karlach")
local laezel = getKarlachOrLaezel("Laezel")
local gale = getKarlachOrLaezel("Gale")

print(karlach)
print(laezel)
print(gale)
```

`S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c`
`S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12`
`nil`


### 5\. If statements

For now we have written code that always executes the same way.
To be able to make it more interactive we can use **flow statements** to change the way our code is executed. 
First we will have a look at if statements.

The general structure of an if statement is 

```lua
if condition then
	-- Your code
end
```

`condition` has to evaluate to `true` for the code underneath the if statement to be executed.
Here are some examples for conditions that evaluate to `true`

```lua

if 1 == 1 then
	print("1 is indeed equal to 1")
end

if "Astarion" then
	print("Astarion exists")
end
```

`1 is indeed equal to 1`

`Astarion exists`


> In Lua, when a value exists, it will automatically evaluate to true.
> That is why "Astarion" evaluates to true
{.is-info}

If `condition` evaluates to `false` then the code underneath the if statement is not executed.
Here are some examples for conditions that evaluate to `false`

```lua

if 0 == 1 then
	print("0 is indeed equal to 1")
end

if nil then
	print("Astarion exists")
end
```

` ` (empty output)


> In Lua, when a value does not exist, it will automatically evaluate to false.
>  Since `nil` means nothing, our condition evaluates to false
{.is-info}

To be able to use your if statement flexibly, you do not want to predefine the condition

```lua

local myNumber = 5

if myNumber == 5 then
	print("My number is 5")
end

```

`My number is 5` 

You can have your if statement in a function to make it even more flexible

```lua

local myFour = 4
local myFive = 5

-- prints "Yes" if the number is five, else prints "No"
---@param number int
local function isItFive(number)
	if number == 5 then
		print("Yes")
    else
  	    print("No")
    end
end

isItFive(myFour)
isItFive(myFive)

```

`No` 
`Yes`

You can also check for something to `not` be true by using the `~=` operator


```lua

local myNumber = 0

if myNumber ~= 5 then
	print("My number is not 5")
end

```

`My number is not 5` 

You can also use multiple conditions in your statement to check if either one `or` another condition is true


```lua

local x = 0
local y = 1

if x == 1 or y == 1 then
	print("Either x or y are 1")
end

```

`Either x or y are 1` 

You can also use multiple conditions in your statement to check if one `and` another condition are true


```lua

local x = 1
local y = 1

if x == 1 and y == 1 then
	print("Both x and y are 1")
end

```

`Both x and y are 1` 

You can stack as many of these statements as you like.

> Beware of a common pitfall when evaluating conditions!
> Since the existence of a value is enough to have it evaluate to true
> never forget to actually compare it to the desited value.
{.is-warning}

```lua

local x = 0
local y = 0

if 1 == x or y then
	print("Either x or y are 1")
end

```

`Either x or y are 1`  (wrong output!)

Even though when reading the statement `if 1 == x or y then` out loud, it might seem like we are comparing both `x` and `y` to `1`, we are not. We are comparing `x` to `1` and checking if `y` simply exists. 

Your variables always have to be compared to the desired value 

```lua

local x = 0
local y = 0

if 1 == x or 1 == y then
	print("Either x or y are 1")
end

```

` ` (empty output - correct!) 

You are not simply restricted to one case with if statements. Using `elseif` you can check if multiple things are true

```lua

local x = 5

if x == 1 then
    print("x is 1")
elseif x == 2 then
    print("x is 2")
elseif x == 3 then
    print("x is 3")
elseif x == 4 then
    print("x is 4")
elseif x == 5 then
    print("x is 5")
else
    print("x is not between 1 and 5")
end


```

`x is 5`



<span style="font-size:24px;">Authors's note: This guide is still a work in progress. Please see <strong>10. Useful Resources</strong> for more information</span>


### 6\. Loops

### 7\. Debugging using print statements

### 8\. A brief introduction to metatables





> This section is about a slightly advanced topic. Feel free to skip it if it sounds too complicated.
> It can be helpful to come back here when your projects grow in size since we discuss one concept of 
> Object-Oriented-Programming (OOP) - read more here:  https://en.wikipedia.org/wiki/Object-oriented_programming
{.is-warning}


Lua is a very flexible language. Through its usage of tables multiple OOP concepts like Inheritance can be realized.
Here we will talk about *Metatables* which is the Lua equivalent of *Objects*.

For this section we will rename `MyFirstSEScript.lua` to `Main.lua` and 
`MySecondSEScript.lua` to `Companion.lua`  , to better showcase this principle.



> **Note:** Make sure to also modify the script names in `BootstrapServer.lua`.
> `Companion.lua` must be loaded before `Main.lua` since we use components of `Companion.lua` in `Main.lua`.
>
>```lua
>Ext.Require("Server/Companion.lua")
>Ext.Require("Server/Main.lua")
>```
{.is-info}


in `Companion.lua`  we will now build a `Companion`
First we have to create our metatable

```lua


-- Companion.lua

-- creating the metatable

Companion = {}
Companion.__index = Companion

```

Now we have to decide what kind of components we need to give a companion when we create them.
We are simply going to choose *name*, *health* and *class*


```lua

---@param name string
---@param health int
---@param class string
function Companion:new(name, health, class)
    local instance = setmetatable({
        name = name,
        health = health,
        class = class
    }, Companion)
    return instance
end

```

If there are any additional components of a `Companion` we can add them now.
Here I chose to add all classes in BG3 as a set like table.

```lua
-- constants (you could also make this global since you should never change this)

local allowedClasses = {
    Barbarian = true,
    Bard = true,
    Cleric = true,
    Druid = true,
    Fighter = true,
    Monk = true,
    Paladin = true,
    Ranger = true,
    Rogue = true,
    Sorcerer = true,
    Warlock = true,
    Wizard = true
}

```


> For the simplicity of this example we do not check for allowed classes when creating a companion
{.is-info}

We also want to access the components of our `Companion` 

```lua
-- getters methods

-- returns the companions name
---@return name string
function Companion:getName()
    return self.name
end


-- returns the companions health
---@return health int
function Companion:getHealth()
    return self.health
end

-- returns the companions class
---@return class string
function Companion:getClass()
    return self.class
end

```

And we want to modify our companions

```lua

-- methods for modifying companions

-- increases the companions health
---@param healAmount int    - the amount by what the companion should be healed
function Companion:heal(healAmount)
    -- We can only heal someone is the healAmount is larger than 0
    if healAmount > 0 then 
        self.health = self.health + healAmount
        print(self.name , " has been healed for ", healAmount)
        print("their health has increased to ", self.health)
    else
        print("Negative healAmounts are not allowed")
    end
end


-- changes the companions class
---@param class string  - the new class of the companion 
function Companion:respec(newClass)
    -- check if the class is in allowedClasses
    if allowedClasses[newClass] then
        self.class = newClass
        print(self.name, " has changed their class to ", self.class)
    else 
        print(newClass, " is not an allowed class")
    end
end



```

Now that our `Companion` class is done, we can use it in `Main.lua`. Below you can see a few examples but feel free to experiment.

Creating the companions:

```lua
-- Main.lua

-- Creating a companion named Astarion
local astarion = Companion:new("Astarion", 100, "Rogue")

-- Creating another companion named Gale
local gale = Companion:new("Gale", 120, "Wizard")

```

Retrieving their components:

```lua
-- Retrieving the companions' components
print("Astarion - Name:", astarion:getName(), "Health:", astarion:getHealth(), "Class:", astarion:getClass())

print("Gale - Name:", gale:getName(), "Health:", gale:getHealth(), "Class:", gale:getClass())


```
`Astarion - Name:        Astarion        Health: 100     Class:  Rogue`
`Gale - Name:    Gale    Health: 120     Class:  Wizard`


Healing the companions:
```lua
-- Healing a companion
print("Before healing, Astarion's health:", astarion:getHealth())
astarion:heal(20)
print("After healing, Astarion's health:", astarion:getHealth())

-- Trying to heal a companion with negative health
print("Before healing, Gale's health:", gale:getHealth())
gale:heal(-50)
print("After attempting negative healing, Gale's health:", gale:getHealth())


```

`Before healing, Astarion's health:      100`
`Astarion         has been healed for    20`
`their health has increased to   120`
`After healing, Astarion's health:       120`

`Before healing, Gale's health:  120`
`Negative healAmounts are not allowed`
`After attempting negative healing, Gale's health:       120`


```lua
-- Respeccing a companion to a legal class
print("Astarion's class before respec:", astarion:getClass())
astarion:respec("Paladin")
print("Astarion's class after respec:", astarion:getClass())

-- Respeccing a companion to an illegal class
print("Gale's class before trying illegal respec:", gale:getClass())
gale:respec("Necromancer")
print("Gale's class after trying illegal respec:", gale:getClass())

```




`Astarion's class before respec: Rogue`
`Astarion         has changed their class to     Paladin`
`Astarion's class after respec:  Paladin`



`Gale's class before trying illegal respec:      Wizard`
`Necromancer      is not an allowed class`
`Gale's class after trying illegal respec:       Wizard`

## **7\. Osiris**

### 1\. Functions

### 2\. Events

### 3\. Using Listeners

## **8\. Script Extender Functions**

-   Dumping
-   Basically go over the API and heavily credit it

## **9\. Advanced Information**

-   IMGUI / Devel stuff?

## **10\. Useful Resources**

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
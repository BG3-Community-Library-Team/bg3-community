---
title: The Basics of Lua
description: 
published: true
date: 2024-05-23T12:13:32.309Z
tags: tutorial, guide, script extender, lua
editor: markdown
dateCreated: 2024-05-01T15:05:08.014Z
---

# The Basics of Lua


> This tutorial can be completed without using the game.
> However it is recommended to use it as part of your workspace
> as this allows you to get used to SE
{.is-info}

> Don't know why you might want to look at this page?
> Check out [Getting started with Script Extender](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted)
{.is-warning}


For modding Baldur's Gate we use the programming language `Lua`

The following section is aimed towards people who have no programming knowledge.

If you don't know what a function is, you might want to read through this. If you have worked with other programmig languages before, feel free to skip this section but make sure to read up on Lua syntax. Its syntax is very similar to `python`

> It is recommended to not only read this section but to follow along. 
> Also try typing some of these commands instead of using copy and paste
> to better familiarize yourself with them
{.is-info}

Use the example mod "MySEMod" to follow along by typing in `MyFirstSEScript.lua` from [Getting started with Script Extender](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted) and resetting the console to see the changes.

## 1\. Order of execution

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


## 2. Comments

You can also add lines to your script that don't do anything. These are `comments`
You can type them by adding two consecutive dashes `--` before your text.

```lua

-- myVariable is 5
local myVariable = 5

-- prints myVariable
print(myVariable)

```

`5`

You can also use comments to `comment out` lines you temporarily want to disable

```lua
-- myVariable is 5
local myVariable = 5


-- prints myVariable
-- print(myVariable)

```

` ` (empty output)

## 3. Variables 

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

## 4. A very special data structure: tables

You might have heard of some data strucutres like `arrays` or `lists` before.
In Lua we use a so called `table` for all of these instances.

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

### 4.1. The basics

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

### 4.2\. Iterating over a table

To be able to access all components, we want to iterate over the tables.
This is what we are doing in the `printMyTable` function.


```lua
for x,y in pairs(myTable) do
	 print(x, " ", y)
end
```


`1 Bread`
`2 Wine`


### 4.3\. Different types of tables


#### 4.3.1\. Arrays

The tables in the example above can fit the description of an "array". They consist of an index and an entry


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

#### 4.3.2\. Maps

We can also create "map-like" tables. These consist of "key - value" pairs. 
The` key ` in this case is the entry on the left. The `value` is the entry on the right next to it.  When we know the `key` we can immediately retrieve the `value`.

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



#### 4.3.3\. Sets

The last tabel structure we will mention is a "set-like" table.
Sets are used to store unique items. That means duplicates are not allowed.
Here we can quickly look up if something exists in our set. For that, we set the entries to `true`.

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

### 4.4\. Tables within tables

Tables are very flexible and allow varied structuring. Below you can see two more examples.
Note that because of the nested structure, our `printMyTable` function does not work anymore.
Instead we can use `_D` to "dump" the whole table and write special loops for them.

#### Example 1

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


#### Example 2

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


## 5\. Scope 

As you have already learned in [1. Order of executions](https://wiki.bg3.community/Tutorials/ScriptExtender/the_basics_of_lua#h-1-order-of-execution) your variables are not available everywhere in your program.
The order of execution is not the only thing that defines this.

### 5.1 Scope within a file

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


### 5.2 Scope across files

if you have followed [5. Creating multiple files](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-5-creating-multiple-files) from [Getting started with Script Extender](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted) then you have two files in your "Server". `MyFirsSEScript.lua` and `MySecondSEScript.lua`

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

Here you got your first intended error message. This is because we try to call the function `getWyll()` but `MySecondSeScript.lua` doesn't know how to access it.


Again we have to make the function global as well to access it from other files

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



## 6\. Functions

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

Parameters allow you to add an input and reuse this input within a function. 
In this case we name our parameter `companion`. You can use any name you like as long as it stays consistent within the function.

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


## 7\. If statements

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
> never forget to actually compare it to the desired value.
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




## 8\. Loops

Another way to make our code more interactive is by the use of **loops** to repeat certain steps.
You have already used in if you have followed **3. A very special data structure: tables** where we used the function `printMyTable`
to iterate over a table.

There are different types of loops. We will only cover the `for loop` here.
They will execute their body for a set amount of iterations.

```lua

-- prints the count from 1 to 5
for i = 1,5 do
	print(i)
end

```

`1`
`2`
`3`
`4`
`5`

We usually do not want to iterate for a set amount of loops, but base it on a table.
using `#tableName` you can get the size of a table. 


```lua

local myTable =  {"Cheese", "Bread", "Wine"}

for _,food in pairs(myTable) do
	print(food)
end

```

`Cheese`
`Bread`
`Wine`

Of course you can also use this in a function

```lua

local myTable =  {"Cheese", "Bread", "Wine"}


-- prints the content from an array like table
local function printArraylike(table)
  for _,content in pairs(table) do
    print(content)
  end
end

printArraylike(myTable)


```

`Cheese`
`Bread`
`Wine`


As you have seen in **3.4. Tables within tables** we can *nest* tables.
That mean swe can put a table within another table.
To retrieve the values in these `nested tables` we can use  `nested loops`


```lua 

local cheeseTable = {"Gorgonzola", "Cheddar", "Brie"}
local breadTable = {"Black Bread", "Whole Grain Bread", "Rye Bread"}
local wineTable = {"Merlot", "Chardonnay", "Cabernet Sauvignon"}

local foodTable =  {myCheeseTable, myBreadTable, myWineTable}


-- prints the content from a table that contains tables
local function printNestedTable(nestedTable)
  for _,table in pairs(nestedTable) do
    for _,content in pairs(table) do
    print(content)
  end
end

printNestedTable(foodTable)

```


`Gorgonzola`
`Cheddar`
`Brie`
`Black Bread`
`Whole Grain Bread`
`Rye Bread`
`Merlot`
`Chardonnay`
`Cabernet Sauvignon`

## 9\. Debugging


### 9.1 Debugging using error output


While following this guide you likely already ran into a few errors.
These are shown in red on the console:

![gswse_error.png](/tutorials/getting_started_with_se/gswse_error.png)


For this we will write some code that will throw an errror:


```lua

local function myMistake(num1, num2)
	print("num1" + num_2)

myMiftake("Astarion")

```

`bg3se::lua::State::LoadScript(): Failed to parse script: [string "MySEMod/MyFirstSEScript.lua"]:4: 'end' expected (to close 'function' at line 1) near <eof>`


Here we get the error message `Failed to parse script`.
This means that we already made a mistake with writing our script regardless of the input.
If like me you started writing at `line 1` you will find the mistake in the same line as well.

`[string "MySEMod/MyFirstSEScript.lua"]:4:` shows us that the issue is in `MyFirstSEScript.lua` in line `4`.

` 'end' expected  (to close 'function' at line 1)` shows us what the errror is. 
We forgot to close the function we start in line `1` with an `end`. So let's add this

```lua

local function myMistake(num1, num2)
	print("num1" + num_2)
end

myMiftake("Astarion")

```

`bg3se::lua::State::LoadScript(): Failed to execute script: [string "Scribe/BootstrapServer.lua"]:5: attempt to call a nil value (global 'myMiftake')`

Now the issue is `Failed to execute script` . This means the code we wrote is at least valid but we made a mistake in executing it.
`[string "Scribe/BootstrapServer.lua"]:5: attempt to call a nil value (global 'myMiftake')`
We have an issue in line 5 where we call a `nil value`, something that doesn't exist.
If you are observant you can spot that here we made a small typo. Instead of calling `myMistake` we called `MyMiftake` which doesn't exist.

`myMiftake("Astarion")` -> `myMistake("Astarion")`

Let us fix this typo

```lua

local function myMistake(num1, num2)
	print("num1" + num_2)
end

myMistake("Astarion")

```
`bg3se::lua::State::LoadScript(): Failed to execute script: [string "Scribe/BootstrapServer.lua"]:2: attempt to perform arithmetic on a string value`

The next error is `attempt to perform arithmetic on a string value` in line `2`


We mistakenly used `"num1"` instead of `num1`, so we cannot perform additions.

`print("num1" + num_2)` ->  `print(num1 + num_2)`


```lua

local function myMistake(num1, num2)
	print(num1 + num_2)
end

myMistake("Astarion")

```

`bg3se::lua::State::LoadScript(): Failed to execute script: [string "Scribe/BootstrapServer.lua"]:2: attempt to perform arithmetic on a string value (local 'num1')`

Here we have another `attempt to perform arithmetic on a string value` but this time we have some more additional information `(local 'num1')`
This means that the parameter we pass to this function `num1` is a string but we cannot perform additions on strings. 
So let us change that

`myMistake("Astarion")` ->  `myMistake(5)`


```lua

local function myMistake(num1, num2)
	print(num1 + num_2)
end

myMistake(5)

```

`bg3se::lua::State::LoadScript(): Failed to execute script: [string "Scribe/BootstrapServer.lua"]:2: attempt to perform arithmetic on a nil value (global 'num_2')`

This time we get the error `attempt to perform arithmetic on a nil value (global 'num_2')`
This means `num2` does not exist. And indeed we do not pass a second argument when calling the function

`myMistake(5)` -> `myMistake(5, 4)`

```lua

local function myMistake(num1, num2)
	print(num1 + num_2)
end

myMistake(5, 4)

```

`bg3se::lua::State::LoadScript(): Failed to execute script: [string "Scribe/BootstrapServer.lua"]:2: attempt to perform arithmetic on a nil value (global 'num_2')`

We still get the same error message as before. We know that we pass a number as `num2`, so we need to check the function. 
It looks like we mistakenly used `num2` as the name of the parameter but later in the print statement we used `num_2`

`print(num1 + num_2)` -> `print(num1 + num2)`


```lua

local function myMistake(num1, num2)
	print(num1 + num2)
end

myMistake(5, 4)

```

`9`

Seems like we were able to succesfully debug our code with the help of errors!

### 9.2 Debugging using print statements

However, mistakes aren't always this obvious. Sometimes our code is "valid"
but we still do not get the desired output.

We will go over how to use `print` statements to debug our code.


```lua

local function isAstarion(uuid)
    if uuid == "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255" then
        return 1
    else
        return 0
    end
end
   
   
if isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255") == true then
    print("Astarion found")
end

``` 

` ` (empty output)

We expect `"Astarion found"` to be printed but instead we get nothing so we don't know where to start looking for mistakes.
Let's start by adding an `else` statement to our `if statement`. 
Right now we get no output, but we suspect that the `if statement` evaluates to false which leads to the `print` statement not being executed.

```lua

local function isAstarion(uuid)
    if uuid == "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255" then
        return 1
    else
        return 0
    end
end
   
   
if isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255") == true then
    print("Astarion found")
else
   print("Astarion not found")
end
```

`Astarion not found`

Now we know for certain that the issue is in the evaluation of our `if statement`.
We expect it to evaluate to true but it does not.

Let's go further and gave a look at our function `isAstarion(uuid)`
and add some `print` statements here as well.


```lua

local function isAstarion(uuid)
    if uuid == "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255" then
    		print(uuid ," is Astarion")
    		return 1
    else
    	  print(uuid ," is not Astarion")
        return 0
    end
end
   
   
if isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255") == true then
    print("Astarion found")
else
   print("Astarion not found")
end
```


` S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255   is Astarion`
`Astarion not found `

Our function `isAstarion()` works and returns the correct value, but our `if statement`
evaluates to false, so there must be a mistake in how we compare the result.

Let us add another statement so we can directly compare.


```lua

local function isAstarion(uuid)
    if uuid == "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255" then
    		print(uuid ," is Astarion")
        print("returning 1")
    		return 1
    else
    	  print(uuid ," is not Astarion")
        return 0
    end
end
   
   
if isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255") == true then
    print("Astarion found")
else
   print("Astarion not found")
   print(isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"), " is not the same as  ", true)
end
```


`S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255   is Astarion` 
` returning 1`
` Astarion not found`
` S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255   is Astarion`
`returning 1`
`1        is not the same as     true`

Here we can see our mistake. In `isAstarion(uuid)` we return `0` or `1` but in our `if statement` we check whether something is `true`. 
We have to change our `if statement` to reflect the correct return values of the function `isAstarion(uuid)`


```lua

local function isAstarion(uuid)
    if uuid == "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255" then
    		print(uuid ," is Astarion")
        print("returning 1")
    		return 1
    else
    	  print(uuid ," is not Astarion")
        return 0
    end
end
   
   
if isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255") == 1 then
    print("Astarion found")
else
   print("Astarion not found")
   print(isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"), " is not the same as  ", true)
end
```

`S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255   is Astarion`
`returning 1 `
`Astarion found` 

Now we get the correct output.
We can delete, or comment out our print statement so they don't clutter up our console.

```lua

local function isAstarion(uuid)
    if uuid == "S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255" then
    		return 1
    else
        return 0
    end
end
   
   
if isAstarion("S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255") == 1 then
    print("Astarion found")
end
```

`Astarion found` 


## 10\. A brief introduction to metatables

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



> Want to practive more Lua? 
> Visit exercism: https://exercism.org/tracks/lua
{.is-info}


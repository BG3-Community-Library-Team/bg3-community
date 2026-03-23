---
title: Creating and Using Dialogue Script Flags
description: A guide to making script flags, to allow you to test for multiple conditions at once in dialogue.
published: false
date: 2026-03-23T13:34:51.959Z
tags: tutorial, tutorials, dialogue, dialog
editor: markdown
dateCreated: 2026-03-23T13:34:51.959Z
---

# Creating and Using Dialogue Script Flags
This is a guide to making script flags, which are special flags that allow you to test for multiple conditions at once in dialogue, using boolean functions beyond just the AND function!

This tutorial assumes you know how to use boolean functions, and at least the basics of BG3 modding and dialogue editing, although it *will* cover the syntax for boolean functions required by script flags.

Let's get started!

## Why script flags?

Normally, flag tests in dialogue will only allow you to check flags via the AND and NOT boolean functions. This means that when testing for flags in dialogue, all conditions you're testing for will need to be true at once. There's no way to test for OR or NOR conditions, which can be particularly annoying when you want to test for multiple conditions that might not be true simultaneously (like if you want to enable a dialogue option for characters tagged with either the cleric OR paladin tags, and don't want to lock that option to characters multiclassing in both rhe cleric and paladin classes.)

Without script flags, you'll need to make multiple dialogue nodes just to test for each of those conditions, but that won't be necessary if you use a script flag instead.

## Making script flags

Start by making a new .lsx file in the following file path:

`\\Mods\[your mod folder\Story\Dialogs\ScriptFlags\ScriptFlags.lsx`

You can do so by copying an existing .lsx file, renaming it to ScriptFlags.lsx, and then clearing its contents and replacing it with this:

```
<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="6" revision="0" build="800"/>
    <region id="ScriptFlags">
        <node id="root">
            <children>



            </children>
        </node>
    </region>
</save>

```

This file should be left an .lsx file, and should not be converted to .lsf in order to function.

You now have a new blank file to place your script flags in, and you're ready to make a new one!

Copy this script flag into your new blank file. This is a vanilla flag used to check for the player having AND read either Chapter 1 OR Chapter 3 of the Orpheus story, and is a good example of checking multiple boolean conditions in the same script flag.

```
<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="6" revision="0" build="800"/>
    <region id="ScriptFlags">
        <node id="root">
            <children>

                <node id="ScriptFlag">
                    <attribute id="Description" type="LSString" value="The player owns and has read one Orpheus chapter already"/>
                    <attribute id="Script" type="LSString" value="CONDITION IsFlag(0,&quot;GLO_OrpheusChapters_State_ReadOrpheusChapter1_c8fa6c18-6491-48b6-9197-43285a07f9c9&quot;,1)
CONDITION IsFlag(0,&quot;GLO_OrpheusChapters_State_ReadOrpheusChapter3_cd913886-8e41-47d2-bba1-fda22b129001&quot;,1)
CONDITION IsFlag(2,&quot;ORI_Laezel_State_HasOrpheusChapter1_24b4f0a1-0512-4164-8c5b-0e3bca62bfb2&quot;,1)
CONDITION IsFlag(2,&quot;ORI_Laezel_State_HasOrpheusChapter3_225b8f68-2134-499d-985b-cbd1d5d85624&quot;, 1)
CHECK &quot;(c1&amp;c3)|(c2&amp;c4)&quot;"/>
                    <attribute id="UUID" type="guid" value="1d57a6b0-67e7-d162-8305-bba827bfd687"/>
                    <attribute id="name" type="FixedString" value="CRE_YouthTraining_HaveOneOrpheusChapter"/>
                </node>

            </children>
        </node>
    </region>
</save>

```

Give the flag a new name and UUID. This is the UUID you'll be testing for in dialogue. Then, update the description to explain what the flag does. You're now ready to start adding conditions for your flag.

## Dialog variables

Dialog variables are variables that can be tested for in script flags and Osiris, the scripting language for the game. These variables include things like, strings to test for the names of custom characters or hirelings to display in dialogue, the cost of specific actions (like renting the Elfsong tavern), and countdowns, like those testing for the number of days you have to rescue the people trapped in Grymforge.

These variables can be altered by Osiris, and tested for by their UUIDs in script flags.

You can put new dialogue variables for testing in the following file path:

``\\Mods\[your mod folder\Story\Dialogs\DialogVariables\DialogVariables.lsx``

## Script flag syntax

New conditions can be defined by putting the word CONDITION on a new line within the script flag. This script flag is only testing for different flags being True or False, but there are multiple other different conditions you can check for. This is a list of the conditions I've found so far:

IsFlag - checks for whether different flags are true or false. Syntax:

```
CONDITION IsFlag(Speaker number of the character to check the condition flag for&quot;Flag name_flag UUID&quot;1 or 0, depending on if you're checing if the flag is True or False)
```

HasItemTagInMagicPockets - Checks whether there's any items in a character's inventory with specific tags attached to it. Syntax:

```
CONDITION HasItemTagInMagicPockets(Speaker number of the character to check the inventory for,&quot;Tag name_tag UUID&quot;)
```

HasItemTemplateInMagicPockets - Checks whether an item with a specific template is in a player character's inventory. Syntax:



IntegerCompare - Checks whether the number stored in a dialog variable matches a certain target number. Syntax:

```
CONDITION IntegerCompare(%Dialog varialbe name_dialog variable UUID,&quot;==&quot;,the target number you want your script flag to match in order to evaluate the condition to True)
```

## Evaluating script flag conditions

To check your script flag conditions, you'll need to put CHECK on a new line, before testing for the operators you'd like to check for your conditions. You can test for each different condition by putting c followed by the order in which you listed each condition, starting from 1 (like c1, c2, c3, and so on)

You can then test for each condition (or set of conditions) with the following operators:

AND - &amp;
OR - |

and you can group sets of conditions and test for them with those operators by putting your sets of conditions in parentheses.

Using the above example of whether the player has the Orpheus chapters, and has read them, you can see the 

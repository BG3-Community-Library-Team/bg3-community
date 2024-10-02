---
title: TreasureTables
description: 
published: true
date: 2024-10-02T01:03:49.232Z
tags: 
editor: markdown
dateCreated: 2024-09-15T07:10:08.311Z
---

# TreasureTables

There are 1.5 ways you can add items to an object inventory. (Container/NPC)
I'll get to the 0.5th way at the very end.

Before anything with treasuretables can happen, except just editing existing ones, a gameobject needs this attribute node added to it:

For items:

```
<node id="InventoryList">
    <children>
        <node id="InventoryItem">
            <attribute id="Object" type="FixedString" value="MyTreasureTable" />
        </node>
    </children>
</node>
```

For NPCs:

```
<node id="TradeTreasures">
		<children>
				<node id="TreasureItem">
						<attribute id="Object" type="FixedString" value="MyTreasureTable" />
				</node>
		</children>
</node>
```

This will ensure that a specific gameobject will spawn with the specified treasuretable. You can name it however you want as long as you create one with said name or use one already in the game.

To create one you need to create a TreasureTable.txt file and add it like this:

```
new treasuretable "MyTreasureTable"
new subtable "1,2;2,1"
object category "T_UND_Supplies",16,0,0,0,0,0,0,0
object category "I_CONS_FOOD_Vegetable_Potato",2,0,0,0,0,0,0,0
object category "I_CONS_FOOD_Fruit_Apple",2,0,0,0,0,0,0,0
```
`new treasuretable` tells the game we start defining a new treasuretable with a specific name (the one you might link to your gameobject)
`new subtable` tells the game we now decide on the probability on the following items being added.
Its `Amount;Weighted Chance`
If we take `"1,2;2,1"` as an example, you can add the second numbers of each set together `2+1=3`.
The first sets second number now basically means its being called 2 out of 3 times, and the second set is being called 1 out of 3 times.
e.g. `"1,19;5,7"` - Means the first set is called 19 our of 26 times and the second is called 7 out of 26 times.

Whenever its decided which set got picked, the first number specifies how many items of the ones we list will be added to the inventory.
```
object category "T_UND_Supplies",16,0,0,0,0,0,0,0
object category "I_CONS_FOOD_Vegetable_Potato",2,0,0,0,0,0,0,0
object category "I_CONS_FOOD_Fruit_Apple",2,0,0,0,0,0,0,0
```
If we say for example the second set was chosen and we have 2 items that will be spawned from this list, these items listed have their own seperate weighting. As specified by their own first numbers, here: 16 - 2 - 2. So 16 out of 20 times `"T_UND_Supplies"` will get chosen as a spawned item.

You may notice that the first link to "an item" here has a `T_` in front while the others have `I_` .
This indicates that `UND_Supplies` is a treasuretable itself.
Yes, you may link additional treasuretable rolls within a treasuretable.
Whatever these may result in is specified by their own rules.
In this case, 4 out of 18 times, one of the other items get picked. 2 out of 18 times its a Potato, and the other 2 times its an Apple.
This chance will get rolled twice because we pretend the second set with `2 Amount` was chosen.
So there is a high chance that the additional treasuretable will get rolled twice.

If you don't want to deal with chances you can tell the subtable to roll like this: `"1,1"`
This means 1 out of 1 times, so basically 100% of the time. It rolls 1 amount of times over whatever you list underneath.

You can also add to existing treasuretables via `CanMerge`.
Lets pretend we want to add an additional 100% dropchance apple to `MyTreasureTable`:

```
new treasuretable "MyTreasureTable"
CanMerge 1
new subtable "1,1"
object category "I_CONS_FOOD_Fruit_Apple",1,0,0,0,0,0,0,0
```

This makes it so `MyTreasureTable` looks like this:

```
new treasuretable "MyTreasureTable"
new subtable "1,2;2,1"
object category "T_UND_Supplies",16,0,0,0,0,0,0,0
object category "I_CONS_FOOD_Vegetable_Potato",2,0,0,0,0,0,0,0
object category "I_CONS_FOOD_Fruit_Apple",2,0,0,0,0,0,0,0
new subtable "1,1"
object category "I_CONS_FOOD_Fruit_Apple",1,0,0,0,0,0,0,0
``` 

This should give some initial insight on how treasuretables work.
A treasuretable only ends whenever the file ends or you start a new treasuretable entry. Just like stats/spells/boosts.

#### The 0.5th way:

```
<node id="InventoryList">
    <children>
        <node id="InventoryItem">
            <attribute id="Object" type="FixedString" value="MyTreasureTable" />
        </node>
        <node id="InventoryItem">
            <attribute id="Object" type="FixedString" value="MyOtherTreasureTable" />
        </node>
    </children>
</node>
```
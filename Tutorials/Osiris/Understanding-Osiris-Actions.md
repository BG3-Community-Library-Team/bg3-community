---
title: Understanding Osiris Rules: Actions
description: 
published: true
date: 2026-02-02T19:32:53.261Z
tags: osiris
editor: markdown
dateCreated: 2026-02-02T19:32:53.261Z
---

The [previous guide in this series](https://wiki.bg3.community/en/Tutorials/Osiris/Understanding-Osiris-Conditions) discussed the conditions that control when an Osiris rule will execute, so now let's take a look at the **actions** we can perform during its execution.

## Databases

**Databases actions** are one of the most fundamental tools at our disposal. Using a database as an action will add a fact to the database unless the fact is already defined, in which case the action won't do anything. This is because facts in each database must be unique, and so it can't be added a second time.

We can also invert database actions by adding `NOT` to the beginning of the line, which will remove a fact from the database if it is already defined. If the fact is not already defined, the action won't do anything because there is nothing to remove.

Database actions must be used with either a literal or an assigned variable.

The following rule attempts to define the literal `"H"` in the database `DB_Letters`:

```
IF
Condition1
THEN
DB_Letters("H");
```

Even if `Condition1` triggers this rule multiple times, `"H"` will only be added to the database the first time `DB_Letters("H");` is executed. Database conditions that require `"H"` will also not be triggered again after it is defined.

We can have another rule that attempts to remove the literal `"H"` from `DB_Letters`:

```
IF
Condition2
THEN
NOT DB_Letters("H");
```

If this rule is triggered before `"H"` is defined, it won't do anything. If it is triggered after `"H"` is defined, then it will remove that fact from `DB_Letters` and trigger inverted database conditions. This will also allow `"H"` to be re-defined and trigger database conditions again.

> We can also use database actions with variables that have already been assigned a value.
{.is-info}

Let's look at a more complicated example that creates a database named `DB_TagTracker`. This database should contain a fact for every player character who has been tagged with something we care about. For simplicity, we'll just call it `EXAMPLE_TAG`. We can maintain this database with these two rules:

```
IF
TagSet(_Player, (TAG)EXAMPLE_TAG)
AND
DB_Players((CHARACTER)_Player)
THEN
DB_TagTracker(_Player);

IF
TagCleared(_Player, (TAG)EXAMPLE_TAG)
AND
DB_TagTracker((CHARACTER)_Player)
THEN
NOT DB_TagTracker(_Player);
```

Notice that `TagSet` and `TagCleared` are **Events** with parameters for the object that has been tagged and the tag that has been applied to it.

In the first rule, we require that the game object that has been assigned the tag is a player, and if it is then we define a fact with their GUID to `DB_TagTracker`. I have preemptively named the variable `_Player` even though it could be any game object because I know the second condition will filter out any versions of the rule where the variable _isn't_ assigned a player, and naming it this way helps to convey the rule's purpose.

In the second rule, we only care about removing the fact from our database if the database already contains it, so we can just check for that instead of having to check that the object is a player first.

## Calls

**Calls** are a special kind of action that change the game state. Every call has one or more in-parameters that must be given a constant value or an assigned variable so that it knows exactly what we want it to do.

For example, there's a call to give a character some gold in [the list of calls and queries](https://github.com/LaughingLeader/BG3ModdingTools/blob/master/generated/Osi.lua) (reformatted for clarity):

`AddGold((GUIDSTRING)_InventoryHolder, (INTEGER)_Amount)`

We can see it has the following two parameters:

1. `_InventoryHolder`: A GUID that identifies the character who we want to give gold

2. `_Amount`: An integer that specifies how much gold we want to give

Let's use this call in a rule that gives every player 50 gold after a long rest:

```
IF
LongRestFinished()
AND
DB_Players(_Player)
THEN
AddGold(_Player, 50);
```

In this rule, we have the **Event** `LongRestFinished` that does not have any parameters and only triggers the rule after a long rest. Next, we have a database condition that will create separate evaluations of the rule for every value that can be assigned to the undeclared variable `_Player`. For every version of the rule, it will execute and use the Call to give 50 gold to the character assigned to `_Player` in this version.

### Overloaded Calls

Some Osiris calls have alternate versions with fewer parameters that are called **overloaded calls**. Overloaded calls are the only time in Osiris that an in-parameter can be left off the end and it will automatically default to some value.

For example, the call to make a character equip an item is pretty big, with five parameters:

`Equip((CHARACTER)_Character, (ITEM)_Item, (INTEGER)_AddToMainInventoryOnFail, (INTEGER)_ShowNotification, (INTEGER)_ClearOriginalOwner)`

Luckily, `Equip` has three overloaded versions. This means we can use the original with all five parameters, but we can also use alternate versions with only the first four, three, or two parameters. Using the version with four parameters means the fifth parameter will default to some value automatically. Using the version with only two parameters means the last three parameters will default to some values.

In the linked list of calls and queries, these overloaded calls are listed before the parameters with `@overload` and describe the different versions of it that you can use.

Unfortunately, as of the time of writing, I don't know of any documentation that lists the default values for every overloaded call. I had to experiment with `Equip` to determine that `_AddToMainInventoryOnFail` and `_ShowNotification` both default to `0` (false). However, I'm not certain what `_ClearOriginalOwner` does or how to test it, and so I don't know what it defaults to.

An important thing to note is that overloaded calls cannot change the order of the parameters. If you want to set the value of the last parameter to be something other than the default, then you have to provide every parameter.

For example, if I wanted to use all of the default values for `Equip`, I could write a rule like this:

```
IF
Condition1
THEN
Equip(_Character, _Item);
```

...where `_Character` and `_Item` are variables that must have been assigned values by `Condition1`.

If I only wanted to change the rule to explicitly assign the last parameter `_ClearOriginalOwner` the value `1`, then I would have to use the full version of `Equip` and also provide the default values for the other two optional parameters, like this:

```
IF
Condition1
THEN
Equip(_Character, _Item, 0, 0, 1);
```

## Procedures

**Procedures** combine many of the concepts we've discussed so far. They're sort of like a Call that triggers our own custom Event.

In order to use a procedure, we need to do two things:

1. Define the procedure as its own kind of standalone rule

2. Call the procedure as an action

Let's look at the structure of a procedure using placeholder values:

```
PROC
PROC_ProcedureName((Type1)Parameter1, (Type2)Parameter2)
AND
Condition1
AND
Condition2
THEN
Action1;
Action2;
```

Procedures can have any number of in-parameters. If you don't want any, leave the parentheses after the procedure name empty.

> Procedures are shared across the entire Osiris story, so you can use procedures defined in other scripts / goals, but you also need to choose a unique name for your own procedures.
{.is-info}

One powerful feature of procedures is that we can have multiple versions of them just like we can have multiple rules triggered by an event or to evaluate a custom query. For example, we can define two different versions of `PROC_MyProc` here:

```
PROC
PROC_MyProc()
AND
Condition1
THEN
Action1;

PROC
PROC_MyProc()
AND
Condition2
THEN
Action2;
```

When this procedure is called, every version of it that we have defined will be evaluated, and any that satisfy all of its conditions will be executed.

We can call the procedure `PROC_MyProc` just like we do with Osiris Calls, like this:

```
IF
Condition1
THEN
PROC_MyProc();
```

If you define the procedure more than once with different numbers of parameters, they will behave like completely different procedures. We can use this to make our own default values, like this:

```
PROC
PROC_MyProc()
THEN
PROC_MyProc("This is the default message");

PROC
PROC_MyProc((STRING)_Message)
THEN
Action1;
```

In this example, the version of the procedure without any parameters will call the version of the procedure with a parameter. This means that calling it without a parameter has the effect of calling it with a default value. That is, `PROC_MyProc();` has the same effect as `PROC_MyProc("This is the default message");`, but we can also provide a custom parameter at any time with something like `PROC_MyProc("This is a custom message");`.
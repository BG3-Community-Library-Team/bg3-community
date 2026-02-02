---
title: Understanding Osiris Rules
description: An in-depth discussion of how Osiris evaluates and executes rules.
published: true
date: 2026-02-02T22:15:15.927Z
tags: osiris
editor: markdown
dateCreated: 2026-02-01T04:11:05.382Z
---

This guide series explains the mechanics of how Osiris evaluates and executes a **rule**. I have tried to make it more like technical documentation than a tutorial, so even though most of the topics in this guide are relatively simple, nothing is _simplified_. That is, I have tried to explain exactly _how_ and _why_ everything works so that you will be able to confidently apply it in new ways. This also means that you won't have to read or understand the entire guide to start benefiting from it - if you're learning all of this for the first time and get stuck on a difficult section, please feel free to skip it and come back later.

If you're completely new to Osiris and just want a simple tutorial for your first project, I'd recommend [my guide on giving everyone a passive](https://mod.io/g/baldursgate3/r/giving-everyone-a-passive).

There's a lot to cover in these guides, so please take breaks if you start to feel overwhelmed, and don't worry about understanding everything at once. Learning a new programming or scripting language usually takes a lot of trial and error, and that's okay.

## Basic Definitions

The official introduction to fundamental Osiris terms are in [the guide "Introduction to Osiris"](https://mod.io/g/baldursgate3/r/introduction-to-osiris). However, I will also provide a few of my own, non-technical definitions here.

**Rule:** The smallest standalone piece of Osiris code. Each rule describes what to do in a specific situation and can be combined with other rules to achieve more complicated behaviors.

**Fact:** A set of one or more values.

**Database:** A container for zero or more unique facts. Facts can be added (also called **defined**) or removed from the database at any time.

It might be helpful to think of a database like a table of rows and columns. Each fact is a row in the table, and each value in the fact is a column.

![osirisrules_databaseillustration.webp](/tutorials/osiris/understanding-osiris-rules/osirisrules_databaseillustration.webp)

Defining a fact in a database just means adding a new row to the table, which you will be able to use again later. Removing a fact from a database also just means removing that row from the table.

## The Structure of an Osiris Rule

Every rule in Osiris has two parts:

1. One or more conditions.
   * This part begins with `IF`
   * This part is **evaluated** whenever the rule is **triggered**
   * Each condition is on its own line
   * Each condition is separated by the line `AND`

2. One or more actions.
   * This part begins with `THEN`
   * This part is **executed** when all of the conditions are met (each condition **evaluates to true**)
   * Each action is on its own line
   * Each action ends with `;`

Let's use placeholders to make it obvious what the different parts of an Osiris rule are:

```
IF
Condition1
AND
Condition2
THEN
Action1;
Action2;
```

[<img align="right" src="https://img.shields.io/static/v1?label=Next&message=Rule+Conditions&color=2ea44f&style=for-the-badge">](/Tutorials/Osiris/Understanding-Osiris-Conditions)
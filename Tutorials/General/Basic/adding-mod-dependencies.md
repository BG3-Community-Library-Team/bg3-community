---
title: How to add mod dependencies and eradicate load order problems with your mods
description: Explains how adding dependencies to meta.lsx ensure correct loading order, reduce user confusion, and simplify troubleshooting. The guide also addresses common concerns about dependencies, such as user reluctance and abandoned mods.
published: true
date: 2025-08-20T15:09:21.748Z
tags: mods, load order, modsuse, dependencies, dependency, meta.lsx, mod dependency, deps
editor: markdown
dateCreated: 2024-09-02T18:33:21.499Z
---

## Why and how you should properly add a dependency to your mod

> **TL;DR**:
> **Why?** Because adding dependencies to your meta.lsx file ensures that your mod is loaded in the correct order, reduces user confusion, and simplifies troubleshooting.
> **How?** Add the dependency to the `Dependencies` node in your meta.lsx file; here is an example with Mod Configuration Menu as a dependency:
> {.is-success}

Before:
```xml
...
    <children>
      <node id="Dependencies" /> <!-- this node is being closed without any children -->
      <node id="ModuleInfo">
        ...
```

After:
```xml
...
    <children>
      <node id="Dependencies">
        <children>
          <node id="ModuleShortDesc">
              <attribute id="Folder" type="LSWString" value="BG3MCM" />
              <attribute id="MD5" type="LSString" value="" />
              <attribute id="Name" type="FixedString" value="Mod Configuration Menu" />
              <attribute id="UUID" type="FixedString" value="755a8a72-407f-4f0d-9a33-274ac0f0b53d" />
              <attribute id="Version64" type="int64" value="37999121855938560" />
          </node>
          <!-- You can add more <node id="ModuleShortDesc"> entries here for additional dependencies, if needed -->
        </children>
      </node>
      <node id="ModuleInfo">
        ...
```

> It is also recommended to always set the required version (`Version64`) of the dependency to the version you're using during the development of your mod. In the example above, it's MCM 1.14.0.0.
> As modding evolves, mod managers may use this to enforce correct versions for dependencies. **MCM already uses it to warn users if they have outdated dependencies**.
>
> Example: if your mod has dependencies *A* and *B*, and you need *B* to be version 2.0.0.0 or greater due to a recent fix, you should use 2.0.0.0 for the dependency version (generate the `Version64` number with BG3MM, in this case `72057594037927936`)
{.is-info}

That's it! You've just added a dependency to your mod. By properly declaring dependencies, you will:

- **Ensure that required mods are loaded in the correct order** - dependencies will automatically be loaded earlier (BG3MM handles this automatically)
- **Eliminate the need for users to follow manual instructions** (e.g., "*don't forget to add **this** mod*", "*load **this** mod before **that** mod*", *"don't forget to update **x** dependency"*)
- **Overall simplify troubleshooting** by reducing incorrect/false positive bug reports

> **Note:** Make sure the `Name` is something that the user will recognize. At the time of writing, it is used by BG3MM and MCM to display the dependency name to the user.
> {.is-warning}

> **Tip**: the [BG3 Mod Helper](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper) extension provides buttons and commands to simplify adding dependencies to your mods.
> {.is-info}

## Declaring conflicts

Conversely, you can also declare other mods your mod **conflicts with**. This is useful when, for example, loading both would break functionality or cause duplicate UI elements, etc.

To declare a conflict, use the `Conflicts` node:

```xml
<node id="Conflicts">
  <children>
    <node id="ModuleShortDesc">
      <attribute id="Folder" type="LSString" value="NoPressAnyKeyButton_2bae5aa8-bf6a-d196-069c-4269f71d22a3" />
      <attribute id="MD5" type="LSString" value="" />
      <attribute id="Name" type="LSString" value="No Press Any Key (non-MCM version)" />
      <attribute id="PublishHandle" type="uint64" value="0" />
      <attribute id="UUID" type="guid" value="2bae5aa8-bf6a-d196-069c-4269f71d22a3" />
      <attribute id="Version64" type="int64" value="37154716253159441" />
    </node>
  </children>
</node>
```

Since this info is embedded in the .pak file of your mod, you can update them as needed for each version of your mod — adding or removing entries depending on what's compatible with that specific release.

> Declaring conflicts helps avoid bugs and confusion by warning users that enabled mutually exclusive mods.
Mod managers may in the future use this information to show warnings or automatically disable conflicting mods. **MCM 1.32+ warns users of conflicts in their load orders**.
> {.is-success}

### Why adding dependencies? I don't need them!

*Disclaimer: I am a maintainer of MCM and VC, so I might be biased. However, I will try to be as neutral as possible.*

Dependencies are essential for the evolution of modding communities. If you take a look at Skyrim's modding scene, the amount of complex and interconnected mods was made possible, for the most part, because of the community's ability to work together and build on top of each other's work. Although most mods are naturally focused on player-facing features, others are focused on providing tools and frameworks for other mod authors. 

> **Dependency mods are the backbone of a great modding community**.
> Framework maintainers spend a lot of time and effort to design and implement systems that other mod authors can leverage to create more complex and feature-rich mods, with less effort.
{.is-info}

Not all dependencies are created equal. Some try to fix inherent issues with the game and offer compatibility capabilities for other mods, and may be even almost unavoidable. You could theoretically implement all the features of a dependency mod in your mod, but that would be a tremendous waste of time and effort. As BG3 modding progresses, you can expect more and more tools and frameworks to be developed, and you should take advantage of them to create better mods.

> Dependencies are tools that will **allow you to build on top of other mods and *focus on what you want to do*, instead of reinventing the wheel.**
{.is-success}

### But then users won't download my mod!

If the dependency is popular or has an easy installation process, users will likely not mind much. It comes down to how impactful your mod is, the dependency is to your mod, and how likely users are to have the dependency installed (whether by popularity or ease of installation).

As mentioned, as modding progresses, users are becoming more and more accustomed to mods that have dependencies. Mod managers will also likely improve their dependency handling capabilities, further streamlining the process for users.

### What if the dependency mod is abandoned or becomes unavailable?

This is a valid concern. However, even though your mod might become unusable for a moment, history has shown that modding communities are resilient and will find a way to keep mods alive. If a mod is abandoned, the community will either find a way to keep it alive or create a new mod that does the same thing. Large dependency mods are hardly ever truly abandoned.

Note that, in a way, **if you build on top of a mod, you are also helping to keep it alive**. By adding a dependency to your mod, you are also promoting the original mod, and that can help to keep it alive one way or another.

In the end, this also brings up another extremely important point: **open source**.  At the time of writing, most of the popular BG3 framework mods are open source and could be picked up by the community if needed. Nexus tracks permissions, and authors cannot suddenly change the permissions of their mods to prevent others from using them. 

If you are a mod author, especially of a framework, **consider making your mod(s) open source with a permissive license**. This will allow other mod authors to keep your mod(s) alive if you are unable or unwilling to do so. Remember:

![If you build it, they will come.](https://i.imgur.com/XlpxKYX.gif)

### Closing thoughts

Adding dependencies to your mod is a great way to leverage the work of other mod authors and build on top of their work so that you can focus on achieving your vision. Adding them to your meta.lsx ensures that load order is correct (and versions, potentially).
In the end, however, it's your mod, and you should do what you want with it. I just hope that my tools and writings can nudge the community into a more collaborative direction!

---
title: How to add mod dependencies and eradicate load order problems with your mods
description: Explains how adding dependencies to meta.lsx ensure correct loading order, reduce user confusion, and simplify troubleshooting. The guide also addresses common concerns about dependencies, such as user reluctance and abandoned mods.
published: true
date: 2024-09-02T18:50:15.146Z
tags: meta, mods, modsuse, dependencies, dependency, meta.lsx, mod dependency
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
    <node id="Dependencies" />
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
              <attribute id="Version64" type="int64" value="36028797018963968" />
          </node>
        </children>
    </node>
    <node id="ModuleInfo">
        ...
```

That's it! You've just added a dependency to your mod. By properly declaring dependencies, you will:

- Ensure that required mods are loaded in the correct order (BG3MM handles this automatically)
- Eliminate the need for users to follow manual instructions (e.g., "*don't forget to add **this** mod*", "*load **this** mod before **that** mod*")
- Overall simplify troubleshooting by reducing incorrect/false positive bug reports

> **Note:** Make sure the `Name` is something that the user will recognize. At the time of writing, it is used by BG3MM to display the dependency name to the user.
> {.is-warning}

> **Tip**: the [BG3 Mod Helper](https://marketplace.visualstudio.com/items?itemName=ghostboats.bg3-mod-helper) extension provides buttons and commands to easily add dependencies to your mods. This tool can simplify the process and ensure correct formatting of the meta.lsx file.
> {.is-info}

### Why adding dependencies? I don't need them!

*Disclaimer: I am a maintainer of MCM and VC, so I might be biased. However, I will try to be as neutral as possible.*

Dependencies are essential for the evolution of modding communities. If you take a look at Skyrim's modding scene, the amount of complex and interconnected mods was made possible, for the most part, because of the community's ability to work together and build on top of each other's work.

> Some mods are focused on player-facing features, while others are focused on providing tools and frameworks for other mod authors. **Dependency mods are the backbone of a great modding community**. Framework maintainers spend a lot of time and effort to design and implement systems that other mod authors can leverage to create more complex and feature-rich mods, with less effort.
{.is-info}

Not all dependencies are created equal. Some try to fix inherent issues with the game and offer compatibility capabilities for other mods, and may be even almost unavoidable. In any case, dependencies are tools that will **allow you to build on top of other mods and focus on what you want to do, instead of reinventing the wheel.** You could theoretically implement all the features of a dependency mod in your mod, but that would be a tremendous waste of time and effort. As BG3 modding progresses, you can expect more and more tools and frameworks to be developed, and you should take advantage of them to create better mods.

### But then users won't download my mod!

As I said, as modding progresses, users are becoming more and more accustomed to mods that have dependencies. Mod managers will also likely improve their dependency handling capabilities, further streamlining the process for users.

If the dependency is popular or has an easy installation process, users will likely not mind much. It comes down to how impactful your mod is, the dependency is to your mod, and how likely users are to have the dependency installed (whether by popularity or ease of installation).

### What if the dependency mod is abandoned or becomes unavailable?

This is a valid concern. However, history has shown that modding communities are resilient and will find a way to keep mods alive. If a mod is abandoned, the community will either find a way to keep it alive or create a new mod that does the same thing. Large dependency mods are hardly ever abandoned.

Note that, in a way, **if you build on top of a mod, you are also helping to keep it alive**. By adding a dependency to your mod, you are also promoting the original mod, and that can help to keep it alive one way or another.

In the end, this also brings up another extremely important point: **open source**.  At the time of writing, most of the popular BG3 framework mods are open source and could be picked up by the community if needed. Nexus tracks permissions, and authors cannot suddenly change the permissions of their mods to prevent others from using them. 

If you are a mod author, especially of a framework, **consider making your mod(s) open source with a permissive license**. This will allow other mod authors to keep your mod(s) alive if you are unable or unwilling to do so. Remember:

![If you build it, they will come.](https://i.imgur.com/XlpxKYX.gif)

### Closing thoughts

Adding dependencies to your mod is a great way to leverage the work of other mod authors and build on top of their work so that you can focus on achieving your vision. In the end, however, it's your mod, and you should do what you want with it. I just hope that my tools and writings can nudge the community into a more collaborative direction!

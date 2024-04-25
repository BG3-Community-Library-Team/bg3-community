---
title: Compatibility Framework Usage
description: Quick guide to using Compatibility Framework
published: true
date: 2024-04-25T21:23:47.838Z
tags: se, script-extender, frameworks, compatibility
editor: markdown
dateCreated: 2024-04-25T20:56:58.092Z
---

# Adding Subclass Compatibility

## Getting Started

The Compatibility Framework(CF) makes it easy to provide compatibility between mods. There are two options:

1. Utilizing the Compatibility Framework's Configuration-Loading method
2. Utilizing the Compatibility Framework's Exposed API

The most common use-case is using CF to make Subclass Mods compatible, although the Framework supports a variety of other types of data: Spells, Spell Lists, Race Data, Action Resource Groups, Progressions, and  Feats, all of which are detailed on the CF [Github](https://github.com/BG3-Community-Library-Team/BG3-Compatibility-Framework/wiki). This tutorial will focus on using CF to make your Subclass mod compatible with others.

## Utilizing JSON Configuration Files
To use the CF's Configuration file method, you'll need to do the following:

1. In your mod's Workspace, under `Mod/ModName/`, create a `ScriptExtender` folder if it doesn't already exist.
2. In the newly-created `ScriptExtender` folder, create a new file, `CompatibilityFrameworkConfig.json`.

Now copy the following into `CompatibilityFrameworkConfig.json`:

```json
{
  "FileVersion": 1,
  "Progressions": [
    {
      "UUID": "UUID for the Main Class' Progression at the level at which subclasses are available  - use this or UUIDs, but not both",
      "UUIDs": ["first-class-progression-uuid", "second-class-progression-uuid"],
      "Subclasses": [
        {
          "UUID": "your-subclasses-class-description-uuid - use this or UUIDs, but not both",
          "UUIDs": ["first-subclass-class-description-uuid", "second-subclass-class-description-uuid"],
          "modGuid": "UUID Of Mod required for Insertion (Optional - defaults to the one that provides the config)"
        }
      ]
    }
  ]
}
```

## Utilizing CF API Directly

To use the CF's API, be sure you have your mod [set up for the Script Extender](https://github.com/Norbyte/bg3se/blob/1e5009ea8bb619341bf394543bcfdb3c9ffe3a9f/API.md#getting-started). Adjacent to your `BootstrapClient.lua` and `BootstrapServer.lua` files, create a file titled `InitCompatabilityFramework.lua`. In your `BoostrapClient.lua` file, paste the following: 

`Ext.Require("InitCompatibilityFramework.lua")`.

Now paste this into your `InitCompatibilityFramework.lua` file:

```lua
modGuid = "your-mods-uuid-in-metalsx"
subClassGuid = "your-subclasses-class-description-uuid"

if Ext.Mod.IsModLoaded("67fbbd53-7c7d-4cfa-9409-6d737b4d92a9") then
  local subClasses = {
    AuthorSubclass = {
      modGuid = modGuid,
      subClassGuid = subClassGuid,
      class = "lowercase parent class name or uuid of the progression where you get the subclass choice",
      subClassName = "English-localized name for your class (Optional)"
    }
  }

  local function OnStatsLoaded()
    Mods.SubclassCompatibilityFramework.Api.InsertSubClasses(subClasses)
  end

  Ext.Events.StatsLoaded:Subscribe(OnStatsLoaded)
end
```

What this does is, it checks if CF is installed by your user. If it is, it builds an object containing your Mod's UUID, your Subclass' UUID, the Parent Class, and a localized version of your Classes name. You'll need to make 4 changes here:

***`AuthorSubclass`:*** Replace the part before the `=` with your username and the name of the subclass. Example: `FeriatHexblade`. These can be shortened.

***`modGuid`:*** Change the value to your Mod's `UUID` as defined in `meta.lsx`.

***`subClassGuid`:*** Change the value to your Subclasses `UUID` as defined in `ClassDescriptions.lsx`.

***`class`:*** This can be one of two things:
1. The lower-case name of your classes Parent class. This will typically be one of the following: `barbarian`, `bard`, `cleric`, `druid`, `fighter`, `monk`, `paladin`, `ranger`, `rogue`, `sorcerer`, `warlock`, `wizard`.
2. The UUID of the Progression at which the subclass options for the parent class become available.

***`subClassName `:*** This field is optional. It will be used for a future sorting feature. Change the value to the English-localized name for your subclass.

Now you're all done! Be sure your mod loads earlier than `CompatibilityFramework`. 

***Note***: If your mod has multiple subclasses within it, you'll want to add an additional object to your `subClasses` table, like so:

```lua
local subClasses = {
    AuthorSubclassA = {
      modGuid = modGuid,
      subClassGuid = subClassAGuid,
      class = "lowercase parent class name or uuid of the progression where you get the subclass choice",
      subClassName = "English-localized name for your class (Optional)"
    },
    AuthorSubclassB = {
      modGuid = modGuid,
      subClassGuid = subClassBGuid,
      class = "lowercase parent class name or uuid of the progression where you get the subclass choice",
      subClassName = "English-localized name for your class (Optional)"
    },
  }
```

Be sure to define the additional subclasses UUID.
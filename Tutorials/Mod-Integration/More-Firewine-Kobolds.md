---
title: More Firewine Kobolds
description: How to customize or add 'More Firewine Kobolds' entries using JSON and SE
published: true
date: 2025-05-22T15:43:38.154Z
tags: se, script-extender, configuration
editor: markdown
dateCreated: 2025-05-21T22:15:15.682Z
---

# More Firewine Kobolds

A Baldur's Gate 3 mod that spawns (mostly) kobolds when destroying firewine barrels, configurable via MCM and very extensible through JSON or SE.

## Overview

By default, the mod spawns:

- 1 kobold in Act 1 areas
- 1 drunk redcap in Hag's lair
- 1 wild magic drunk kobold sorcerer in Crèche
- 3 kobolds (1 drunk) in Act 2
- 6 reduced size (`REDUCE` status) drunk kobolds in Act 3
- Easter egg flock in a later area of the game.

This mod is however highly extensible, and you can add your own spawn templates and region entries by modifying its JSON file in the `ScriptExtender` folder, or by using the public API via SE, in order to change:

- Which creatures are spawned (including defining multiple possible options)
- Status applied to spawned creatures
- Which regions to use specific spawn templates

With MCM, you can also toggle the mod on/off, and control the spawn rate globally or per-region (Act 1, Crèche, Act 2, Act 3). This is a slider (0-100%) that controls the chance of spawning when a Firewine barrel is destroyed.

This mod can be installed and uninstalled at any time.

## Features

- **Data-driven system**: The mod uses a JSON-based configuration system that allows for easy definition of spawn tables with reusable templates.
- **Regional spawns**: Different regions can have their own spawn tables with unique creatures and statuses.
- **Public API**: Other mods can programmatically add or modify spawn templates and region entries.
- **MCM integration**: Control spawn rates globally or per-region through the Mod Configuration Menu.
- **Status effects**: Spawned creatures can automatically receive status effects like `DRUNK`, `WILD_MAGIC`, `HASTE`, etc.
- **Weighted random selection**: Each potential spawn entry can have a weight value that determines its probability among other entries.
- **Composite templates**: Define multiple creatures together as a single spawn entry; easy to reason about and reuse.

### Configuration options

Basic configuration can be performed through the Mod Configuration Menu (MCM):

- **Enable/disable**: Toggle the mod on/off without uninstalling it.
- **Overall spawn rate**: Global slider (0-100%) that controls the chance of spawning when a Firewine barrel is destroyed.
- **Advanced settings**: Enable region-specific spawn rates.

### Customizing spawn tables

The mod uses a JSON file (`mfk_encounter_table.json`) to define what can spawn in each region. This file is located in the `ScriptExtender` folder and can be edited to customize spawns.

#### JSON structure

The mod uses a hybrid schema that supports reusable spawn templates or inline templates. Here are the defaults:

```lua
DefaultEncounterTable = {
    SpawnTemplatesDefs = {
        TwoNormalKobolds = {
            TemplateID = "45e31b7d-32ec-4f3d-8067-79061aeec77b",
            Quantity = { fixed = 2 },
            Statuses = {}
        },
        DrunkKobold = {
            TemplateID = "45e31b7d-32ec-4f3d-8067-79061aeec77b",
            Quantity = { fixed = 1 },
            Statuses = { "DRUNK" }
        },
        DrunkRedcap = {
            TemplateID = "c27dd409-9c26-458b-a845-03a8de78e330",
            Quantity = { fixed = 1 },
            Statuses = { "DRUNK" }
        },
        DualMeleeInvisible = {
            TemplateID = "dfdcfbaa-ed9b-48ba-8302-927c5f5af12d",
            Quantity = { fixed = 2 },
            Statuses = { "INVISIBLE" }
        },
        RangerDrunkWildMagic = {
            TemplateID = "1ad1fdb1-ea7f-492d-a72a-e282d9965b47",
            Quantity = { fixed = 1 },
            Statuses = { "DRUNK", "WILD_MAGIC" }
        },
        ["3Imps"] = {
            TemplateID = "feb1d610-4644-4dd0-8432-6e6a7be130d5",
            Quantity = { fixed = 3 },
            Statuses = { "DRUNK" }
        },
        SCL_KoboldEncounter = {
            Members = {
                { SpawnTemplate = "TwoNormalKobolds" },
                { SpawnTemplate = "DrunkKobold" }
            }
        },
        ["6SmallDrunkKobold"] = {
            TemplateID = "45e31b7d-32ec-4f3d-8067-79061aeec77b",
            Quantity = { fixed = 6 },
            Statuses = { "DRUNK", "REDUCE" }
        }
    },

    Regions = {
        WLD = {
            Entries = {
                {
                    TemplateID = "45e31b7d-32ec-4f3d-8067-79061aeec77b",
                    Quantity = { fixed = 1 },
                    Statuses = {},
                    Weight = 25
                }
            }
        },

        WLD_Hag = {
            Entries = {
                { SpawnTemplate = "DrunkRedcap", Weight = 30 },
                {
                    TemplateID = "08f651c6-d6ca-44c9-bae0-eb0318c4ca6b",
                    Quantity = { fixed = 1 },
                    Statuses = { "DRUNK", "HASTE" },
                    Weight = 25
                }
            }
        },

        CRE = {
            Entries = {
                { SpawnTemplate = "RangerDrunkWildMagic", Weight = 20 }
            }
        },

        SCL = {
            Entries = {
                { SpawnTemplate = "SCL_KoboldEncounter", Weight = 100 }
            }
        },

        BGO = {
            Entries = {
                { SpawnTemplate = "6SmallDrunkKobold", Weight = 15 }
            }
        },
        HOH = {
            Entries = {
                { SpawnTemplate = "3Imps", Weight = 100 }
            }
        },
    }
}
```

#### Field explanations

##### `SpawnTemplatesDefs` section

- **SpawnTemplatesDefs**: A dictionary of reusable spawn templates that can be referenced in region entries. They are defined by their key (e.g., "DrunkKobold"): A unique identifier for the template. Inside, you can define atomic templates (single creatures) or composite templates (multiple creatures together).

- **Atomic templates**:
  - **TemplateID**: The UUID of the creature template to spawn. Use [Norbyte's website](https://bg3.norbyte.dev) or other tools to find template UUIDs.
  - **Quantity**: How many creatures to spawn. Currently only supports `{"fixed": N}` format.
  - **Statuses**: An array of status effect names to apply to the spawned creature.

- **Composite templates**:
  - **Members** (for composite templates): An array of member templates to spawn together. Cannot be combined with TemplateID/Quantity/Statuses.
    - Each member can be either:
      - A reference to another template: `{ "Template": "TemplateName" }`
      - An inline atomic template: `{ "TemplateID": "...", "Quantity": {...}, "Statuses": [...] }`

#### Composite templates

Composite templates allow you to spawn multiple creatures together as a single encounter. For example:

```json
"SCL_KoboldEncounter": {
  "Members": [
    { "Template": "TwoNormalKobolds" },
    { "Template": "DrunkKobold" }
  ]
}
```

This will spawn 2 normal kobolds and 1 drunk kobold together as a single encounter, to be referenced by `SCL_KoboldEncounter`.

**Important notes about composite templates:**

- Composite templates cannot be nested (a composite cannot contain another composite).
- All members of a composite template must be atomic templates.
- The weight system still applies at the *region entry* level, not per member.

#### `Regions` section

- **Regions**: A dictionary of regions, with region IDs as keys.
  - **Entries**: A list of potential spawns for this region.
    - Option 1: Reference a spawn template with `{ "SpawnTemplate": "TemplateName", "Weight": N }`
    - Option 2: Define an inline entry with the same fields as a spawn template plus a Weight.
  - **Weight**: The weight of this entry. This is used to determine the probability of this entry being selected in the pool of possible spawns.

### Adding new entries

To add a new spawn type:

1. Open the `mfk_encounter_table.json` file in the `ScriptExtender` folder.
2. Find the UUID of the creature template you want to use.
3. Either:
   - Add a new spawn template to the `SpawnTemplatesDefs` section, then reference it in a region's entries.
   - Add an inline entry directly to a region's entries.
4. Set the weight relative to other entries.
5. Specify any status effects you want the creature to have.

You can also do this programmatically using the public API (see below).

### Default regions

The mod comes with default configurations for these regions:

- `WLD`: The main wilderness area (Act 1)
- `WLD_Hag`: The Hag's lair (Act 1)
- `CRE`: The Crèche (Act 1.5)
- `SCL`: Shadow-cursed lands (Act 2, Shadow-cursed lands, Nightsong, etc)
- `BGO`: Baldur's Gate areas (Act 3, Wyrms Crossing and city proper)

You can add more regions as needed, using level names to work correctly. It will match partial names, so `WLD` will match all Act 1, `SCL` will match all shadow-cursed lands (All Act 2 areas), etc.
`WLD_Hag` will match all Act 1 Hag levels, being used instead of `WLD` entries; The closest/longest match will be used.

### Technical notes

- The mod automatically creates the default JSON file if no valid JSON is found.
- The weights are normalized within each region. If a region has only one entry, any positive weight guarantees 100% chance of that entry being selected.

---

## Public API for modders

*More Firewine Kobolds* provides a (server-side) Lua API that other mods can use to add or modify spawn templates and region entries programmatically. This is useful if you want to add your custom creatures to the spawn tables without editing the JSON file directly, or if you want to add your own spawn templates and region entries.

Changes made via the API are persisted to disk automatically.

### Available functions

```lua
-- Register or overwrite a spawn template
-- Returns true on success, false on failure
Mods.MoreFirewineKobolds.API.RegisterSpawnTemplateDef(id, spawnTemplateTable)

-- Add (or overwrite if same SpawnTemplates present) an entry to a region
-- Returns true on success, false on failure
Mods.MoreFirewineKobolds.API.AddRegionEntry(regionId, entryTable)

-- Change weight for an existing region entry
-- Key can be either an index number or a SpawnTemplates ID
-- Returns true on success, false on failure
Mods.MoreFirewineKobolds.API.SetEntryWeight(regionId, key, newWeight)
```

### Example usage

```lua
-- Register a new spawn template for a stealth kobold
Mods.MoreFirewineKobolds.API.RegisterSpawnTemplateDef("StealthRangerKobold", {TemplateID = "1ad1fdb1-ea7f-492d-a72a-e282d9965b47",Quantity = { fixed = 1 },Statuses = { "INVISIBLE", "HASTE" }})

-- Add a new entry to a region using a spawn template
Mods.MoreFirewineKobolds.API.AddRegionEntry("WLD", {
  SpawnTemplate = "StealthRangerKobold",
  Weight = 25
})

-- Add an inline entry directly to a region
Mods.MoreFirewineKobolds.API.AddRegionEntry("SCL", {
  TemplateID = "22fc3ef8-64f0-4298-a598-03fbc9dfb9aa",
  Quantity = { fixed = 1 },
  Statuses = { "WILD_MAGIC" },
  Weight = 15
})

-- Change the weight of an existing entry
Mods.MoreFirewineKobolds.API.SetEntryWeight("WLD_Main_A", "DrunkKobold", 40)
```

### Integration tips

There are two main approaches to integrating with More Firewine Kobolds:

1. **API calls at load time**: Use the API functions in your mod's initialization code to register templates and add entries. Changes will be persisted automatically.

```lua
Ext.Events.SessionLoaded:Subscribe(function()
  -- Make sure MFK is loaded
  if Mods.MoreFirewineKobolds and Mods.MoreFirewineKobolds.API then
    -- Add your custom templates and entries here
    Mods.MoreFirewineKobolds.API.RegisterSpawnTemplateDef("MyCustomKobold", { ... })
  end
end)
```

2. **Companion JSON file**: Create a companion JSON file with your additions and load it into the mod's tables:

```lua
Ext.Events.SessionLoaded:Subscribe(function()
  -- Make sure MFK is loaded
  if Mods.MoreFirewineKobolds and Mods.MoreFirewineKobolds.API then
    local data = Ext.Json.Parse(Ext.IO.LoadFile("my_kobold_additions.json"))

    -- Register spawn templates
    for id, template in pairs(data.SpawnTemplate or {}) do
      Mods.MoreFirewineKobolds.API.RegisterSpawnTemplateDef(id, template)
    end

    -- Add region entries
    for regionId, region in pairs(data.Regions or {}) do
      for _, entry in ipairs(region.Entries or {}) do
        Mods.MoreFirewineKobolds.API.AddRegionEntry(regionId, entry)
      end
    end
  end
end)
```

> If your mod *requires* More Firewine Kobolds, [add it as a dependency](/Tutorials/General/Basic/adding-mod-dependencies) to minimize load order problems.
> {.is-success}

---

## Common template IDs

Here are some template IDs used in the default configuration:

- `45e31b7d-32ec-4f3d-8067-79061aeec77b`: Kobold
- `1ad1fdb1-ea7f-492d-a72a-e282d9965b47`: Kobold Ranger
- `22fc3ef8-64f0-4298-a598-03fbc9dfb9aa`: Kobold Inventor
- `dfdcfbaa-ed9b-48ba-8302-927c5f5af12d`: Kobold Melee

## Common status effects

Some common status effects to apply:

- `DRUNK`: Makes the creature drunk
- `WILD_MAGIC`: Causes wild magic effects
- `HASTE`: Increases speed and grants an extra action
- `POISONED`: Applies poison condition

## Game Levels

Here's a list of levels that the game uses, which can be used as region IDs:

| Level ID       |
|----------------|
| BGO_Main_A     |
| BGO_WyrmsCrossing_C |
| GLO_Cambion_B  |
| GUS_WorkAtmosphere_A |
| SCL_Main_A     |
| TUT_Avernus_C  |
| WLD_CAMP_CineTriggers |
| WLD_Campfire_E |
| WLD_Chapel_H   |
| WLD_Chapel_Push |
| WLD_CIN_Dreamscene_Daisy_A |
| WLD_CIN_Dreamscene_Forest_A |
| WLD_CIN_Dreamscene_Laezel_A |
| WLD_CIN_Raft_A |
| WLD_Crashsite_D |
| WLD_DenSubs_B  |
| WLD_DruidSubs_B |
| WLD_Forest_G   |
| WLD_GoblinCamp_D |
| WLD_Hag_C_Evil |
| WLD_Hag_C_Happy |
| WLD_HagLair_D  |
| WLD_Main_A     |
| WLD_NautiloidCockpit_A |
| WLD_OwlbearCave_B |
| WLD_Plains_D   |
| WLD_Raft_A     |
| WLD_RangerCamp_I |
| WLD_SharTemple_E |
| WLD_Underdark_C |
| WLD_UnderdarkShrine_A |
| WLD_UnderdarkSubs_C |
| WLD_UnderdarkSubs_SharVista_A |
| WLD_UnderdarkTransitions_A |
| WLD_UnderdarkTransitions_B |
| WLD_UnderdarkTransitions_C |

Note that some of these are used in very specific locations, and may only be used in cut content. Use generic level names (e.g., `WLD` for Act 1) if you want to apply your changes to broader regions.
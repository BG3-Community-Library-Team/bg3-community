---
title: Mod Configuration Menu
description: Brief MCM overview + detailed guide for integrating mods with it
published: true
date: 2024-05-22T13:02:15.029Z
tags: mcm, mod configuration menu, settings, config, configuration, se mod settings, se mod configuration, mod settings, mod menu
editor: markdown
dateCreated: 2024-05-05T22:37:40.947Z
---

# Mod Configuration Menu	

Baldur's Gate 3 Mod Configuration Menu (`BG3MCM` or MCM) is a mod that provides an in-game UI to enable players to intuitively manage mod settings as defined by mod authors. It supports various setting types, including integers, floats, checkboxes, text inputs, combos/dropdowns, radio buttons, sliders, drags, and color pickers.

This documentation is aimed at mod authors who want to integrate their mods with MCM. If you are a player looking to use MCM to configure mods, please refer to the [Nexus Mods page](https://www.nexusmods.com/baldursgate3/mods/9162 'MCM on Nexus Mods') for instructions. This documentation provides a thorough guide on the concepts behind MCM, the features it provides to mod authors, and how to integrate MCM into your mod. You can also use the table of contents below to navigate to a desired section.

## Table of Contents

- [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features for mod authors](#features-for-mod-authors)
  - [Concepts](#concepts)
  - [Integrating MCM into your mod](#integrating-mcm-into-your-mod)
    - [Defining a blueprint](#defining-a-blueprint)
    - [The MCM Schema](#the-mcm-schema)
    - [Using values from MCM](#using-values-from-mcm)
    - [Inserting custom UI elements](#inserting-custom-ui-elements)
    - [How validation works](#how-validation-works)
    - [Localization support](#localization-support)
  - [MCM demo](#mcm-demo)
  
## Features for mod authors

Below are listed some nice features that MCM provides to mod authors:
> • ***Easy to use***: MCM provides a simple and intuitive way to define your mod's settings. Integrating MCM into your mod only requires creating a simple blueprint JSON file and replacing a few lines of code;
>
> • ***UI without writing client-side code***: MCM handles the UI for you, so you don't have to write any client-side code or learn the IMGUI API to display your mod's settings, since IMGUI is only available on the client-side.
>
> • ***Simplifies settings management***: MCM takes care of saving and loading your mod's settings automatically, so you don't have to build an entire configuration system to manage JSON files;
>
> • ***Instant saving and loading***: Unlike the traditional way of handling settings, MCM-integrated mods update settings in real-time as they are changed, without requiring save reloads;
>
> • ***Minimizes user error***: MCM handles the UI and validation of settings, reducing the risk of user error when configuring your mod and encouraging them to do so safely. It skips the need for manual editing of configuration files, which is a very common source of errors;
>
> • ***Validation checks***: MCM runs dozens of validation checks to ensure that your blueprint for integration was correctly written, while providing detailed error messages if something is wrong. It also validates the settings' values at runtime to ensure that they respect the defined constraints, which is especially useful if JSON settings files were manually edited, something that is supported by MCM;
>
> • ***Supports bespoke UI injection***: MCM allows you to inject your own UI elements into the MCM UI, so you could even have a mix of MCM-generated UI and your own custom UI in the same mod. This is useful when your mod has customized features largely unrelated to configuration;
>
> • **Cross-mod settings access**: The unified config approach promoted by MCM allows for straightforward access to settings from other mods, as arbitrary implementations are mostly eliminated, facilitating compatibility and interoperability.
>
> • ***Doesn't clutter UI***: MCM centralizes settings for all mods that use it, so you don't have to worry about cluttering players' screens with yet another IMGUI window, thinking when should it initialize, activate, or even about keybindings - and possible conflicts thereof - for  showing such windows.
>
> • ***Robustness***: MCM has more than 40 automated server-side tests aiming to ensure that it works as expected, edge cases are handled, and errors are gracefully reported without halting the framework or game; errors from one mod won't affect the others.
>
> • ***UI agnostic***: MCM was designed to be, first and foremost, a standalone configuration manager. This means that even if support for IMGUI were to be entirely removed or replaced, the underlying structure of MCM would still function correctly;
	> • This also means that **users who can't see the IMGUI window will still have MCM working as a config manager**.
>
> • ***Multiple profiles***: MCM has support for creating, saving, loading, and deleting multiple configuration profiles, which is useful for mod authors to separate their testing configurations while developing mods;
>
> • ***Localization support***: MCM supports localizing mod settings, allowing you to optionally provide translations for different languages.
{.is-success}

## Concepts

First, let's establish some concepts that are important for understanding MCM. These will be used throughout the documentation:

>**Setting**: A **single configuration option** that can be set by the user.
>**Config/Configuration/Settings**: All the possible settings; the **entire set of settings** for a mod.
>**Blueprint**: Defines the **structure of a mod's configuration for MCM** to use (with a `MCM_blueprint.json` file).
>**MCM Schema**: Dictates the **structure of the blueprint**/configuration definition; the 'metaschema'.
{.is-info}

## Integrating MCM into your mod

Mod authors need to integrate their mods with MCM for their settings to appear in the UI. The subsections below go in detail about this process, but it is essentially done in two steps:

  1. Define the blueprint JSON file for your mod's settings and place it alongside your mod's `meta.lsx` file. It's also recommended to define BG3MCM as a dependency in your meta.lsx file. [Listing a dependency in a meta.lsx file](https://github.com/AtilioA/BG3-auto-send-food-to-camp/blob/46822bb0a8af4db524fd1ccb6f8a277724f5630c/Auto%20Send%20Food%20To%20Camp/Mods/AutoSendFoodToCamp/meta.lsx#L7-L24 'Auto Send Food To Camp');
  2. Replace your mod's logic for reading/writing settings with calls to the MCM API, using the setting's ID as defined in the blueprint.

The `MCM_blueprint.json` file is how you specify your mod's configuration definition; this JSON file will define how your settings are to be structured, what are their names, defaults, etc., allowing for automatic generation of a user-friendly interface and validation of user-set values.

### Defining a blueprint

> **Recap**: a blueprint is a JSON file that defines the structure of your mod's configuration settings. It is used by MCM to generate the UI and validate the settings. It should be named `MCM_blueprint.json` and placed alongside your mod's `meta.lsx` file.
{.is-info}

### The MCM Schema

The MCM Schema dictates how you should structure your blueprint file, and you can [get it from GitHub](https://github.com/AtilioA/BG3-MCM/blob/main/.vscode/schema.json).

This schema file can be used to **write and validate** your `MCM_blueprint.json` file, as it will help enforcing the intended structure of the MCM Schema in your blueprint file, ensuring that it is correctly formatted and adheres to the schema.

**Although not mandatory, it is extremely recommended that you set it up, as you can easily validate your blueprint files** using VSCode by adding this JSON schema entry to your settings:

1. Press F1, type and select 'Open User Settings (JSON)'
2. Copy the following and paste inside the main object of the JSON you just opened:

```json
"json.schemas": [
  {
    "fileMatch": [
      "MCM_blueprint*.json"
    ],
    "url": "https://raw.githubusercontent.com/AtilioA/BG3-MCM/main/.vscode/schema.json"
  }
],
```
*Alternatively, you could replace `url` with the schema JSON file path (e.g. could be where you place IDEHelpers or Osi.lua files). It should work with the URL though, and this way you'll always have an up-to-date schema.

3. This might require a Reload Window or just reopening your editor, but you're done! You won't need to do this again, and the schema file will be always up-to-date with MCM releases.


> Having the schema file set up in your IDE will help you write the blueprint file correctly, without having to guess the structure or wonder if you're missing something. A few minor features, such as `ModName` (to replace the string used for your mod's name) are only documented by the JSON schema.
{.is-info}

Following are the main components of the MCM schema. Don't stress over this too much, the schema file will guide you when writing blueprints.

- **Organizational structure**: the MCM Schema defines a hierarchical organization using `Tabs` and `Sections`:
  - `Tabs`: Serve as top-level organizational units in the MCM menu. Each tab can exclusively contain either `Sections` or standalone `Settings`.
    - `Sections`: Sub-divisions within tabs to group related settings.

  - **`Settings`**:
    - `Id`: A unique string identifier for each setting, similar to a variable name in your code; used to reference the setting programmatically.
    - `Name`: The readable name of the setting as to be displayed in the MCM menu.
    - `Type`: Defines the data type and ultimately the UI representation of the setting, with supported types including `int`, `float`, `checkbox`, `text`, `enum`, `radio`, `slider_int`, `slider_float`, `drag_int`, `drag_float`, `color_picker`, `color_edit`;
    - `Default`: Specifies the initial value of the setting used during initialization or when a reset is needed. Supports various data types (`integer`, `number`, `boolean`, `string`, `object`, `null`) depending on the setting type.
    - `Description` and `Tooltip`: Textual explanations of the setting's purpose and usage, where `Description` is visible below the setting's widget and `Tooltip` appears on hover. It is required to have at least one of these.
    - `Options`: Additional parameters that tailor the setting's behavior, applicable to certain types like `enum`, `radio`, sliders and drags. This includes:
      - `Choices`: The options to be made available for `enum` and `radio` types.
      - `Min` and `Max`: Boundary values for types such as `slider`/`drag`.

Thus, the main content of the blueprint is defined in the `Tabs` and `Settings` properties. You'll need to include at least one of these - either a list of tabs, or a list of standalone settings.
Within each tab, you can define either `Sections` or a list of `Settings`. Sections provide a way to group related settings together under a header. Each setting has an `Id`, `Name`, `Type`, `Default` value, and at least a `Tooltip` or a `Description`. Each setting `Id` must be unique across the entire blueprint, and that is validated by one of the many validation checks MCM performs.

Future versions of MCM might make this structure less strict, allowing nesting tabs inside sections and vice-versa.


> If your [mod is symlinked](https://wiki.bg3.community/en/Tutorials/ScriptExtender/GettingStarted#h-4-symlinking 'Symlinking mods tutorial'), you can try out changes to your mod's blueprint in-game by using `reset` in the console without having to restart the game every time you make a change to the blueprint file.
{.is-info}


> For examples of mods that use MCM, you can check:
> [MCM Demo (WIP)](https://github.com/AtilioA/BG3-MCM/blob/308141a5c1b1e91d87440f066a62a4f2b9f41e55/Mod%20Configuration%20Menu/Mods/BG3MCM/MCM_blueprint.json) - showcases all input types, tab insertion and a bit of client/server communication
> [Auto Send Food To Camp](https://github.com/AtilioA/BG3-auto-send-food-to-camp/blob/MCM-integration/Auto%20Send%20Food%20To%20Camp/Mods/AutoSendFoodToCamp/MCM_blueprint.json)
> [Smart Autosaving](https://github.com/AtilioA/BG3-smart-autosaving/blob/main/Smart%20Autosaving/Mods/SmartAutosaving/MCM_blueprint.json)
> [Preemptively Label Containers](https://github.com/AtilioA/BG3-preemptively-label-containers/blob/main/Preemptively%20Label%20Containers/Mods/PreemptivelyLabelContainers/MCM_blueprint.json)
{.is-success}

---

### Using values from MCM

After setting up the blueprint, mod authors can access the values set by the player through the MCM API from anywhere in their mod's code.

```lua
-- Get the value of a setting with the ID "MySetting"
local mySettingValue = Mods.BG3MCM.MCMAPI:GetSettingValue("MySetting", ModuleUUID)

-- Set the value of a setting
Mods.BG3MCM.MCMAPI:SetSettingValue("MySetting", newValue, ModuleUUID)
```

You can also listen to changes to settings values by listening to net messages like this:

```lua
Ext.RegisterNetListener("MCM_Saved_Setting", function(call, payload)
    local data = Ext.Json.Parse(payload)
    if not data or data.modGUID ~= ModuleUUID or not data.settingId then
        return
    end

    if data.settingId == "debug_level" then
        _D("Setting debug level to " .. data.value)
        ASFTCPrinter.DebugLevel = data.value
    end
end)
```

#### Reducing verbiage
You can allow global usage of `MCMAPI` by incorporating MCM's table early in your scripts with `setmetatable(Mods[Ext.Mod.GetMod(ModuleUUID).Info.Directory], { __index = Mods.BG3MCM })`. 
Likewise, you can define a global function such as this early in your scripts:
```lua
function MCMGet(settingID)
    return Mods.BG3MCM.MCMAPI:GetSettingValue(settingID, ModuleUUID)
end
-- Now, get values by calling MCMGet("setting_id")
```
Otherwise, prepend `Mods.BG3MCM` to all API calls.


### Inserting custom UI elements

MCM allows mod authors to insert custom UI elements into the MCM UI. This can be done using the `InsertModMenuTab` function from MCM's `IMGUIAPI`:

```lua
Mods.BG3MCM.IMGUIAPI:InsertModMenuTab(ModuleUUID, "Inserted tab", function(tabHeader)
    local myCustomWidget = tabHeader:AddButton("My custom widget")
    myCustomWidget.OnClick = function()
        _D("My custom widget was clicked!")
    end
end)
```

> You can define an entire tab's content — not just a widget — and call the `InsertModMenuTab` function to insert it into the MCM window, inside the space dedicated for your mod.
{.is-info}

### Listening to MCM events

MCM uses a set of channels to communicate between the client and server. Some of these can be useful for mod authors to listen to, as they can use this to update their mod's behavior based on changes from MCM, such as when a setting is saved:

`MCM_Saved_Setting`: fired whenever a setting value is saved by MCM, to be written to the settings JSON file. The payload contains the setting ID and the new value. Example usage:
```lua
-- In your MCM-integrated mod's code
Ext.RegisterNetListener("MCM_Saved_Setting", function(call, payload)
    local data = Ext.Json.Parse(payload)
    if not data or data.modGUID ~= ModuleUUID or not data.settingId then
        return
    end

    if data.settingId == "debug_level" then
        _D("Setting debug level to " .. data.value)
        MyMod.DebugLevel = data.value
    end
end)
```

Here are some other events that can be listened to:
- `MCM_Setting_Reset`: Fired when a setting is reset to its default value.
- Profile-related events:
	- `MCM_Server_Created_Profile`: Fired when a new profile is created.
	- `MCM_Server_Set_Profile`: Fired when a profile is set as the active one.
	- `MCM_Server_Deleted_Profile`: Fired when a profile is deleted.
- Other events:
	- `MCM_Mod_Tab_Added`: Fired when a mod inserts a custom tab into the MCM UI.

> Always verify the `modGUID` in the payload to confirm that the event pertains to the mod of interest (typically your own, which you have global access to via `ModuleUUID`).
{.is-warning}

### How validation works

Validation is divided into two main categories: blueprint validation and settings validation. Blueprint validation ensures that the blueprint JSON file is correctly formatted and adheres to the MCM schema. Settings validation, on the other hand, ensures that the settings values are valid and respect the constraints defined in the blueprint.

MCM performs validation checks when:

- Blueprint validation:
  - Loading blueprints from the `MCM_blueprint.json`;
- Settings validation:
  - Loading settings from a JSON file (+ e.g., switching between profiles);
  - Setting values programmatically through the API (TODO, effectively same as below);
  - Processing user input from the UI (TODO, effectively same as above);


>• Settings not present in the blueprint will be removed from the settings JSON file;
>• Invalid settings values will be replaced with their respective default value as specified in the blueprint;
>• New settings are automatically introduced to the settings JSON file when new settings are added to the schema;
>Therefore, mod authors can safely add or remove settings from the blueprint without worrying about inconsistencies in the settings JSON file.
{.is-success}
### Localization support

In your blueprint, you can define localization handles for various elements of the configuration, including:

- Tab names and descriptions
- Section names
- Setting names, descriptions, and tooltips
- Enum/radio choice labels

This is achieved through the use of "handles" - unique identifiers that can be used to look up the localized strings, just as used by the vanilla game. For every element that you can put a string in the blueprint, you can use a handle by adding a `Handles` object in the same level as the element, like this:

```json
{
    "TabId": "myTab",
    "TabName": "My tab default display name",
    "Handles": {
        "NameHandle": "h3b019e17g75fcg48ccg8063g4de5bfcc7792"
    }
},
```

> These handles should have been listed in a loca file in your mod in order to be used;
> • If handles are provided and their content can be retrieved, the localized string will be used instead of the usual name/description/tooltip;
> • If the handle is not found, the usual string will be used.
{.is-info}

## MCM demo

WIP: this demo will showcase every widget and also some use cases: listening to settings changes & other events, custom UI, custom UI + config
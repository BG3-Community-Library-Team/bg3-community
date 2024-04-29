---
title: Oath Framework Usage
description: Learn how to utilize the Oath Framework for improved handling of Oathbreaking
published: true
date: 2024-04-29T20:17:21.325Z
tags: se, script-extender, frameworks, scripting
editor: markdown
dateCreated: 2024-04-27T18:26:12.159Z
---


# Oath Framework Usage
The Oath Framework is an API designed to allow Custom Paladin mods to take advantage of the Oathbreaking features of Baldur's Gate 3, while providing a unique way to Break their Oaths, separate from how Vanilla Paladins would. It also provides the capability for Redemption events, allowing a way to regain your oath without bribing the Oathbreaker Knight. In the future, it is also planned to add ways to allow Clerics and Warlocks to have similar functionality.

Custom Paladin subclasses all run into the problem of having to piggy-back off of Vanilla Oathbreaking triggers. This is both due to the complexity of the game's Dialog/Flag/Tag system, and due to SE still seeming "scary" to some. While Oath Framework doesn't resolve the second piece, it does provide an easy configuration method to register your custom tags and flags for Paladins, as well as API functions that can be used to both Break and Redeem an Oath.

This is a guide on on how to set up your mod to have custom Oath Breaking/Redemption events. This guide involves a bit of Lua know-how, but will attempt to explain the general set-up for the Lua.

<div class="row">
	<div class="col col-4">

  There are a couple common acronym's I'll be using:
   
- Script Extender (SE)
- Community Library (CL)
- Oath Framework (OF)
  </div>
  <div class="col col-8">

These links will help you further understand how to use Script Extender
- [Script Extender API documentation](https://github.com/Norbyte/bg3se/blob/main/Docs/API.md)
- [LaughingLeader's SE Development Set-up Guide](https://github.com/LaughingLeader/BG3ModdingTools/wiki/Script-Extender-Lua-Setup)
- [CL's Script Extender mod template](https://github.com/BG3-Community-Library-Team/SETemplate)

  </div>
</div>

    
## Basic Set-up
You will need to make sure you have the following files set up:
> 1. Your Class Tag (`Public/ModName/Tags/uuid.lsf.lsx`)
> 2. Your Oathbreaking Class Tag (`Public/ModName/Tags/uuid.lsf.lsx`)
> 3. Your Oathbreaker Event Flag (`Public/Shared/Flags/uuid.lsf.lsx`)
{.is-info}

Replace `uuid` with a brand new UUID that will also be used in the file's UUID field.

### Tags
> This is unnecessary if you're just adding Oathbreak/Redemption Pathways to vanilla classes
{.is-warning}


Here is where you define the tags needed to ensure your custom subclass is properly registered. You'll need two of these, one for your Subclass, and one for the Broken Oath:

**Subclass**
```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="8" build="606" lslib_meta="v1,bswap_guids" />
	<region id="Tags">
		<node id="Tags">
			<attribute id="UUID" type="guid" value="7c89622b-4194-41df-b2ff-145a5056ee49" />
			<attribute id="Name" type="FixedString" value="PALADIN_ANCIENTS" />
			<attribute id="DisplayName" type="TranslatedString" handle="h26fe3b00g79b5g4150g9647gbfea0f24acc9" version="2" />
			<attribute id="DisplayDescription" type="TranslatedString" handle="h7f1a984fgbf47g443fg904dgc1629c44d642" version="1" />
			<attribute id="Icon" type="FixedString" value="" />
			<attribute id="Description" type="LSString" value="Paladin subclass" />
			<children>
				<node id="Categories">
					<children>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Code" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Dialog" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Story" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Class" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="CharacterSheet" />
						</node>
					</children>
				</node>
				<node id="Properties" />
			</children>
		</node>
	</region>
</save>
```
**Broken Oath**
```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="8" build="606" lslib_meta="v1,bswap_guids" />
	<region id="Tags">
		<node id="Tags">
			<attribute id="UUID" type="guid" value="d84a8a0b-b648-464c-9bd5-1ed9b965da2a" />
			<attribute id="Name" type="FixedString" value="OATHBREAKER_ANCIENTS" />
			<attribute id="DisplayName" type="TranslatedString" handle="hd3d471e4g80eag4be7ga23eg8cc07e2e27a3" version="2" />
			<attribute id="DisplayDescription" type="TranslatedString" handle="hc230d5e2g8d38g4541ga8fbgf0f061d7c093" version="1" />
			<attribute id="Icon" type="FixedString" value="" />
			<attribute id="Description" type="LSString" value="Used to remember paladin subclass" />
			<children>
				<node id="Categories">
					<children>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Code" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Dialog" />
						</node>
						<node id="Category">
							<attribute id="Name" type="LSString" value="Story" />
						</node>
					</children>
				</node>
				<node id="Properties" />
			</children>
		</node>
	</region>
</save>
```

### Oathbreaker Event Flag
> This is always required
{.is-warning}


Finally, we need our event flag. This, along with the tags, is how the underlying Larian code handles conditionals and keeps things from breaking behind the scenes.

```xml
<?xml version="1.0" encoding="utf-8"?>
<save>
	<version major="4" minor="0" revision="8" build="607" lslib_meta="v1,bswap_guids" />
	<region id="Flags">
		<node id="Flags">
			<attribute id="UUID" type="guid" value="7cf0bd9c-f089-45a3-88fb-03087d3d8b95" />
			<attribute id="Name" type="FixedString" value="GLO_PaladinOathbreaker_Event_AncientsBrokeOath" />
			<attribute id="Description" type="LSString" value="Paladin with oath of the ancients broke their oath. If character who receives this flags does not have this oath it will do nothing." />
			<attribute id="Usage" type="uint8" value="4" />
		</node>
	</region>
</save>
```

## Configuration/Registration
If you're adding new Paladin Oaths, you'll need to supply an `OathFrameworkConfig.json` file. This file is what allows Oath Framework to register Subclasses for the game to properly identify when breaking or redeeming an Oath. A [Sample Config](https://github.com/BG3-Community-Library-Team/OathFramework/blob/main/OathFrameworkConfig.sample.json) is provided in the repo.

Your file will look something like this:
```json
{
  "FileVersion": 1,
  "Tags": [
    {
      "OathbreakerSubclassData": [
        {
          "SubclassTag": "PALADIN_SUBCLASS_tag-uuid-value",
          "OathbreakerTag": "OATHBREAKER_SUBCLASS_tag-uuid-value",
          "SubclassOathBrokenEventFlag": "FLAG_NAME_VALUE_flag-uuid-value",
          "CrimesToReact": ["Crime", "Another Crime", "Even more Crime"]
        }
      ]
    }
  ]
}
```

The `SubclassTag` and `OathbreakerTag` will typically be required, as will the `SubclassOathBrokenEventFlag`, when dealing with custom Oaths. `CrimesToReact` is entirely optional, but may be useful if you want certain crimes to be more likely to break a specific Oath. A full list of valid Crimes for the `CrimesToReact` field can be found [here](https://github.com/BG3-Community-Library-Team/OathFramework/wiki/List-of-Crimes)

Example:
```json
{
  "FileVersion": 1,
  "Tags": [
    {
      "modGuids": [""],
      "OathbreakerSubclassData": [
        {
          "SubclassTag": "PALADIN_ANCIENTS_7c89622b-4194-41df-b2ff-145a5056ee49",
          "OathbreakerTag": "OATHBREAKER_ANCIENTS_d84a8a0b-b648-464c-9bd5-1ed9b965da2a",
          "SubclassOathBrokenEventFlag": "GLO_PaladinOathbreaker_Event_AncientsBrokeOath_7cf0bd9c-f089-45a3-88fb-03087d3d8b95",
          "CrimesToReact": ["Assault", "UseForbiddenItem", "Vandalise"]
        }
      ]
    }
  ]
}
```

> **A note on Flags**
> There is no comprehensive list of flags in the game yet, but there are a few ways to find them.
> - Community Library is in the process of [indexing flags](https://github.com/BG3-Community-Library-Team/BG3-Community-Library/tree/main/CommunityLibrary/Mods/CommunityLibrary/ScriptExtender/Lua/IdDictionary/StaticData/Flags) for easy reference.
> - `Shared`, `SharedDev`, `Gustav`, and `GustavDev` have a `Public/ModuleName/Flags` folder that you can search through manually.
> - Unpacking `Mods/GustavDev/Story/story.div.osi` using [LSLib's](https://github.com/Norbyte/lslib/) story tools, and looking through the story goals.
{.is-info}
    
## Working with Script Extender
Once your Custom Paladin Subclass has been registered, all that's left is listening for events that should cause an Oath to Break or Redeem, and then calling the Modify Oath API function.

You'll need to utilize Script Extender to create Osiris Listeners, watching for events that you will then provide logic to in order to determine if the conditions are met or not. Once the conditions are met, you need a few things things: any IDs for required mods, the relevant Character's ID the relevant Subclass Tag, and whether you want it to be a `Break` or `Redeem` event.

Let's start simple though. Follow the basic SE set-up, and then create a folder structure like this, subbing `MODNAME` with the name of your mod:
```
Mods/MODNAME/ScriptExtender/
                            Config.json
                            OathFrameworkConfig.json
                            Lua/
                                BoostrapServer.lua
                                Globals.lua
                                Listeners/
                                          _init.lua
                                          DescriptiveNameForListener.lua
```

> From this point onward, we're going to assume the ScriptExtender/Lua folder to be our root folder.
{.is-warning}

By default, SE only looks at `BootstrapServer.lua.` We need to make sure that our scripts are getting loaded. SE has a a function, `Ext.Require()`, which does this for us.

1. Add the following lines to `BootstrapServer.lua`:
```lua
Ext.Require("Globals.lua")
Ext.Require("Listeners/_init.lua")
```

2.  Add the following lines to `Listeners/_init.lua`, replacing `FILENAME` with the name of the other lua file in the folder. Be sure to add a line like this to `_init.lua` for **every** .lua file within the `Listeners` folder *except for `_init.lua`:
```lua
Ext.Require("Listeners/FILENAME.lua")
```

### Initializing Globals

There are a few values that are always going to remain the same, and that we'll want to access in multiple files. Instead of repeating them, we're going to create a **Global Variable**. These variables are values we can reference anywhere in our code.

1. Add the following to your `Globals.lua` file:
```lua
ModuleUUID = "your-mods-uuid-value-here"
PaladinTagId = "PALADIN_6d85ab2d-5c23-498c-a61e-98f05a00177a"
SubclassTagId = "SUBCLASS_TAGNAME_your-subclass-tag-uuid-value"
```

### Defining your Listener

> When you see `--` in any lua code, that means that anything on that line will be considered a comment, and won't be executed. It's great for notes.
{.is-warning}

Next, we need to watch for certain events to happen before our Oath Break/Redemption happens. 
1/ In your `Listeners/FILENAME` file, add the following:
```lua
-- Osiris Listener for a Flag being set - convention is RegisterListener(function name as a string, number of parameters, 
-- before or after, and an anonymous function containing the logic)
Ext.Osiris.RegisterListener("FlagSet", 3, "after", function (flag, _, dialogInstance)
  -- If the Flag set equals the flag for the Hag being given mercy, then...
  if flag == "HAG_Hag_State_HagGivenMercy_a3c0a36a-ccce-4f35-7b54-9ab22d6ac534" then
    -- Loop through the characters within the specific dialog instance
    for _, character in pairs(Osi.DB_DialogPlayers:Get(dialogInstance, _)) do
      -- If the character found is tagged as a Devotion Paladin and a Paladin...
      if IsTagged(character[1], SubclassTagId) and 
         IsTagged(character[1], PaladinTagId) then
        -- Call the Oath Framework API passing in our mod's UUID, the character ID, their subclass tag, and whether to Break or Redeem them.
        Mods.OF.Api.ModifyOath({
          modGuids = {ModuleUUID},
          CharacterId = character[1],
          SubclassTagId = SubclassTagId,
          EventType = "Break"})
      end
    end
  end
end)
```

This effectively watches for the flag indicating that the Hag from Act 1 has been granted mercy, checks to make sure that a player is involved in the event, and if they have the Paladin and Subclass tags, calls the Oath Framework to break the character's Oath.

## Handling Multiple Events
You have your Script-Extender setup working, but it's getting a bit hard to work with,and you want to handle multiple situations? Let's change things up a little bit on the SE side.

### Another look at File Structure
The above file structure is good, but we'll want to add a new section to our code, **Actions**. This section is going to hold functions that handle logic for specific events. This keeps our code cleaner, more understandable, and easier to maintain.

1. In your `ScriptExtender/Lua` folder, add a subfolder `Actions`, and create these two files: `_init.lua` and `MercyToHag.lua`. Your folder structure should now look like this:
```
Mods/MODNAME/ScriptExtender/
                            Config.json
                            OathFrameworkConfig.json
                            Lua/
                                BoostrapServer.lua
                                Globals.lua
                                Actions/
                                        _init.lua
                                        MercyToHag.lua
                                Listeners/
                                          _init.lua
                                          DescriptiveNameForListener.lua
```

2. Modify your `BootstrapServer.lua` file to look like this:
```lua
Ext.Require("Globals.lua")
Ext.Require("Actions/_init.lua")
Ext.Require("Listeners/_init.lua")
```

3. In your `Actions/_init.lua` file, add this:
```lua
-- We want Actions to be in its own category/table, so it's easier to reference things
Actions = {}

Ext.Require("Actions/MercyToHag.lua")
```

You'll notice we've added an `Actions` variable. We've defined this as a **Table** - think of it like a section of code that contains other things. We'll be putting our Action functions within this table, but more on that later.

### Adding to our Globals

To make things easier, we're going to create another table, this time in our Globals file. This table is going to contain a quick, referenceable Variable that contains the flags we want to look for.

1. Add the following to `Globals.lua`:
```lua
OF_Flags = {
  MercyToHag = "HAG_Hag_State_HagGivenMercy_a3c0a36a-ccce-4f35-7b54-9ab22d6ac534"
}
```

This Global Variable is a Table, like `Actions`. Within it is a **Key/Value Pair** - the Key is on the left side of the equals sign, while then Value is on the right. Our key, `MercyToHag` is identical to the filename of our Action - that's on purpose. You may also notice that the value is the same as that flag we were checking for in our Listener file.

### Reorganizing our Listener

Now we need to change how we're handling our Listener. We're going to remove the logic from our listener, and instead have it search through every flag we've defined in our new `OF_Flags` Global Variable. Whenever the flag matches, it'll execute the relevant Action function.

1. Rename your listener file to `Listeners/FlagSet.lua`.

2. Change the reference to the listener file in `Listeners/_init.lua` to match the new filename.

3. Modify `Listeners/FlagSet.lua` to look like this:
```lua
-- Osiris Listener for a Flag being set - convention is RegisterListener(function name as a string, number of parameters, 
-- before or after, and an anonymous function containing the logic)
Ext.Osiris.RegisterListener("FlagSet", 3, "after", function (flag, _, dialogInstance)
    -- Loop through all flags we want to support in our Flags global
    for flagKey, supportedFlag in pairs(OF_Flags) do
      	-- if the supported flag matches the flag our listener hears, call a function to handle the specific flag
    	if flag == supportedFlag then
      		Actions[flagKey](dialogInstance)
      	end
    end
end)
```

### Setting up our Actions

Now, whenever our `FlagSet` listener detects the MercyToHag flag being set, it will attempt to fire our Action Function. We previously got out `Actions/_init.lua` file set up, and created our `MercyToHag.lua` file, but we didn't actually create the action, so right now, it'll create an error. Let's fix that. We're going to replicate the logic from our old version of the listener, but we don't need to Register a new listener, or check if the flag matches anymore, because we're handling that within the new listener already.

1. In `Actions/MercyToHag.lua`, add this:
```lua
-- We've already checked if the flag matches, so we only need the dialog instance
function Actions.MercyToHag(dialogInstance)
-- Loop through the characters within the specific dialog instance
  for _, character in pairs(Osi.DB_DialogPlayers:Get(dialogInstance, _) do
    -- If the character found is tagged as a Devotion Paladin and a Paladin...
    if IsTagged(character[1], SubclassTagId) and 
       IsTagged(character[1], PaladinTagId) then
      -- Call the Oath Framework API passing in our mod's UUID, the character ID, their subclass tag, and whether to Break or Redeem them.
      Mods.OF.Api.ModifyOath({
        modGuids = {ModuleUUID},
        CharacterId = character[1],
        SubclassTagId = SubclassTagId,
        EventType = "Break"})
    end
  end
end
```

By prefixing our function's name with `Actions.`, we're creating it _within_ the Actions table, which is what allows our listener to call the Action. The name, as well, must match the Key of the value that we've added to our `OF_Flags` Global Table.

### Adding additional Oath Break Events

Now that we have this set-up, adding additional Oath Break Events is much simpler. You only need to do 2 things:

1. Add a new entry to `OF_Flags`.

2. Add a new `Actions/FILENAME.lua`, replacing `FILENAME` with the `OF_Flags` entry's Key, which will perform the Oath Break/Redeem event.

Be sure to add an entry to `Actions/_init.lua` for each new Action Function you create.
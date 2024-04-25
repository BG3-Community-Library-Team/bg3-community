---
title: Using Inspiration Framework
description: A guide on using Inspiration Framework to apply custom Inspiration Points
published: true
date: 2024-04-25T22:56:28.239Z
tags: se, script-extender, frameworks, inspiration, backgrounds
editor: markdown
dateCreated: 2024-04-25T22:54:22.149Z
---

# Using Inspiration Framework
Inspiration Points are notoriously difficult to set up for Custom Backgrounds - the code behind them for vanilla Backgrounds is hidden away in the story.div.osi, written entirely in Osiris code that we can't really directly edit at this time. Inspiration Framework allows you to leverage the game Databases in conjunction with Script Extenders Listeners to both register your custom background correctly, and mark goals as completed when certain conditions are met. 

Effectively, this makes it possible to for a mod author to easily register and complete custom background goals, whether they're for custom backgrounds or new goals for existing backgrounds. However, there's still a solid chunk of effort needed. This page will be a brief overview of how to utilize Inspiration Framework.

## Mod Set-Up
First thing's first, we need to set up our mod. Chances are, by the time you're looking Inspiration Framework, you have your mod set-up already, but just in case, these are the core files you'll need:

1. `Public/Backgrounds/Backgrounds.lsx`
2. `Public/Backgrounds/BackgroundGoals.lsx`
3. `Public/Tags/[TagId].lsf`

### Backgrounds.lsx
_Note: This is unnecessary if you're just adding goals to vanilla backgrounds_

Here is where you define custom background entries. They'll look something like this:
```xml
<node id="Background">
  <attribute id="Description" type="TranslatedString" handle="h913f8f46gbf83g430cgb3d1ge7c017689ae9" version="6"/>
  <attribute id="Description" type="TranslatedString" handle="h913f8f46gbf83g430cgb3d1ge7c017689ae9" version="6"/>
  <attribute id="DisplayName" type="TranslatedString" handle="h4fce3c63ge9a2g4bfeg9248gfb0c2ee004c1" version="1"/>
  <attribute id="Passives" type="LSString" value="AGTT_BS_Warwyrd"/>
  <attribute id="UUID" type="guid" value="4f816071-1bd3-4c0c-8f3e-6d21bb4f6307"/>
  <children>
    <node id="Tags">
      <attribute id="Object" type="guid" value="1ea45ccc-f072-4d0f-880e-896dbe56038b"/>
    </node>
  </children>
</node>
```

An important think to keep in mind is that Tag object - we'll need to create a custom Background Tag to get ourselves set up properly. For now, make sure you have a newly-generated UUID as the value for your tag. We'll get back to it later.

### BackgroundGoals.lsx
_Note: Always required_

We'll need to define our Background Goals with the UUID of the relevant background and experience reward. We'll also need localization for the description and title, an amount of inspiration points to grant, and a reward level, plus a UUID to identify the goal. For more examples, see `GustavDev/Backgrounds/BackgroundGoals.lsx`

```xml
<node id="BackgroundGoal">
  <attribute id="BackgroundUUID" type="guid" value="ecb6ee29-5805-474b-9eb7-1d5ee7b89eba"/>
  <attribute id="Description" type="TranslatedString" handle="hbec913fdg613dg4b11gabc2g2e8c4130f180" version="1"/>
  <attribute id="ExperienceReward" type="guid" value="90f636c0-2d85-46d8-9760-30b57c664f4b"/>
  <attribute id="InspirationPoints" type="uint32" value="1"/>
  <attribute id="RewardLevel" type="uint32" value="2"/>
  <attribute id="Title" type="TranslatedString" handle="h35f10ee2g177dg4cecga5e3g286ffb336223" version="1"/>
  <attribute id="UUID" type="guid" value="261cf8cb-a978-4560-b8f4-9db43a734509"/>
</node>
```

### Tags
_Note: This is unnecessary if you're just adding goals to vanilla backgrounds_

Finally, we need our background tags. This file will need to be named after its UUID (which we generated in Backgrounds.lsx for that Tag object). This tag is how the underlying Larian code will find the background and its goals, so it's imperative that each background has a unique tag,

```lsx
<node id="Tags">
  <attribute id="Description" type="LSString" value="" />
  <attribute id="DisplayDescription" type="TranslatedString" handle="he2abacb3gaefeg429agba51gc5960d48e096" version="1" />
  <attribute id="DisplayName" type="TranslatedString" handle="h78795127g018bg4dfag80c6g27bd2aec6f90" version="1" />
  <attribute id="Icon" type="FixedString" value="" />
  <attribute id="Name" type="FixedString" value="AGTT_BS_APPRENTICE" />
  <attribute id="UUID" type="guid" value="694f1ffb-bb01-46ba-a6f2-1a82e6bad030" />
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
	  <attribute id="Name" type="LSString" value="Background" />
	</node>
      </children>
    </node>
  </children>
</node>
```

## Configuration
Whether you're adding new backgrounds and goals, or new goals for existing backgrounds, you'll need to supply an `InspirationFrameworkConfig.json` file. This file is what allows Inspiration Framework to register custom backgrounds and custom goals into the game. A [Sample Config](https://github.com/BG3-Community-Library-Team/InspirationFramework/blob/main/InspirationFrameworkConfig.sample.json) is provided in the repo.

Your file will look something like this:
```json
{
  "FileVersion": 1,
  "Backgrounds": [
    {
      "Name": "Name of Background",
      "Id": "UUID of Background Entry",
      "Goals": [
        {
          "Name": "Identifier for your Background Goal - Convention: Act#_BackgroundName_ShortGoalDescriptor or GLO_BackgroundName_ShortGoalDescriptor",
          "Id": "UUID of BackgroundGoals Entry",
          "Global": "Optional. Defaults to Global if not supplied. Should be either Global or GlobalAvatar"
        }
      ]
    }
  ]
}
```
Example:
```json
{
  "FileVersion": 1,
  "Backgrounds": [
    {
      "Name": "AGTT_BS_Apprentice",
      "Id": "ecb6ee29-5805-474b-9eb7-1d5ee7b89eba",
      "Goals": [
        {
          "Name": "Act1_AGTTBS_Apprentice_DivinityUndone",
          "Id": "261cf8cb-a978-4560-b8f4-9db43a734509"
        }
      ]
    }
  ]
}
```

## How to Complete a Goal
Once your Custom background and/or goals have been registered, completing a goal is all that's left. 

You'll need to utilize Script Extender to create Osiris Listeners, watching for events that you will then provide logic to in order to determine if the Goal is completed or not. Once the conditions are met, make sure you have both the Goal's Name as well as the Character meeting the criteria's UUID. Pass those in to `Mods.IF.Api.CompleteGoal()` like so:

```lua
Mods.IF.Api.CompleteGoal({
  modGuid = "UUID of Mod",
  Goals = {
    GoalName = {
      GoalId = "UUID of Goal"
      CharacterId = "ID of Character"
    }
  }
})
```

Example:
```lua
{
  modGuid = "33d8dcef-c9e2-4e19-9a90-86f6e35d065a",
  Goals = {
    Act1_AGTT_BS_Apprentice_TestGoal = {
      GoalId = "fc8b0dcc-01fc-4d18-818e-457f37a2516b"
      CharacterId = "Elves_Female_High_Player_39cda0f1-b0e1-15c9-a896-3bd8f0abb6ae",
    }
  }
}
```

An example of this in practice might look like this:

```lua
ModuleUUID = "2a4c5620-f219-4bbd-a157-04091020ea11"
GoalIds = {
  GLO_Criminal_EscapePrison = "5a217ebc-5ba2-4199-9a63-1d1edb78b923"
}

-- Registering Listener for a Prison Escape - all we need is the character variable here, so null out everything else
Ext.Osiris.RegisterListener("PROC_CRIME_Prison_Escaped", 7, "after", function (character, _, _, _, _, _, _)
  -- returns true if our character is in DB_Players
  if not not next(Osi.DB_Players:Get(character)) then
    Mods.IF.Api.CompleteGoal({
      modGuid = ModuleUUID,
      Goals = {
        GLO_Criminal_EscapePrison = {
          GoalId = GoalIds.GLO_Criminal_EscapePrison,
          CharacterId = character
        }
      }
    })
  end
end)
```
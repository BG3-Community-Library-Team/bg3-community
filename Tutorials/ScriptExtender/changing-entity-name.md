---
title: Changing an entity's name
description: A simple guide to update an entity's name with Script Extender.
published: false
date: 2024-08-04T19:33:00.471Z
tags: tutorial
editor: markdown
dateCreated: 2024-08-04T19:32:05.725Z
---

Handling Display Names
==============================================

Introduction
------------

In this tutorial, we'll explore how to manage entity display names in Larian's game using `DisplayName.NameKey`. We'll discuss how to extract the display name handle, why using `DisplayName.NameKey` is superior to `Osi.SetStoryDisplayName`, and demonstrate functions to add and remove prefixes to display names dynamically.

Extracting `DisplayName.NameKey`
--------------------------------

To manipulate an entity's display name, we need to extract the handle from `DisplayName.NameKey`. Here’s how you can achieve this:

1.  **Retrieve the Entity Object:**
    
    ```lua
    
    local entityObject = Ext.Entity.Get(entity)
    ```
    
2.  **Extract the Handle:**
    
    ```lua
    
    local handle = entityObject.DisplayName.NameKey.Handle.Handle
    ```
    
3.  **Get the Display Name:**
    
    ```lua
    
    local displayName = Ext.Loca.GetTranslatedString(handle)
    ```
    

Why Use `DisplayName.NameKey`?
------------------------------

Using `DisplayName.NameKey` is better than `SetStoryDisplayName` because it provides a persistent and consistent way to handle display names. `SetStoryDisplayName` creates temporary mappings that are lost upon game reload, leading to issues where names may revert to "Not Found". `DisplayName.NameKey` ensures that the changes remain consistent across game sessions.

Adding Prefix to Display Name
-----------------------------

To add a prefix to an entity's display name, we can use the following function. It checks if the prefix already exists to avoid redundant updates:

```lua

local 
function UpdateEntityDisplayName
(entity, prefix)

    local entityObject = Ext.Entity.Get(entity)
    local handle = entityObject.DisplayName.NameKey.Handle.Handle  -- Extracting the handle
    if handle then
        local displayName = Ext.Loca.GetTranslatedString(handle)
        if not displayName:find(prefix) then
            local updatedName = prefix .. " " .. displayName
            Ext.Loca.UpdateTranslatedString(handle, updatedName)
        end
    end
end
```

### Usage Example:

```lua
UpdateEntityDisplayName(someEntity, "Stoneskin")
```

This function ensures that the display name is updated only if the prefix is not already present.

Removing Prefix from Display Name
---------------------------------

To remove a prefix from an entity's display name, we can use the following function:

```lua

local 
function RemovePrefixFromDisplayName
(entity, prefix)

    local entityObject = Ext.Entity.Get(entity)
    local handle = entityObject.DisplayName.NameKey.Handle.Handle  -- Extracting the handle
    if handle then
        local displayName = Ext.Loca.GetTranslatedString(handle)
        local updatedName = displayName:gsub("^" .. prefix .. " ", "")
        Ext.Loca.UpdateTranslatedString(handle, updatedName)
    end
end
```

### Usage Example:

```lua
RemovePrefixFromDisplayName(someEntity, "Stoneskin")
```

This function removes the specified prefix if it exists in the display name.

Practical Application
---------------------

### Updating Display Name on Turn Start

To update the display name based on active status during the entity's turn start:

```lua

local statusToPrefixMap = {
    STONESKIN = "Stoneskin",
    GOLDEN = "Golden",
    -- Add other statuses and their corresponding prefixes here
}

Ext.Osiris.RegisterListener("TurnStarted", 1, "after", 
function
(object)

    -- Check and update display name based on status
    for status, prefix in pairs(statusToPrefixMap) do
        if HasActiveStatus(object, status) == 1 then
            UpdateEntityDisplayName(object, prefix)
        end
    end

    -- Add your existing TurnStarted logic here
end)
```

### Removing Prefix on Death

To remove the prefix when the entity dies:

```lua
Ext.Osiris.RegisterListener("Dying", 1, "after", 
function
(entity)

    -- Check and remove prefix based on status
    for status, prefix in pairs(statusToPrefixMap) do
        if HasActiveStatus(entity, status) == 1 then
            RemovePrefixFromDisplayName(entity, prefix)
        end
    end

    -- Add your existing Dying logic here
end)
```

Conclusion
----------

Using `DisplayName.NameKey` for managing entity display names provides a robust solution for maintaining consistency across game sessions. The functions for adding and removing prefixes ensure that display names are updated dynamically based on the entity's status. This approach prevents issues related to temporary mappings and provides a better overall experience in managing display names.
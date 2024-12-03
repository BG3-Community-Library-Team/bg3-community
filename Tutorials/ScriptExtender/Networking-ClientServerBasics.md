---
title: Networking, Client-Server Basics
description: Quick rundown of core networking concepts and client/server differences
published: false
date: 2024-12-03T23:31:17.267Z
tags: networking, client, server
editor: markdown
dateCreated: 2024-12-03T21:16:11.259Z
---

# Necessary Basics
Before jumping into networking concepts, it's important to point out a few Lua and game basics so your understanding has some footing to build upon. BG3 like many games, has a one-to-many server->client structure, where even singleplayer has a server-client relationship. When the game is booted up, the game is a client and you'll notice many things will not work in the SE console, with the error:
> Cannot queue server commands in game state Uninitialized
> S >>
{.is-danger}

By default, the SE console will launch into server context (shown as S >>), and you can switch into client context by simply typing `client` (shown as C >>), and vice-versa with `server` to switch back into server context. **These are fully separate contexts**, with their own separate scopes, provided and managed by SE. To reiterate, this means defining a variable in one context would not define that variable in the other context; they are completely separate, a server context and client context. Because they are separate, SE provides two bootstrap locations you can define in your mod to tap into each context and build out from there:
- `<YourModName>/Mods/<YourModName>/ScriptExtender/Lua/BootstrapClient.lua`
- `<YourModName>/Mods/<YourModName>/ScriptExtender/Lua/BootstrapServer.lua`

With that said, when you start a game or load into a save, the game spins up a server with you as a host-client.
## Why?
Yes. But also, why is there a whole complicated server<->client structure? The main benefit of this technique is that it's built with multiplayer in mind. The server acts as a sole source of truth, for the current state of the game, and the clients are simply in charge of replicating what this state looks like, and providing each client with ways to request changes to the server's game state. Some examples:
1. Moving your character
\- Your client uses client-only features, like what you clicked on, to send a request to the server to move your currently selected character to this newly clicked position.
2. Rearranging your inventory
\- Your client has received the arrangement of items in a character's inventory, and displays it in client-sided UI.
\- When you click on an item or move it, the request is sent to the server, to move the item to the new position.
\- The server moves the item, and relays the change to all clients, which is why in multiplayer you can see when someone else is rearranging inventories.
3. Leveling up
\- The game client simulates leveling up with that character creation scene, but this interaction is very layered
\- The initial "I clicked on the Level Up" button sends a request to the server to check if this is allowed, and if so, the server tells the client to begin the level up simulation
\- If allowed, the level up simulation pulls up a character creation scene with a dummy character and a TLPreviewDummy component (cutscene character stuff), where the dummy is made to look exactly like you, and any choices you make are applied to this dummy first.
\- If you abort the level up (and mirror works the same way) simulation, the server is sent an abort message, while the dummy character disappears and your real character remains, of course, unchanged.
\- If you finalize the level up simulation, those changes are sent to the server while the client dummy disappears, the server makes those changes to your real character, and then these changes are relayed to all clients for replication.

There are a LOT of back and forth interactions that happen between the server and client(s), and many of them are near-instantaneous, but it's important to keep in mind **how** and **why** they are necessary. The server controls the state of the game, and clients are a way of viewing this game state and more importantly, giving separation between clients. When you move your cursor across the screen, it's on your client; ie- another player's cursor DOES NOT move on their screen in response. Every client has its own separate version of what's happening, and the magic is that the server is keeping these clients in sync, by *replicating changes*.

# NetMessages
The meat of all client-server interaction is through SE-defined NetMessages, which are ways of passing information from client context to server context, locally or across the internet.
## Receiving messages
```lua
--- @class LuaEventBase
--- @field ActionPrevented boolean
--- @field CanPreventAction boolean
--- @field Name FixedString
--- @field Stopped boolean
--- @field PreventAction fun(self:LuaEventBase)
--- @field StopPropagation fun(self:LuaEventBase)

--- @class LuaNetMessageEvent:LuaEventBase
--- @field Channel string
--- @field Payload string
--- @field UserID UserId

--- @param e LuaNetMessageEvent
Ext.Events.NetMessage:Subscribe(function (e)
    -- e is a LuaNetMessageEvent from SE, where you can check if the e.Channel is something you're listening for
    if e.Channel == "ChannelImListeningFor" then
        -- this message is for me, and I can check e.Payload and e.UserID
    end
end)
```
Or more simply, if you don't need the extra complication, SE has slightly shorter shorthand:
```lua
Ext.RegisterNetListener("specificChannelID", function(channel, payload, user)
    -- This is a NetMessage with "specificChannelID", handle the payload from user
end)
```

### Peers vs Users
This is a bit annoying, but when listening on the server for NetMessages from clients, the id you receive is actually a peerID, and not a userID. When it's important to know the correct userID of the client who sent the message, you must convert using some bitwise operations, so it's good to make some Helper functions if you haven't already:
```lua
-- Define some global helpers, if none exist already
if Helpers == nil then Helpers = {} end
if Helpers.Format == nil then Helpers.Format = {} end

--- When receiving messages from a client (on the server), NetMessage user is actually peerid, convert using this
--- @param p integer peerid
--- @return integer userid
function Helpers.Format.PeerToUserID(p)
    -- all this for userid+1 usually smh
    return (p & 0xffff0000) | 0x0001
end

--- Probably unreliable/unnecessary
--- @param u integer userid
--- @return integer peerid
function Helpers.Format.UserToPeerID(u)
    return (u & 0xffff0000)
end
```
### Processing payloads and users
When listening for messages from a specific NetMessage channel, you may or may not receive payloads with the message, which are stringified json data objects.

```lua
-- In server context
--- @param _ string        # ignored channel string, since it's already specified in the listener
--- @param payload string  # stringified json object
--- @param peer int32      # peerID that will need to be converted to a userid
Ext.RegisterNetListener("AChannelImListeningFor", function(_, payload, peer))
    local u = Helpers.Format.PeerToUserID(peer)
    local p = Ext.Json.Parse(payload)
    local someData = p.SomeDataISent
    
    local character = Osi.GetCurrentCharacter(u) --[[@as Character]]
    local name = character and character.DisplayName.Get and character.DisplayName:Get()
        or character and Ext.Loca.GetTranslatedString(character.DisplayName.NameKey.Handle.Handle)
        or "Unknown"
    
    print(string.format("Received %s from user: %d (%s)", someData, u, name))
end)
```
Almost any arbitrary data can be sent over NetMessages, like `SomeDataISent` in the method above, as long as it can be stringified by `Ext.Json.Stringify()` and parsed by `Ext.Json.Parse()`.

## Sending messages
You can subscribe to listen in both client/server contexts, but it's important to note that clients **cannot** message each other directly. Your options are:
**Ext.Server** in server context
- `Ext.Server.BroadcastMessage()`
- `Ext.Server.PostMessageToClient()`
- `Ext.Server.PostMessageToUser()`

**Ext.Client** in client context
- `Ext.Client.PostMessageToServer()`





# Client
asdf

# Server
asdf

# Final thoughts
what's that smell, some bullshit?
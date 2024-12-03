---
title: Networking, Client-Server Basics
description: Quick rundown of core networking concepts and client/server differences
published: false
date: 2024-12-03T21:16:11.259Z
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
- \<YourModName>/Mods/\<YourModName>/ScriptExtender/Lua/BootstrapClient.lua
- \<YourModName>/Mods/\<YourModName>/ScriptExtender/Lua/BootstrapServer.lua

With that said, when you start a game or load into a save, the game spins up a server with you as a host-client.


# Some other shit

# Client
asdf

# Server
asdf

# Final thoughts
what's that smell, some bullshit?
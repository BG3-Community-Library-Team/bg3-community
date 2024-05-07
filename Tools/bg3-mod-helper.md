---
title: VSCod(e/ium) Extension
description: an extension for VSCode and VSCodium by @khbsd and @ghostboats that has lots of helpful features for modders.
published: true
date: 2024-05-07T19:36:37.271Z
tags: vscode, vscodium, bg3-mod-helper, tool, tools, ghostboats, khbsd
editor: markdown
dateCreated: 2024-04-25T01:43:35.054Z
---

# BG3 Mod Helper - A VSCod(e/ium) Extention

This vscode extension is designed to help mod authors speed up their mod creation workflows. The extension has multiple useful utilities that include but are not limited to:
- Mod Packing
- UUID/Handle generation
- UUID Mapping
- LSX/XML/LOCA/ETC File Conversions
- Generate mod templates
- And then some

While the extension is still recieving regular updates, it's at a stable point where it can be very useful to mod authors and save them alot of time. It is built off the philosopy of being able to mod without having to tab out as often while requiring as little clicks as possible to get the job done. It has saved us alot of time and I hope it can do the same for you! The goal of this section of the the wiki is two fold: Provide documentation for users of the extension and provide documentation for developers who may wish to contribute or fork their own version.

# Requirements
- [Visual Studio Code](https://code.visualstudio.com/)
- [LSLib](https://github.com/Norbyte/lslib/releases)
- Python
The following are required for image/icon related actions but the extension will prompt you to install
- ImageMagik

> Previous versions of the extension required direct use of divine.exe. This has since been replaced and you will simply need [LSLib](https://github.com/Norbyte/lslib/releases)
<!-- {blockquote:.is-info} -->
<p>ghostboats and I (khbsd) made this extension with love. On this page we'll go into its features, explanations of the machinations behind functions, and quirks that we've been unable to iron out.</p>

# Goals


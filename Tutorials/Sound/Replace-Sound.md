---
title: Replacing in-game Sound
description: This is a guide for how to replace sound files (voices, sound effects, music) in game
published: true
date: 2024-05-11T22:26:34.997Z
tags: audio, sound, music, voice
editor: markdown
dateCreated: 2024-05-11T22:26:34.997Z
---

# Introduction
This guide explains how to replace sound files in BG3.
> It is worth noting that there is currently (as of May 11th 2024) not a way add new soundbanks or sound events, we can only replace existing soundfiles that are tied to in-game events.
{.is-info}


# Requirements
- An audio editing program, such as Adobe Audition (paid) or Audacity (free), to trim and export audio to `.wav`
- [Wwise](https://www.audiokinetic.com/download/) - To convert `.wav` to `.wem`
- Having already followed [this](/Tutorials/Sound/Extract-Audio) guide to extract sound files from the game, which also contains another program you'll need.

# Identification
In order to replace a sound, you have to first identify which sound it is. 
This can happen a variety of ways.

Assuming you've followed the guide to extract sound files, you should have many directories with `.wav` files in them.
You can infer a little bit from the directory name, like `MUSIC` should have music files, `VOCALS` has the voice lines, etc.

You can use [Norbyte's BG3 Search Engine](https://bg3.norbyte.dev/search) to find sound events. 
For example, if I wanted to find events from the `SCRIPTED_EVENTS.bnk`, I would search "**SCRIPTED_EVENTS type:sound**"
![scripted-events-search.png](/tutorials/sound/scripted-events-search.png)

Having just the event doesn't help, you need to have the actual `.wem` file

For the purpose of this guide, we're going to replace `379124917.wem` which is part of `SCRIPTED_EVENTS.bnk`. 
It is the sound with the spoken words "who are you?" that plays over top of the intro theme, during the character creation.


# Extract Properties
Open a terminal and navigate to the directory where vgmstream is located.
You'll also need to know the location of the `.wem`. (You could just copy it to the same location if you wanted.)

From the command prompt, enter this command: 
> `vgmstream-cli.exe -m path\to\file\filename.wem`

Example: `vgmstream-cli.exe -m E:\GitHub\BG3\bg3-modders-multitool\UnpackedData\SharedSounds\Public\Shared\Assets\Sound\379124917.wem `

> If you can't figure out how to (or don't want to) nativate through cli, you can also enter the full path of `vgmstream-cli.exe` for the first part of the command instead.
{.is-info}

This prints the metadata for the file, which includes the sample rate, number of channels, encoding format, etc.
![vgmstream-cli-metadata.png](/tutorials/sound/vgmstream-cli-metadata.png)

Save this somewhere, we'll need to match this format for the `.wem` we add back to the game.

# Tips for editing your new sound
The sound you replace should be roughly the same length.
It technically doesn't have to be, but you should aim to match it if possible.

If the original clip is 18 seconds and you insert a 2 minute clip, it will only play the first 18 seconds.
So rather than have the wasted time, you should edit your clip to be the same 18 seconds. 
That way you can control what exactly happens in those 18 seconds.

Trim extra time off of long tracks or add silence/noise to extend tracks that are too short.

If you're replacing spoken words, try to match the tempo of the orignal so that the mouth matches the new voice.

You may have to adjust the volume of your clip, if it comes across too quiet or too loud in game. The sound system in BG3 already applies attenuation on its own, so it's usually better to normalize the volume up to about -6db

Once you've finished editing it, export it to a `.wav` file. 
Most of the export settings won't matter since it will be converted to `.wem` later, but try to match the sample rate of the original.

# Replacing the Sound
Open Wwise and start a new project. It doesn't matter what you name it
![wwise-project-create.png](/tutorials/sound/wwise-project-create.png)

From the **Actor-Mixer Hierarchy** folder, right click on **Default Work Unit** and select `Import Audio Files...`
![wwise-import-audio.png](/tutorials/sound/wwise-import-audio.png)

You can leave these settings at default, just select **Add Files** and select your `.wav` file, then select **Import**.
![wwise-import-audio-2.png](/tutorials/sound/wwise-import-audio-2.png)

You should now have the file along the left side under **Actor-Mixer Hierarchy/Default Work Unit**.
![wwise-new-child-audio-file.png](/tutorials/sound/wwise-new-child-audio-file.png)

Next, double click on the file from the left side and it should open up a mixing window with a lot of options and tabs. 
All we need is the *conversion* tab.

From the conversion tab, change **Mode** to "Define Custom" and then select the button that opens the conversion settings (looks like a window with an arrow).
![wwise-conversion-1.png](/tutorials/sound/wwise-conversion-1.png)

Change the settings to match the input you recorded earlier. This includes the channels, sample rate, and make sure the format matches. Then select **Convert**.
![wwise-conversion-2.png](/tutorials/sound/wwise-conversion-2.png)
> If you end up with no sound in game for the event, the format is probably wrong.
{.is-info}

Close the conversion window.
Right click on the file from the left and select Open Containing Folder then the file.
![wwise-conversion-3.png](/tutorials/sound/wwise-conversion-3.png)

This takes you to the directory with your `.wav`.
We didn't technically need to go this far but it was the fastest way to find your project file.
Back out of this directory until you are at your main project directory. 
You should see `.cache` and a bunch of other directories, open `.cache`.
Then continue browsing until you get to your `.wem` file (should be -> Windows -> SFX)
The last thing to note here is that Wwise added some junk to your filename, make sure to rename it. It needs to match 1-to-1 with the source `.wem` file.
![converted-wem-location.png](/tutorials/sound/converted-wem-location.png)

So now that it has the right name, copy it, and we're going to place it in a specific location.
`SteamLibrary\steamapps\common\Baldurs Gate 3\Data\Public\Shared\Assets\Sound\379124917.wem"`

> I believe voice lines go in `Data\Mods\Gustav\Localization\English\Soundbanks\` but I haven't personally tested it. It's different for voice lines than it is for Sounds/Music.
{.is-info}


Afaik, there isn't a way to bundle them up as a .pak yet.

# Conclusion
You should be able to replace music, sound effects, and voice clips now. 
Have fun bringing chaos to Faerûn.
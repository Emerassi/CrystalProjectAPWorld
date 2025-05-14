# Crystal Project AP World Setup Guide

## What You Need

- Crystal Project Installer from the
  [Crystal Project AP World Releases Page](https://github.com/Emerassi/CrystalProjectAPWorld/releases)

- .Net 8.0 Desktop Runtime x64 or .Net 8.0 Runtime x64 (not the SDK!) is required to run the Crystal Project Archipelago Mod Installer: 
https://dotnet.microsoft.com/en-us/download/dotnet/8.0

## Recommended Installation Instructions

In your Steam library, right-click Crystal Project in the list and select "Properties...". Go to the Betas section, open the Beta Participation dropdown, and select the archipelago branch (version 1.6.5). 

Install .Net 8.0 x64 if you don't already have it.

Go to [Crystal Project AP World Releases Page](https://github.com/Emerassi/CrystalProjectAPWorld/releases).
Download the installer file, extract it, and run the executable. When prompted, choose your Crystal Project installation location.

## Switching Between Different Versions of Archipelago

FYI: Your save files for the unmodified game will not be visible inside the Arhcipelago version of the game, and vice versa.
 The unmodified game and the AP version of the game store saves in different folders to prevent you from loading incompatible saves and getting errors.

If you want to switch back to unmodded Crystal Project:
 1. In your Steam library, right-click Crystal Project in the list and select "Properties...".
 1. In the Betas menu, select the branch that matches the save file you want to switch to (likely the release branch, a.k.a. None in the Beta Participation dropdown).

When you want to back to the Archipelago version of Crystal Project:
 1. Change back to the archipelago branch in Steam's Beta Participation menu
 1. Run the installer for the version you want.

If you want to switch to a different version of Archipelago Crystal Project:
 1. In your Steam library, right-click Crystal Project in the list and select "Properties...".
 1. Go to the Installed Files section and select "Verify integrity of game files"
 1. Run the installer for the version of Crystal Project Archipelago you want to switch to.

## Configuring your YAML file

### What is a YAML file and why do I need one?

A YAML file lets you configure options for your randomizer game.
See [Archipelago Multiworld Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup/en#generating-a-game) for a more in-depth explanation!

### Where do I get a YAML file?

A YAML file is included on the [Crystal Project AP World Releases Page](https://github.com/Emerassi/CrystalProjectAPWorld/releases)

### Connect to the MultiServer

Start a new game in Crystal Project. Don't touch the in-game randomizer settings (some of them may still work, but some of them will break things lol).
Once loaded into the world, open the menu and select Archipelago from the sidebar.
Fill out the hostname and port (archipelago.gg: ######), slot name, and password (if applicable).  You can use your keyboard to type here FYI!
 Then hit the Save button. You should now be connected! 
(Note: settings like starting job randomization will only apply after you've connected to the multiworld for the first time.)

### Play the game

After you've successfully connected once, your save file will automatically reconnect to the multiworld the next time you open the game.
(Remember to refresh the multiworld room page if no one has connected in a while.)
Set forth on adventure!

# Watchlist plug-in for [XVM](http://www.modxvm.com/en/)

Add personalize icons and text for players and clans using XVM.

## USAGE:
```
{{py:watchlist.icon('{{name}}','{{clan}}')}}

{{py:watchlist.note('{{name}}','{{clan}}')}}
```

Use it in any *.xc files in the World_of_Tanks/res_mods/configs/xvm/:

Player icons have priority over clan icons

Use {{py:watchlist.icon('{{name}}','{{clan}}')}} to show ICON

Use {{py:watchlist.note('{{name}}','{{clan}}')}} to show Custom Text field

![screenshot](https://raw.githubusercontent.com/dataserver/wot-xvm-watchlist/master/screenshot-1.png)


## watchlist.txt

The list of players/clans and image icon used is saved in a text file 'watchlist.txt', saved in the directory:

```
World_of_Tanks/res_mods/configs/watchlist.txt
```

Formatting (fields separed by comma, 1 entry per line)

```
Name, player_or_clan, icon.png, custom text field
```

examples:
```
PlayerName, player, imagefile.png, some text here
CABRA, clan, enemy.png, BR clan
bulba, clan, ally.png, some xyz clan
quickfingers, player, twitch.png, EU streamer
skill4ltu, player, twitch.png, EU streamer
sirfoch, player, twitch.png, EU streamer
circonflexes, player, twitch.png, EU streamer
```

Images are saved into:
```
World_of_Tanks/res_mods/mods/shared_resources/xvm/res/
```

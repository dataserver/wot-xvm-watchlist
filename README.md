# Watchlist plug-in for [XVM](http://www.modxvm.com/en/)

Add personalize icons for players and clans using XVM.

## USAGE:
```
{{py:watchlist.verify('{{name}}','{{clan}}')}}
```

Use it in any *.xc files in the World_of_Tanks/res_mods/configs/xvm/:

Player icons have priority over clan icons

## watchlist.txt

The list of players/clans and image icon used is saved in a text file 'watchlist.txt', saved in the directory:

```
World_of_Tanks/res_mods/configs/watchlist.txt
```

Formatting (tree fields separed by comma, 1 entry per line)

```
Name, player_or_clan, icon.png
```

examples:
```
Quickfingers, player, twtich.png
skill4ltu, player, twitch.png
sirfoch, player, twitch.png
circonflexes, player, twitch.png
Bulba, clan, ally.png
CABRA, clan, enemy.png
```

Images are saved into:
```
World_of_Tanks/res_mods/mods/shared_resources/xvm/res/
```

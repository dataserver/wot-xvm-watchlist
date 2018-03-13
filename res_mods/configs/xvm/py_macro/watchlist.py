import traceback
import re
'''
Custom Icon for players/clans
2018-03-13
required:
- XVM

USAGE:

Use in *.xc files in the World_of_Tanks/res_mods/configs/xvm/:

2 custom tags added:

{{py:watchlist.icon('{{name}}','{{clan}}')}}
- show icon image (player icon has has priority over clan icons)

{{py:watchlist.note('{{name}}','{{clan}}')}}
- show field "note" from watchlist.txt


World_of_Tanks/res_mods/configs/watchlist.txt

watchlist.txt formatting (tree fields separed by comma, 1 entry per line)
playerNameOrClanName, playerOrClan, image.png, noteText

ex:
Quickfingers, player, twitch.png, EU streamer
CABRA, clan, enemy.png, brazillian clan


check screenshot-1.png
   In this screenshot the left side show the normal view, and the right is when you click ALT and 
the watchlist.note will display the "custom text" field.

'''

watchlistfile = './res_mods/configs/watchlist.txt'
# watchlistfile = './../../watchlist.txt'
lst = []
lst_orig = []
with open(watchlistfile, 'r') as fh:
    for line in fh:
        formatedline = re.sub(r'\s+', '', line)
        formatedline = formatedline.lower()
        lst.append( formatedline.split(',') )
        lst_orig.append( line.split(',') )

def find_player(key):
    key = key.lower()
    found = False
    for index, sublist in enumerate(lst):
        if (sublist[0] == key) and (sublist[1] == 'player'):
            found = index
            break
    if found:
        img = lst[found][2]
        return '<img src="xvm://res/'+ img +'" width="12" height="12">'
    else:
        return None

def find_clan(key):
    key = key.strip('[]')
    key = key.lower()
    found = False
    for index, sublist in enumerate(lst):
        if (sublist[0] == key) and (sublist[1] == 'clan'):
            found = index
            break
    if found:
        img = lst[found][2]
        return '<img src="xvm://res/'+ img +'" width="12" height="12">'
    else:
        return None

def find_note_player(key):
    key = key.lower()
    found = False
    for index, sublist in enumerate(lst):
        if (sublist[0] == key) and (sublist[1] == 'player'):
            found = index
            break
    if found:
        return lst_orig[found][3]
    else:
        return None

def find_note_clan(key):
    key = key.strip('[]')
    key = key.lower()
    found = False
    for index, sublist in enumerate(lst):
        if (sublist[0] == key) and (sublist[1] == 'clan'):
            found = index
            break
    if found:
        return lst_orig[found][3]
    else:
        return None

@xvm.export('watchlist.icon', deterministic=False)
def watchlist_icon(username, clanname=''):
    user_found = find_player( username )
    if not (user_found is None):
        return user_found
    clan_found = find_clan( clanname )
    if not (clan_found is None):
        return clan_found
    return ''

@xvm.export('watchlist.note', deterministic=False)
def watchlist_note(username, clanname=''):
    user_found = find_note_player( username )
    if not (user_found is None):
        return user_found
    clan_found = find_note_clan( clanname )
    if not (clan_found is None):
        return clan_found
    return ''

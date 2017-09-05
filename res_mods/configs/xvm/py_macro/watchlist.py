import traceback
import re
'''
Custom Icon for players/clans
2017-09-04
required:
- XVM

USAGE:

Use in *.xc files in the World_of_Tanks/res_mods/configs/xvm/:

{{py:watchlist.verify('{{name}}','{{clan}}')}}

Player specific icon has priority over clan icons


World_of_Tanks/res_mods/configs/watchlist.txt

watchlist.txt formatting (tree fields separed by comma, 1 entry per line)
playerNameOrClanName, playerOrClan, image.png

ex:
Quickfingers, player, twitch.png
CABRA, clan, enemy.png

'''

watchlistfile = './res_mods/configs/watchlist.txt'
# watchlistfile = './../../watchlist.txt'
with open(watchlistfile, 'r') as fh:
    lst = []
    for line in fh:
        line = re.sub(r'\s+', '', line)
        line = line.lower()
        lst.append( line.split(',') )

def find_player(key):
    key = key.lower()
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

@xvm.export('watchlist.verify', deterministic=False)
def watchlist_verify(username, clanname=''):
    user_found = find_player( username )
    if not (user_found is None):
        return user_found
    clan_found = find_clan( clanname )
    if not (clan_found is None):
        return clan_found
    return ''


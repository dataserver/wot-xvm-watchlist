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

watchlist.txt formatting(tree fields separed by comma, 1 entry per line)
playerNameOrClanName, playerOrClan, image.png, noteText

ex:
Quickfingers, player, twitch.png, EU streamer
CABRA, clan, enemy.png, brazillian clan


check screenshot-1.png
   In this screenshot the left side show the normal view, and the right 
is when you click ALT and the watchlist.note will display the "custom 
text" field.

'''

watchlistfile = './res_mods/configs/watchlist.txt'

formatted_list = []
orig_list = []
with open(watchlistfile, 'r') as fh:
    for line in fh:
        formatted_line = re.sub(r'\s+', '', line)
        formatted_line = formatted_line.lower()
        formatted_list.append(formatted_line.split(','))
        orig_list.append(line.split(','))

def get_icon_player(player_name):
    player_name = player_name.lower()
    row_found = False
    for row_number, row in enumerate(formatted_list):
        if (row[0] == player_name) and (row[1] == 'player'):
            row_found = row_number
            break
    if row_found:
        img = formatted_list[row_found][2]
        return ('<img src="xvm://res/'
               + img 
               + '" width="12" height="12">')
    else:
        return None

def get_icon_clan(clan_name):
    clan_name = clan_name.strip('[]')
    clan_name = clan_name.lower()
    row_found = False
    for row_number, row in enumerate(formatted_list):
        if (row[0] == clan_name) and (row[1] == 'clan'):
            row_found = row_number
            break
    if row_found:
        img = formatted_list[row_found][2]
        return ('<img src="xvm://res/'
               + img 
               + '" width="12" height="12">')
    else:
        return None

def get_note_player(player_name):
    player_name = player_name.lower()
    row_found = False
    for row_number, row in enumerate(formatted_list):
        if (row[0] == player_name) and (row[1] == 'player'):
            row_found = row_number
            break
    if row_found:
        return orig_list[row_found][3]
    else:
        return None

def get_note_clan(clan_name):
    clan_name = clan_name.strip('[]')
    clan_name = clan_name.lower()
    row_found = False
    for row_number, row in enumerate(formatted_list):
        if (row[0] == clan_name) and (row[1] == 'clan'):
            row_found = row_number
            break
    if row_found:
        return orig_list[row_found][3]
    else:
        return None

@xvm.export('watchlist.icon', deterministic=False)
def watchlist_icon(username, clan_name=''):
    icon = get_icon_player(username)
    if not (icon is None):
        return icon
    icon = get_icon_clan(clan_name)
    if not (icon is None):
        return icon
    return ''

@xvm.export('watchlist.note', deterministic=False)
def watchlist_note(username, clan_name=''):
    note = get_note_player(username)
    if not (note is None):
        return note
    note = get_note_clan(clan_name)
    if not (note is None):
        return note
    return ''

#python
from framework import gui
from framework import mappings

#Get Chat- [player#] (message)
def chat_get(data_bytes):
    player = data_bytes[1]
    playerName = mappings.player_mapping.get(player, 'Unknown')
    message = data_bytes[2:].decode('ascii', 'ignore')
    builtMessage = playerName + ": " + message
    gui.App.instance.add_to_chat(builtMessage)

#109- Name Picked- [?] [player#] (name)
def pick_name(data_bytes):
    player = data_bytes[2]
    name = data_bytes[3:].decode('ascii', 'ignore')
    mappings.player_mapping[player] = name
    gui.App.instance.gui_playerList[player]['name'].set(name)

#Received a PM- [?] [player#] [?] (message)
def recieved_pm(data_bytes):
    print ("")
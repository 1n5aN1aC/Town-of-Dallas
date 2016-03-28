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

#Received a PM- [?] [player#] [?] (message)
def recieved_pm(data_bytes):
    print ("")
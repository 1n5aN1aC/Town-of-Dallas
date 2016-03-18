#!python

#  3- Send Chat- (message)
def chat_send(data_bytes):
    print ("Sent Chat Message:")
    print ("   Message:", data_bytes.decode('ascii', 'ignore') )

#  6- Get Chat- [player#] (message)
def chat_get(data_bytes):
    print ("Got Chat Message:")
    print ("   Player#:", data_bytes[1] )
    print ("   Message:", data_bytes[2:].decode('ascii', 'ignore') )

#  8- Send PM- [player#] (message)
def send_pm(data_bytes):
    print ("Sent a PM:")
    print ("   Player#:", data_bytes[1] )
    print ("   Message:", data_bytes[2:].decode('ascii', 'ignore') )

# 10- Client vote to lynch- [player#]
def you_vote_lynch(data_bytes):
    print ("Client vote to lynch:")
    print ("   Player#:", data_bytes[1] )

# 11- Ability Use- [player#]
def use_normal_ability(data_bytes):
    print ("Player Used Ability:")
    if data_bytes[1] is not 30:
        print ("    Target:", data_bytes[1] )
    else:
        print ("    Target Canceled")

# 17- Set Last Will- (message)
def set_lastwill(data_bytes):
    print ("Update Last Will:")
    print ("    message:", data_bytes[1:].decode('ascii', 'ignore') )

# 18- Set Death Note- (message)
def set_deathnote(data_bytes):
    print ("Update Death Note:")
    print ("    message:", data_bytes[1:].decode('ascii', 'ignore') )

# 35- Lobby Get Chat- (player name) [*] (message)
def lobby_get_chat(data_bytes):
    print ("Lobby got chat:")
    new_bytes = data_bytes[1:].decode('ascii', 'ignore').split('*')
    print ("    Player:", new_bytes[0] )
    if new_bytes[1]:
        print ("    Message:", new_bytes[1] )

# 36- Lobby Send Chat- (message)
def lobby_send_chat(data_bytes):
    print ("Lobby sent Chat:")
    print ("    Message:", data_bytes[1:].decode('ascii', 'ignore') )

# 54- You gave player invite power- [player#]
def lobby_give_invite_power(data_bytes):
    print ("You gave invite power:")
    print ("    Player:", data_bytes[1:] )

# 62- Player received invite power- [player#]
def lobby_get_invite_power(data_bytes):
    print ("Player received invite power:")
    print ("    Player:", data_bytes[1:] )

# 95- Death Information- [player#] [role#] [death time] (killed by)
def death_information(data_bytes):
    print ("Death Information:")
    print ("    Player#:", data_bytes[1] )
    print ("    Role:", data_bytes[2] )
    print ("    Death time:", data_bytes[3] )
    for byte in data_bytes[4:]:
        if byte is not 0:
            print ("    Killed By:", byte)

#103- Vote to Lynch- [player#] [voted#] [?]
def vote_lynch(data_bytes):
    print ("Vote to Lynch")
    print ("    Player#:", data_bytes[1] )
    print ("    Voted Player#:", data_bytes[2] )
    print ("    :", data_bytes[3] )

#107- Resurrection- [player#] [1]
def resurrection(data_bytes):
    print ("Player Resurrected!")
    print ("    Player#:", data_bytes[1] )
    print ("    :", data_bytes[2] )

#109- Name Picked- [?] [player#] (name)
def pick_name(data_bytes):
    print ("Name Pick:")
    print ("    :", data_bytes[1] )
    print ("    Player#:", data_bytes[2] )
    print ("    Name:", data_bytes[3:].decode('ascii', 'ignore') )

#117- Vote to kill- [player#]
def vote_kill(data_bytes):
    print ("Vote to kill:")
    print ("    Player#:", data_bytes[1] )

#123- Reveal as mayor- [player#]
def mayor_reveal(data_bytes):
    print ("Reveal as Mayor:")
    print ("    Player#:", data_bytes[1] )

#130- Last will no death note- [player#] (last will)
def lastwill(data_bytes):
    print ("Last Will (no dn):")
    print ("    Player#:", data_bytes[1] )
    print ("    Last Will:", data_bytes[3:].decode('ascii', 'ignore') )
        
#146- Death notification- (player #'s)
def death_notification(data_bytes):
    print ("Death notification:")
    for byte in data_bytes[1:]:
        if byte is not 0:
            print ("    Player#:", byte)

#148- Last will w/ death note- [player#] (death note) [2] (last will)
def lastwill_deathnote(data_bytes):
    print ("Last Will (w/ dn):")
    print ("    Player#:", data_bytes[1] )
    posOf2 = data_bytes[3:].find(b'2')
    print ("    Death Note:", data_bytes[3:posOf2].decode('ascii', 'ignore') )
    print ("    Last Will:", data_bytes[posOf2:].decode('ascii', 'ignore') )

#159- Whisper notification- [source player#] [dest player#]
def whisper_notification(data_bytes):
    print ("Whisper notification:")
    print ("    Source Player#:", data_bytes[1] )
    print ("    Dest Player#:", data_bytes[2] )

#160- Received a PM- [?] [player#] [?] (message)
def recieved_pm(data_bytes):
    print ("You received a PM:")
    print ("    :", data_bytes[1] )
    print ("    Player#:", data_bytes[2] )
    print ("    :", data_bytes[3] )
    print ("    Message:", data_bytes[3:].decode('ascii', 'ignore') )

#???- Unknown packet- ????
def print_unknown(data, data_bytes):
    print ("Unknown Packet:")
    for byte in data_bytes:
        print ('{:>4}'.format(byte), end="")
    print ("")
    print (data_bytes)
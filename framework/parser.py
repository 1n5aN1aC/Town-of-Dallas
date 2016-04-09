#!python
from framework import debug_printers
from framework import handlers

# Called by parse_packet to actually print something.
def parse_data(data):
    data_bytes = bytearray(data)

    # Don't show me blank packets.
    if data_bytes[0] is 0:
        return

    # Switch on packet id
    if data_bytes[0] is 3:
        debug_printers.chat_send(data_bytes)
    elif data_bytes[0] is 6:
        handlers.chat_get(data_bytes)
    elif data_bytes[0] is 8:
        debug_printers.send_pm(data_bytes)
    elif data_bytes[0] is 10:
        debug_printers.you_vote_lynch(data_bytes)
    elif data_bytes[0] is 11:
        debug_printers.use_normal_ability(data_bytes)
    elif data_bytes[0] is 17:
        debug_printers.set_lastwill(data_bytes)
    elif data_bytes[0] is 18:
        debug_printers.set_deathnote(data_bytes)
    elif data_bytes[0] is 35:
        debug_printers.lobby_get_chat(data_bytes)
    elif data_bytes[0] is 36:
        debug_printers.lobby_send_chat(data_bytes)
    elif data_bytes[0] is 54:
        debug_printers.lobby_give_invite_power(data_bytes)
    elif data_bytes[0] is 62:
        debug_printers.lobby_get_invite_power(data_bytes)
    elif data_bytes[0] is 95:
        debug_printers.death_information(data_bytes)
    elif data_bytes[0] is 103:
        debug_printers.vote_lynch(data_bytes)
    elif data_bytes[0] is 107:
        debug_printers.resurrection(data_bytes)
    elif data_bytes[0] is 109:
        debug_printers.pick_name(data_bytes)##############
        handlers.pick_name(data_bytes)
    elif data_bytes[0] is 117:
        debug_printers.vote_kill(data_bytes)
    elif data_bytes[0] is 123:
        debug_printers.mayor_reveal(data_bytes)
    elif data_bytes[0] is 130:
        debug_printers.lastwill(data_bytes)
    elif data_bytes[0] is 146:
        debug_printers.death_notification(data_bytes)
    elif data_bytes[0] is 148:
        debug_printers.lastwill_deathnote(data_bytes)
    elif data_bytes[0] is 159:
        debug_printers.whisper_notification(data_bytes)
    elif data_bytes[0] is 160:
        debug_printers.recieved_pm(data_bytes)
    else:
        debug_printers.print_unknown(data, data_bytes)
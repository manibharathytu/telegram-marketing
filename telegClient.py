from telethon import TelegramClient,sync
from telethon.tl.functions.messages import AddChatUserRequest

import traceback

import lc
import bl
import settings

try :
	lc.check_license()
	client = TelegramClient('session_name', settings.API_ID, settings.API_HASH)
	client.start()
	bl.doAction(client) 

except :
	print ("exception happened")
	traceback.print_exc()
	input()

    

    


import time
import traceback

import settings

client = 0

def send_message() :

    members = client.get_participants(settings.SOURCE_GROUP)

    for member in members :
        print(member.id)
        time.sleep(settings.WAIT_TIME)
        if settings.CONTENT_TYPE=="text" :
            client.send_message(member.id, settings.CONTENT)               

        elif settings.CONTENT_TYPE=="file" :
            client.send_file(member.id, settings.CONTENT)

def add_people() :
    members = client.get_participants(settings.SOURCE_GROUP)

    for member in members :
        print(member.id)
        time.sleep(settings.WAIT_TIME)
        try:
            client(AddChatUserRequest(settings.TARGET_GROUP, member.id,fwd_limit=10 ))
            print("added successfully")
        except:
            print("exception accured when adding user-> AddChatUserRequest")
            traceback.print_exc() 

def doAction(telegClient) :
    global client
    client = telegClient
    if settings.ACTION == "message" :
        send_message()
    elif settings.ACTION == "add" :
        add_people()
import settings
from datetime import datetime
import hashlib
import sys

def check_license():     
      

        constStr='telegbotlicense'
        email_id=settings.EMAIL_ID
        license=settings.LICENSE_KEY
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year

        strToHash=constStr+str(email_id)+str(day)+str(month)+str(year)
        #print(strToHash)
        strToHash_b=strToHash.encode('utf-8')


        hash_object = hashlib.sha1(strToHash_b)
        hex_dig = hash_object.hexdigest()

        #print(hex_dig)
        

        if license==hex_dig :            
             return True

        print("----------------------------------------") 
        print("LICENCE EXPIRED. CONTACT VENDOR")             
        print("----------------------------------------") 
        sys.exit()     
        return False
# web whatsapp must be initiated on the browser first before usage linked to your account 
import pywhatkit as pwk
import datetime
e=datetime.datetime.now()

pwk.sendwhatmsg('#mobile number with country code',"this is jarvis here",e.hour,e.minute +1) #send to number,message, time in 24 hrs , mins 

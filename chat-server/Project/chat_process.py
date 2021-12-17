
from Project import db
import datetime
def save_message(sender_id,message,type):
    
    db.collection(u'users').document(sender_id).collection('chat').document().set({"message":message['message'],"time":datetime.datetime.timestamp(datetime.datetime.now()),"type":type})



from Project import db
import datetime
def checkType(payload):
    if 'message' in payload['events'][0].keys():
        message_type = payload['events'][0]['message']['type']
    elif 'postback' in payload['events'][0].keys():
        message_type = 'postback'
    else:
        message_type = 'else'
    return message_type


def defineSender(sender, profile):
    doc_ref = db.collection(u'users').document(sender)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.update({'pictureUrl': profile.picture_url, 'display_name': profile.display_name,'userId':sender,
                       'last_message': datetime.datetime.timestamp(datetime.datetime.now())})

    else:
        obj = {'pictureUrl': profile.picture_url, 'display_name': profile.display_name,'userId':sender,
               'last_message': datetime.datetime.timestamp(datetime.datetime.now()), 'subState': 'none','mainState':'none','profile':False,'symptom':False}
        doc_ref.set(obj)
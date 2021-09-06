from starlette import responses
from Project import db
from Project.extensions import getAnswer
import json

def stateHandler(**kwargs):
    doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    doc = doc_ref.get()
    user_define = doc.to_dict()
    #customer_define = customer_collection.find_one({'$and':[{"userID": kwargs['sender_id']},{"botID": ObjectId(kwargs['botID'])}]})
    res={"message":"เกิดข้อผิดพลาดโปรดลองใหม่หรือทำกระบวนการที่ทำอยู่ให้เสร็จก่อนครับ"}
    if 'message' in kwargs.keys():
        # if customer_define['state'] == "name":
        #     return {"flex":json.loads(confirm_flexmessage(kwargs['message']['message'])),"alt":"ยืนยันชื่อ-นามสกุล"}
        # elif customer_define['state'] == "address":
        #     return {"flex":json.loads(address_flex(kwargs['message']['message'])),"alt":"ยืนยันที่อยู่"}
        # elif customer_define['state'] == "tel":
        #     return {"flex":json.loads(tel_flexmessage(kwargs['message']['message'])),"alt":"ยืนยันเบอร์โทร"}
        if user_define['state'] == "none":

            # data = kwargs['message'],kwargs['confident'],kwargs['sender_id']
            response=getAnswer(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
            res = json.loads(response.text)
            print(res['message'])
            #res = process_message(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res
from starlette import responses
from Project import db
from Project.extensions import getAnswer
import json
from pythainlp.tokenize import word_tokenize
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
            # msg_token = word_tokenize(kwargs['message'])
            ans = ''
            flag = True
            flag,ans = basicEventHandler(kwargs['message'])
            if not flag:
                # data = kwargs['message'],kwargs['confident'],kwargs['sender_id']
                response=getAnswer(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
                res = json.loads(response.text)
                print(res['message'])
            if flag :
                return ans
            #res = process_message(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res


def basicEventHandler(msg):

    # event_collection = mongo.db.events
    if msg['message'] == 'หาหมอครับ':
        event = tt()
        return True,{'flex':event}
    return False,'Not found'
      
    # for x in ['ครับ', 'ค่ะ', 'ค่า', 'คะ', 'คับ', 'คร้าบ', 'ฮ่ะ', 'อ่ะ', 'อ่า', 'ป้ะ', 'ป่ะ', 'บ่', 'แมะ', 'มะ', 'ก๊า', 'ไหม', 'มั้ย', 'หน่อย']:
    #     try:
    #         msg.remove(x)
    #     except :
    #         continue
        
    # event_define = event_collection.find_one({'data_set': {'$regex': key,"$options" :'i'}}) #####มาเช็คดีๆ
    # if event_define != None and event_define['type'] == 'search':
    #     if isnotSymbol(''.join(msg)):
    #         item = json.loads(item_list_flexmessage(botID = botID, query=''.join(msg),platform=platform,sender_id = sender_id))
    #     else:
    #         item = {"message" : "การค้นหาผิดพลาด"}
    #     if type(item) == list:
    #         return True,{"flex":CarouselContainer(item),"alt":"ค้นหาสินค้า","type":"none"}
    #     elif "message" in item.keys():
    #         return True,item
    #     elif "facebook" == platform:
    #         return True,{"flex":item,"type":"none"}
    # elif event_define != None and event_define['type'] == 'confirm_order':
    #     item = json.loads(invoice_flexmessage(botID = botID, sender_id=sender_id))
    #     if "message" in item.keys():
    #         return True,item
    #     return True,{"flex":item, "alt": "ยืนยันรายการ","type":"none"}
    # elif event_define != None and event_define['type'] == 'call_merchant':
    #     customer_collection = mongo.db.customers
    #     customer_collection.update_one({"userID": sender_id},{"$set":{"call_merchant":True}})
    #     return True,{"group":[{"data":"ติดต่อแม่ค้าไปแล้วครับ กรุณารอสักครู่","type":"text"},{"data":"ระหว่างนี้เลือกซื้อของรอไปก่อนได้เลยครับบ","type":"text"}]}
    # # elif event_define != None and event_define['type'] == 'liff':
    # #     return True,{"message":"https://liff.line.me/1655652942-YyMAypje"}
    # return False,'not found word'


def tt():
    a = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Go",
              "uri": "https://example.com"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Hello, World!",
            "wrap": True
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Go",
              "uri": "https://example.com"
            }
          }
        ]
      }
    }
  ]
}
    return a


from linebot.models import actions
from starlette import responses
from Project import db
from Project.extensions import getAnswer,predict
import json
from pythainlp.tokenize import word_tokenize
from Project.profileState import preFlexProfile
from Project.mainState import stateHandler
from Project.helper import handleSequence,getSequence,createFlex
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)

def basicEventHandler(**kwargs):

    doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    # event_collection = mongo.db.events
    # if kwargs['subState'] == 'done' or kwargs['subState'] == 'none':
    #     return False, {'message': "Done"},"done"
    if kwargs['message']['message'] == 'หาหมอครับ':   #command for first time
        isProfileComplete = checkProfile(doc_ref)
        if isProfileComplete :
            seq = handleSequence()
            event = createFlex(seq)
            doc_ref.update({"mainState": "covid","subState":seq['id']})
            return {'flex': event,'alt':seq['Question']}
        else :
            event = preFlexProfile(state="real_name")
            doc_ref.update({"mainState": "profile","subState":"real_name"})
            return {'flex': event,'alt':"กรุณากรอกชื่อจริงของท่าน"}
    elif kwargs['message']['message'] == 'ยกเลิก': #command for cancel
        return {'message':"ยกเลิกการทำงาน"}
    elif  kwargs['message']['message'] == "test":
            content =  {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "กรุณาใส่วันเกิดของคุณ"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "action": {
          "type": "datetimepicker",
          "label": "action",
          "data": "hello",
          "mode": "date"
        }
      }
    ]
  }
}
            print(content)
            return {"flex":content,"alt":"ยืนยันที่อยู่"}
    else :
        res = stateHandler(sender_id = kwargs['sender_id'],message = kwargs['message'],confident = kwargs['confident'])
        return res


def checkProfile(doc_ref):
    doc = doc_ref.get()
    if doc.exists:
        userProfile = doc.to_dict()
        if "isProfileComplete" in userProfile :
          return True
        else :
          return False
    else:
        return False
    # newList = []
    # for seq in sequenceLogics:
    #   newList.append(seq.to_dict())
    # return newList


# def handleSequence(subState = 'none',next = False):
#     seqs = getSequence() # get logic from db
#     res = {}
#     for seq in seqs:

#       if seq['id'] == subState and subState != 'none': #check current subState
#         res = seq
#         break
#       elif subState == 'none': 
#         res = seq
#         break
#     if subState != 'none': #if current subState not None
#       # if res['Type'] == "input" or res['Type'] == "boolean" : 
#       print(res)
#       if res['Type'] == "input" or res['Type'] == "boolean" : 
#         if next == True: # Has next Question ?
#           flag = False
#           for seq in seqs: # get next question
#             if res['Next'] == seq['id']:
#               res = seq 
#               flag = True
#               break
#           if flag == False: # has no next question
#               res = "Done"

#       else :  # check if type not input not accept respons
#         res = None
#     return res




# def getSequence():
#     sequenceLogics =  db.collection(u'lineLogic').stream()
#     newList = []
#     for seq in sequenceLogics:
#       newList.append(seq.to_dict())
#     return newList



# def createFlex(seq):
#     context = {
#       "type": "bubble",
#       "body": {
#         "type": "box",
#         "layout": "horizontal",
#         "contents": [
#           {
#             "type": "text",
#             "text": seq['Question'],
#             "wrap": True
#           }
#         ]
#       }
#     }
#     if seq['Type'] == 'boolean':
#         context['footer'] = {

#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#         "type": "button",
#         "style": "primary",
#         "height": "sm",
#             "action": {
#           "type": "postback",
#           "label": "ใช่",
#           "data": "action=%=true//subState=%="+seq['id'],
#         "displayText": "เป็น"
#         }
#       },
#                 {
#         "type": "button",
#         "style": "primary",
#         "height": "sm",
#             "action": {
#           "type": "postback",
#           "label": "ไม่ใช่",
#           "data": "action=%=false//subState=%="+seq['id'],
#         "displayText": "ไม่เป็น"
#         }
#       },
#         ]
#       }

#     return context
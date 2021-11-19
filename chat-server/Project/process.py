
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
    elif kwargs['message']['message'] == 'ช่วยเหลือ': #command for cancel
        replay_message = getReplyMessage('helpingMessage')
        content = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "โรคทั่วไป",
          "data": "action=%=common"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "โรคผิวหนัง",
          "data": "action=%=skin"
        }
      }
    ],
    "flex": 0
  }
}
        return {'group': [{'message':replay_message},{'flex':content,"alt":"skin detail"}]}
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

            return {"flex":content,"alt":"ยืนยันที่อยู่"}
    elif kwargs['message']['message'] == "โรคผิวหนัง":
        doc_ref.update({"mainState": "skin","subState":None})
        content =  {
          "type": "bubble",
          "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "uri": "http://linecorp.com/"
            }
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "เริ่มการวินิจฉัยโรคผิวหนัง",
                "size": "xl",
                "style": "normal",
                "weight": "bold",
                "decoration": "underline",
                "position": "relative"
              },
              {
                "type": "text",
                "text": "กรุณาส่งรูปภาพหรือถ่ายภาพจากกล้อง",
                "size": "xs",
                "margin": "none",
                "weight": "regular",
                "maxLines": 3,
                "contents": [
                  {
                    "type": "span",
                    "text": "กรุณาส่งรูปภาพหรือถ่ายภาพจาก"
                  }
                ]
              },
              {
                "type": "text",
                "text": "hello, world",
                "contents": [
                  {
                    "type": "span",
                    "text": "กล้องโทรศัพท์ของคุณเพื่อให้ระบบนำไปวินิจฉัย"
                  }
                ],
                "size": "xs",
                "style": "normal",
                "weight": "regular"
              }
            ]
          }
        }
        replay_message = getReplyMessage('skinMessage')
        return {'group': [{'message':replay_message},{'flex':content,"alt":"skin detail"}]}
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

def getReplyMessage(event):
    if event == 'helpingMessage':
      return """สวัสดีครับ ผมชื่อน้องสุขภาพดี ผมเป็นระบบแชทบอทช่วยวินิจฉัยอาการป่วยเบื้องต้นและจำแนกโรคทางผิวหนังทั่วไปจากรูปภาพของคุณ

กรุณาพิมพ์คำสั่งต่อไปนี้หรือกดดที่แถบเมนูด้านล่างข้อความนี้เพื่อให้ผมเริ่มวินิจฉัยอาการป่วยของคุณ

"โรคทั่วไป" เพื่อเรื่มการวินิจฉัยอาการป่วยของคุณ
"โรคผิวหนัง" เพื่อเริ่มการวินิจฉัยอาการป่วยของโรคทางผิวหนังจากรูปภาพหรือภาพถ่ายของคุณ
"ชวยเหลือ" เพื่อแสดงข้อความนี้อีกครั้ง"""
    elif event == 'skinMessage':
      return """สำหรับการวินิจฉัยอาการป่วยของโรคผิวหนัง ระบบจะให้คุณส่งรูปภาพหรือถ่ายภาพจากโทรศัพท์ของคุณมายังแชทบอท จากนั้นระบบจะใช้เวลาประมวลผลจากรูปภาพของคุณสักครู่ เมื่อประมวลผลเวร็จสิ้นแล้ว ระบบจะส่งผลการวินิจฉัยออกมาว่าท่านอยู่ในกลุ่มเสี่ยงของโรคผิวหนังชนิดใดจาก 3 โรค ซึ่งใดแก่

1.) โรคผื่นแพ้อักเสบ (Eczema)
2.) โรคผื่นภูมิแพ้ผิวหนัง (Atopic Dermatitis)
3.) โรคกลากเกลื้อนและการติดเชื้อราอื่น ๆ (Tinea Ringworm Candidiasis and Fungal Infections)

กรุณาพิมคำสั่ง "วินิจฉัยโรคผิวหนัง" เพื่อเริ่มการวินิจฉัย หรือกดจากแถบเมนูด้านล่างข้อความนี้ """
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
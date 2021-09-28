from fastapi import APIRouter
from Project import db
from Project.chat_process import save_message
import requests
from typing import Dict
from pydantic import BaseModel
from typing import Optional
import datetime
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)
import json
import datetime
from Project.process import basicEventHandler
from Project.mainState import stateHandler
from fastapi.responses import HTMLResponse

class TrainedModel(BaseModel):
    question: str
    answer: str


router = APIRouter()


@router.get("/")
async def test():
    docs = db.collection(u'trained').stream()
    obj = []
    for doc in docs:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        obj.append(train_dict)
    return obj


@router.post("/webhook")
async def webhook(payload: Dict):
    line_bot_api = LineBotApi(
        '/j7EhbUFpBEyRWQ/S4L/ENoFex6cRKDTSgWLfHnBbRHJrGW2DfFzndBaUTDqS+ryp+37YkTpE+ApqsGOF3gGnOgK3qdALaGKXPfNcDIVZ+yr5GZ5I3NRz8l6DtK4jnAxOwsXWsG5BxhzLUr6sHhbSgdB04t89/1O/w1cDnyilFU=')
    print(payload)
    if not payload['events']:
        return HTMLResponse( status_code=200)
    Reply_token = payload['events'][0]['replyToken']
    sender = payload['events'][0]['source']
    profile = line_bot_api.get_profile(sender['userId'])
    message_type = checkType(payload)
    response=[TextSendMessage(text='บางอย่างผิดพลาดกรุณาติดตต่อเจ้าหน้าที่')]
    # if message_type == 'text':
    #     data = {"message":payload['events'][0]['message']['text']}
    #     timestamp = datetime.datetime.timestamp(datetime.datetime.now())
    #     res = stateHandler(sender_id=sender_define['userID'], botID=botID, message= data, confident=bot_define['confident'])
    #     save_message(message=data['message'],bot_name=bot_define['bot_name'],message_type="text",sender=profile.display_name,sender_id=sender_define['userID'],sender_type="line",room=botID+'&'+sender_define['userID'],botId=bot_define['_id'],userID=bot_define['owner'],pictureUrl=profile.picture_url)
    # else :
    #     res = {"message":"ขอโทษครับ ผมรับเป็นตัวหนังสือเท่านั้น"}
    defineSender(sender['userId'], profile)

    if message_type == 'text':
        data = {"message": payload['events'][0]['message']['text']}
        timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        res = basicEventHandler(
            sender_id=sender['userId'], message=data, confident=0.6 )
        print('response',res)
        # basicEventHandler(sender_id=sender['userId'], message=data, type="text")
        # save_message(message=data['message'],bot_name=bot_define['bot_name'],message_type="text",sender=profile.display_name,sender_id=sender_define['userID'],sender_type="line",room=botID+'&'+sender_define['userID'],botId=bot_define['_id'],userID=bot_define['owner'],pictureUrl=profile.picture_url)
    elif message_type == 'postback':
        data = {'postback':payload['events'][0]['postback']['data']}
        if "params"  in payload['events'][0]['postback'].keys():
            
            res = stateHandler(sender_id=sender['userId'], postback=data,params=payload['events'][0]['postback']['params'])
        else :
            res = stateHandler(
                sender_id=sender['userId'], postback=data)
    if "message" in res.keys():
        response = [TextSendMessage(text=res['message'])]

    elif 'flex' in res.keys():
        response = FlexSendMessage(
            alt_text=res['alt'],
            contents=res['flex']

        )
#                     response = TemplateSendMessage(
#     alt_text='Confirm template',
#     template=ConfirmTemplate(
#         text='Are you sure?',
#         actions=[
#             PostbackAction(
#                 label='postback',
#                 display_text='postback text',
#                 data='action=buy&itemid=1'
#             ),
#             PostbackAction(
#                 label='CA',
#                 display_text='postback CA',
#                 data='action=buy&itemid=1'
#             ),

#         ]
#     )
# )

    line_bot_api.reply_message(Reply_token, response)


    return HTMLResponse( status_code=200)


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
        doc_ref.update({'pictureUrl': profile.picture_url, 'display_name': profile.display_name,
                       'last_message': datetime.datetime.timestamp(datetime.datetime.now())})

    else:
        obj = {'pictureUrl': profile.picture_url, 'display_name': profile.display_name,
               'last_message': datetime.datetime.timestamp(datetime.datetime.now()), 'subState': 'none','mainState':'none','profile':False,'symptom':False}
        doc_ref.set(obj)

# def save_message(message,message_type)
# @router.post("/")
# async def createTrainWord(data: TrainedModel):
#     data = data.dict()
#     # Add a new doc in collection 'cities' with ID 'LA'
#     obj = {"answer":data['question'],"question":data['answer'],"time": datetime.datetime.timestamp(datetime.datetime.now())}
#     db.collection(u'trained').document().set(obj)
#     return "done"


# @router.patch("/{id}")
# async def updateTrainWord(data: TrainedModel,id: str):
#     print(id)
#     data = data.dict()
#     # Add a new doc in collection 'cities' with ID 'LA'
#     doc_ref = db.collection(u'trained').document(id)
#     doc_ref.update({'question': data['question'],'answer':data['answer']})
#     return "PATCH"

# @router.delete("/{id}")
# async def deleteTrainWord(id: str):
#     db.collection(u'trained').document(id).delete()
#     return "Delete Done"

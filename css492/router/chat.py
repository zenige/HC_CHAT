from fastapi import APIRouter
from Project import db
# from Project.chat_process import save_message
import requests
from typing import Dict
from pydantic import BaseModel
from typing import Optional
import datetime
from Project.Services.chatBot import postbackHandler
from Project.Services.ImageClassifly import predict
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)
import json
import datetime
from fastapi.responses import HTMLResponse
# from Project.process import basicEventHandler
# from Project.mainState import stateHandler
# from fastapi.responses import HTMLResponse
# from PIL import Image
# import cv2
from Project.Services.chatBot import chatService
from Project.Services.chatBot import basicState, chatService

class TrainedModel(BaseModel):
    question: str
    answer: str


router = APIRouter()


@router.get("/")
async def test():
    docs = db.collection(u'users').stream()
    obj = []
    for doc in docs:
        train_dict = doc.to_dict()
        obj.append(train_dict)
    return obj



@router.post("/webhook")
async def webhook(payload: Dict):
    line_bot_api = LineBotApi(
        '/j7EhbUFpBEyRWQ/S4L/ENoFex6cRKDTSgWLfHnBbRHJrGW2DfFzndBaUTDqS+ryp+37YkTpE+ApqsGOF3gGnOgK3qdALaGKXPfNcDIVZ+yr5GZ5I3NRz8l6DtK4jnAxOwsXWsG5BxhzLUr6sHhbSgdB04t89/1O/w1cDnyilFU=')
    print(payload)
    if not payload['events']:
        return HTMLResponse(status_code=200)
    Reply_token = payload['events'][0]['replyToken']
    sender = payload['events'][0]['source']
    profile = line_bot_api.get_profile(sender['userId'])
    message_type = chatService.checkType(payload)
    response = [TextSendMessage(text='บางอย่างผิดพลาดกรุณาติดตต่อเจ้าหน้าที่')]
    print(message_type)
    chatService.defineSender(sender['userId'], profile)
    if message_type == 'text':
        data = {"message": payload['events'][0]['message']['text']}
        timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        res = basicState.basicEventHandler(
            sender_id=sender['userId'], message=data, confident=0.6,reply_token=Reply_token)
    elif message_type == 'postback':
        data = {'postback':payload['events'][0]['postback']['data']}
        if "params"  in payload['events'][0]['postback'].keys():
            
            res = postbackHandler.stateHandler(sender_id=sender['userId'], postback=data,params=payload['events'][0]['postback']['params'])
        else :
            res = postbackHandler.stateHandler(
                sender_id=sender['userId'], postback=data)
    elif message_type == 'image':
        data = {'imageId':payload['events'][0]['message']['id']}
        res = postbackHandler.stateHandler(sender_id=sender['userId'], image=data ,line_bot_api=line_bot_api)

    if "message" in res.keys():
        response = [TextSendMessage(text=res['message'])]
    elif 'flex' in res.keys():
        response = FlexSendMessage(
            alt_text=res['alt'],
            contents=res['flex']
        )
    elif 'carousel' in res.keys():
        response = TemplateSendMessage(
            alt_text=res['alt'],
            template=CarouselTemplate(list(res['carousel']))
        )

    elif 'group' in res.keys():
        response = []
        # isAlreadyReply = True
        for i in res['group']:
            if "message" in i.keys():
                response.append(TextSendMessage(text=i['message']))
            elif 'flex' in i.keys():
                response.append(FlexSendMessage(
                    alt_text=i['alt'],
                    contents=i['flex']
                ))
            elif 'carousel' in i.keys():
                
                response.append(TemplateSendMessage(
                    alt_text=i['alt'],
                    template=CarouselTemplate(list(i['carousel']))
                ))
    line_bot_api.reply_message(Reply_token, response)
    return HTMLResponse(status_code=200)

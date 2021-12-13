import json

from linebot.models import (MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
                            BubbleContainer, TemplateSendMessage, ConfirmTemplate,
                            PostbackAction, MessageAction, ImageSendMessage, StickerSendMessage,
                            ImageCarouselTemplate, ImageCarouselColumn, CarouselTemplate, CarouselColumn, URIAction,
                            CarouselContainer, ImageComponent)
def welcomMessage():
    firstMessage = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://cdn.discordapp.com/attachments/791178261371289631/917601652649889812/Healthcare_Chatbot_-_LINE_Chatbot_Logo.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            },
            "margin": "sm",
            "position": "relative",
            "align": "start"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "ผมสามารถวินิจฉัยโรคผิวหนังของคุณได้ว่าคุณป่วยเป็นโรคอะไร เพียงคุณส่งรูปมาให้ผม เริ่มวินิจฉัยกันเลยไหมครับ? กรุณาเลือกเมนูด้านล่าง",
                "size": "md",
                "style": "normal",
                "decoration": "none",
                "position": "relative",
                "wrap": True
            }
            ]
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
                "label": "เริ่มการวินิฉัย",
                "data": "action=start&state=start"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "postback",
                "label": "ดูเพิ่มเติม",
                "data": "action=seeMore&state=seeMore"

                }
            }
            ],
            "flex": 0
        }
        }
    secondMessage = """สวัสดีครับ ชือผู้ใช้! ผมชื่อน้องสุขภาพดี ผมเป็นระบบแชทบอทช่วยวินิจฉัยและจำแนกโรคทางผิวหนังทั่วไปครับ"""
    return firstMessage,secondMessage

def seeMoreMessage():
  
    content = columns=[
            CarouselColumn(
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6v7lBLWbECKWyBe6HHrB3gCfweE9sI10tqg&usqp=CAU',
                title='1.) โรคผื่นแพ้อักเสบ (Eczema)',
                text='description1',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text1',
                        data='action=seeMore&state=eczema'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
            ,
            CarouselColumn(
                thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
                title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
                text='description2',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='postback text2',
                         data='action=seeMore&state=warts'
                    )
                ]
            )
        ]
    return {'group': [{'message':"secondMessage"},{'carousel':content,"alt":"skin detail"}]}


def seeMoreEczema():
    return {"message" : "ข้อมูลของโรค Eczema"}
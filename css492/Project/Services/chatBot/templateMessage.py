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
    return firstMessage, secondMessage


def seeMoreMessage():

    content = columns = [
        CarouselColumn(
            thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6v7lBLWbECKWyBe6HHrB3gCfweE9sI10tqg&usqp=CAU',
            title='1.) โรคผื่นแพ้อักเสบ ',
            text='กดเพื่อดูข้อมูลเพิ่มเติม',
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
            text='กดเพื่อดูข้อมูลเพิ่มเติม',
            actions=[
                PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='postback text2',
                    data='action=seeMore&state=warts'
                )
            ]
        ),
        CarouselColumn(
            thumbnail_image_url='https://medthai.com/images/2016/03/%E0%B8%AB%E0%B8%B9%E0%B8%94%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B8%E0%B8%81.jpg',
            title='2.) หูดข้าวสุกหรือหูดที่เกิดจากเชื้อไวรัสอื่นๆ',
            text='กดเพื่อดูข้อมูลเพิ่มเติม',
            actions=[
                PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='postback text2',
                    data='action=seeMore&state=warts'
                )
            ]
        )

    ]
    return {'group': [{'message': "การวินิจฉัยนั้น ระบบจะให้คุณส่งรูปภาพหรือถ่ายภาพจากโทรศัพท์ของคุณมายังแชทบอท จากนั้นระบบจะใช้เวลาประมวลผลจากรูปภาพของคุณสักครู่ เมื่อประมวลผลเสร็จสิ้น ระบบจะส่งผลการวินิจฉัยมาให้คุณ พร้อมทั้งคำแนะนำต่าง ๆ ในการรักษา"}, {'message': "โดยระบบจะวินิจฉัยว่าคุณมีความน่าจะเป็นที่จะอยู่ในกลุ่มเสี่ยงของโรคใดจากทั้งหมด 3 โรค ได้แก่"}, {'carousel': content, "alt": "skin detail"}]}


def seeMoreEczema():
    return {"message": "โรคผื่นแพ้อักเสบ (Eczema) คือภาวะการอักเสบของผิวหนังที่เกิดขึ้น เป็นได้จากหลายสาเหตุ มักมาด้วยอาการผื่นคัน บวม หรือแดงตามผิวหนัง แต่ในบางรายอาจเกิดเป็นแผลพุพอง มีน้ำหนอง หรือตกสะเก็ดร่วมด้วย โดยภาวะผิวหนังอักเสบที่พบบ่อย ได้แก่ โรคผื่นภูมิแพ้ผิวหนัง โรคเซบเดิร์ม และโรคผื่นแพ้สัมผัส อย่างไรก็ตามภาวะนี้จะไม่ติดต่อสู่ผู้อื่น แต่อาจทำให้รู้สึกคันหรือระคายเคือง และเสียความมั่นใจเพราะลักษณะผิวหนังที่ผิดปกติได้\n\nอ่านเพิ่มเติมที่: https://www.lcclinics.com/ผิวหนังอักเสบ-eczema-คืออะไร/"}


def listPredictImg(disease,userId):
    content = columns = []

    for i in disease:
        url = ''
        if i['label'] == 'Tinea Ringworm Candidiasis':
            url = 'https://liff.line.me/1656721605-52PWxpmj'
            content.append(CarouselColumn(
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6v7lBLWbECKWyBe6HHrB3gCfweE9sI10tqg&usqp=CAU',
                title='1.) '+str(i['label']),
                text='มีความน่าจะเป็น = '+str(i['predict']),
                actions=[
                    URIAction(
                        label='tineaRingworm',
                        uri='https://liff.line.me/1656721605-52PWxpmj'
                    )
                ]
            ))
        elif i['label'] == 'Eczema':
            
            content.append(CarouselColumn(
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6v7lBLWbECKWyBe6HHrB3gCfweE9sI10tqg&usqp=CAU',
                title='1.) '+str(i['label']),
                text='มีความน่าจะเป็น = '+str(i['predict']),
                actions=[
                     PostbackAction(
                    label='ดูรายละเอียดเพิ่มเติม',
                    display_text='postback text1',
                    data='action=seeMore&state=eczema'
                    )
                ]
            ))
        elif i['label'] == 'Atopic Dermatitis':
            url = 'https://liff.line.me/1656721598-rbNWDBag'
            content.append(CarouselColumn(
                thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6v7lBLWbECKWyBe6HHrB3gCfweE9sI10tqg&usqp=CAU',
                title='1.) '+str(i['label']),
                text='มีความน่าจะเป็น = '+str(i['predict']),
                actions=[
                    URIAction(
                        label='atopicDermatitis',
                        uri='https://liff.line.me/1656721598-rbNWDBag'
                    )
                ]
            ))
        if(str(disease[0]['label'])) == 'Tinea Ringworm Candidiasis':
            url='https://liff.line.me/1656721605-52PWxpmj'
        elif(str(disease[0]['label'])) == 'Eczema':
            url = 'https://liff.line.me/1655993001-QLqyKnVe'
        elif(str(disease[0]['label'])) == 'Atopic Dermatitis':
            url='https://liff.line.me/1656721598-rbNWDBag'
        flexContent = {
            "type": "bubble",
            "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "คุณต้องการทำแบบสอบถามเพื่อประเมินระดับความรุนแรงของโรค ผื่นแพ้อักเสบ (Eczema) หรือไม่?",
                            "weight": "regular",
                            "decoration": "none",
                            "position": "relative",
                            "align": "start",
                            "gravity": "top",
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
                                "type": "uri",
                                "label": "ใช่ ทำเลย",
                                "uri": url+"?userId="+userId
                            }
                        },
                    {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                                "type": "postback",
                                "label": "ไม่ละ ขอบคุณ",
                                "data": "action=moreDetail&state="+str(disease[0]['label'])
                            }
                        }
                ],
                "flex": 0
            }
        }
    return {"group": [{'carousel': content, "alt": "skin detail"}, {'message': 'คุณมีความน่าจะเป็นที่จะเป็นโรค'+str(disease[0]['label']) + 'มากที่สุดถึง' + str(disease[0]['predict']) + '% '}, {'flex': flexContent, 'alt': 'ต้องการทำแบบทดสอบเพิ่มเติมไหม'}]}
    #     content['colums']


def moreDetailTreatment(i):
    if i == 'Eczema':
        content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/94zF8gW/Eczema.jpg',
                title='1.) สาเหตุที่ทำให้เกิดโรคผืนแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม สาเหตุที่ทำให้เกิดโรคผืนแพ้อักเสบ',
                        data='action=moreDetailTreat&state=eczema&subState=reason'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/FwCBX3d/image.png',
                title='2.) การดูแลตัวเองสำหรับโรคผื่นแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม การดูแลตัวเองสำหรับโรคผื่นแพ้อักเสบ',
                        data='action=moreDetailTreat&state=eczema&subState=treatSelf'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/892W6mJ/image.jpg',
                title='3.) การใช้ยารักษาโรคผืนแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม การใช้ยารักษา',
                        data='action=moreDetailTreat&state=eczema&subState=med'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/QdtdwjN/image.jpg',
                title='4.) ผลิตภัณที่แนะนำทั่วไปสำหรับโรคผื่นแพ้อักเสบ',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                    PostbackAction(
                        label='ดูรายละเอียดเพิ่มเติม',
                        display_text='ดูเพิ่มเติม ผลิตภัณที่แนะนำทั่วไปสำหรับโรคผื่นแพ้อักเสบ',
                        data='action=moreDetailTreat&state=eczema&subState=prod'
                    )
                ]
            )

        ]
    return {'carousel': content, 'alt': "ดูรายละเอียดการรักษา"}


def moreDetailTreatReason(i):
    if i == 'eczema':
        content = "สาเหตุที่ทำให้เกิดโรคผื่นแพ้อักเสบนั้น แบ่งออกเป็น 2 สาเหตุหลัก ๆ ดังนี้ \n\n1. สาเหตุภายนอกร่างกาย เช่น การสัมผัสสารระคายเคือง หรือ การแพ้สารต่างๆ โรคภูมิแพ้ หรือ อื่นๆ เช่น แมลงกัดแล้วแพ้ \n\n2. สาเหตุภายในร่างกาย มีได้หลายชนิด และมีลักษณะจำเพาะที่แตกต่างกันไป ซึ่งเกิดจากโรคต่าง ๆ ดังนี้ Atopic dermatitis ,Seborrheic dermatitis ,Nummular eczema , Dyshidrosis ,Stasis dermatitis ,Lichen simplexchronicus\n\nอ่านเพิ่มเติมที่: https://www.clinicneo.com/eczema/"
    return {"message": content}


def moreDetailTreatSelf(i):
    if i == 'eczema':
        content = "การดูแลตัวเองสำหรับโรคผื่นแพ้อักเสบ\n\nการดูแลตัวเองของโรคในกลุ่มนี้จะมุ่งเน้นไปที่การป้องกันและบรรเทาอาการคันให้ลดน้อยลง เนื่องจากภาวะผื่นแพ้อักเสบนั้นจะส่งผลให้ผิวแห้งและคัน โดยการดูแลตัวเองนั้นจะเป็นในลักษณะดังต่อไปนี้\n\n- หลีกเลี่ยงการถูหรือเกาบริเวณผื่นและผิวหนังที่มีอาการคัน\n- สวมใส่เสื้อผ้าที่ทำจากผ้าฝ้าย\n- เลือกใช้ผลิตภัณฑ์ซักผ้าที่อ่อนโยน\n- เพิ่มความชุ่มชื้นให้กับผิวเป็นประจำด้วยมอยซ์เจอร์ไรเซอร์\n- หลีกเลี่ยงสารก่อภูมิแพ้\n- ลดความเครียด\n\nอ่านเพิ่มเติมที่: https://www.clinicneo.com/eczema/"
    return {"message": content}


def moreDetailMed(i):
    if i == 'eczema':
        content = "การใช้ยารักษาโรคผื่นแพ้อักเสบ\n\nกลุ่มยาทาหรือครีมทารักษาโรคผื่นแพ้อักเสบ\n- ยาทากลุ่มคอร์ติโคสเตียรอยด์ (Corticosteroids)\n- ยาทาชนิดกดภูมิคุ้มกันของร่างกาย (Calcineurin Inhibitor)\n- ครีมทามอยซ์เจอร์ไรเซอร์ชนิดเข้มข้น\n- กลุ่มน้ำมันทาผิว\n\nกลุ่มยารับประทานรักษาโรคผื่นแพ้อักเสบ\n- ยาแก้แพ้\n- ยารับประทานกลุ่มคอร์ติโคสเตียรอยด์ (Corticosteroids)\n- ยาฆ่าเชื้อ\n\nอ่านเพิ่มเติมที่: https://www.clinicneo.com/eczema/"
    return {"message": content}


def moreDetailProd(i):
    if i == 'eczema':
        content = columns = [
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/SVDF0vn/1.png',
                title='Betamethasone Dipropionate 0.05%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Betamethasone ',
                         data='action=medDetail&state=betamethasone'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/wNQTgbg/2.jpg',
                title='Clobetasol Propionate 0.05%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Clobetasol',
                         data='action=medDetail&state=clobetasol'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/SxNvS2X/3.jpg',
                title='Topicorte Desoximetasone 0.25%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Topicorte',
                         data='action=medDetail&state=topicorte'
                     )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.ibb.co/BjDLqfX/4.jpg',
                title='Hydrocortisone Cream 1%',
                text='กดเพื่อดูข้อมูลเพิ่มเติม',
                actions=[
                     PostbackAction(
                         label='ดูรายละเอียดเพิ่มเติม',
                         display_text='ดูเพิ่มเติม Hydrocortisone',
                         data='action=medDetail&state=hydrocortisone'
                     )
                ]
            )

        ]
    return {"carousel": content, 'alt': "ข้อมูลยาต่างๆ"}

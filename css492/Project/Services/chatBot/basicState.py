from Project.Services.chatBot import templateMessage
from pythainlp.tokenize import word_tokenize
from Project.Services.ImageClassifly import predict
def basicEventHandler(**kwargs):

    # doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    # event_collection = mongo.db.events
    # if kwargs['subState'] == 'done' or kwargs['subState'] == 'none':
    #     return False, {'message': "Done"},"done"
    msg = kwargs['message']['message']
    msg = word_tokenize(msg)
    print(kwargs)
    for x in ['ครับ', 'ค่ะ', 'ค่า', 'คะ', 'คับ', 'คร้าบ', 'ฮ่ะ', 'อ่ะ', 'อ่า', 'ป้ะ', 'ป่ะ', 'บ่', 'แมะ', 'มะ', 'ก๊า', 'ไหม', 'มั้ย', 'หน่อย']:
        try:
            msg.remove(x)
            break
        except :
            continue
    msg = ''.join(msg)
    if msg == 'สวัดดี' or msg == 'ช่วยเหลือ' or msg == 'สวัสดี' :   #command for first time
        firstMessage,secondMessage = templateMessage.welcomMessage()
        return {'group': [{'message':secondMessage},{'flex':firstMessage,"alt":"skin detail"}]}
    elif msg == 'เริ่มการวินิฉัย':
        return {"message":"กรุณาเลือกรูปภาพหรือถ่ายภาพส่งมาที่แชทเพื่อให้ผมวินิจฉัยได้เลยครับ (ส่งได้ครั้งละ 1 รูป)😉"}
    elif msg == 'test':
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
                  "text": "Brown Cafe",
                  "weight": "bold",
                  "size": "xl"
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "margin": "md",
                  "contents": [
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                    },
                    {
                      "type": "icon",
                      "size": "sm",
                      "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                    },
                    {
                      "type": "text",
                      "text": "4.0",
                      "size": "sm",
                      "color": "#999999",
                      "margin": "md",
                      "flex": 0
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "lg",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Place",
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1
                        },
                        {
                          "type": "text",
                          "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                          "wrap": True,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5
                        }
                      ]
                    },
                    {
                      "type": "box",
                      "layout": "baseline",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Time",
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1
                        },
                        {
                          "type": "text",
                          "text": "10:00 - 23:00",
                          "wrap": True,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5
                        }
                      ]
                    }
                  ]
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
                    "label": "CALL",
                    "uri": "https://linecorp.com"
                  }
                },
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "uri",
                    "label": "WEBSITE",
                    "uri": "https://linecorp.com"
                  }
                }
              ],
              "flex": 0
            }
          }
        return {'flex':content,'alt':"sss"}
    # elif msg == '1':
    #     a = [1,2,3]
    #     return templateMessage.listPredictImg(a)
    elif msg =='ใช่':
        return {"message": "รอแปป"}




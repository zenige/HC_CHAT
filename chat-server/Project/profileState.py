


import json

def preFlexProfile(state):
    if state == 'real_name':
          return createFlexProfile(state)
    elif state == 'last_name':
        return createFlexProfile(state)
    elif state == 'birthday':
        return createBirthdayFlex()
    elif state == 'phone':
        return createFlexProfile(state)
    
        





def createFlexProfile(state):
  text = ''
  if state == 'real_name':
    text = 'กรุณาพิมพ์ชื่อจริงของท่าน'
  elif state == 'last_name':
    text = 'กรุณาพิมพ์นามสกุลของท่าน'
  elif state == 'birthday':
    text = 'กรุณาพิมพ์วันเกิดของท่าน'
  elif state == 'phone':
    text = 'กรุณาพิมพ์เบอร์มือถือของท่าน'
  context = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": text,
            "wrap": True
          }
        ]
      }
    }
  return context

def createBirthdayFlex():
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
          "data": "action=%=true//subState=%=birthday",
          "mode": "date"
        }
      }
    ]
  }
}
    return content

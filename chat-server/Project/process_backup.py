from linebot.models import actions
from starlette import responses
from Project import db
from Project.extensions import getAnswer,predict
import json
from pythainlp.tokenize import word_tokenize
from Project.profileState import profileStateHandler

def stateHandler(**kwargs):
    doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    doc = doc_ref.get()
    user_define = doc.to_dict()


    #customer_define = customer_collection.find_one({'$and':[{"userID": kwargs['sender_id']},{"botID": ObjectId(kwargs['botID'])}]})
    res = {"message": "เกิดข้อผิดพลาดโปรดลองใหม่หรือทำกระบวนการที่ทำอยู่ให้เสร็จก่อนครับ"}

    if 'message' in kwargs.keys():
        # if customer_define['subState'] == "name":
        #     return {"flex":json.loads(confirm_flexmessage(kwargs['message']['message'])),"alt":"ยืนยันชื่อ-นามสกุล"}
        # elif customer_define['subState'] == "address":
        #     return {"flex":json.loads(address_flex(kwargs['message']['message'])),"alt":"ยืนยันที่อยู่"}
        # elif customer_define['subState'] == "tel":
        #     return {"flex":json.loads(tel_flexmessage(kwargs['message']['message'])),"alt":"ยืนยันเบอร์โทร"}
        if user_define['mainState'] == "none":
          #  or user_define['mainState'] == "Done" 
            # msg_token = word_tokenize(kwargs['message'])
            ans = ''
            flag = True
            flag, ans,subState = basicEventHandler(message = kwargs['message'],subState = user_define['subState'],sender_id = kwargs['sender_id'])
            if not flag:
                # data = kwargs['message'],kwargs['confident'],kwargs['sender_id']
                response = getAnswer(
                    kwargs['message'], kwargs['confident'], kwargs['sender_id'])
                res = json.loads(response.text)
            if flag:
                doc_ref.update({"subState": subState})
                return ans
        # elif user_define['subState'] == "name":
        #     print("D")
        else:
            
            flag, ans,subState = basicEventHandler(message = kwargs['message'],subState = user_define['subState'],sender_id = kwargs['sender_id'])
            if flag:
                doc_ref.update({"subState": subState})
                return ans
    elif 'postback' in kwargs.keys():

        res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'])

        #res = process_message(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res



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
          return True, {'flex': event,'alt':seq['Question']},seq['id']
        else :
          event = profileStateHandler(state="real_name")
          return True, {'flex': event,'alt':"กรุณากรอกชื่อจริงของท่าน"},"real_name"
    elif kwargs['message']['message'] == 'ยกเลิก': #command for cancel
        return True, {'message':"ยกเลิกการทำงาน"},'none'
    else :
        if kwargs['subState'] == 'none' or kwargs['subState'] == 'Done':    
          return False,"not found word","Err"
        else : 
          isnum = False
          if kwargs['message']['message'].isnumeric():
              isnum = True
          seq = handleSequence(kwargs['subState'],True) #finding next question
          if isnum == False:
              return False,{'message': "กรุณากรอกเป็นตัวเลขเท่านั้น"},"Err"
          if seq != None and seq != 'Done' :  #has next question
            event = createFlex(seq)
            query = findAndUpdate(doc_ref.get(),kwargs['subState'],kwargs['message']['message'])
            # doc = doc_ref.get()
            # doc = doc.to_dict()
            # if doc:
            #     if doc['symptom']:

            # else:
            #     print(u'No such document!')
            doc_ref.update(query)
            return True, {'flex': event,'alt':seq['Question']},seq['id']
          elif seq == 'Done' : #done all 
            return True, {'message': "Done"},"done"
          elif seq == None: #not in command
            return False,"not found word","Err"

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

def findAndUpdate(doc,subState,msg):
    doc = doc.to_dict()
    if doc['symptom']:

          doc['symptom'][subState] = msg
          return doc

    else:
        return {"symptom":{subState:msg}}
    


def handleSequence(subState = 'none',next = False):
    seqs = getSequence() # get logic from db
    res = {}
    for seq in seqs:

      if seq['id'] == subState and subState != 'none': #check current subState
        res = seq
        break
      elif subState == 'none': 
        res = seq
        break
    if subState != 'none': #if current subState not None
      # if res['Type'] == "input" or res['Type'] == "boolean" : 

      if res['Type'] == "input" or res['Type'] == "boolean" : 
        if next == True: # Has next Question ?
          flag = False
          for seq in seqs: # get next question
            if res['Next'] == seq['id']:
              res = seq 
              flag = True
              break
          if flag == False: # has no next question
              res = "Done"

      else :  # check if type not input not accept respons
        res = None
    return res




def getSequence():
    sequenceLogics =  db.collection(u'lineLogic').stream()
    newList = []
    for seq in sequenceLogics:
      newList.append(seq.to_dict())
    return newList



def createFlex(seq):
    context = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": seq['Question'],
            "wrap": True
          }
        ]
      }
    }
    if seq['Type'] == 'boolean':
        context['footer'] = {

        "type": "box",
        "layout": "vertical",
        "contents": [
          {
        "type": "button",
        "style": "primary",
        "height": "sm",
            "action": {
          "type": "postback",
          "label": "ใช่",
          "data": "action=%=true//subState=%="+seq['id'],
        "displayText": "เป็น"
        }
      },
                {
        "type": "button",
        "style": "primary",
        "height": "sm",
            "action": {
          "type": "postback",
          "label": "ไม่ใช่",
          "data": "action=%=false//subState=%="+seq['id'],
        "displayText": "ไม่เป็น"
        }
      },
        ]
      }

    return context

def commandsHandler(**kwargs):
  print("in comand")
  commands = kwargs['commands']['postback'].split("//")
  actions = commands[0].split("=%=")
  subState = commands[1].split("=%=")
  if subState[1]:
    print("in in comand")
    doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    query = findAndUpdate(doc_ref.get(),subState[1],actions[1])
    doc_ref.update(query)
    seq = handleSequence(subState[1],True)
    print(seq)
    if seq != 'Done':
      event = createFlex(seq)
      doc_ref.update({'subState': seq['id']})
      return {'flex': event,'alt':seq['Question']}
    else:
      pred = predict()
      res = json.loads(pred.text)
      doc_ref.update({'subState': "Done"})
      return {'message': res}



    





from Project.profileState import preFlexProfile
from Project import db

def subStateProfileHandler(user_define,doc_ref,msg):
    print('user_define',user_define)
    if user_define['subState'] == 'real_name':
        if isnumberic(msg) :
            return {"message":"กรุณากรอกเป็นตัวอักษรเท่านั้น"}
        else :
            query = findAndUpdateProfile(doc_ref,'real_name',msg)
            query['subState'] = 'last_name'
            doc_ref.update(query)
            # doc_ref.update({'subState':"last_name","profile": {'real_name' : msg}})
            res = preFlexProfile(state="last_name")
            return {"flex":res,"alt":"ยืนยันที่อยู่"}
    elif user_define['subState'] == 'last_name':
        if isnumberic(msg) :
            return {"message":"กรุณากรอกเป็นตัวอักษรเท่านั้น"}
        else :
            query = findAndUpdateProfile(doc_ref,'last_name',msg)
            query['subState'] = 'phone'
            doc_ref.update(query)
            # doc_ref.update({'subState':"birthday","profile": {'last_name' : msg}})
            res = preFlexProfile(state="phone")
            return {"flex":res,"alt":"ยืนยันที่อยู่"}
    elif user_define['subState'] == 'phone':
        if isnumberic(msg) :
            query = findAndUpdateProfile(doc_ref,'phone',msg)
            query['subState'] = 'birthday'
            doc_ref.update(query)
            # doc_ref.update({'subState':"birthday","profile": {'last_name' : msg}})
            res = preFlexProfile(state="birthday")
            return {"flex":res,"alt":"ยืนยันที่อยู่"}
        else :
            return {"message":"กรุณากรอกเป็นตัวเลขเท่านั้น"}
    elif user_define['subState'] == 'birthday':
        print("IS HERE")
        query = findAndUpdateProfile(doc_ref,'birthday',msg)
        query['subState'] = 'none'
        query['isProfileComplete'] =True
        query['mainState'] = 'none'
        user_define['mainState'] = 'covid'
        user_define['subState'] = 'none'
        doc_ref.update(query)
        # res = subStateCovidHandler(user_define,msg,doc_ref)
        # doc_ref.update({'subState':"done",'isProfileComplete':True,"profile": {'birthday' : msg}})
        # res = profileStateHandler(state="last_name")
        return {'message':"อัพเดทโปรไฟล์เสร็จสิ้น กรุณาพิมพ์ หาหมอครับ อีกครั้ง"}
    return 0

def subStateCovidHandler(user_define,msg,doc_ref):

    seq = getCurrentSeq(subState = user_define['subState'])
    print('seq',seq)
    flag,event = checkTypeSeq(seq,msg)
    print('flag',flag)
    print('event',event)
    if flag:
        doc_ref.update({"symptom":{seq['id']:msg}})
        seq = getNextSeq(subState = user_define['subState'])
        event = createFlex(seq)
        return {'flex': event,'alt':seq['Question']}
    return event


# def findAndUpdateProfile(doc_ref,subState,msg):
#     docs = doc_ref.get()
#     doc = docs.to_dict()
#     if doc['profile']:

#           doc['profile'][subState] = msg
#           doc_ref.update(doc)
#           return doc

#     else:
#         return doc_ref.update({'subState':"last_name","profile": {'real_name' : msg}})



def findAndUpdateProfile(doc_ref,subState,msg):
    docs = doc_ref.get()
    doc = docs.to_dict()
    if doc['profile']:

          doc['profile'][subState] = msg
          return doc

    else:
        return {"profile":{subState:msg}}
    

def getNextSeq(subState = 'none'):
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
        if res['Next']: # Has next Question ?
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



def getCurrentSeq(subState = 'none'):
    seqs = getSequence() # get logic from db
    res = {}
    for seq in seqs:

        if seq['id'] == subState and subState != 'none': #check current subState
            res = seq
            break
        elif subState == 'none': 

            res = seq
            print("???",res)
            break
    return res

def isnumberic(msg):
    if msg.isnumeric():
        return True
    else:
        return False

def checkTypeSeq(seq,msg):
    if seq['Type'] == 'input' and msg.isnumeric():
        return True,{}
    elif seq['Type'] == 'boolean' :
        return False,{"message": "กรุณากดปุ่มที่แสดงบนจอของท่าน"}
    elif seq['Type'] == 'input':
        return True,{}
    return False,{"message": "กรุณากรอกเป็นตัวเลขเท่านั้น"}


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
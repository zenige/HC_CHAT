from Project import db
from Project.subState import subStateProfileHandler,subStateCovidHandler
import json
from Project.extensions import getAnswer,predict
from Project.extensions import getAnswer
from Project.helper import handleSequence,getSequence,createFlex
def stateHandler(**kwargs):
    doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    doc = doc_ref.get()
    user_define = doc.to_dict()


    #customer_define = customer_collection.find_one({'$and':[{"userID": kwargs['sender_id']},{"botID": ObjectId(kwargs['botID'])}]})
    res = {"message": "เกิดข้อผิดพลาดโปรดลองใหม่หรือทำกระบวนการที่ทำอยู่ให้เสร็จก่อนครับ"}

    if 'message' in kwargs.keys():
        if user_define['mainState'] == "profile":
            res = subStateProfileHandler(user_define = user_define , doc_ref= doc_ref,msg = kwargs['message']['message'])
            return res
        elif user_define['mainState'] == "covid":
            res = subStateCovidHandler(user_define = user_define,msg = kwargs['message']['message'] , doc_ref= doc_ref)
            return res
        elif user_define['mainState'] == "none" or user_define['mainState'] == "" :
          #  or user_define['mainState'] == "Done" 
            # msg_token = word_tokenize(kwargs['message'])

            # ans = ''
            # flag = True
            # flag, ans,subState = basicEventHandler(message = kwargs['message'],subState = user_define['subState'],sender_id = kwargs['sender_id'])
            # if not flag:
                # data = kwargs['message'],kwargs['confident'],kwargs['sender_id']
            response = getAnswer(
                kwargs['message'], kwargs['confident'], kwargs['sender_id'])
            res = json.loads(response.text)


            # if flag:
            #     doc_ref.update({"subState": subState})
            #     return ans

        # else:
            
        #     flag, ans,subState = basicEventHandler(message = kwargs['message'],subState = user_define['subState'],sender_id = kwargs['sender_id'])
        #     if flag:
        #         doc_ref.update({"subState": subState})
        #         return ans
    elif 'postback' in kwargs.keys():
        if 'params' in kwargs.keys():
            res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'] ,params = kwargs['params'] ,user_define=user_define)
        else :
             res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id']  ,user_define=user_define)
        #res = process_message(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res


def basicEventHandler(**kwargs):
    doc_ref = db.collection(u'users').document(kwargs['sender_id'])

    if kwargs['message']['message'] == 'หาหมอครับ':   #command for first time
        return True
        # isProfileComplete = checkProfile(doc_ref)
        # if isProfileComplete :
        #   seq = handleSequence()
        #   event = createFlex(seq)
        #   return True, {'flex': event,'alt':seq['Question']},seq['id']
        # else :
        #   event = profileStateHandler(state="real_name")
        #   return True, {'flex': event,'alt':"กรุณากรอกชื่อจริงของท่าน"},"real_name"
    elif kwargs['message']['message'] == 'ยกเลิก': #command for cancel
        # return True, {'message':"ยกเลิกการทำงาน"},'none'
        return True
        
    else :
        return False
        # if kwargs['subState'] == 'none' or kwargs['subState'] == 'Done':    
        #   return False,"not found word","Err"
        # else : 
        #   isnum = False
        #   if kwargs['message']['message'].isnumeric():
        #       isnum = True
        #   seq = handleSequence(kwargs['subState'],True) #finding next question
        #   if isnum == False:
        #       return False,{'message': "กรุณากรอกเป็นตัวเลขเท่านั้น"},"Err"
        #   if seq != None and seq != 'Done' :  #has next question
        #     event = createFlex(seq)
        #     query = findAndUpdate(doc_ref.get(),kwargs['subState'],kwargs['message']['message'])
        #     doc_ref.update(query)
        #     return True, {'flex': event,'alt':seq['Question']},seq['id']
        #   elif seq == 'Done' : #done all 
        #     return True, {'message': "Done"},"done"
        #   elif seq == None: #not in command
        #     return False,"not found word","Err"

def commandsHandler(**kwargs):

    # doc_ref = db.collection(u'users').document(kwargs['sender_id'])
    # doc = doc_ref.get()
    # user_define = doc.to_dict()
    commands = kwargs['commands']['postback'].split("//")
    actions = commands[0].split("=%=")
    subState = commands[1].split("=%=")
    if subState[1]:
        print("in in comand",subState[1])
        doc_ref = db.collection(u'users').document(kwargs['sender_id'])

        if subState[1] == 'birthday':
            query = findAndUpdateProfile(doc_ref.get(),subState[1],kwargs['params']['date'])
            doc_ref.update(query)
            res = subStateProfileHandler(user_define= kwargs['user_define'],doc_ref = doc_ref,msg = kwargs['params']['date'])
            print('res',res)
            return res
        else:
            query = findAndUpdate(doc_ref.get(),subState[1],actions[1])
            seq = handleSequence(subState[1],True)
            doc_ref.update(query)


        if seq != 'Done':
            event = createFlex(seq)
            doc_ref.update({'subState': seq['id']})
            return {'flex': event,'alt':seq['Question']}
        else:
            doc_ref.update({'subState': 'none','mainState':'none'})
            obj = {"userId":kwargs['sender_id']}
            pred = predict(obj)
            res = json.loads(pred.text)
            doc_ref.update({'subState': "Done",'group': res})
            return {'message': "คุณอยู่ Group ความเสี่ยงที่ : "+res}


def findAndUpdate(doc,subState,msg):
    doc = doc.to_dict()
    if doc['symptom']:

          doc['symptom'][subState] = msg
          return doc

    else:
        return {"symptom":{subState:msg}}



def findAndUpdateProfile(doc,subState,msg):

    doc = doc.to_dict()
    if doc['profile']:

          doc['profile'][subState] = msg
          return doc

    else:
        return {"profile":{subState:msg}}
    
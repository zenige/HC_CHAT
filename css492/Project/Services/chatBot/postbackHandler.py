from Project.Services.chatBot import templateMessage
from datetime import datetime
from Project.Services.ImageClassifly import predict
def stateHandler(**kwargs):
   
    print("kwargs",kwargs)

    #customer_define = customer_collection.find_one({'$and':[{"userID": kwargs['sender_id']},{"botID": ObjectId(kwargs['botID'])}]})
    res = {"message": "เกิดข้อผิดพลาดโปรดลองใหม่หรือทำกระบวนการที่ทำอยู่ให้เสร็จก่อนครับ"}
    if 'postback' in kwargs.keys():
        commands = kwargs['postback']['postback'].split("&")
        action = commands[0].split("=")
        state = commands[1].split("=")
        if(action[1] == 'start'):
            if(state[1] == 'start'):
                return {"message":"กรุณาเลือกรูปภาพหรือถ่ายภาพส่งมาที่แชทเพื่อให้ผมวินิจฉัยได้เลยครับ (ส่งได้ครั้งละ 1 รูป)"}
        elif(action[1] == 'seeMore'):
            if(state[1] == 'seeMore'):
                return templateMessage.seeMoreMessage()
            if(state[1] == 'eczema'):
                return templateMessage.seeMoreEczema()
    # if 'message' in kwargs.keys():
    #     if user_define['mainState'] == "profile":
    #         res = subStateProfileHandler(user_define = user_define , doc_ref= doc_ref,msg = kwargs['message']['message'])
    #         return res
    #     elif user_define['mainState'] == "covid":
    #         res = subStateCovidHandler(user_define = user_define,msg = kwargs['message']['message'] , doc_ref= doc_ref)
    #         return res
    #     elif user_define['mainState'] == "none" or user_define['mainState'] == "" :
    #       #  or user_define['mainState'] == "Done" 
    #         # msg_token = word_tokenize(kwargs['message'])

    #         # ans = ''
    #         # flag = True
    #         # flag, ans,subState = basicEventHandler(message = kwargs['message'],subState = user_define['subState'],sender_id = kwargs['sender_id'])
    #         # if not flag:
    #             # data = kwargs['message'],kwargs['confident'],kwargs['sender_id']
    #         response = getAnswer(
    #             kwargs['message'], kwargs['confident'], kwargs['sender_id'])
    #         res = json.loads(response.text)


    #         # if flag:
    #         #     doc_ref.update({"subState": subState})
    #         #     return ans

    #     # else:
            
    #     #     flag, ans,subState = basicEventHandler(message = kwargs['message'],subState = user_define['subState'],sender_id = kwargs['sender_id'])
    #     #     if flag:
    #     #         doc_ref.update({"subState": subState})
    #     #         return ans
    # if 'postback' in kwargs.keys():
    #     if 'params' in kwargs.keys():
    #         res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'] ,params = kwargs['params'] ,user_define=user_define)
    #     else :
    #          res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id']  ,user_define=user_define)
        #res = process_message(kwargs['message'],kwargs['confident'],kwargs['sender_id'])
    if 'image' in kwargs.keys():
        now = datetime.now()
        message_content = kwargs['line_bot_api'].get_message_content(kwargs['image']['imageId'])
        print(message_content)
        with open("./static/img/"+kwargs['sender_id']+'&&'+str(now)+".jpg", 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        res = predict.predictImage()
       
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res


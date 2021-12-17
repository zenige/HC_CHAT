from Project.Services.chatBot import templateMessage,chatService
from datetime import datetime
from Project.Services.ImageClassifly import predict

import webbrowser
def stateHandler(**kwargs):
    # if kwargs['postback']['postback'] == 'a':
    #     # return webbrowser.open('https://liff.line.me/1655993001-QLqyKnVe')
    #     print("SSSS")
    print("kwargs",kwargs)

    #customer_define = customer_collection.find_one({'$and':[{"userID": kwargs['sender_id']},{"botID": ObjectId(kwargs['botID'])}]})
    res = {"message": "เกิดข้อผิดพลาดโปรดลองใหม่หรือทำกระบวนการที่ทำอยู่ให้เสร็จก่อนครับ"}
    if 'postback' in kwargs.keys():
        commands = kwargs['postback']['postback'].split("&")
        action = commands[0].split("=")
        state = commands[1].split("=")
        print(action)
        if(action[1] == 'start'):
            if(state[1] == 'start'):
                return {"message":"กรุณาเลือกรูปภาพหรือถ่ายภาพส่งมาที่แชทเพื่อให้ผมวินิจฉัยได้เลยครับ (ส่งได้ครั้งละ 1 รูป)"}
        elif(action[1] == 'seeMore'):
            if(state[1] == 'seeMore'):
                return templateMessage.seeMoreMessage()
            if(state[1] == 'eczema'):
                return templateMessage.seeMoreEczema()
        elif(action[1] == 'moreDetail'):
            return templateMessage.moreDetailTreatment(state[1])
        elif(action[1] == 'moreDetailTreat'):
            substate = commands[2].split("=")
            if state[1] =='eczema':
                if substate[1] =='reason':
                    return templateMessage.moreDetailTreatReason(state[1])
                elif substate[1] == 'treatSelf':
                    return templateMessage.moreDetailTreatSelf(state[1])
                elif substate[1] == 'med':
                    return templateMessage.moreDetailMed(state[1])
                elif substate[1] == 'prod':
                    return templateMessage.moreDetailProd(state[1])
        elif(action[1] == 'medDetail'):
            return chatService.medHandler(state[1])
        # elif(action[1] == 'startDoc'):
        #     return 
            


    if 'image' in kwargs.keys():
        now = datetime.now()
        message_content = kwargs['line_bot_api'].get_message_content(kwargs['image']['imageId'])
        print(message_content)
        with open("./static/img/"+kwargs['sender_id']+'&&'+str(now)+".jpg", 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        res = predict.predictImage("./static/img/"+kwargs['sender_id']+'&&'+str(now)+".jpg",kwargs['sender_id'])
       
    # elif 'postback' in kwargs.keys():
    #     res = commandsHandler(commands = kwargs['postback'], sender_id = kwargs['sender_id'], botID=kwargs['botID'])
    return res


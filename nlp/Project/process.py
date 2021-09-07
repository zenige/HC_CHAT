
from pythainlp.tokenize import word_tokenize
from Project import db
from Project.nlp import sentence_get_confident
import datetime
def process_message(message,min_conf,sender_id,platform="line"):
    # training_collection = mongo.db.training
    # trained_collection = mongo.db.trained

    #msg_token = word_tokenize(message['message'])
    max = 0
    ans = ''
    flag = False
    # flag,ans = basicEventHandler(msg_token,botID,sender_id,platform)
    if not flag:
        similar_trained_word = getTrainedInfo()
        print(similar_trained_word)
        #similar_trained_word = trained_collection.find({'botID': ObjectId(botID)})
        for word in similar_trained_word:
            print("_____")
            print(message)
            print(word['question'])
            print("_____")
            conf = float("{:.2f}".format(sentence_get_confident(message,word['question'])))
            print(conf)
            if conf == False and type(conf) == bool:
                flag = False
                max = -1
                break
            elif conf == 1.0:
                max = conf
                ans = {"message":word['answer']}
                flag = False
                break
            elif conf > max:
                max = conf
                ans = {"message":word['answer']}
        if max < 0:
            ans = {"message":"ขอโทษครับ ผมพูดได้แค่ภาษาไทย"}
        elif (max < min_conf):
            ans = {"message":"ขอโทษครับ ผมยังไม่เข้าใจคำนี้ครับกำลังศึกษาอยู่"}
        similar_training_word = getTrainingInfo(message['message'])
        print(similar_training_word)
        #similar_training_word = training_collection.find_one({'question':message['message'],'botID': ObjectId(botID)})
        if similar_training_word == None and max != 1 :
            obj = {"question":message['message'],"answer":ans["message"], 'confident': max,"time": datetime.datetime.timestamp(datetime.datetime.now())}
            db.collection(u'training').document().set(obj)
        #ans = objectReader(ans["message"],botID)
    return ans


def getTrainedInfo():
    docs = db.collection(u'trained').stream()
    arr = []
    for doc in docs:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        arr.append(train_dict)
        
    return arr

def getTrainingInfo(message):
    docs = db.collection(u'training').where(u'question', u'==', message).stream()
    arr = []
    flag = False
    for doc in docs:
        flag = True
        train_dict = doc.to_dict()
        arr.append(train_dict)
        return arr
    if not flag:
        return None
    # arr = []
    # for doc in docs:
    #     train_dict = doc.to_dict()
    #     train_dict['id'] = doc.id
    #     arr.append(train_dict)
    #     return arr

# def objectReader(ss,botID):
#     s = word_tokenize(ss)
#     if s[0] == "<<":
#         if s[-1] == ">>":
#             key = ss.replace(">","").replace("<","")
#             groups_collection = mongo.db.groups 
#             object_define = groups_collection.find_one({'$and':[{'botID':ObjectId(botID)},{'name':key}]})
#             return {"group":object_define['message']}
#     return {"message":ss}
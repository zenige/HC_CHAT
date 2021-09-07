from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime


class TrainedModel(BaseModel):
    question: str
    answer: str


router = APIRouter()


@router.get("/trained/count")
async def getTrainedWord():
    docs = db.collection(u'trained').stream()

    count = 0
    for doc in docs:
        count = count+1
    return count




@router.get("/trained")
async def getTrainedWord(pages: Optional[int] = None,limit: Optional[int] = 0):
    print(limit)
    docs_ref = db.collection(u'trained')
    if pages == None:
        docs = docs_ref.order_by("question").stream()
        query = streamToDict(docs)
        return query
    elif pages != None:
        first_query = docs_ref.order_by("question").limit(limit)
        docs = first_query.stream()
        # test = streamToDict(docs)
        # print(test)
        # print("____")

        if pages == 1 :
            query = streamToDict(docs)
            return query
        elif pages > 1 :
            for page in range(pages-1):
    
                last_doc = list(docs)[-1]

                last_pop = last_doc.to_dict()[u'question']

                next_query = (
                    docs_ref
                    .order_by(u'question')
                    .start_after({
                        u'question': last_pop
                    })
                    .limit(limit)
                )
                docs = next_query.stream()
                # results = docs.get()
                # print(results)
            query = streamToDict(docs)
            return query


def streamToDict(stream):
    obj = []
    for doc in stream:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        obj.append(train_dict)
    return obj

@router.post("/trained")
async def createTrainWord(data: TrainedModel):
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    obj = {"question": data['question'], "answer": data['answer'],
           "time": datetime.datetime.timestamp(datetime.datetime.now())}
    db.collection(u'trained').document().set(obj)
    return "done"


@router.patch("/trained/{id}")
async def updateTrainWord(data: TrainedModel, id: str):
    print(id)
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    doc_ref = db.collection(u'trained').document(id)
    doc_ref.update({'question': data['question'], 'answer': data['answer']})
    return "PATCH"


@router.delete("/trained/{id}")
async def deleteTrainWord(id: str):
    db.collection(u'trained').document(id).delete()
    return "Delete Done"


@router.get("/training")
async def getTrainedWord():
    docs = db.collection(u'training').stream()
    obj = []
    for doc in docs:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        obj.append(train_dict)
    return obj

# @router.post("/training")
# async def createTrainWord(data: TrainedModel):
#     data = data.dict()
#     # Add a new doc in collection 'cities' with ID 'LA'
#     obj = {"question":data['answer'],"answer":data['question'],"time": datetime.datetime.timestamp(datetime.datetime.now())}
#     db.collection(u'training').document().set(obj)
#     return "done"


@router.patch("/training/{id}")
async def updateTrainWord(data: TrainedModel, id: str):
    print(id)
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    doc_ref = db.collection(u'training').document(id)
    doc_ref.update({'question': data['question'], 'answer': data['answer']})
    return "PATCH"


@router.delete("/training/{id}")
async def deleteTrainWord(id: str):
    db.collection(u'training').document(id).delete()
    return "Delete Done"

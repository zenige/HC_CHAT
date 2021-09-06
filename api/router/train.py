from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
class TrainedModel(BaseModel):
    question : str
    answer : str



router = APIRouter()
@router.get("/trained")
async def getTrainedWord():
    docs = db.collection(u'trained').stream()
    obj = []
    for doc in docs:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        obj.append(train_dict)
    return obj

@router.post("/trained")
async def createTrainWord(data: TrainedModel):
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    obj = {"question":data['answer'],"answer":data['question'],"time": datetime.datetime.timestamp(datetime.datetime.now())}
    db.collection(u'trained').document().set(obj)
    return "done"


@router.patch("/trained/{id}")
async def updateTrainWord(data: TrainedModel,id: str):
    print(id)
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    doc_ref = db.collection(u'trained').document(id)
    doc_ref.update({'question': data['question'],'answer':data['answer']})
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
async def updateTrainWord(data: TrainedModel,id: str):
    print(id)
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    doc_ref = db.collection(u'training').document(id)
    doc_ref.update({'question': data['question'],'answer':data['answer']})
    return "PATCH"

@router.delete("/training/{id}")
async def deleteTrainWord(id: str):
    db.collection(u'training').document(id).delete()
    return "Delete Done"
from fastapi import APIRouter,Request,Body
from Project import db
from typing import Dict
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union
from Project.process import process_message
import datetime
import json
import datetime

class trainInfo(BaseModel):
    message : dict
    confident : float
    sender_id : str

# JSONObject = Dict[AnyStr, Any]
# JSONArray = List[Any]
# JSONStructure = Union[JSONObject]

router = APIRouter()
@router.get("/")
async def test():
    docs = db.collection(u'trained').stream()
    obj = []
    for doc in docs:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        obj.append(train_dict)
    return obj

@router.post("/getconfident")
async def getConfident(data: trainInfo):
    print(data.message['message'])
    res = process_message(data.message,data.confident,data.sender_id)
    return res
    # docs = db.collection(u'trained').stream()
    # obj = []
    # for doc in docs:
    #     train_dict = doc.to_dict()
    #     train_dict['id'] = doc.id
    #     obj.append(train_dict)
    # return obj
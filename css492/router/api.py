from fastapi import APIRouter
from Project import db
# from Project.chat_process import save_message
import requests
from typing import Dict
from pydantic import BaseModel
from typing import Optional

import json
import datetime
from fastapi.responses import HTMLResponse

from Project.Services.chatBot import basicState, chatService

class updateState(BaseModel):
    userId:str
    state: str
    subState: str


router = APIRouter()

@router.get("/")
async def test():
    docs = db.collection(u'users').stream()
    obj = []
    for doc in docs:
        train_dict = doc.to_dict()
        obj.append(train_dict)
    return "obj"

@router.post("/updatestate")
async def test(data: updateState):
    print('in updateState')
    try:
        data = data.dict()
        print(data)
        doc_ref = db.collection(u'users').document(data['userId'])
        doc_ref.update({'mainState': data['state'], 'subState': data['subState']})
        res = "Update Successful"
    except:
        res = "Update Failed" 
    return res


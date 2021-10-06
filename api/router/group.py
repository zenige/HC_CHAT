from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
from model.Logic import Logic
from firebase_admin import firestore
router = APIRouter()


@router.get("/")
async def getTrainedWord():
    count = 0
    docs_ref = db.collection(u'logics').stream()
    groups =[]
    for doc in docs_ref:
        group = doc.to_dict()
        groups.append(group)
    return groups

def streamToList(docs):
    userGroup = []
    count = 0
    for doc in docs:
        count = count+1
        fakeDict = doc.to_dict()
        userGroup.append(fakeDict)
    return userGroup,count
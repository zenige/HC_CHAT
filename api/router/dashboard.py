
from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
router = APIRouter()
@router.get("/")
async def getUsers():
    docs = db.collection("users").stream()
    users = []
    for doc in docs:
        fakedict = doc.to_dict()
        fakedict['id'] = doc.id
        users.append(fakedict)
    print(users)
    # for i in users:
    #     if i['']
    return users

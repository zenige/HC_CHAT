from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

router = APIRouter()
@router.post("/")
async def createLogic(arbitrary_json: JSONStructure = None):
    docs = db.collection("logics").get()
    for doc in docs:
        doc.reference.delete()
    for arr in arbitrary_json:
        db.collection(u'logics').document().set(arr)
    return {"received_data": arbitrary_json}

@router.get("/")
async def getLogic():
    docs = db.collection("logics").get()
    arr = []
    for doc in docs:
        arr.append(doc.to_dict())
    return arr


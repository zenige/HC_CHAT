from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
from model.Logic import Logic
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



@router.get("/linelogic")
async def getLineLogic():
    docs = db.collection("pre-lineLogic").stream()
    logic = []
    for doc in docs:

        fakedict = doc.to_dict()
        logic.append(fakedict)
    print(logic)

    return logic


@router.post("/linelogic")
async def createLineLogic(data: Logic):

    docs = db.collection("pre-lineLogic").stream()
    logic = []
    for doc in docs:

        fakedict = doc.to_dict()
        logic.append(fakedict)

    for i in logic :
        if i['Next'] == None:
            lastLogic = i 
            break

    lastLogic['Next'] = data.id
    newLogic = dict(data)

    newLogic['Next'] = None
    newLogic['Previous'] = lastLogic['id']
    db.collection("pre-lineLogic").document(lastLogic['id']).set(lastLogic)
    db.collection("pre-lineLogic").document(newLogic['id']).set(newLogic)
    # print(newLogic)
    return newLogic


@router.delete("/linelogic")
async def deleteLineLogic(data: Logic):

    docs = db.collection("pre-lineLogic").stream()
    logic = []
    deleteLogic = {}
    previousLogic = {}
    nextLogic = {}
    for doc in docs:

        fakedict = doc.to_dict()
        logic.append(fakedict)

    for i in logic :
        if i['id'] == data.id:
            deleteLogic = i
            break
    for i in logic:
        if i['Next'] == deleteLogic['id']:
            previousLogic = i
            break
    for i in logic:
        if i['Previous'] == deleteLogic['id']:
            nextLogic = i
            break
    if nextLogic:
        previousLogic['Next'] = nextLogic['id']
        nextLogic['Previous'] = previousLogic['id']
        db.collection("pre-lineLogic").document(previousLogic['id']).set(previousLogic)
        db.collection("pre-lineLogic").document(nextLogic['id']).set(nextLogic)
    elif not previousLogic:
        return {"error" : "at least should have one logic left"}
    else :
        previousLogic['Next'] = None
        db.collection("pre-lineLogic").document(previousLogic['id']).set(previousLogic)
    db.collection(u'pre-lineLogic').document(data.id).delete()
 

    # lastLogic['Next'] = data.id
    # newLogic = dict(data)

    # newLogic['Next'] = None
    # newLogic['Previous'] = lastLogic['id']
    # db.collection("lineLogic").document(lastLogic['id']).set(lastLogic)
    # db.collection("lineLogic").document(newLogic['id']).set(newLogic)
    # print(newLogic)
    return "done"


@router.post("/linelogic/update")
async def updateLineLogic(data: Logic):

    docs = db.collection("pre-lineLogic").stream()
    logic = []
    for doc in docs:

        fakedict = doc.to_dict()
        logic.append(fakedict)
    
    for i in logic :
        if i['id'] == data.id:
            currentLogic = i 
            break
    if currentLogic:
        currentLogic['id'] = data.id
        currentLogic['Question'] = data.Question
        currentLogic['Type'] = data.Type
        db.collection("pre-lineLogic").document(currentLogic['id']).set(currentLogic)
        return 'done'
    else :
        return {"err": "no logic id"}


@router.get("/updateLogic")
async def updateDataBeforeTrain():
    docs = db.collection("pre-lineLogic").stream()
    logic = []
    for doc in docs:

        fakedict = doc.to_dict()
        logic.append(fakedict)
    for i in logic:
        db.collection("lineLogic").document(i['id']).set(i)
    return "ok"
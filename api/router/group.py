from fastapi import APIRouter
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
from model.Logic import Logic
from firebase_admin import firestore
from model.Feature import updateFeature,Feature
import ast
router = APIRouter()


@router.get("/")
async def getTrainedWord():
    count = 0
    docs_ref = db.collection(u'logics').stream()
    groups =[]
    for doc in docs_ref:
        group = doc.to_dict()

        group['id'] = doc.id
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

@router.patch("/")
async def UpdateGroupName(body:Feature):
    body = dict(body)
    docs = db.collection(u'logics').document(body['id']).get()
    # docs = db.collection(u'feature').document(body['id'])
    # docs.update({u'Name': body['Name']})
    # db.collection(u'feature').document(body['Name']).set(body)
    # feat = docs.to_dict()
    # print(feat)
    # new_key = body['Name']
    # old_key = feat['Name']
    # docs = db.collection("logics").document(old_key).get()

    # users = []


    features = []
    data =  docs.to_dict()
    dataStr = data['data']
    group = ast.literal_eval(dataStr)
    print(group)
    new_key = body['Name']
    old_key = group['group']

    group['group'] = new_key

    features.append(group)
    for feature in features:
        featureStr = str(feature)
        # print(featureStr)
        # print(feature['group'])
        # db.collection(u'logics').document(feature['group']).delete()
        db.collection(u'logics').document(feature['group']).set({"data":featureStr})
    db.collection(u'logics').document(old_key).delete()
    return "update done"


@router.delete("/{id}")
async def getUsers(id:str):

    # docs = db.collection(u'feature').document(body['id'])
    # docs.update({u'Name': body['Name']})
    # db.collection(u'feature').document(body['Name']).set(body)
    
    # new_key = body['Name']
    # old_key = body['old_Name']
    # docs = db.collection("logics").document(old_key).get()
    db.collection(u'logics').document(id).delete()
    # # users = []
    # features = []
    # data =  docs.to_dict()
    # dataStr = data['data']
    # group = ast.literal_eval(dataStr)

  
    # group['group'] = new_key

    # features.append(group)
    # for feature in features:
    #     featureStr = str(feature)
    #     # print(featureStr)
    #     # print(feature['group'])
    #     # db.collection(u'logics').document(feature['group']).delete()
    #     db.collection(u'logics').document(feature['group']).set({"data":featureStr})
    return "update done"


@router.post("/")
async def createGroupName(body:Feature):
    body = dict(body)
    strBody = "{group:"+body['Name']+"}"
    docs = db.collection(u'logics').document(body['Name']).set({"data":strBody})


    return "Create done"



@router.get("/orcondition")
async def createGroupName():
    docs_ref = db.collection(u'orCondition').stream()
    orCondition =[]
    for doc in docs_ref:
        group = doc.to_dict()
        group['id'] = doc.id
        orCondition.append(group)
    return orCondition


@router.post("/orcondition")
async def createGroupName(body:Dict):

    docs = db.collection(u'orCondition').document().set(body)
    return "done"

@router.patch("/orcondition")
async def createGroupName(body:Dict):

    docs = db.collection(u'orCondition').document(body['id']).set(body)
    return "done"

@router.delete("/orcondition/{id}")
async def createGroupName(id:str):

    db.collection(u'orCondition').document(id).delete()
    return "done"

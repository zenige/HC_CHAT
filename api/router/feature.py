
from fastapi import APIRouter
from starlette import responses
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
import ast
from model.Feature import Feature,updateFeature
router = APIRouter()


@router.get("/")
async def getUsers():

    docs = db.collection("feature").stream()
    # users = []
    features = []
    for doc in docs:
        feature = doc.to_dict()
        feature['id'] = doc.id

    #     fakedict = doc.to_dict()
    #     fakedict['id'] = doc.id
        features.append(feature)

    return features

@router.post("/")
async def getUsers(body:Feature):
    body = dict(body)
    docs = db.collection("feature").stream()
    for doc in docs:
        feat = doc.to_dict()
        if feat['Name'] == body['Name']:
            return "Duplicate Name"
    db.collection(u'feature').document().set({"Name":body['Name']})

    
    return "update done"

@router.patch("/")
async def getUsers(body:Feature):
    body = dict(body)
    docs = db.collection(u'feature').document(body['id']).get()

    # db.collection(u'feature').document(body['Name']).set(body)
    feat = docs.to_dict()
    print(feat)
    new_key = body['Name']
    old_key = feat['Name']
    docs = db.collection(u'feature').document(body['id'])
    docs.update({u'Name': body['Name']})
    docs = db.collection("logics").stream()
    # users = []
    features = []
    for doc in docs:
        data =  doc.to_dict()
        dataStr = data['data']
        group = ast.literal_eval(dataStr)

        flag = True
        if old_key in group.keys():
            group[new_key] = group.pop(old_key)
        #     del group[featName]
            flag = False
        if flag:
            if "Relation" in group.keys():
                for i in  group['Relation'][0]:
                    if i == old_key:
                        group['Relation'][0].remove(i)
                        group['Relation'][0].append(new_key)


        features.append(group)
    for feature in features:
        featureStr = str(feature)
        print(featureStr)
        print(feature['group'])
        # db.collection(u'logics').document(feature['group']).delete()
        db.collection(u'logics').document(feature['group']).set({"data":featureStr})
    return "update done"

@router.delete("/{id}/{featName}")
async def getUsers(id:str,featName:str):
    db.collection(u'feature').document(id).delete()
    docs = db.collection("logics").stream()
    # users = []
    features = []
    for doc in docs:
        data =  doc.to_dict()
        dataStr = data['data']
        group = ast.literal_eval(dataStr)
        flag = True
        if featName in group.keys():
            del group[featName]
            flag = False
        if flag:
            if "Relation" in group.keys():
                del group["Relation"]
        features.append(group)
    for feature in features:
        featureStr = str(feature)
        print(featureStr)
        print(feature['group'])
        # db.collection(u'logics').document(feature['group']).delete()
        db.collection(u'logics').document(feature['group']).set({"data":featureStr})
    # db.collection(u'feature').document(body['Name']).set(body)
    return "delete done"



@router.get("/getAllRawLogic")
async def getAllRawLogic():

    docs = db.collection("logics").stream()
    # users = []
    features = []
    for doc in docs:
        feature = doc.to_dict()
        feature['id'] = doc.id

    #     fakedict = doc.to_dict()
    #     fakedict['id'] = doc.id
        features.append(feature)

    return features
@router.get("/deleteLogicafterDeleteFeature")
def deleteLogicafterDeleteFeature():
    featName = "cough"
    docs = db.collection("logics").stream()
    # users = []
    features = []
    for doc in docs:
        data =  doc.to_dict()
        dataStr = data['data']
        group = ast.literal_eval(dataStr)
        flag = True
        if featName in group.keys():
            del group[featName]
            flag = False
        if flag:
            if "Relation" in group.keys():
                del group["Relation"]
        features.append(group)
        
    return features

@router.patch("/updateLogicAfterUpdateFeaTure")
def updateLogicAfterUpdateFeaTure():
    new_key = "getcough"
    old_key = "cough"
    docs = db.collection("logics").stream()
    # users = []
    features = []
    for doc in docs:
        data =  doc.to_dict()
        dataStr = data['data']
        group = ast.literal_eval(dataStr)

        flag = True
        if old_key in group.keys():
            group[new_key] = group.pop(old_key)
        #     del group[featName]
            flag = False
        if flag:
            if "Relation" in group.keys():
                for i in  group['Relation'][0]:
                    if i == old_key:
                        group['Relation'][0].remove(i)
                        group['Relation'][0].append(new_key)


        features.append(group)
        
    return features
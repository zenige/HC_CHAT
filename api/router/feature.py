
from fastapi import APIRouter
from starlette import responses
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
import ast
from model.Feature import Feature
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
    docs = db.collection(u'feature').document(body['id'])
    docs.update({u'Name': body['Name']})
    # db.collection(u'feature').document(body['Name']).set(body)
    return "update done"

@router.delete("/{id}")
async def getUsers(id:str):
    db.collection(u'feature').document(id).delete()
    # db.collection(u'feature').document(body['Name']).set(body)
    return "delete done"



@router.get("/dsadsadsadsa")
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

from fastapi import APIRouter
from starlette import responses
from Project import db
import requests
from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Any, Dict, AnyStr, List, Union
import ast
router = APIRouter()


class updateState(BaseModel):
    userId:str
    state: str
    subState: str

@router.get("/")
async def getUsers():
    docs = db.collection("users").stream()
    users = []
    
    for doc in docs:
        fakedict = doc.to_dict()
        fakedict['id'] = doc.id
        users.append(fakedict)
    groupName = defineGroupName()
    groups = []

    for i in groupName :
        group = {}
        count = 0
        for user in users:
            if user['group'] == i:
                group['name'] = i
                count = count+1
        group['total'] = count

        
        if "name" in group.keys():
            groups.append(group)

    # print(groups)
    # for i in users:
    #     if i['']
    return groups


def defineGroupName():
    docs = db.collection("logics").stream()
    datas = []
    data = {}
    answer = ''
    for doc in docs:
        data =  doc.to_dict()
        dataStr = data['data']
        dataDict = ast.literal_eval(dataStr)
        datas.append(dataDict)
    groupName = []
    for i in datas:

        if i['group'] not in groupName:
            groupName.append(i['group'])
    groupName.sort()
    return groupName



@router.get("/group")
async def getUsersByGroup(group: Optional[str] = None):
    docs = db.collection("users").where('group', '==', group).stream()
    group = []
    
    for doc in docs:
        group.append(doc.to_dict())


    return group

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

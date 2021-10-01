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


@router.get("/trained")
async def getTrainedWord(pages: Optional[int] = None,limit: Optional[int] = 0,group: Optional[str] = "all"):
    count = 0
    docs_ref = db.collection(u'users')
    docs = docs_ref.where("group", "!=", False).stream()
    users =[]
    for doc in docs:
        user = doc.to_dict()
        users.append(user)
    if pages == None:
        res = []
        for user in users :
            if user['group'] == group:
                res.append(user)
        return res
    elif pages != None:
        first_query = docs_ref.where("group", "!=", False).where("group", "==", group).order_by("group", direction=firestore.Query.DESCENDING).limit(limit)
       
        docs = first_query.stream()
        if pages == 1 :
            groupList,count = streamToList(docs)
            groupList.append({"total" : count})
            return groupList
        elif pages > 1 :
            for page in range(pages-1):

                last_doc = list(docs)[-1]

                last_pop = last_doc.to_dict()['userId']

                next_query = (
                    docs_ref
                    .order_by("userId", direction=firestore.Query.DESCENDING)
                    .start_after({
                        "userId": last_pop
                    })
                    .limit(limit)
                )
                docs = next_query.stream()
                # results = docs.get()
                # print(results)
            query,count = streamToList(docs)
            query.append({"total" : count})
            return query
        # userGroup = []
        # for doc in docs:
        #     fakeDict = doc.to_dict()
        #     userGroup.append(fakeDict)
        # return userGroup

    return users

def streamToList(docs):
    userGroup = []
    count = 0
    for doc in docs:
        count = count+1
        fakeDict = doc.to_dict()
        userGroup.append(fakeDict)
    return userGroup,count
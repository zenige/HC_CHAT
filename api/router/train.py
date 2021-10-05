from fastapi import APIRouter
from starlette import responses
from Project import db
import requests
from pydantic import BaseModel,HttpUrl
from typing import Optional
import datetime
from firebase_admin import firestore
from typing import Any, Dict, AnyStr, List, Union ,Set 
from model.trainModel import TrainedModel,JSONStructureCREATE,JSONStructureDELETE
router = APIRouter()





@router.get("/trained")
async def getTrainedWord(filter: Optional[str] = None,pages: Optional[int] = None,limit: Optional[int] = 0,order_by: Optional[str] = "question",sort_by: Optional[str] = "DESCENDING"):
    count = 0
    docs_ref = db.collection(u'trained')
    docs = docs_ref.stream()
    if sort_by == "DESCENDING":
        sort_by = firestore.Query.DESCENDING
    else :
        sort_by = firestore.Query.ASCENDING
    for doc in docs:
        count = count+1
    if filter:
        count = 0
        docs = docs_ref.order_by(order_by, direction=sort_by).stream()
        query = streamToDict(docs)
        # query.append({"total" : count})
        res = []

        for i in query:
            if filter in i[order_by] or filter in i['answer']:
                count = count+1
                res.append(i)
        res.append({"total" : count})
        return res
    if pages == None:
        docs = docs_ref.order_by(order_by, direction=sort_by).stream()
        query = streamToDict(docs)
        query.append({"total" : count})
        return query
    elif pages != None:
        first_query = docs_ref.order_by(order_by, direction=sort_by).limit(limit)
        docs = first_query.stream()
        # test = streamToDict(docs)
        # print(test)
        # print("____")

        if pages == 1 :
            query = streamToDict(docs)
            count = 0
            for i in query:
                count = count+1
            query.append({"total" : count})
            return query
        elif pages > 1 :
            for page in range(pages-1):
    
                last_doc = list(docs)[-1]

                last_pop = last_doc.to_dict()[order_by]

                next_query = (
                    docs_ref
                    .order_by(order_by, direction=sort_by)
                    .start_after({
                        order_by: last_pop
                    })
                    .limit(limit)
                )
                docs = next_query.stream()
                # results = docs.get()
                # print(results)
            query = streamToDict(docs)
            count = 0
            for i in query:
                count = count+1
            query.append({"total" : count})
            return query


def streamToDict(stream):
    obj = []
    for doc in stream:
        train_dict = doc.to_dict()
        train_dict['id'] = doc.id
        obj.append(train_dict)
    return obj

@router.post("/trained")
async def createTrainWord(data: TrainedModel):
    try:
        data = data.dict()

        # Add a new doc in collection 'cities' with ID 'LA'
        obj = {"question": data['question'], "answer": data['answer'],
            "time": datetime.datetime.timestamp(datetime.datetime.now())}
        db.collection(u'trained').document().set(obj)
        print(obj)
        res = {"response" : "Create Successful" }
    except: 
        res = {"response" : "Create Failed" }     
    return res

@router.post("/trained/many")
async def createTrainWord(arbitrary_json: JSONStructureCREATE = None):
    try:
        for i in arbitrary_json:
            fakeDict = i.__dict__
            fakeDict['time'] = datetime.datetime.timestamp(datetime.datetime.now())
            db.collection(u'trained').document().set(fakeDict)
            res = {"response" : "Create Successful" }
    except:
            res = {"response" : "Create Failed" }
    return res

@router.patch("/trained/{id}")
async def updateTrainWord(data: TrainedModel, id: str):
    try:
        data = data.dict()
        doc_ref = db.collection(u'trained').document(id)
        doc_ref.update({'question': data['question'], 'answer': data['answer']})
        res = {"response" : "Update Successful" }
    except:
        res = {"response" : "Update Failed" }    
    return res

@router.delete("/trained/delete/many")
async def deleteTrainWord(arbitrary_json: JSONStructureDELETE = None):
    try:
        for i in arbitrary_json:
            i = i.__dict__
            db.collection(u'trained').document(i['id']).delete()
        res = {"response" : "Delete Successful" }
    except:
        res = {"response" : "Delete Failed" }
    return res

@router.delete("/trained/delete/{id}")
async def deleteTrainWordById(id: str):
    db.collection(u'trained').document(id).delete()
    return {"response" : "Deleted" }


@router.get("/training")
async def getTrainedWord(filter: Optional[str] = None,pages: Optional[int] = None,limit: Optional[int] = 0,order_by: Optional[str] = "question",sort_by: Optional[str] = "DESCENDING"):

    count = 0
    docs_ref = db.collection(u'training')
    docs = docs_ref.stream()
    if sort_by == "DESCENDING":
        sort_by = firestore.Query.DESCENDING
    else :
        sort_by = firestore.Query.ASCENDING
    if filter:
        res = []
        count = 0
        docs = docs_ref.order_by(order_by, direction=sort_by).stream()
        query = streamToDict(docs)

        for i in query:
            if order_by == 'count':
                i['count'] = str(i['count'])

            if filter in i[order_by] or filter in i['answer']:
                count = count+1
                res.append(i)
            
        if pages == 1 :
            query = searchPage1(docs)
        print(query)
            # if limit:
                # for i in range(limit):
                #     print(query)
            #     return query
            # elif pages > 1 :
            #     query =  searchPages(pages,order_by,sort_by,docs_ref,limit,docs)

            #     return query
        res.append({"total" : count})
        return res
    if pages == None:
        docs = docs_ref.order_by(order_by, direction=sort_by).stream()
        query = streamToDict(docs)
        count = 0
        for doc in query:
            count = count+1
        query.append({"total" : count})
        return query
    elif pages != None:
        first_query = docs_ref.order_by(order_by, direction=sort_by).limit(limit)
        docs = first_query.stream()
        # test = streamToDict(docs)
        # print(test)
        # print("____")

        if pages == 1 :
            query = searchPage1(docs)

            return query
        elif pages > 1 :
            query =  searchPages(pages,order_by,sort_by,docs_ref,limit,docs)

            return query

def searchPage1(docs):
    query = streamToDict(docs)
    count = 0
    for i in query:
        count = count+1
    query.append({"total" : count})
    return query

def searchPages(pages,order_by,sort_by,docs_ref,limit,docs):
    for page in range(pages-1):

        last_doc = list(docs)[-1]

        last_pop = last_doc.to_dict()[order_by]

        next_query = (
            docs_ref
            .order_by(order_by, direction=sort_by)
            .start_after({
                order_by: last_pop
            })
            .limit(limit)
        )
        docs = next_query.stream()
        # results = docs.get()
        # print(results)
    query = streamToDict(docs)
    count = 0
    for i in query:
        count = count+1
    query.append({"total" : count})
    return query


@router.patch("/training/{id}")
async def updateTrainWord(data: TrainedModel, id: str):
    print(id)
    data = data.dict()
    # Add a new doc in collection 'cities' with ID 'LA'
    try:
        doc_ref = db.collection(u'training').document(id)
        doc_ref.update({'question': data['question'], 'answer': data['answer']})
        res = {"response" : "Update Successful" }
    except:
        res = {"response" : "Update Failed" }
    return res



@router.delete("/training/delete/many")
async def deleteTrainingWord(arbitrary_json: JSONStructureDELETE = None):
    try:
        for i in arbitrary_json:
            i = i.__dict__
            db.collection(u'training').document(i['id']).delete()
        res = {"response" : "Delete Successful" }
    except:   
        res = {"response" : "Delete Failed" }
    return res

@router.delete("/training/{id}")
async def deleteTrainingWord(id: str):
    try:
        doc_ref = db.collection(u'training').document(id).delete()
        res = {"response" : "Deleted" }
    except:  
        res = {"response" : "Delete Failed" }

    return res


from typing import Any, Dict, AnyStr, List, Union, Set
from pydantic import BaseModel, HttpUrl
import json
from firebase_admin import firestore
import pickle
from fastapi import APIRouter, Request
from Project import db
from Project.create_model import cleanData, create_model, TrainModelSVM, checkOr, checkOrPredict
from Project.test_mode import testModelRF, readCSV, cleanTestData, testModelRF, testModelSVM
import ttg
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import warnings
import ast
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore")
router = APIRouter()


class user(BaseModel):

    userId: str


class group(BaseModel):
    group: str


JSONObject = Dict[AnyStr, Any]
JSONArrayCREATE = List


JSONStructureDELETE = Union[List, JSONObject]


@router.get("/")
async def test():
    docs_ref = db.collection(u'logics')
    query = docs_ref.order_by(u'group')
    docs = query.get()
    data = []
    for doc in docs:
        docDict = doc.to_dict()
        dictSort = dict(sorted(docDict.items()))
        data.append(dictSort)
    newDF = createTruthTable(data)
    TrainModel(newDF)
    return "newDF"


@router.get("/createModel")
async def createModel():
    datas = [{"group": "group0", "AGE": "ANY", 'disease': "ANY", "cough": "ANY", "Fever": "ANY", "tired": "ANY", "close": "false", "Travel": "false"},
             {"group": "group1", "AGE": "ANY", 'disease': "ANY", "cough": "ANY", "Fever": "false", "tired": "ANY", "close": "true", "Travel": "true"}, {
        "group": "group1p2", "AGE": "ANY", 'disease': "ANY", "cough": "false", "Fever": "true", "tired": "false", "close": "true", "Travel": "true"}, {
        "group": "group2", "AGE": 4, 'disease': "false", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]}, {
        "group": "group3", "AGE": 5, 'disease': "false", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]
    }, {
        "group": "group3", "AGE": "ANY", 'disease': "true", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]
    },
        {
        "group": "group4", "AGE": "ANY", 'disease': "ANY", "Fever": "true", "close": "ANY", "Travel": "true", "cough": "true", "tired": "true"
    }
    ]
    newDF = await create_model(datas)

    newDF = cleanData(newDF)

    TrainModelSVM(newDF)

    return "newDF"


@router.post("/createModelRF")
async def createModelRF():
    # datas = [{"group": "group0", "AGE": "ANY", 'disease': "ANY", "cough": "ANY", "Fever": "ANY", "tired": "ANY", "close": "false", "Travel": "false"},
    #         {"group": "group1", "AGE": "ANY", 'disease': "ANY", "cough": "ANY", "Fever": "false", "tired": "ANY", "close": "true", "Travel": "true"}, {
    #         "group": "group1p2", "AGE": "ANY", 'disease': "ANY", "cough": "false", "Fever": "true", "tired": "false", "close": "true", "Travel": "true"}, {
    #         "group": "group2", "AGE": 4, 'disease': "false", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]}, {
    #         "group": "group3", "AGE": 5, 'disease': "false", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]
    # },{
    #         "group": "group3", "AGE": "ANY", 'disease': "true", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]
    # },
    # {
    #          "group": "group4", "AGE": "ANY", 'disease': "ANY", "Fever": "true", "close": "ANY", "Travel": "true","cough":"true","tired":"true"
    # }
    # ]
    docs = db.collection("logics").stream()
    datas = []
    data = {}
    for doc in docs:
        data = doc.to_dict()
        dataStr = data['data']
        dataDict = ast.literal_eval(dataStr)
        datas.append(dataDict)
    groupName = []
    groupArr = []
    detailArr = []
    groupDict = {}
    for i in datas:
        if i['group'] not in groupName:
            groupName.append(i['group'])

    for i in datas:
        groupDict = {}
        if "group" in i.keys():
            groupDict['group'] = i['group']
        del i["group"]
        keys = i.keys()

        for key in keys:
            groupDict[key] = i[key]
        groupArr.append(groupDict)
 

    # print(groupArr)
    # print("__________________")
    # print(detailArr)
    # print(groupName)
    newDF = await create_model(groupArr)

    newDF = cleanData(newDF, groupName)

    TrainModelRF(newDF)

    return "newDF"


@router.get("/test")
async def test():
    checkOr()
    return "newDF"


def createTruthTable(datas):
    newDF = pd.DataFrame()
    for data in datas:
        Any = []
        notYet = []
        for i in data:
            if data[i] == 'ANY':
                Any.append(i)
            elif i != 'ANY':
                notYet.append(i)
        truthTable = ttg.Truths(Any)
        df = truthTable.as_pandas()
        for arr in notYet:
            df[arr] = data[arr]
        newDF = newDF.append(df)
    return newDF


def TrainModelRF(newDF):
    newDF = newDF.reindex(sorted(newDF.columns), axis=1)
    df0 = newDF[newDF.group == 2]
    print(df0.to_string())
    colss = newDF.columns
    newcol = []
    for col in colss:
        if col != 'group':
            newcol.append(col)
    model = RandomForestClassifier(n_estimators=50, max_depth=None,
                                   min_samples_split=2, random_state=0)
    XX = newDF[newcol]
    yy = newDF['group']
    model.fit(XX, yy)
    print("accuracy DT train: {:.3f}".format(model.score(XX, yy)))
    filename = 'RF_model.sav'
    pickle.dump(model, open(filename, 'wb'))


@router.post("/predict")
async def predict():
    userId = "Ueb59687406ee1813431033235e2b83ec"
    loaded_model = pickle.load(open("SVM_model.sav", 'rb'))
    doc_ref = db.collection(u'users').document(userId)
    doc = doc_ref.get()
    if doc.exists:
        userInfo = doc.to_dict()
        userInfo['symptom']['AGE'] = 4
        df = pd.DataFrame([userInfo['symptom']],
                          columns=userInfo['symptom'].keys())

        df = await checkOrPredict(df)
        df = df.reindex(sorted(df.columns), axis=1)
        df = cleanData(df)
        print(df)
        result = loaded_model.predict([[8.0, 1, 1, 1, 0, 0]])
        print(result[0])

    else:
        print(u'No such document!')
    # result = loaded_model.predict([[1, 1, 1, 1, 1, 0, 0]])
    # str1 = str(result)
    # print(result)
    if result:
        lists = result[0].tolist()
        json_str = json.dumps(lists)
        return json_str
    else:
        return "something went wrong"


@router.post("/predictRF")
async def predict(user: user):
    print(user)
    # userId = "Ueb59687406ee1813431033235e2b83ec"
    loaded_model = pickle.load(open("RF_model.sav", 'rb'))
    doc_ref = db.collection(u'users').document(user.userId)
    doc = doc_ref.get()
    result = ''
    if doc.exists:
        userInfo = doc.to_dict()
        age = int(userInfo['symptom']['AGE'])
        if age < 22 and age >= 0:
            agegroup = 2
        elif age <= 30:
            agegroup = 3
        elif age <= 40:
            agegroup = 4
        elif age <= 50:
            agegroup = 5
        elif age <= 60:
            agegroup = 6
        elif age > 60:
            agegroup = 7
        userInfo['symptom']['AGE'] = agegroup
        df = pd.DataFrame([userInfo['symptom']],
                          columns=userInfo['symptom'].keys())
        print(df)
        df = await checkOrPredict(df)
        print(df)
        df = df.reindex(sorted(df.columns), axis=1)
        groupName = None
        print(df)
        df = cleanData(df, groupName)
        print(df)
        result = loaded_model.predict(df)
        docs = db.collection("logics").stream()
        datas = []
        data = {}
        answer = ''
        for doc in docs:
            data = doc.to_dict()
            dataStr = data['data']
            dataDict = ast.literal_eval(dataStr)
            datas.append(dataDict)

        groupName = []
        for i in datas:

            if i['group'] not in groupName:
                groupName.append(i['group'])
        groupName.sort()
        for idx, val in enumerate(groupName):
            if result[0] == idx:
                answer = val
        print(answer)

    else:
        print(u'No such document!')
    # result = loaded_model.predict([[1, 1, 1, 1, 1, 0, 0]])
    # str1 = str(result)
    # print(result)

    # if len (result) >0 :
    #     lists = result[0].tolist()
    #     json_str = json.dumps(lists)
    #     return json_str
    if answer:
        return answer
    else:

        return "something went wrong"


@router.get("/testmodelSVM")
async def testModelRoute():
    df = readCSV()
    df = cleanTestData(df)
    testModelSVM(df)
    return "newDF"


@router.get("/testmodelRF")
async def testModelRoute():
    df = readCSV()
    df = cleanTestData(df)
    testModelRF(df)
    return "newDF"


@router.post('/addlogic')
async def testna(request: Request):
    # data = await request.json()

    data = [{"group": "group0", "AGE": "ANY", 'disease': "ANY", "cough": "ANY", "Fever": "ANY", "tired": "ANY", "close": "false", "Travel": "false"},
            {"group": "group1", "AGE": "ANY", 'disease': "ANY", "cough": "ANY", "Fever": "false", "tired": "ANY", "close": "true", "Travel": "true"}, {
            "group": "group1p2", "AGE": "ANY", 'disease': "ANY", "cough": "false", "Fever": "true", "tired": "false", "close": "true", "Travel": "true"}, {
            "group": "group2", "AGE": 4, 'disease': "false", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]}, {
            "group": "group3", "AGE": 5, 'disease': "false", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]
            }, {
            "group": "group3p2", "AGE": "ANY", 'disease': "true", "Fever": "true", "close": "true", "Travel": "true", "Relation": [["cough", "tired"]]
            },
            {
        "group": "group4", "AGE": "ANY", 'disease': "ANY", "Fever": "true", "close": "ANY", "Travel": "true", "cough": "true", "tired": "true"
    }
    ]
    for i in data:
        print(i)
        group = str(i)
        db.collection("logics").document(i['group']).set({"data": group})
    return "done"


@router.post('/addlineLogic')
async def testna(request: Request):
    data = await request.json()
    print(data)

    for i in data:
        print(i)
        group = str(i)
        db.collection("logics").document(i['group']).set({"data": group})
    return "done"

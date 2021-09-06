from fastapi import APIRouter
from Project import db
import ttg
import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore")
router = APIRouter()
import pickle
from firebase_admin import firestore
@router.get("/")
async def test():
    docs_ref =  db.collection(u'logics')
    query = docs_ref.order_by(u'group')
    docs =  query.get()
    data = []
    for doc in docs:
        docDict = doc.to_dict()
        dictSort = dict(sorted(docDict.items()))
        data.append(dictSort)
    newDF = createTruthTable(data)
    TrainModel(newDF)
    return "newDF"


def createTruthTable(datas):
    newDF = pd.DataFrame()
    for data in datas:
        Any = []
        notYet = []
        for i in data:
            if data[i] == 'ANY':
                Any.append(i)
            elif i != 'ANY'  :
                notYet.append(i)
        truthTable = ttg.Truths(Any)
        df = truthTable.as_pandas()
        for arr in notYet:
            df[arr] = data[arr]
            print(arr)
        newDF = newDF.append(df)
    return newDF


def TrainModel(newDF):
    newDF = newDF.replace("True", 1)
    newDF = newDF.replace("False", 0)
    colss = newDF.columns
    newcol = []
    for col in colss:
        if col != 'group':
            newcol.append(col)
    model = RandomForestClassifier(n_estimators=50, max_depth=None,
    min_samples_split=2, random_state=0)
    print(newcol)
    XX =newDF[newcol]
    yy = newDF['group']
    model.fit(XX,yy)
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))

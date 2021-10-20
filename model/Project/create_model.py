
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from Project import db
from sklearn.datasets import load_iris
import ttg
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


async def create_model(datas):

    newDF = pd.DataFrame()
    flag = False
    cols2 = []
    # mainCols = list(datas[0].keys())
    # print(mainCols)
    for data in datas:
        df = pd.DataFrame()
        list2 = []
        Any = []
        notYet = []
        relation = []
        for i in data:
            if data[i] == 'ANY':
                Any.append(i)
            elif i != 'ANY' and i != "Relation":
                notYet.append(i)
            elif i == "Relation":
                relation.append(data[i])

        if len(Any) > 0:
            truthTable = ttg.Truths(Any)
            df = truthTable.as_pandas()
        if flag == False:

            cols = df.columns

            cols = list(cols)
            cols = cols+notYet
    #         print(cols)
            flag = True
            for arr in notYet:
                df[arr] = data[arr]
                head = list(df.columns)
        else:
            cols2 = df.columns

            cols2 = list(cols2)
            for i in cols:
                if i not in cols2:

                    list2.append(i)
    #         print(notYet)
    #         print(data)
    #         print(list2)
            if len(relation) > 0:
                list2.sort()
                print(list2)

# ['AGE', 'disease', 'cough', 'Fever', 'tired', 'group', 'close', 'Travel']


# ['AGE', 'disease', 'cough', 'Fever', 'tired', 'group', 'close', 'Travel']
# ['disease', 'cough', 'Fever', 'tired', 'group', 'close', 'Travel']
                for i in list2:
                    if i in relation[0][0]:

                        list2.remove(i)

            for arr in list2:

                if df.empty:
                    d = data[arr]
                    df = df.append({arr: d}, ignore_index=True)
    #             print(df)
    #             print("_____")
                else:

                    data_series = pd.Series([data[arr]])
                    df[arr] = data[arr]  # 2
            df = df.reindex(sorted(df.columns), axis=1)
            # print("00000000000000000000000000000")
            # print(df)
            # print("_______________________")
            head = list(df.columns)

        for i in notYet:
            colum = df.columns
        if len(relation) > 0:

            for i in range(len(relation)):
                for idxJ, j in enumerate(relation[i]):
                    head = head + j
                    listDF = df.to_numpy()
                    newList = []
                    for idxK, k in enumerate(listDF):

                        for idx, val in enumerate(j):

                            for idxM, m in enumerate(j):
                                # print(listDF)
                                if idx == idxM:
                                    newList.append("true")

                                else:
                                    newList.append("false")

    #                         print(k)

                            newList = np.append(k, newList)
                            # print(newList)
                            # print(head)
                            newDF2 = pd.DataFrame([newList],
                                                  columns=head)
                            # newDF2.columns = newDF2.columns.droplevel()

                            # newDF2 = newDF2.reindex(sorted(newDF2.columns), axis=1)

                            if newDF.empty:

                                newDF = pd.DataFrame([newList],
                                                     columns=[head])

                                # newDF = newDF.reindex(sorted(newDF.columns), axis=1)

                            else:
                                newDF = newDF.append(newDF2)

                                # # newDF = pd.concat(frames)
                                # print("_________________")
                                # newDF = pd.concat([newDF, newDF2], ignore_index=True, sort=False)
                                # print(newDF)
                                # print("***********************")
                                # print(newDF2)
                                # print("000000000000000")

                                # newDF = newDF.append(newDF2, sort=False)
                                # print(newDF)
                                # newDF.append(newDF2, ignore_index=True)
                                # print(newDF)
                                # newDF.loc[len(newDF)]=newList
                                # print("00000000000000000000000000000")

                                # print("_______________________")
                                # newDF = newDF.reindex(sorted(newDF.columns), axis=1)

                            newList = []
        else:
            df = df.reindex(sorted(df.columns), axis=1)
            if newDF.empty:
                newDF = df
            else:
                newDF = newDF.append(df, ignore_index=True)

    newDF = await checkOr(newDF)

    return newDF


async def checkOr(newDF):

    newDF = newDF.replace("true", True)
    newDF = newDF.replace("false", False)
    arr = []
    docs = db.collection('orCondition').stream()
    orDict = {}
    rows = []
    for doc in docs:
        orDict = doc.to_dict()
    sorted_items = sorted(orDict)
    for i in sorted_items:

        # if len(newDF[i]) > 0:
        #     newDF = newDF.drop(columns=[i])

        rows.append(i)
    if rows:
        for index, row in newDF.iterrows():

            arr.append(row[rows[0]] or row[rows[1]])
        str = rows[0] + "OR" + rows[1]

        newDF[str] = arr
    for i in sorted_items:
        newDF = newDF.drop(columns=[i])

    return newDF


async def checkOrPredict(newDF):
    newDF = newDF.replace("true", True)
    newDF = newDF.replace("false", False)
    arr = []
    docs = db.collection('orCondition').stream()
    orDict = {}
    rows = []
    for doc in docs:
        orDict = doc.to_dict()
    sorted_items = sorted(orDict)

    for i in sorted_items:
        rows.append(i)

    if rows:
        for index, row in newDF.iterrows():

            result = row[rows[0]] or row[rows[1]]

            arr.append(result)
        str = rows[0] + "OR" + rows[1]

        newDF[str] = arr
    for i in sorted_items:
        newDF = newDF.drop(columns=[i])

    return newDF


def cleanData(newDF, groupName):

    newDF = newDF.replace("true", 1)
    newDF = newDF.replace("false", 0)
    newDF = newDF.replace(True, 1)
    newDF = newDF.replace(False, 0)
    # newDF2newDF2 = newDF.replace("group0", 0)
    docs = db.collection("logics").stream()
    # for doc in docs:
    #     fakeDict = doc.to_dict()
    #     groupName.append(fakeDict['group'])
    # print(groupName)
    if groupName:
        groupName.sort()

        for idx, val in enumerate(groupName):
            newDF = newDF.replace(val, idx)

    return newDF


def TrainModelSVM(newDF):
    newDF = newDF.reindex(sorted(newDF.columns), axis=1)
    df0 = newDF[newDF.group == 3]
    print(df0.to_string())
    y_train = newDF.group
    X_train = newDF.drop(['group'], axis='columns')
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)
    print("accuracy DT train: {:.3f}".format(model.score(X_train, y_train)))

    filename = 'SVM_model.sav'
    pickle.dump(model, open(filename, 'wb'))


def NormalizeAge(age):

    return age

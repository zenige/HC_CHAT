import csv
import pandas as pd
from sklearn.metrics import confusion_matrix
import pickle

def testModelSVM(df):
    X_test  = df.drop(['group'], axis='columns')
    y_test = df.group
    y_test= pd.Series(y_test, dtype="int64")
    print(X_test)
    loaded_model = pickle.load(open("SVM_model.sav", 'rb'))
    predictions = loaded_model.predict(X_test)
    print(predictions)
    percentage = loaded_model.score(X_test, y_test)
    res = confusion_matrix(y_test, predictions)
    print("Confusion Matrix")
    print(res)
    print(f"Test Set: {len(X_test)}")
    print(f"SVM Accuracy = {percentage*100} %")

def readCSV():
    with open('dataset4.csv', newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        dict1 = {}
        newList = []
        for row in reader:
            dict1['close'] = row['isCloseToCovid19Patient']
            dict1['disease'] = row['haveUnderlyingDisease']
            dict1['Fever'] = row['haveFever']
            dict1['tired'] = row['haveTired']
            dict1['Travel'] = row['isTravelToCovid19Country']
            dict1['group'] = row['outcome']
            dict1['cough'] = row['haveCough']
            dict1['AGE'] = row['ageGroup']
            newList.append(dict1)
            dict1 = {}
    df = pd.DataFrame.from_dict(newList)
    return df


def cleanTestData(df):
    df = df.replace("TRUE", 1)
    df = df.replace("FALSE", 0)
    df = df.replace("SENIOR", 6)
    df = df.replace("OLD_ADULT", 5)
    df = df.replace("MIDDLE_AGED_ADULT", 4)
    df = df.replace("YOUNG_ADULT", 3)
    df = df.replace("JUNIOR", 2)
    df = df.replace("ELDER", 7)
    df = df.replace("GROUP1p1", 4)
    df = df.replace("GROUP1p2", 3)
    df = df.replace("GROUP2", 2)
    df = df.replace("GROUP3", 1)
    df = df.replace("GROUP4", 0)
    df[df['Fever'] == ''].index
    df = df.drop([2403,1522, 1523, 2401, 2402,1524,1521,2400]).reset_index()
    df = df.drop(['index'], axis='columns')
    arr = []
    for index, row in df.iterrows():
        arr.append(row['close'] or  row['Travel'] )
    df['closeORTravel']  = arr
    df = df.reindex(sorted(df.columns), axis=1)
    df = df.drop(columns=['close','Travel'])
    return df



def testModelRF(df):
    X_test  = df.drop(['group'], axis='columns')
    y_test = df.group
    y_test= pd.Series(y_test, dtype="int64")
    print(X_test)
    loaded_model = pickle.load(open("RF_model.sav", 'rb'))
    predictions = loaded_model.predict(X_test)
    print(predictions)
    percentage = loaded_model.score(X_test, y_test)
    res = confusion_matrix(y_test, predictions)
    print("Confusion Matrix")
    print(res)
    print(f"Test Set: {len(X_test)}")
    print(f"RF Accuracy = {percentage*100} %")
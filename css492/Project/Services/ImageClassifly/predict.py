
import cv2
import numpy as np
import pickle
from tensorflow import keras
from Project.Services.chatBot import templateMessage
def predictImage(imgPath,userId):
    print(1)
    model = keras.models.load_model('/Users/zenige/Desktop/css492/model-image')
    print(2)
    img = cv2.imread(imgPath, cv2.COLOR_BGR2RGB)
    # ori = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (128, 128))
    rimg = np.array(img)
    rimg = rimg.astype('float32')
    rimg /= 255
    rimg = np.reshape(rimg, (1, 128, 128, 3))
    print("BEFORE PREDICT")
    predict = model.predict(rimg)
    print("after")
    y_predict = predict.argmax(axis=-1)
    # predict = predict.argmax(axis=-1)
    label = ['Tinea Ringworm Candidiasis and other Fungal Infections', 'Eczema', 'Atopic Dermatitis']
    result = label[np.argmax(predict)]
    print(predict)
    print('predict : ' + str(result))
    list1 = predict.tolist()
    print("________")
    print(list1)
    print("________")
    bg = str(list1[0])
    bg = bg.replace('[', '').replace(']', '')
    bg = bg.split(", ")
    jsonobg = []
    jsonobg.append({"label":"Tinea Ringworm Candidiasis", "predict":round(float(bg[0]) * 100, 2)})
    jsonobg.append({"label":"Eczema", "predict":round(float(bg[1]) * 100, 2)})
    jsonobg.append({"label":"Atopic Dermatitis", "predict":round(float(bg[2]) * 100, 2)})
    jsonobg = sorted(jsonobg, key=lambda k: k['predict'], reverse=True)
    print(f'all                                     : {jsonobg[0]}')
    print(jsonobg)
    print("_____")
    return templateMessage.listPredictImg(jsonobg,userId)
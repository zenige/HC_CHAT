
import cv2
import numpy as np
import pickle
from tensorflow import keras
def predictImage():
    print(1)
    model = keras.models.load_model('/Users/zenige/Desktop/css492/model-image')
    print(2)
    img = cv2.imread('/Users/zenige/Desktop/css492/static/img/what-is-eczema-atopic-dermatitis-symptoms-causes-diagnosis-treatment-prevention-01-722x406.jpg', cv2.COLOR_BGR2RGB)
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
    return {"message":str(result)}
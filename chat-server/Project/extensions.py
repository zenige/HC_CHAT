
import requests
import json


def getAnswer(message, confident, sender_id):

    url = 'http://127.0.0.1:400/nlp/getconfident'
    myobj = {'message': message,
             'confident': confident, 'sender_id': sender_id}
    json_object = json.dumps(myobj)

    x = requests.post(url, json_object, headers={
                      'Content-type': 'application/json'})

    return x


def predict():

    url = 'http://127.0.0.1:500/trainModel/predictRF'
    myobj = {}
    json_object = json.dumps(myobj)

    x = requests.post(url, json_object, headers={
                      'Content-type': 'application/json'})

    return x

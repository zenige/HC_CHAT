from Project import db
def handleSequence(subState = 'none',next = False):
    seqs = getSequence() # get logic from db
    res = {}
    for seq in seqs:

      if seq['id'] == subState and subState != 'none': #check current subState
        res = seq
        break
      elif subState == 'none': 
        res = seq
        break
    if subState != 'none': #if current subState not None
      # if res['Type'] == "input" or res['Type'] == "boolean" : 
      if res['Type'] == "input" or res['Type'] == "boolean" : 
        if next == True: # Has next Question ?
          flag = False
          for seq in seqs: # get next question
            if res['Next'] == seq['id']:
              res = seq 
              flag = True
              break
          if flag == False: # has no next question
              res = "Done"

      else :  # check if type not input not accept respons
        res = None
    print(res)
    return res




def getSequence():
    sequenceLogics =  db.collection(u'lineLogic').stream()
    newList = []
    for seq in sequenceLogics:
      newList.append(seq.to_dict())
    return newList



def createFlex(seq):
    context = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": seq['Question'],
            "wrap": True
          }
        ]
      }
    }
    if seq['Type'] == 'boolean':
        context['footer'] = {

        "type": "box",
        "layout": "vertical",
        "contents": [
          {
        "type": "button",
        "style": "primary",
        "height": "sm",
            "action": {
          "type": "postback",
          "label": "ใช่",
          "data": "action=%=true//subState=%="+seq['id'],
        "displayText": "เป็น"
        }
      },
                {
        "type": "button",
        "style": "primary",
        "height": "sm",
            "action": {
          "type": "postback",
          "label": "ไม่ใช่",
          "data": "action=%=false//subState=%="+seq['id'],
        "displayText": "ไม่เป็น"
        }
      },
        ]
      }

    return context
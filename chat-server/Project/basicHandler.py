


def basicEventHandler(**kwargs):
    doc_ref = db.collection(u'users').document(kwargs['sender_id'])

    if kwargs['message']['message'] == 'หาหมอครับ':   #command for first time
        return True
        # isProfileComplete = checkProfile(doc_ref)
        # if isProfileComplete :
        #   seq = handleSequence()
        #   event = createFlex(seq)
        #   return True, {'flex': event,'alt':seq['Question']},seq['id']
        # else :
        #   event = profileStateHandler(state="real_name")
        #   return True, {'flex': event,'alt':"กรุณากรอกชื่อจริงของท่าน"},"real_name"
    elif kwargs['message']['message'] == 'ยกเลิก': #command for cancel
        # return True, {'message':"ยกเลิกการทำงาน"},'none'
        return True
    else :
        return False
        # if kwargs['subState'] == 'none' or kwargs['subState'] == 'Done':    
        #   return False,"not found word","Err"
        # else : 
        #   isnum = False
        #   if kwargs['message']['message'].isnumeric():
        #       isnum = True
        #   seq = handleSequence(kwargs['subState'],True) #finding next question
        #   if isnum == False:
        #       return False,{'message': "กรุณากรอกเป็นตัวเลขเท่านั้น"},"Err"
        #   if seq != None and seq != 'Done' :  #has next question
        #     event = createFlex(seq)
        #     query = findAndUpdate(doc_ref.get(),kwargs['subState'],kwargs['message']['message'])
        #     doc_ref.update(query)
        #     return True, {'flex': event,'alt':seq['Question']},seq['id']
        #   elif seq == 'Done' : #done all 
        #     return True, {'message': "Done"},"done"
        #   elif seq == None: #not in command
        #     return False,"not found word","Err"
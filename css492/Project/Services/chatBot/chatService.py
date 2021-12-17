from Project import db
import datetime
def checkType(payload):
    if 'message' in payload['events'][0].keys():
        message_type = payload['events'][0]['message']['type']
    elif 'postback' in payload['events'][0].keys():
        message_type = 'postback'
    else:
        message_type = 'else'
    return message_type


def defineSender(sender, profile):
    doc_ref = db.collection(u'users').document(sender)
    doc = doc_ref.get()
    if doc.exists:
        doc_ref.update({'pictureUrl': profile.picture_url, 'display_name': profile.display_name,'userId':sender,
                       'last_message': datetime.datetime.timestamp(datetime.datetime.now())})

    else:
        obj = {'pictureUrl': profile.picture_url, 'display_name': profile.display_name,'userId':sender,
               'last_message': datetime.datetime.timestamp(datetime.datetime.now()), 'subState': 'none','mainState':'none','profile':False,'symptom':False}
        doc_ref.set(obj)

def medHandler(medName):
    if medName == 'betamethasone':
        return {"message":"Betamethasone (เบต้าเมทาโซน) เป็นยาในกลุ่มคอร์ติโคสเตียรอยด์ มีฤทธิ์รักษาภาวะต่าง ๆ จากการอักเสบ เช่น อาการแพ้ โรคสะเก็ดเงิน และผื่นผิวหนัง ยา Betamethasone มีข้อควรระวังในการใช้ยามากมาย ผู้ป่วยควรอ่านฉลากยาอย่างละเอียด และปรึกษาแพทย์หรือเภสัชกรให้ดีก่อนใช้ยาเสมอ\n\nกลุ่มยา: คอร์ติโคสเตียรอยด์\nประเภทยา: ยาตามใบสั่งแพทย์\nสรรพคุณ: ต้านการอักเสบ\nกลุ่มผู้ป่วย: ผู้ใหญ่\nรูปแบบของยา: ยาทาภายนอก\n\nรายละเอียดเพิ่มเติม: https://www.pobpad.com/betamethasone"}
    elif medName == 'clobetasol':
        return {"message":"Clobetasol (โคลเบทาซอล) เป็นยาคอร์ติโคสเตียรอยด์ชนิดใช้เฉพาะที่ นำมาใช้รักษาโรคผิวหนังที่ตอบสนองต่อยาสเตียรอยด์ (Corticosteroid-Responsive Dermatoses) เช่น การระคายเคือง ผื่นคัน ผิวหนังอักเสบ และอาการแพ้ทางผิวหนัง นอกจากนี้ ยังอาจใช้รักษาโรคอื่น ๆ ตามดุลยพินิจของแพทย์\n\nกลุ่มยา: ยาคอร์ติโคสเตียรอยด์ชนิดใช้เฉพาะที่\nประเภทยา: ยาตามใบสั่งแพทย์\nสรรพคุณ: \tรักษาภาวะทางผิวหนังที่ตอบสนองต่อยาสเตียรอยด์\nกลุ่มผู้ป่วย: เด็ก ผู้ใหญ่\nรูปแบบของยา: ยาใช้เฉพาะที่ชนิดยาขี้ผึ้ง ครีม โลชั่น เจล โฟม แชมพู และสารละลายที่ใช้กับหนังศีรษะ\n\nรายละเอียดเพิ่มเติม: https://www.pobpad.com/clobetasol-โคลเบทาซอล"}
    elif medName == 'topicorte':
        return {"message":"เดสออกซิเมทาโซน (Desoximetasone) เป็นยาในกลุ่มคอร์ติโคสเตอรอยด์ (Corticosteroids) ใช้กับโรคผิวหนังที่ไม่ได้เกิดจากการติดเชื้อ เช่น ผื่นแพ้อักเสบ, โรคผิวหนังที่เกิดจากสารระคายเคืองหรือผื่นภูมิแพ้, อาการอักเสบผิวหนังของโรคสะเก็ดเงิน และผิวไหม้เนื่องจากแสงแดด เป็นต้น\n\nกลุ่มยา: ยาคอร์ติโคสเตียรอยด์\nประเภทยา: ยาตามใบสั่งแพทย์\nสรรพคุณ: \tรักษาภาวะทางผิวหนังที่ตอบสนองต่อยาสเตียรอยด์\nกลุ่มผู้ป่วย: เด็ก ผู้ใหญ่ ผู้สูงอายุ\nรูปแบบของยา: ยาใช้เฉพาะที่ชนิดยาขี้ผึ้ง ครีม \n\nรายละเอียดเพิ่มเติม: https://healthythai.online/drug/desoximetasone (topical)/"}
    elif medName == 'hydrocortisone':
        return {"message":"Hydrocortisone (ไฮโดรคอร์ติโซน) เป็นยาสเตียรอยด์ที่ใช้รักษาการอักเสบตามอวัยวะต่าง ๆ เช่น ผิวหนัง และรักษาโรคภูมิแพ้ โรคหืด โรคเกี่ยวกับต่อมไทรอยด์ ข้ออักเสบ ลำไส้ใหญ่อักเสบ โรคสะเก็ดเงิน โรคไต โรคภูมิคุ้มกันทำลายตนเองอย่างโรคลูปัส และรักษาผู้ที่ต่อมหมวกไตไม่สามารถผลิตสารไฮโดรคอร์ติโซนได้ตามปริมาณปกติ หรืออาจใช้รักษาโรคอื่น ๆ นอกเหนือจากนี้ตามดุลยพินิจของแพทย์\n\nกลุ่มยา: ยาคอร์ติโคสเตียรอยด์\nประเภทยา: ยาตามใบสั่งแพทย์\nสรรพคุณ: \tรักษาการอักเสบ\nกลุ่มผู้ป่วย: เด็ก ผู้ใหญ่ \nรูปแบบของยา: ยารับประทาน ยาทาเฉพาะที่ ยาฉีด\n\nรายละเอียดเพิ่มเติม: https://www.pobpad.com/hydrocortisone"}


def liffHandler(i):
    if i == "Tinea Ringworm Candidiasis":
        return 
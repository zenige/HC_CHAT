import warnings
from pythainlp.tokenize import word_tokenize
import pythainlp.util
from pythainlp.word_vector import *
from sklearn.metrics.pairwise import cosine_similarity  # ใช้หาค่าความคล้ายคลึง
from pythainlp.soundex import lk82, metasound
import numpy as np

warnings.filterwarnings('ignore')
#ss1 is input from client
#ss2 is from data base

model=get_model() # ดึง model ของ thai2vec มาเก็บไว้ในตัวแปร model
def sentence_vectorizer(ss,dim=300,use_mean=True): # ประกาศฟังก์ชัน sentence_vectorizer
    s = pythainlp.word_tokenize(ss)
    vec = np.zeros((1,dim))
    for word in s:
        if word in model.wv.index2word:
            vec+= model.wv.word_vec(word)
        else: pass
    if use_mean: vec /= len(s)
    return vec

def sentence_similarity(s1,s2):
    return float(cosine_similarity(sentence_vectorizer(str(s1)),sentence_vectorizer(str(s2))))

def sentence_sound_index(ss1,ss2,list = "none"):
    if list == "invert":
        s1 = word_tokenize(ss1)
        s2 = word_tokenize(ss2)
        if len(s1) > len(s2):
            x = s1
            s1 = s2
            s2 = x
        catch = 0
        for i in range(len(s1)):
            if lk82(s1[i]) == lk82(s2[i]) or (i+2<len(s2) and lk82(s1[i]) == lk82(s2[i+2])) or (i+1<len(s2) and lk82(s1[i]) == lk82(s2[i+1])) or (i-1 >=0 and lk82(s1[i]) == lk82(s2[i-1])): 
                catch += 1
        if len(s1) < len(s2):
            return catch/len(s1)
        else:
            return catch/len(s2)
    elif list == "none":
        s1 = word_tokenize(ss1)
        s2 = word_tokenize(ss2)
        if len(s1) > len(s2):
            x = s1
            s1 = s2
            s2 = x
        catch = 0
        for i in range(len(s1)):
            if lk82(s1[i]) == lk82(s2[i]) or (i+2<len(s2) and lk82(s1[i]) == lk82(s2[i+2])) or (i+1<len(s2) and lk82(s1[i]) == lk82(s2[i+1])) or (i-1 >=0 and lk82(s1[i]) == lk82(s2[i-1])): 
                catch += 1
        if len(s1) > len(s2):
            return float(catch/len(s1))
        else:
            return float(catch/len(s2))

def sentence_get_confident(ss1,ss2,list = "none"):
    if list == "none":
        # if pythainlp.util.isthai(ss1['message'], ignore_chars="1234567890.-,$[@_!#$%^&*()<>?/\|}{~:] "):
            return (sentence_similarity(ss1,ss2)+sentence_sound_index(ss1, ss2))/2
        # else:
            # return False #"ขอโทษครับ ผมพูดได้แค่ภาษาไทย"
    elif list == "invert":

        # if pythainlp.util.isthai(ss1['message'], ignore_chars="1234567890.-,$[@_!#$%^&*()<>?/\|}{~:] "):

        return (sentence_similarity(ss1,ss2)+sentence_sound_index(ss1, ss2, list='invert'))/2
        # else:
            # return False #"ขอโทษครับ ผมพูดได้แค่ภาษาไทย"

# print(example[inp])
# print(pythainlp.util.isthai(inp))
print(sentence_similarity("ฮัลโหล","โหล"))
print(word_tokenize("บายดี"))
print(word_tokenize("สบายดี"))
print(sentence_sound_index('สนใจทานข้าวไหม','กินข้าวกันไหม',list='invert'))
print("DDD")

print(sentence_get_confident("ทำไรหรอค่ะ", "อะไรอยู่หรอค่ะ"))

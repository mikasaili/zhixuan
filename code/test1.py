import docx
import docx2txt
import re
from datetime import datetime
#import nltk

def process(txt):#return处理过后的词条
    lst=[]
    textlst = txt.split('\n')
    for i in textlst:
        if i !='' and i not in lst:
            lst.append(i)
    return lst


def extract_text_from_docx(docx_path):#简历全部内容,返回str
    txt = docx2txt.process(docx_path)
    if txt:
        txt = txt.replace('\t', ' ')
        txt = txt.replace('\n+','\n')
        return txt
    return None


def extract_names(txt):
    '''person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )

    return person_names'''

def get_age(txt):
    AGE_REG = re.compile(r'年.*龄.*')
    age = re.findall(AGE_REG, txt)
    if age == []:
        AGE_REG = re.compile(r'出.*生.*')
        age = re.findall(AGE_REG, txt)
        if age != []:
            BIRTH_REG = re.compile(r'\d{4}.*\d{0,2}.*\d{0,2}')
            birth = re.findall(BIRTH_REG,age[0])
            age = datetime.now().year-int(birth[0][:4])
            return age
    else:
        age_REG = re.compile(r'\d{2}')
        return re.findall(age_REG,age[0])

def get_data(txt):
    d=dict()



    PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\\(\)]{8,}[0-9]')
    phone = re.findall(PHONE_REG, txt)
    if phone != []:
        d['phone']=phone[0]

    EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
    email = re.findall(EMAIL_REG,txt)
    if email != []:
        d['email'] = email[0]

    SEX_REG = re.compile(r'性.*别.*')
    SEX = re.findall(SEX_REG,txt)
    if SEX != []:
        if '男' in SEX[0]:
            d['性别'] = '男'
        else:
            d['性别'] = '女'


    age = (get_age(txt))
    d['年龄']  = age


    print(d)




if __name__ == '__main__':
    path='D:\\zhixuan\\dataset_CV\\dataset_CV\\CV\\19.docx'
    txt=extract_text_from_docx(path)
    lst = process(txt)
    print(lst)

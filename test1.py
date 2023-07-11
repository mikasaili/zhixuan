import docx
import docx2txt
import re
from datetime import datetime
import nltk

'''nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
]
'''

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

def extract_highest_degree(lst):
    degree_levels = ['博士','硕士','本科','大专','专科','中专']
    for i in lst:
        for j in degree_levels:
            if j in i:
                return j
    return None


def extract_education(input_text):
    '''organizations = []

    # first get all the organization names using nltk
    for sent in nltk.sent_tokenize(input_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk.leaves()))

    # we search for each bigram and trigram for reserved words
    # (college, university etc...)
    education = set()
    for org in organizations:
        for word in RESERVED_WORDS:
            if org.lower().find(word) & gt;= 0:
                education.add(org)

    return education'''

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
    lst = process(txt)


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

    d['学历'] = extract_highest_degree(lst)


    print(d)




if __name__ == '__main__':
    path='D:\\zhixuan\\dataset_CV\\dataset_CV\\CV\\1.docx'
    txt=extract_text_from_docx(path)
    #get_data(txt)
    lst = process(txt)
    print(extract_school(txt))

import docx2txt
import re
from datetime import datetime
import jieba.posseg as pseg

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
    words = pseg.cut(txt)
    candidates = []
    for word, flag in words:
        if flag == 'nr':
            candidates.append(word)
    NAME_REG = re.compile(r'\s[\u4e00-\u9fa5]{2,4}\s')
    namelst = re.findall(NAME_REG,txt)
    names = []
    for i in candidates:
        for j in namelst:
            if i in j:
                return j[1:-1]


def extract_highest_degree(lst):
    degree_levels = ['博士','硕士','本科','大专','专科','中专']
    for i in lst:
        for j in degree_levels:
            if j in i:
                return j
    return None


def extract_education(lst):
    schools=['大学','学院','专业学校','中专','技术学校','中学']
    for i in lst:
       for j in schools:
           SCHOOL = re.compile('\S{1,}'+j)
           if re.findall(SCHOOL,i):
               for k in i.split():
                   if j in k:
                       return k



def get_age(txt,lst):
    AGE_REG = re.compile(r'年.*龄.*')
    age = re.findall(AGE_REG, txt)
    if age == []:
        AGE_REG = re.compile(r'出.*生.*')
        age = re.findall(AGE_REG, txt)
        try:
            BIRTH_REG = re.compile(r'\d{4}.*\d{0,2}.*\d{0,2}')
            birth = re.findall(BIRTH_REG,age[0])
            age = datetime.now().year-int(birth[0][:4])
            return age
        except:
            for i in range(len(lst)):
                if '出生'in lst[i]:
                    birth = lst[i+1]
                    age = datetime.now().year - int(birth[:4])
                    return age
            else:
                AGE_REG = re.compile(r'\d.\d.岁')
                age = re.findall(AGE_REG, txt)
                a=''
                try:
                    for num in age[0]:
                        if str(num).isdigit():
                            a+=str(num)
                    return int(a)
                except: return None


    else:
        age_REG = re.compile(r'\d{2}')
        return re.findall(age_REG,age[0])

def get_data(txt):
    d=dict()
    lst = process(txt)

    name = extract_names(txt)
    d['姓名'] = name

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


    age = (get_age(txt,lst))
    d['年龄']  = age

    d['学历'] = extract_highest_degree(lst)

    d['毕业院校'] = extract_education(lst)
    return d



if __name__ == '__main__':
    path='D:\\zhixuan\\dataset_CV\\dataset_CV\\CV\\18.docx'
    txt=extract_text_from_docx(path)
    print(get_data(txt))




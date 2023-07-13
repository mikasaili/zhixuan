import docx2txt
import re

def process(txt):#return处理过后的词条
    lst=[]
    s=''
    textlst = txt.split('\n')
    for i in textlst:
        if i !='' and i not in lst:
            lst.append(i)
            s+=i
            s+='\n'
    return s



def extract_text_from_docx(docx_path):#简历全部内容,返回str
    txt = docx2txt.process(docx_path)
    if txt:
        txt = txt.replace('\t', ' ')
        txt = txt.replace('\n+','\n')
        return txt
    return None


def getEXPList():
    lstEXP = [0]
    for i in range(1, 101):
        path = "F:\\CODE_Djiango\\dataset_CV\\CV\\" + "{}".format(i) + ".docx"
        # 从文件中提取文本并处理
        txt = process(extract_text_from_docx(path))
        lstEXP.append(txt)
    return lstEXP


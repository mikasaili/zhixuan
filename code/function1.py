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


if __name__ == '__main__':
    path='D:\\zhixuan\\dataset_CV\\dataset_CV\\CV\\13.docx'
    txt=extract_text_from_docx(path)
    print(process(txt))
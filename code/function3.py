import docx2txt
import re
from datetime import datetime
import os
from function2 import extract_text_from_docx,get_data
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def eachFile(filepath):
    res=[]
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        res.append(child)
    return res

def countinformation(pathlist):
    res=[]
    d_sex=dict()
    d_degree = dict()
    d_age = dict()
    d_sex['男'] = 0
    d_sex['女'] = 0
    d_sex['未填'] = 0
    d_degree['博士']=0
    d_degree['硕士'] = 0
    d_degree['本科'] = 0
    d_degree['大专'] = 0
    d_degree['专科'] = 0
    d_degree['中专'] = 0
    d_degree['未知'] = 0
    d_age[1] = 0
    d_age[2] = 0
    d_age[3] = 0
    d_age['未知'] = 0
    for i in pathlist:
        txt = extract_text_from_docx(i)
        d = get_data(txt)
        try:
            d_sex[d['性别']]+=1
        except: d_sex['未填']+=1
        try:
            d_degree[d['学历']]+=1
        except: d_degree['未知']+=1
        try:
            if d['年龄'] <30:
                d_age[1]+=1
            elif 30<=d['年龄']<40:
                d_age[2] += 1
            else:
                d_age[3] += 1
        except: d_age['未知'] +=1

    res.append(d_age)
    res.append(d_degree)
    res.append(d_sex)
    return res

def pie_sex(res):
    d_sex = res[2]
    plt.rcParams["font.sans-serif"] = ["Microsoft Yahei"]
    labels = ['男', '女', '未填']
    X = [d_sex['男'], d_sex['女'], d_sex['未填']]
    colors = ["#126bae", "#b7ae8f", "#8cc269"]
    plt.title("目前招聘者性别比例")
    plt.pie(X, labels=labels, colors=colors, autopct='%1.2f%%', pctdistance=0.8)
    plt.show()
def pie_age(res):
    d_age = res[0]
    plt.rcParams["font.sans-serif"] = ["Microsoft Yahei"]
    labels = ['30岁以下','30-40岁','40岁以上']
    X = [d_age[1],d_age[2],d_age[3]]
    colors = ["#FF8C00", "#DAA520", "#FF7F50"]
    plt.title("目前招聘者年龄比例")
    plt.pie(X, labels=labels, colors=colors, autopct='%1.2f%%', pctdistance=0.8)
    plt.show()

def pie_degree(res):
    d_degree = res[1]
    plt.rcParams["font.sans-serif"] = ["Microsoft Yahei"]
    labels = ['博士','硕士','本科','大专','专科','中专']
    X = [d_degree['博士'],d_degree['硕士'],d_degree['本科'],d_degree['大专'],d_degree['专科'],d_degree['中专']]
    colors = ["#FF8C00", "#DAA520", "#FF7F50","#FFA07A","#FF4500","#F0E68C"]
    plt.title("目前招聘者学历分布")
    plt.pie(X, labels=labels, colors=colors, autopct='%1.2f%%', pctdistance=0.8)
    plt.show()


if __name__ == '__main__':
    path='D:\\zhixuan\\dataset_CV\\dataset_CV\\CV\\'
    pathlist = eachFile(path)[:100]

    res = countinformation(pathlist)
    pie_age(res)


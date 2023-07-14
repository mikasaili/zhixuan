from django.shortcuts import render
from django.views import View
from web_zhixuan.models import Candidate

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm


def tfidf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


def match(txt,position,description):
    REG = re.compile('求职' + '.*' + position)
    target = re.findall(REG, txt)
    if target:
        tf = tfidf_similarity(description, txt)
        return tf
    else:
        return -1


def post(request):
    if request.method == 'POST':
        position = request.POST.get('position')
        description = request.POST.get('description')
        db = Candidate.objects.all()
        lst=[]
        for person in db:
            d=dict()
            d['姓名'] = person.candidateName
            d['年龄'] = person.candidateAge
            d['性别'] = person.candidateSex
            d['学历'] = person.candidateEdu
            d['工作年限'] = person.candidateYearsOfWork
            #d['求职意向'] = person.
            exp = person.candidateExp
            tf = match(exp,position,description)
            d['tf'] = tf
            if tf >0:
                lst.append([d,tf])
        lst.sort(key = lambda x:x[1],reverse=True)
        l = min(5,len(lst))
        c=dict()
        for i in range(l):
            c['candidate'+str(i+1)] = lst[i]
        return render(request,'blog_single.html',context=c)



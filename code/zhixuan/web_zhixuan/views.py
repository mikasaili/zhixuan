import re

from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from web_zhixuan import models
import function2, function1

name1 = ''


# Create your views here.


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def index(request):
    return render(request, "index.html")


def teachers(request):
    return render(request, "teachers.html")


def contact(request):
    return render(request, "contact.html")


def pricing(request):
    return render(request, "pricing.html")


def search(request):
    return render(request, "search.html")


def blog_single(request):
    candidate_count = models.Candidate.objects.count()
    return render(request, "blog-single.html", {'candidate_count': candidate_count})


def updateinfo(request):
    if request.method == 'POST':
        # img = request.FILES.get('photo')
        # user = request.FILES.get('photo').name
        new_img = models.zhixuanDB(
            photo=request.FILES.get('photo'),  # 拿到图片
            www=request.FILES.get('photo').name  # 拿到图片的名字
        )
        new_img.save()  # 保存图片
        name1 = request.FILES.get('photo').name
        print(name1)
        path = "F:\\CODE_Djiango\\dataset_CV\\CV\\" + name1
        txt = function2.extract_text_from_docx(path)  # 其他
        txt2 = function1.process(function1.extract_text_from_docx(path))  # exp
        dic = function2.get_data(txt)
        Name = dic['姓名']
        if models.Candidate.objects.filter(candidateName=Name).exists():
            models.Candidate.objects.filter(candidateName=Name). \
                update(candidateAge=dic.get('年龄', -1), candidateEdu=dic.get('学历', ''),
                       candidateSex=dic.get('性别', ''), candidateExp=txt2)

        else:
            models.Candidate.objects.create(candidateName=dic.get('姓名', ''), candidateAge=dic.get('年龄', -1),
                                            candidateEdu=dic.get('学历', ''), candidateSex=dic.get('性别', ''),
                                            candidateExp=txt2)
    return render(request, 'blog-single.html')


def addPos(request):
    def ma(txt):
        REG = re.compile('求职' + '.*')
        target = re.findall(REG, txt)
        try:
            s = target[0][5:]
            s = s.replace('\n', '')
            if len(s) > 15:
                return None
            else:
                return s
        except:
            return None

    objs = models.Candidate.objects.all()
    for i in objs:
        po = ma(i.candidateExp)
        if po is not None:
            i.candidatePos = po
        else:
            i.candidatePos = ''
        i.save()
    return HttpResponse('成功')

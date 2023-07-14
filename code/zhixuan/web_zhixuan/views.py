import base64
import re
from django.shortcuts import render, HttpResponse, redirect
from function3 import pie_degree, pie_age
from web_zhixuan import models
import function2, function1
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
from django.shortcuts import render,HttpResponse,redirect
from web_zhixuan.models import candidate
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import nor

name1 = ''



# Create your views here.


def about(request):
    c = {}
    position1 = ""
    description1 = ""
    d = {}
    a = dict()
    if request.method == 'POST':
        position = request.POST.get('position')
        position1 = str(position)
        description = request.POST.get('description')
        description1 = str(description)
        db = candidate.objects.all()
        lst=[]
        for person in db:
            d['姓名'] = person.candidateName
            d['年龄'] = person.candidateAge
            d['性别'] = person.candidateSex
            d['学历'] = person.candidateEdu
            d['工作年限'] = person.candidateYearsOfWork
            d['经历'] = person.candidateExp
            #d['求职意向'] = person.
            exp = person.candidateExp
            tf = match(exp,position,description)
            d['tf'] = tf
            if tf >0:
                lst.append([d,tf])
        lst.sort(key = lambda x:x[1],reverse=True)
        l = min(4,len(lst))
        for i in range(l):
            c['candidate'+str(i+1)] = lst[i]
    return render(request,"about.html",{"n0":position1,"n1":c,'n2':description1})


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


def updatePies(request):
    res = []
    d_sex = dict()
    d_degree = dict()
    d_age = dict()
    d_sex['男'] = 0
    d_sex['女'] = 0
    d_sex['未填'] = 0
    d_degree['博士'] = 0
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
    for i in models.Candidate.objects.all():
        txt = i.candidateExp
        d = function2.get_data(txt)  # func2中的
        try:
            d_sex[d['性别']] += 1
        except:
            d_sex['未填'] += 1
        try:
            d_degree[d['学历']] += 1
        except:
            d_degree['未知'] += 1
        try:
            if d['年龄'] < 30:
                d_age[1] += 1
            elif 30 <= d['年龄'] < 40:
                d_age[2] += 1
            else:
                d_age[3] += 1
        except:
            d_age['未知'] += 1
    res.append(d_age)
    res.append(d_degree)
    res.append(d_sex)

    # Generate pie charts
    fig_degree = Figure()
    ax_degree = fig_degree.add_subplot(111)
    pie_degree(res, ax_degree)
    canvas_degree = FigureCanvas(fig_degree)
    buf_degree = io.BytesIO()
    canvas_degree.print_png(buf_degree)
    plt.close(fig_degree)

    fig_age = Figure()
    ax_age = fig_age.add_subplot(111)
    pie_age(res, ax_age)
    canvas_age = FigureCanvas(fig_age)
    buf_age = io.BytesIO()
    canvas_age.print_png(buf_age)
    plt.close(fig_age)

    # Prepare chart data as base64 strings
    chart_degree = base64.b64encode(buf_degree.getvalue()).decode('utf-8')
    chart_age = base64.b64encode(buf_age.getvalue()).decode('utf-8')

    context = {
        'chart_degree': chart_degree,
        'chart_age': chart_age,
    }
    return render(request, 'teachers.html', context)

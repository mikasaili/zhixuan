from django.shortcuts import render,HttpResponse


# Create your views here.

def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def index(request):
    return render(request, "index.html")


def teachers(request):
    return render(request, "teachers.html")

def updateinfo(request):
    if request.method == 'POST':
        # img = request.FILES.get('photo')
        # user = request.FILES.get('photo').name
        new_img = models.zhixuanDB(
            photo=request.FILES.get('photo'),  # 拿到图片
           # user=request.FILES.get('photo').name # 拿到图片的名字
        )
        new_img.save()  # 保存图片
        return HttpResponse('上传成功！')

    return render(request, 'blog-single.html')

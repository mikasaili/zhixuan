from django.shortcuts import render,HttpResponse


# Create your views here.

def about(request):
    return render(request, "about.html")

def search(request):
    return render(request,"search.html")

def blog(request):
    return render(request, "blog.html")


def index(request):
        if request.method == "POST":
        if 'login_submit' in request.POST:
            # 用户选择了登录
            username = request.POST.get("username")
            password = request.POST.get("password")

            # 在数据库中查询用户密码
            user = models.userPassword.objects.get(name=username)
            if user.password == password:
                    # 用户名和密码匹配成功，跳转到 contact.html
                return redirect("/contact/")
            else:
                return redirect("/index/")
        elif 'register_submit' in request.POST:
            # 用户选择了注册
            username = request.POST.get("username")
            email = request.POST.get("email")
            telephone = request.POST.get("telephone")
            password = request.POST.get("password")

            # 创建新用户并保存到数据库
            models.userPassword.objects.create(name=username, eemail=email, telephone=telephone, password=password)
            return redirect("/contact/")
    else:
        # 处理 GET 请求，返回页面
        return render(request, 'index.html')
    return render(request, "index.html")


def teachers(request):
    return render(request, "teachers.html")

def updateinfo(request):
    if request.method == 'POST':
        # img = request.FILES.get('photo')
        # user = request.FILES.get('photo').name
        new_img = models.zhixuanDB(
            photo=request.FILES.get('photo'),  # 拿到图片
           www=request.FILES.get('photo').name # 拿到图片的名字
        )
        name1=request.FILES.get('photo').name
        new_img.save()  # 保存图片
        return HttpResponse('上传成功！')

    return render(request, 'blog-single.html')

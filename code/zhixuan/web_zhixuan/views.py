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

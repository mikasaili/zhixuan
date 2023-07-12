from django.shortcuts import render,HttpResponse


# Create your views here.

def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def blog_single(request):
    return render(request, "blog-single.html")


def contact(request):
    return render(request, "contact.html")


def course_grid2(request):
    return render(request, "course-grid-2.html")


def course_grid3(request):
    return render(request, "course-grid-3.html")


def course_grid4(request):
    return render(request, "course-grid-4.html")


def index(request):
    return render(request, "index.html")


def pricing(request):
    return render(request, "pricing.html")


def teachers(request):
    return render(request, "teachers.html")

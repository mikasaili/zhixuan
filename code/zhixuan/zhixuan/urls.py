"""zhixuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_zhixuan import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('about/', views.about),
    path('blog/', views.blog),
    path('blog_single/', views.blog_single),
    path('contact/', views.contact),
    path('course/grid2/', views.course_grid2),
    path('course/grid3/', views.course_grid3),
    path('course/grid4/', views.course_grid4),
    path('index/', views.index),
    path('pricing/', views.pricing),
    path('teachers/', views.teachers),
    path('admin/', admin.site.urls),
    path('updateinfo/', views.updateinfo),
    path('', views.index),
]


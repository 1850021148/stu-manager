"""djangoProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from stuManager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 第一个参数是路由, 第二个参数是要使用的view

    # core
    path(r'', views.index),
    path(r'login', views.login),
    path(r'register', views.register),
    path('manager/new', views.addStu),
    path('manager/findStuBySnoOrSname', views.findStuBySnoOrSname),
    path('manager/find', views.findStuList),
    path('manager/getTotalNo', views.getStuCount),
    path('manager/update', views.updateStu),
    path('manager/delete', views.delStuBySno),

    # test
    path(r'test', views.indexTest),
    path(r'loginTest', views.loginTest),
    path(r'registerPageTest', views.registerPageTest),
    path(r'registerTest', views.registerTest),
]

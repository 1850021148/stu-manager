import json
import re

from django.shortcuts import render

from .models import User, Manager, Student
from django.http import HttpResponse
from django.http.response import JsonResponse

# Create your views here.

# core

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def login(request):
    if request.method == 'POST' and request.body:
        body = json.loads(request.body.decode())
        name, password = body['name'], body['password']
        manager = Manager.objects.get(name=name)
        if password == manager.password: # 登录成功
            print('登录成功: ', body)
            request.session.get('islogin', True)
            return JsonResponse({
                "data": {
                    "msg": "success"
                }
            })
        else: # 登录失败
            print('登录失败: ', body)
            return JsonResponse({
                "data": {
                    "msg": "error"
                }
            })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def register(request):
    if request.method == 'POST' and request.body:
        body = json.loads(request.body.decode())
        name, password = body['name'], body['password']
        result = Manager.objects.filter(name=name).exists()
        if len(name) == 10 and not result: # 注册成功
            print('注册成功: ', body)
            request.session.get('islogin', True)
            Manager.objects.create(name=name, password=password)
            return JsonResponse({
                "data": {
                    "msg": "success"
                }
            })
        else: # 注册失败
            print('注册失败: ', body)
            return JsonResponse({
                "data": {
                    "msg": "error"
                }
            })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def addStu(request):
    if request.method == 'POST' and request.body:
        body = json.loads(request.body.decode())
        if re.match(r'^\d{10}$', body['sno']) and re.match(r'^\D{2,5}$', body['sname']):
            print('新增学生信息成功: ', body)
            Student.objects.create(
                sno=body['sno'],
                sname=body['sname'],
                sex=body['sex'],
                age=body['age'],
                pro=body['pro'],
                address=body['address']
            )
            return JsonResponse({
                "data": {
                    "msg": "success"
                }
            })
        else:
            print('新增学生信息失败: ', body)
            return JsonResponse({
                "data": {
                    "msg": "error"
                }
            })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def findStuBySnoOrSname(request):
    if request.method == 'GET' and request.GET and request.GET['keyword']:
        keyword = request.GET['keyword']
        result1 = Student.objects.filter(sno=keyword)
        result2 = Student.objects.filter(sname=keyword)
        if result1.exists():
            result1 = result1.get(sno=keyword)
            print('查询学生信息成功: ', result1.sname, result1.sno)
            return JsonResponse({
                "data": {
                    "sno": result1.sno,
                    "sname": result1.sname,
                    "sex": result1.sex,
                    "age": result1.age,
                    "pro": result1.pro,
                    "address": result1.address
                }
            })
        elif result2.exists():
            result2 = result2.get(sname=keyword)
            print('查询学生信息成功: ', result2.sname, result2.sno)
            return JsonResponse({
                "data": {
                    "sno": result2.sno,
                    "sname": result2.sname,
                    "sex": result2.sex,
                    "age": result2.age,
                    "pro": result2.pro,
                    "address": result2.address
                }
            })
        else:
            print('修改学生信息失败: ', keyword)
            return JsonResponse({
                "data": {
                    "msg": "error"
                }
            })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def findStuList(request):
    if request.method == 'GET':
        startIndex = int(request.GET['startIndex']) \
            if request.GET and request.GET['startIndex'] and re.match(r'^\d*$', request.GET['startIndex']) \
            else 0
        size = int(request.GET['size']) \
            if request.GET and request.GET['size'] and re.match(r'^\d*$', request.GET['size']) \
            else 8
        stuList = Student.objects.all()[startIndex:startIndex+size]
        str = '| '
        _stuList = []
        for stu in stuList:
            str += stu.sname + ' | '
            _stuList.append({
                "sno": stu.sno,
                "sname": stu.sname,
                "sex": stu.sex,
                "age": stu.age,
                "pro": stu.pro,
                "address": stu.address
            })
        print('查询到以下学生: ', str)
        return JsonResponse({
            "data": _stuList
        })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def getStuCount(request):
    return JsonResponse({
      "data": {
        "number": Student.objects.count(),
      }
    })

def updateStu(request):
    if request.method == 'POST' and request.body:
        body = json.loads(request.body.decode())
        if re.match(r'^\d{10}$', body['beforeSno']) and re.match(r'^\d{10}$', body['sno']) and re.match(r'^\D{2,5}$', body['sname']):
            result = Student.objects.filter(sno=body['beforeSno'])
            if result.exists():
                result.update(
                    sno=body['sno'],
                    sname=body['sname'],
                    sex=body['sex'],
                    age=body['age'],
                    pro=body['pro'],
                    address=body['address']
                )
                print('修改学生信息成功: ', body)
                return JsonResponse({
                    "data": {
                        "msg": "success"
                    }
                })
        print('修改学生信息失败: ', body)
        return JsonResponse({
            "data": {
                "msg": "error"
            }
        })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')

def delStuBySno(request):
    if request.method == 'GET' and request.GET and request.GET['sno']:
        sno = request.GET['sno']
        result = Student.objects.filter(sno=sno)
        if result.exists():
            result = result.get(sno=sno)
            result.delete()
            print('删除成功: ', result.sname, '  ', sno)
            return JsonResponse({
              "data": {
                "msg": 'success',
              }
            })
        else:
            print('学号不存在,删除失败: ', sno)
            return JsonResponse({
                "data": {
                    "msg": 'error',
                }
            })
    else:
        return HttpResponse('<h1>404</h1><a href="/#/index">点击此处返回首页</a>')


# test

def indexTest(request):
    return render(request, 'indexTest.html')

def registerPageTest(request):
    return render(request, 'registerPageTest.html')

def loginTest(request):
    if request.method == 'POST':
        name, password = request.POST['name'], request.POST['password']
        print('登录成功', name, password)
        return render(request, 'coreTest.html', context={
            'data': {
                'msg': 'success'
            }
        })
    else:
        return HttpResponse("<a href='./test'>404...from juln</a>")

def registerTest(request):
    if request.method == 'POST':
        name, password = request.POST['name'], request.POST['password']
        print('注册成功', name, password)
        User.objects.create(name=name, password=password)
        return render(request, 'coreTest.html', context={
            'data': {
                'msg': 'success'
            }
        })
    else:
        return HttpResponse("<a href='./test'>404...from juln</a>")
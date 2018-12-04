from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>Hello Test App</h1>')


def login(request):
    # f = open('templates/login.html','r',encoding='utf-8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    return render(request,'login.html') # 打开 templates 目录下的 login.html 文件返回给浏览器，此方法html文件必须放在templates目录下;templates 目录可以放在工程根目录或app目录下。

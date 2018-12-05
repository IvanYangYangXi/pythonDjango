from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse # 返回内容函数
from django.shortcuts import render # 读取文件并返回内容函数
from django.shortcuts import redirect # 重定向函数


def home(request):
    return HttpResponse('<h1>Hello Test App</h1>')


def loginSimple(request):
    # f = open('templates/login.html','r',encoding='utf-8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    return render(request,'login.html') # 打开 templates 目录下的 login.html 文件返回给浏览器，此方法html文件必须放在templates目录下;templates 目录可以放在工程根目录或app目录下。


def login(request):
    
    error_msg = "" # 提示信息
    if request.method == 'POST':
        #获得表单数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'user1' and pwd == '123':
            return redirect('http://ivan.cgartech.com') # 跳转到……
        else:
            error_msg = '用户名或密码错误'
    
    return render(request, 'login.html', {'error_msg':error_msg}) 
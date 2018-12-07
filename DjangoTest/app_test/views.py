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
        # 获得表单数据
        # a = request.GET('a') # GET方法
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'user1' and pwd == '123':
            return redirect('http://ivan.cgartech.com') # 跳转到……
        else:
            error_msg = '用户名或密码错误'
        # 获取上传文件
        obj = request.FILES.get('file')
        print(obj, type(obj), obj.name)
        import os
        file_path = os.path.join('app_test/media', obj.name) # 路径拼接
        f = open(file_path, mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()

    return render(request, 'login.html', {'error_msg':error_msg}) 


# 数据库操作
from app_test import models
def orm(request):
    # 创建
    
    obj = models.UserInfo(username='ivan',password='123',salary='1')
    obj.save()

    dic = {'username':'disUser', 'password':'666','salary':'1'}
    models.UserInfo.objects.create(**dic)

    models.UserInfo.objects.create(username='root',password='123',salary='1')

    # 查
    # result = models.UserInfo.objects.all()
    # models.UserInfo.objects.all()[:10] 切片操作，获取10个数据，不支持负索引
    result = models.UserInfo.objects.filter(username='root')
    print(result)
    # 打印查找到的所有内容
    for row in result:
        print(row.id, row.username, row.password)

    # 删除
    models.UserInfo.objects.filter(username='root').delete()

    # 更新
    models.UserInfo.objects.filter(id=2).update(password='6699')

    return HttpResponse('orm')
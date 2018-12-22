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


def loginTest(request):
    
    error_msg = "" # 提示信息
    if request.method == 'POST':
        # 获得表单数据
        # a = request.GET('a') # GET方法
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'user1' and pwd == '123':
            return redirect('http://ivan.cgartech.com') # 跳转到……
            # json_data = {'errorcode': 100, 'detail': 'Get success'}
            # return HttpResponse(json_data,content_type="application/json") # 返回 JSON 格式数据
        else:
            error_msg = '用户名或密码错误'
        # 获取上传文件
        obj = request.FILES.get('file')
        if obj is not None:
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
    # 方式一：
    obj = models.UserInfo(username='ivan',password='123')
    obj.save()
    # 方式二：
    dic = {'username':'disUser', 'password':'666'}
    models.UserInfo.objects.create(**dic)
    # 方式三：
    models.UserInfo.objects.create(username='root',password='123')

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


# 注册
def signUp(request):
    error_msg = "" # 提示信息
    if request.method == 'POST':
        # 获得表单数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == None or pwd == None:
            error_msg = '用户名或密码不能为空'
        else:
            # 验证用户名密码
            result = models.UserInfo.objects.filter(username=user)
            if len(result) == 0:            
                models.UserInfo.objects.create(username=user, password=pwd)
                error_msg = '用户创建成功'
            else:
                error_msg = '用户名已存在'

    return render(request, 'signUp.html', {'error_msg':error_msg})

import json
# 游戏注册
def gameSignUp(request):
    error_msg = "" # 提示信息
    if request.method == 'POST':
         # 获得JSON数据
        req = json.loads(request.body)
        user = req.get('user') # user = req['user'] ,此方法 user 必须存在，否则报错，所以使用 get() 方法
        pwd = req.get('pwd')
        if user == None or pwd == None:
            error_msg = 'Username or password cannot be empty'
        else:
            # 验证用户名密码
            result = models.UserInfo.objects.filter(username=user)
            if len(result) == 0:            
                models.UserInfo.objects.create(username=user, password=pwd)
                error_msg = 'User creation success'
            else:
                error_msg = 'Username already exists'

    json_data = {'errorcode': 100, 'msg': error_msg}
    return HttpResponse(json.dumps(json_data),content_type="application/json") # 返回 JSON 格式数据 


# 游戏登录
def gamelogin(request):
    error_msg = "" # 提示信息
    if request.method == 'POST':
        # 获得JSON数据
        req = json.loads(request.body)
        user = req.get('user')
        pwd = req.get('pwd')
        if user == None or pwd == None:
            error_msg = 'username or password is none'
        else:
            # 验证用户名密码
            result = models.UserInfo.objects.filter(username=user)
            if len(result) == 0:            
                error_msg = 'username does not exist'
            elif result[0].password == pwd:
                error_msg = 'Login successfully'
            else:
                error_msg = 'ERROR Incorrect username or password'
                

    json_data = {'errorcode': 101, 'msg': error_msg}
    return HttpResponse(json.dumps(json_data),content_type="application/json") # 返回 JSON 格式数据 
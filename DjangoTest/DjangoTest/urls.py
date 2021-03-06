"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app_test import views # 建立app的url连接

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'h.html', views.home), # 访问http://127.0.0.1:8001/h.html 返回app的home函数值
    path(r'loginSimple', views.loginSimple), # 访问http://127.0.0.1:8001/loginSimple 返回app的 loginSimple 函数值
    path(r'loginTest', views.loginTest), # 访问http://127.0.0.1:8001/login 返回app的 login 函数值
    path('orm/', views.orm),
    path('signUp/',views.signUp),
    path('gameSignUp/',views.gameSignUp),
    path('gamelogin/',views.gamelogin)

]

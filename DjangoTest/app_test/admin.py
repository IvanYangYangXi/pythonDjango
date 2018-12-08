from django.contrib import admin

# Register your models here.


from app_test.models import UserInfo,UserGroup,AddData

# 注册 models 的类
admin.site.register([UserInfo,UserGroup,AddData]) # 注意 register 的‘r’为小写
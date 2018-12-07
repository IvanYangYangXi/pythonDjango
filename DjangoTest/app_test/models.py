from django.db import models

# Create your models here.

# 定义数据结构
class userinfo(models.Model):
    # id 列，自动创建，主键
    # 用户名、密码及一个参数列，设置数据最大长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    salary = models.IntegerField()
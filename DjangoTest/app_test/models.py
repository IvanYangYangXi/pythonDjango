from django.db import models

# Create your models here.

# 定义数据结构
class UserInfo(models.Model):
    # id 列，自动创建，主键
    # 用户名、密码及一个整数参数列，设置数据最大长度
    username = models.CharField(max_length=32, verbose_name='姓名')
    password = models.CharField(max_length=32)

    # 返回模型的字符串表示
    def __str__(self):
        return self.username


# 外键关联（一对一关联，要实现一对多，只需要把关联写到用户信息类中即可）
class AddData(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE) # 以 UserInfo 为外键, django2.0 下 on_delete 为必选参数
    data = models.CharField(max_length=64)
    def __str__(self):
        return self.data



# 多对多须通过第三张表实现

# 自动多对多(用户组与用户关联)
class UserGroup(models.Model):
    groupName = models.CharField(max_length=32, verbose_name='用户组')
    user_group = models.ManyToManyField('UserInfo')

# 第三张操作
    # obj = UserGroup.objects.get(id=1)
    # obj.user_group.add(1) # 增加对映关系
    # obj.user_group.add(2,3,4) # 增加多个对映关系
    # obj.user_group.add(*[2,3,4]) # 增加多个对映关系

    # obj.user_group.remove(1) # 删除对映关系
    # obj.user_group.remove(2,3,4)
    # obj.user_group.remove(*[2,3,4])

    # obj.user_group.clear() # 清除

    # obj.set([2,3,4]) # 覆盖设置

    # obj.user_group.all() # 获得所有




# 手动多对多关联
class UserGroup2(models.Model):
    uObj = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    gObj = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
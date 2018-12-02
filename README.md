Start Django
================

# 环境配置
  1. Python
  2. Django


# Django基本命令
## 创建django工程
  1. 进入cmd，切换当需要创建项目的路径
  2. 执行以下命令创建工程：django-admin startproject 工程名称

### 项目文件说明
  - **Django工程/** :项目的容器，它的名字与Django无关，可以将它重命名为任何任何名字
      - **Django 目录/** :是项目的实际python包，它的名字是你需要用来导入任何内容的python包名
          - **__init__.py**：一个空文件，告诉Python该目录是一个Python包
          - **settings.py**：该Django项目的设置/配置。
          - **urls.py**：该Django项目的URL声明，一份由Django驱动的网站“目录”
          - **wsgi.py**：一个WSGI兼容的Web服务器的入口，以便运行你的项目
      - **manage.py**：一个实用的命令行工具，可让你以各种方式与该Django项目进行交互。


### 开启django服务器
  - 执行命令：python manage.py runserver 8001
      - 如果VScode提示：'python' 不是内部或外部命令，也不是可运行的程序或批处理文件。
      - 解决方案：
          - 方案1： 在‘manage.py’文件上右键，选择‘在终端打开’，再运行上面的命令
          - 方案2： 在环境变量中添加python路径
  - 在浏览器上输入：http://localhost:8001


## 新建app
  1. 切换到项目目录下
  2. 执行命令：python manage.py startapp app_name
  3. 或者django-admin.py startapp app-name

### app目录
  - **migrations** ： 数据表结构
  - **admin**： Django为我们提供的后台管理
  - **apps**： 配置当前app
  - **models**： ORM，写指定的类；通过命令可以创建数据结构
  - **tests**： 单元测试
  - **views**： 业务代码


## 创建数据库表或更改数据库表或字段

### 在APP的models中建立类数据模版
  ```
  class userinfo(models.Model):
      username = models.CharField(max_length=32)
      password = models.CharField(max_length=32)
      salary = models.IntegerField()
  ```

### 全局配置文件settings.py里的INSTALLED_APPS中加入App名字
  ```
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'app_test', # My App
  ]
  ```

### 生成配置文件：
  执行以下命令:
  ```
  python manage.py makemigrations app_name
  ```
  >将模式加入缓存，此时会返回以下内容:
  Migrations for 'app_test':
      app_test\migrations\0001_initial.py
          - Create model userinfo

### 根据配置文件粗昂居数据库相关表：
  执行以下命令创建与models代码相对应的表:
  ```
  python manage.py migrate
  ```
  >返回以下内容:
  Operations to perform:
      Apply all migrations: admin, app01, auth, contenttypes, sessions
  Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying app01.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying sessions.0001_initial... OK
    

## 常用命令
  - 开发服务器使用：
      ```      
      python manage.py runserver 0.0.0.0:8000
      ```
  - 清空数据库:
      ```
      python manage.py flush
      ```
      >此命令会把数据全部清空掉，只留下空表
  - 创建超级管理员:
      ```
      python manage.py createsuperuser 
      ```
      >根据提示输入用户名、邮箱和密码，邮箱可以为空
      ```
      python manage.py changepassword username
      ```
      >修改用户密码
  - 导出数据和导入数据:
      - 导出数据:
          ```
          python manage.py dumpdata appname > appname.json
          ```
      - 导入数据：
          ```
          python manage.py loaddata appname.json
          ```
  - 更多命令:
      - 项目环境终端：python manage.py shell
      - 数据库命令行：python manage.py dbshell
      - 查看命令：python manage.py


# 项目视图、网址、URL、模块、模型http://www.cnblogs.com/zhangxinqi/p/8969006.html?tdsourcetag=s_pctim_aiomsg#_label2

## 在 app 的 views 里添加业务代码

## 在 urls 里指定 url 连接
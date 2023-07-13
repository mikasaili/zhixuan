# 文件内容说明
**zhixuan**是基于django的web文件夹。

注意：
+ 文件夹中没有包含全部文件，只添加了需要修改代码内容的文件。
+ 所有已经添加的文件是按照本地文件结构上传的，层次嵌套关系不要改变。

# 数据库安装
1. 安装MySQL

   + 参考教程：https://blog.csdn.net/weixin_39289696/article/details/128850498

   + 记住密码！！我设的密码是mysql。

2. 安装 mysqlclient  

   + pip大概率会报错

   + 可以去网上搜mysqlclient.wheel，下载对应的版本，然后安装这个wheel

3. 创建数据库

   + 启动mysql服务
   + 创建数据库
     + `create database zhixuanDB DEFAULT CHARSET utf8 COLLATE utf8_general_ci;`
     + zhixuanDB是数据库名

4. django连接数据库

   + 在settings.py中，修改

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'zhixuanDB',      
           'USER': 'root',
           'PASSWORD': 'mysql',
           'HOST': 'localhost',
           'PORT': 3306,
       }
   }
   ```

5. 创建、修改、删除表

   + 在models.py中，写代码

   ```python
   from django.db import models
   
   class UserInfo(models.Model):                 # 创建表
       name = models.CharField(max_length=32)    # name varchar(32)
       password = models.CharField(max_length=64)   # password varchar(64)
       age = models.IntegerField()  # age int
   ```

   + 注意：如果已经生成过这个表，现在想要修改表结构，比如增加一列id，那么需要给定初始值`id=models.CharField(default=2)`

   + 执行命令（两个都要执行）
     + `python manage.py makemigrations`
     + `python manage.py migrate`
   + 检查是否创建这个表【可选】
     + 去mysql服务器中，
     + `use zhixuanDB;`
       `show columns from web_zhixuanDB_candidate;`

6. 添加表内容
   
   + 可以在models.py中直接写类名.objects.create(name=””,…)
   + 可以在views中添加函数

总之，b站有一个课讲的很好：[django-数据库指路](https://www.bilibili.com/video/BV183411N7Lx/?buvid=XY0F5270EE0C69C91F5ED56C2C15ED5B3E978&is_story_h5=false&mid=XpRg6s7gZQU3zWLHjcW9aA%3D%3D&p=3&plat_id=114&share_from=ugc&share_medium=android&share_plat=android&share_session_id=fb6f79dd-4a96-47f0-9432-026cb4d7c2f4&share_source=COPY&share_tag=s_i&timestamp=1689050201&unique_k=sT4PBp1&up_id=2052067002&vd_source=713c7edde91b9f295c48c8835f0614e4)




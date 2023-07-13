from django.db import models
import pandas as pd
import random
# Create your models here.



'''

'''
class zhixuanDB(models.Model):
    photo = models.FileField(upload_to='files/')
    www = models.CharField(max_length=64, default='user1')


'''
创建表
'''
class userPassword(models.Model):
    name = models.CharField(verbose_name="name",max_length=32)
    eemail = models.CharField(verbose_name="email",max_length=64)
    telephone = models.CharField(verbose_name="telephone",max_length=13)
    password = models.CharField(verbose_name="password",max_length=64)


class Company(models.Model):  # 公司
    companyName = models.CharField(max_length=32, primary_key=True)


class Candidate(models.Model):    # 应聘者
    # candidateID = models.AutoField(primary_key=True)  # 新增的自增序号字段
    candidateName = models.CharField(max_length=32, primary_key=True)
    candidateAge = models.IntegerField(null=True)
    candidateSex = models.CharField(max_length=64, null=True)
    candidateEdu = models.CharField(max_length=64, null=True)  # 学历
    candidateYearsOfWork = models.IntegerField(default=0)    # 工作经历/年
    candidateExp = models.TextField(max_length=None)  # 经历
    candidatePos = models.CharField(max_length=64, null=True)


class Department(models.Model):  # 部门
    departmentID = models.IntegerField(primary_key=True)
    departmentName = models.CharField(max_length=32)


class Position(models.Model):    # 岗位
    positionName = models.CharField(max_length=32, primary_key=True)
    positionNum = models.IntegerField()   # 需要人数


# positions = [
#     "市场总监",
#     "市场专员",
#     "设计师",
#     "市场运营专员",
#     "简历设计师",
#     "设计市场专员",
#     "产品经理",
#     "行政专员",
#     "医护",
#     "电气工程师",
#     "市场营销总监",
#     "财务相关",
#     "国际贸易",
#     "产品开发",
#     "会计",
#     "产品设计",
#     "检验相关",
#     "理财分析师",
#     "教师",
#     "编辑",
#     "运营经理",
#     "行政管理类"
# ]
#
# for i in positions:   # 可行
#     Position.objects.get_or_create(positionName=i, positionNum=random.randint(1, 21))


# import function1
# df = pd.read_excel(r'F:\CODE_Djiango\dataset_CV\CV\ground_truth.xlsx')
# lstExp = function1.getEXPList()
# # 将读取的数据保存到数据库中
# j = 1
# for _, row in df.iterrows():
#     if j>100:
#         break
#     candidate_name = row['姓名']
#     candidate_age = row['年龄']
#     candidate_edu = row['最高学历']
#     candidate_years = row['工作年限']
#
#     # 创建 Candidate 对象并保存到数据库
#     Candidate.objects.create(
#         candidateName=candidate_name,
#         candidateAge=candidate_age,
#         candidateEdu=candidate_edu,
#         candidateYearsOfWork=candidate_years,
#         candidateExp=lstExp[j],
#         candidateSex=random.choice(['男', '女'])
#     )
#     j += 1


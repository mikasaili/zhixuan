from django.db import models
import pandas as pd
import random
# Create your models here.

# 想再创建一个表，就再写一个class

'''
这部分是创建表，可以进行修改。
'''
class Company(models.Model):  # 公司
    companyName = models.CharField(max_length=32, primary_key=True)

class zhixuanDB(models.Model):
    www = models.CharField(max_length=64, default='user1')
    photo = models.FileField(upload_to='files/')
    
class Candidate(models.Model):    # 应聘者
    candidateName = models.CharField(max_length=32, primary_key=True)
    candidateAge = models.IntegerField()
    candidateSex = models.CharField(max_length=64)
    candidateEdu = models.CharField(max_length=64)  # 学历
    candidateYearsOfWork = models.IntegerField(default=0)    # 工作经历/年
    candidateExp = models.TextField(max_length=None)  # 经历


class Department(models.Model):  # 部门
    departmentID = models.IntegerField(primary_key=True)
    departmentName = models.CharField(max_length=32)


class Position(models.Model):    # 岗位
    positionName = models.CharField(max_length=32, primary_key=True)
    positionNum = models.IntegerField()   # 需要人数


'''
以下内容，运行一遍之后，就注释掉，不要重复运行。设置了主键，不能重复添加相同的数据。
'''
positions = [
    "市场总监",
    "市场专员",
    "设计师",
    "市场运营专员",
    "简历设计师",
    "设计市场专员",
    "产品经理",
    "行政专员",
    "医护",
    "电气工程师",
    "市场营销总监",
    "财务相关",
    "国际贸易",
    "产品开发",
    "会计",
    "产品设计",
    "检验相关",
    "理财分析师",
    "教师",
    "编辑",
    "运营经理",
    "行政管理类"
]

for i in positions:   # 可行
    Position.objects.get_or_create(positionName=i, positionNum=random.randint(1, 21))

# 读取所有的candidate，录入表
df = pd.read_excel(r'F:\CODE_Djiango\dataset_CV\CV\ground_truth.xlsx')

# 将读取的数据保存到数据库中
for _, row in df.iterrows():
    candidate_name = row['姓名']
    candidate_age = row['年龄']
    candidate_edu = row['最高学历']
    candidate_years = row['工作年限']

    # 创建 Candidate 对象并保存到数据库
    Candidate.objects.create(
        candidateName=candidate_name,
        candidateAge=candidate_age,
        candidateEdu=candidate_edu,
        candidateYearsOfWork=candidate_years
    )

from django.db import models
import datetime
from user.models import User

# 课程种类表
class Category(models.Model):
    name= models.CharField(max_length=50,unique=True,verbose_name='课程种类')

# 课程表
class Course(models.Model):
    courseName=models.CharField(max_length=40, verbose_name='课程名称')
    fileName=models.FileField(verbose_name='文件名称')
    imgname=models.IntegerField(verbose_name='课程图片')
    pCategory=models.ForeignKey(to=Category,related_name='courses_set',on_delete=models.CASCADE,verbose_name='课程类别')
    price=models.DecimalField(max_digits=7,decimal_places=2,default=0,verbose_name='售价')
    summary=models.CharField(max_length=1000,default='',verbose_name='课程介绍')
    status=models.PositiveSmallIntegerField(default=0,verbose_name='状态')
    createDatetime=models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    userBuyer=models.ManyToManyField(to=User,related_name='userBuyer_set',verbose_name='购买用户')
    userShopingCart=models.ManyToManyField(to=User,related_name='userShoppingcart',verbose_name='加入购物车的用户')
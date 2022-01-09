from django.db import models

# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=16,unique=True,verbose_name='账号')
    password = models.CharField(max_length=16,verbose_name='密码')
    username=models.CharField(max_length=16,verbose_name='用户名')
    money=models.DecimalField(max_digits=12,decimal_places=2,default=0,verbose_name='余额')
    gender=models.PositiveSmallIntegerField(default=0,verbose_name='性别')
    tel= models.CharField(max_length=11,default='',verbose_name='手机号')
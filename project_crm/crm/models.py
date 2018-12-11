from django.db import models

# Create your models here.
class DepartMent(models.Model):
    """
    部门表
    """
    title = models.CharField(verbose_name="部门名称",max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    email = models.EmailField(verbose_name='邮箱',max_length=128)
    gender_choice = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.IntegerField(verbose_name='性别',choices=gender_choice)
    depart = models.ForeignKey(verbose_name="所在部门",to='DepartMent')
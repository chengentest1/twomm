from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=32)
class UserInfo(models.Model):
    #用户名列，字符串类型，指定长度
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    email=models.CharField(max_length=60)
    test=models.EmailField(max_length=19,null=True)
    user_type_choices=(
        (1,'超级用户'),
        (2, '普通用户'),
        (3, '普普通用户'),
    )
    user_type_id=models.IntegerField(choices=user_type_choices,default=1)
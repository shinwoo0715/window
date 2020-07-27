from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime , timezone , timedelta
import os , sys

# Create your models here.

def uploadpath(instance, filename):
    path = '{username}/{datetime}/{filename}'.format(
        # datetime=datetime.now().strftime('%Y%m%d%H%M%S'),
        datetime=datetime.now().strftime('%Y%m%d'), # year month day 까지
        username=instance.사용자.username,
        filename=filename

        )
    print('path:', path)
    return path

#request.GET.get('...' , '') # 여기서 get() : 뒤에 아무것도 안적혀있는거는 없는 경우 공백을 가져온다.


def roadUsername(username):
    username = username
    print('model username : ', username)
    return username

def roadUserid(userid):
    userid = userid
    print('model userid : ', userid)
    return userid



class Photo(models.Model):
    사용자 = models.ForeignKey(User, on_delete=models.CASCADE , default=1)
    사진 = models.ImageField(blank=False, upload_to=uploadpath)
    # content=models.TextField(max_length=100 , blank=True , null=True)
    content=models.CharField(max_length=100)
    postdate = models.DateField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

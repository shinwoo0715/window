from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
import os , sys
from PIL import Image
import mimetypes
from django.forms.fields import FilePathField
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import auth



sys.path.insert(0, "D:/shinwoo/workspace/window/updown")
from updown import form
from updown.form import PhotoForm
# from updown.views import index
from updown import models
from updown.models import Photo


# username = User.objects.get(username=userid)
# username을 찾아샤 밑에 thumbnail이랑 username이랑 바꿀수 잇따. 그럼
# media에 username과 같은 파일을 찾아서 그 사진을 가져올수 있다.
# print('유저네임을 출력합니다.',username)


def index(request):
    # username = User.objects.get(username=userid)
    allowedFileType = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    # fileList = os.listdir(settings.MEDIA_ROOT)
    fileList = os.walk(settings.MEDIA_ROOT)
    print('fileList 를 출력 : ', fileList)

    # context = {'fileList':fileList}

    if request.method == 'GET':
        print('get방식으로 if문 도달')
        post = models.Photo.objects.all().order_by('-create_date')
        # 오름차순으로 하고싶으면 앞에 '-' 를 없에면된다.
        print(post)
        context = {'post' : post}


    return render(request , 'index.html' , context=context)


def about(request):
    return render(request , 'about.html')

def service(request):
    return render(request , 'service.html')

def inquiry(request):
    return render(request , 'inquiry.html')


def myfage(request , userid):
    print("#### myfage ####")
    # # username = User.objects.get(username=userid)
    # allowedFileType = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    # # fileList = os.listdir(settings.MEDIA_ROOT)
    # fileList = os.walk(settings.MEDIA_ROOT)
    # print('fileList 를 출력 : ', fileList)
    #
    #
    # context = {'fileList':fileList}
    #
    # if request.method == 'GET':
    #     print('get방식으로 if문 도달')
    #     post = models.Photo.objects.get()
    #     print(post)
    #     context = {'post' : post}
    if request.method == 'GET':
        print(userid)
        username = User.objects.get(id=userid)
        print('username : ', username)
        myfage = Photo.objects.filter(사용자=username).order_by('-create_date')
        print(myfage)
        context = {
            'post' : myfage
        }


    return render(request , 'myfage.html' , context)

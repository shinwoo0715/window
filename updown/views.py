from django.shortcuts import render , redirect ,get_object_or_404
from django.conf import settings
import os
from PIL import Image
import mimetypes
from django.forms.fields import FilePathField
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from updown import form
from .form import PhotoForm
from .models import Photo, roadUserid , roadUserid
from django.contrib.auth.models import User
from django.contrib import messages

def createFolder(directory):
    directory = str(directory)
    directory.replace("\\" , '/')
    print('함수안에변경후 디렉토리 : ',directory)

    try:
        if not os.path.isdir(directory):
            os.mkdir(directory)
    except OSError:
        print('Error에러다임마: Creating directory. '+ directory)



#
# def upload(request , userid):
#     context = {}
#     print("-"*30)
#     username = User.objects.get(id=userid)
#     print('username : ',username)
#     allowedFileType = ['.jpg', '.png', '.gif', '.jpeg', '.webp', '.heic']
#
#     if request.method == 'POST':
#         form = PhotoForm(request.POST , request.FILES)
#         print("upload의 form을 post방식으로 전달")
#         print("form : \n" , form)
#
#         if form.is_valid():
#             print("[ 이 데이터는 유효합니다. ]")
#             for file in request.FILE.getlist('uploadFiles'):
#                 extension = os.path.splitext(str(file))[-1].lower()
#
#                 if extension in allowedFileType:
#
#                     # 폴더 생성
#                     directory = str(settings.MEDIA_ROOT +"\\"+str(username))
#                     createFolder(directory)
#
#                     uploadFile = open(settings.MEDIA_ROOT +"\\"+str(username) +"\\" + str(file), 'wb')
#                     for chunk in file.chunks():
#                         uploadFile.write(chunk)
#             form.save()
#             print("form 저장")
#
#             context = {
#             'form' : form
#             }
#             return redirect("index")
#
#
#     return render(request , 'updown/upload.html' , context=context or None)

def upload(request , userid):
    print('---------------------------------')
    form = PhotoForm(request.POST)
    if request.method == 'POST':
        print('post 진입')
        username = User.objects.get(id=userid)
        form = PhotoForm(request.POST , request.FILES)
        if form.is_valid():
            print('is_valid() 진입')
            form = form.save(commit=False)
            form.사용자 = request.user
            form.save()

            return redirect("index")

    context = {
        'form' : form
    }
    return render(request ,'updown/upload.html' ,context=context)

def download(request):
    context = {

    }
    return render(request , 'updown/download.html' , context=context)



def change(request, photoid):
    data = get_object_or_404(Photo , id=photoid)
    print('data : ',data ,'\n','photoid : ', photoid)

    if request.user != data.사용자:
        messages.warning(request , '권한 없읍')
        return redirect('index')

    if request.method == 'POST': # 글을 수정사항을 입력하고 제출을 눌렀을 때
        print("(change)post 진입")
        form = PhotoForm(request.POST,  request.FILES , instance=data)

        if form.is_valid():
            print("form.is_valid() 진입")

            # data = form.save(commit=False)
            # data.save()
            form.save()
            print("수정 데이터 저장 완료")
            return redirect('index')

        else:
            return render(request , 'updown/fail.html')
    else: # 수정사항을 입력하기 위해 페이지를 처음 접속 했을때
        data = Photo.objects.get(id=photoid)
        form = PhotoForm(instance=data)
        context = {
            'data' : data,
            'form' : form
        }
    return render(request , 'updown/detail.html' , context=context)


def delete(request , photoid):
    print('-'*20)
    data = Photo.objects.get(id=photoid)

    if request.user != data.사용자 and not request.user.is_staff:
        messages.warning(request , '권한 없음')
        return redirect('index')

    if request.method == 'POST':
        os.remove(data.사진.path)

        data.delete()

        print("블로그 삭제 Success!!")
        return redirect("index")

    return render(request , 'updown/delete.html')




def index(request):
    allowedFileType = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    fileList = os.listdir(settings.MEDIA_ROOT + "/thumbnail/")
    # listdir() = 디렉터리 스캔 함수, 자식 디렉터리는 검색 X
    # 만약에 내부폴더까지 검색 하고 싶으면 walk() 함수를 사용
    for file in fileList[:]:
        if not mimetypes.guess_type(file, strict=True)[0] in allowedFileType:
            fileList.remove(file)
    context = {'imageList':fileList}


    if request.method == 'POST':
        form = PhotoForm(request.POST , request.FILES)
        if form.is_valid(): # 유효성 검사
            form.save()
            return redirect('UD:index')
    else:
        form = PhotoForm() #

    context['form'] = form # context 에 form 을 추가한것이다.
    return render(request, 'updown/index.html', context)



def fail(request):
    return render(request , 'updown/fail.html')

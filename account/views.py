from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from .form import SignupForm
from django.contrib import auth
from django.http import HttpResponseRedirect
# from django.forms import LoginForm

def signup(request):
    print("signup views에 도착함")
    if request.method == 'POST':
        print("포스트 방식으로 request 받음")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pw")

        print("username : ", username,'\nemial : ',email ,'\npassword : ',password)

        # form = SignupForm(request.POST)

        # if form.is_valid():
            # print("유효성검사 succes")
        User.objects.create_user(username, email, password)
        print("")
            # form.save()
            # print("form 저장 완료!")
        return redirect('AC:login')

    return render(request , 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('userpw')
        print('password : ',password , "\nemail : ", email)
        user =  auth.authenticate(request, username=username ,password=password ,email=email)
        print("user : ", user)

        if user is not None:
            print("로그인 성공")
            auth.login(request, user)
            return redirect("index")
            # return HttpResponseRedirect(request.POST['path'])
        else:
            print("로그인 실패")

            return render(request , 'registration/login.html')

    return render(request , 'registration/login.html')

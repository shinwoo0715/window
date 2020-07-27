from django.contrib import admin
from django.urls import path , re_path , include
from . import views

app_name = 'AC'

urlpatterns = [
    # path('login/', views.login , name='login'),
    path("login/" , views.login , name='login'),
    re_path(r'^signup/' , views.signup , name='signup'),
    re_path('^', include('django.contrib.auth.urls')),
    # path("logout/" , views.logout, name='logout'),
]

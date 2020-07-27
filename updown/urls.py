
from django.contrib import admin
from django.urls import path , re_path , include
from . import views

app_name = 'UD'

urlpatterns = [
    # re_path(r'^upload/(\d+)', views.upload , name='upload'),
    re_path(r'^upload/(\d+)?', views.upload , name='upload'),
    # re_path(r'^detail/(\d+)?',views.change , name='detail'),
    path('upload/<int:userid>', views.upload , name='upload'),
    re_path(r'^download/', views.download , name='download'),
    re_path(r'^delete/(\d+)?', views.delete,name='delete'),
    re_path(r'^detail/(\d+)?', views.change , name='change'),
    re_path(r"^fail", views.fail , name='fail')
]

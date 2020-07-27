from django.contrib import admin
from .models import Photo


class ViewPhoto(admin.ModelAdmin):
    list_display = ('id',  '사용자' , '사진' , 'postdate' , 'create_date')

admin.site.register(Photo, ViewPhoto)

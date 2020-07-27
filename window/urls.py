
from django.contrib import admin
from django.urls import path , re_path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from ..updown.views import UpdownViews

urlpatterns = [
    re_path(r'^$' ,views.index , name='index'),
    # path('*<userid>' ,views.index , name='index'),
    re_path(r'^about/$' , views.about , name='about'),
    re_path(r'^service/$' ,views.service , name='service'),
    re_path(r"^inquiry/$" , views.inquiry , name='inquiry'),
    re_path(r"^MyFage/(\d+)?" , views.myfage , name='myfage'),

    path('updown/' , include('updown.urls', namespace='UD')),
    path('account/', include('account.urls' , namespace='AC')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from views import hour_ahead

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'time/plus/(\d{1,2})/$', hour_ahead),   #使用url需要另外导入，目前url()才能用正则
]

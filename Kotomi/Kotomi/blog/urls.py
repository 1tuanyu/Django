from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^home/',views.Home,name="blog_home"),
    url(r'^post/',views.Post,name="blog_post"),
    url(r'^post_success/', views.Post_success, name="post_success"),
]

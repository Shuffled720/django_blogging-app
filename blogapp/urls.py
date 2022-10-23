
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path


from .views import *

urlpatterns = [
    path('/createBlog', createBlog, name='createBlog'),
    path('postComment', postComment, name='postComment'),
    path('', blog_home, name='blog_home'),
    path('<str:slug>', blog_post, name='blog_post'),


    
]
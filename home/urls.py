
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('search', search, name='search'),
    path('signup', handelSignup, name='handelSignup'),
    path('login', handelLogin, name='handelLogin'),
    path('logout', handelLogout, name='handelLogout')
]
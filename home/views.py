from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from blogapp.models import * 

# Create your views here.


def handelSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        if len(username)>10:
            messages.warning(request, "Username should be under 10 char")
            return redirect('home')
        if not username.isalnum():
            messages.warning(request, "Username should contain only alphanumeric terms")
            return redirect('home')
        if password!= cpassword:
            messages.warning(request, "Passwords Not Matching")
            return redirect('home')
        
        try:
            user=User.objects.create_user(username, email, password)
            user.first_name =fname
            user.last_name=lname
            user.save()
            return redirect("home")
        except:
            messages.warning(request, "username to be unique")
            return redirect('home')
        
    else:
        return HttpResponse("NOT ALLOWDED!!!")


def handelLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword )

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect("home")
        else:
            messages.warning(request, "INVALID CREDENTIALS")
            return redirect("home")


def handelLogout(request):
    
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect("home")




def home(request):
    return render(request ,'home/home.html')





@login_required(redirect_field_name='about', login_url=home)
def about(request):
    user=request.user
    username=user.username
    name=user.first_name
    email=user.email


    context={'name': name, 'username':username, 'email':email}
    return render(request ,'home/about.html', context)


def blog(request):
        return render(request ,'home/blog.html')

        
def contact(request):

    if(request.method=='POST'):
        name=request.POST.get['name']
        email=request.POST.get['email']
        phone=request.POST.get['phone']
        content=request.POST.get['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, 'Message sent!!!')


    return render(request ,'home/contact.html')



def search(request):
    query=request.GET['query']
    
    if(len(query) > 100):
        allposts=[]

    else:
        allpostsTitle=Post.objects.filter(title__contains=query)
        allpostsContent=Post.objects.filter(content__contains=query)
        allposts=allpostsTitle.union(allpostsContent)




    context={'posts': allposts}
    return render(request, 'home/search.html', context)



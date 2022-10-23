from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .templatetags import extras


# Create your views here.

def blog_home(request):
    allPosts=Post.objects.all()
    context={'posts': allPosts}

    return render(request ,'blogapp/blog_home.html', context)

def blog_post(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blogapp/blog_post.html", context)



def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect(f"/blog/{post.slug}")

def createBlog(request):


    if request.method=="POST":
        user=request.user
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=user.username
        post=Post(title=title, content=content, author=author )
        post.save()
        messages.success(request, 'Blog created successfully!!!')



        


    return render(request, "blogapp/createBlog.html")


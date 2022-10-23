from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from matplotlib.pyplot import title
from django.contrib.auth.models import User
from django.utils.timezone import now
from .helper import *


# Create your models here.


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=20)
    slug=models.SlugField(max_length=100,null=True, blank=True)
    timeStamp=models.DateTimeField(default=now)


    def __str__(self):
        return self.title + ' by ' + self.author
    def save(self, *args, **kwargs):
        self.slug=generate_slug(self.title)
        super(Post, self).save(*args, **kwargs)


class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
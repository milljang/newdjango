import re
from django.db import models
from django.utils import timezone
from django.forms import ValidationError



class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,verbose_name='제목',)
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag',blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='작성일시')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='수정일시')

class comment (models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title
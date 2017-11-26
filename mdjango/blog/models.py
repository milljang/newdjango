import re
from django.db import models
from django.forms import ValidationError



class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='제목', #국제화 안됨
          choices = (
               ('제목1', '제목 1 레이블'), # 실제 저장될값 2. 보여주는값
               ('제목2', '제목 2 레이블'),
               ('제목3', '제목 3 레이블'),
          ))
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
        return self.name

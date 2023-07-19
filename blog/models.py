from django.db import models
from django.contrib.auth.models import User
from django_tuieditor.models import MarkdownField


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownField()
    # content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=50)

    # 좋아요
    # 조회수
    # 카테고리
    # 공유,,,?


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

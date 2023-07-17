from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=50)  # 이후 auth user로 변환 필요
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 좋아요
    # 조회수
    # 카테고리
    # 공유,,,?


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=50)  # 이후 auth user로 변환 필요
    created_at = models.DateTimeField(auto_now_add=True)

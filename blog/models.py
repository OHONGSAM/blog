from django.db import models
from user.models import User


class Post(models.Model):
    CATEGORY_CHOICES = [
        ("HTML/CSS", "HTML/CSS"),
        ("Python", "Python"),
        ("Django", "Django"),
        ("고양이", "고양이"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True)
    thumbnail_url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} on {self.post}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.post}, {self.user})"

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


def profile_img_path(instance, filename):
    return f"profiles/{instance.username}/{filename}"


class User(AbstractUser):
    profile_img = models.ImageField(upload_to=profile_img_path, blank=True, null=True)

    def __str__(self):
        return self.username

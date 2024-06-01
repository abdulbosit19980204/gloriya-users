from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=100, unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.user_type


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    codeProject = models.IntegerField(blank=True, null=True)
    codeSklad = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.IntegerField(default=2)
    profile_pic = models.ImageField(upload_to='profile/profile_pics', default="profile/profile_pics/nouserimage.png")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

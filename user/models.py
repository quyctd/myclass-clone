from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to="user/")
    headline = models.CharField(max_length = 255)
    biography = models.TextField()

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    base_info = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
    first_name = models.CharField(max_length = 30, blank = True, null = True)
    last_name = models.CharField(max_length = 30, blank = True, null = True)
    avatar = models.ImageField(upload_to="teacher/")
    biography = models.TextField()
    professional = models.CharField(max_length = 30)
    def __str__(self):
        return (self.first_name +" "+ self.last_name)

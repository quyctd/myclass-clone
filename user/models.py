from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    base_info = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
    first_name = models.CharField(max_length = 30, blank = True, null = True)
    last_name = models.CharField(max_length = 30, blank = True, null = True)

    def __str__(self):
        return self.first_name
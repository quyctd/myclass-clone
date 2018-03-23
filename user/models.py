from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username



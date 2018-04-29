from django.contrib import admin
from user.models import UserProfile, Teacher
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Teacher)
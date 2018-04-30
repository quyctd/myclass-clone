from django.db import models
from taggit.managers import TaggableManager
from user.models import Teacher
# Create your models here.

class Course(models.Model):
    tac_gia = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    ten_khoa_hoc = models.CharField(max_length = 255)
    anh_cover = models.FileField(upload_to = "media/cover/")
    ngay_tao = models.DateTimeField()
    mieu_ta = models.TextField()
    tags = TaggableManager()
    students = models.ManyToManyField("auth.User", related_name='course', blank = True)
    
    def __str__(self):
        return self.ten_khoa_hoc

class Video(models.Model):
    khoa_hoc = models.ForeignKey(Course, related_name= "video", on_delete= models.CASCADE)
    link_video = models.URLField()

class Category(models.Model):
    ten_danh_muc = models.CharField(max_length = 255)
    khoa_hoc = models.ManyToManyField(Course, blank = True, related_name="categories")

    def __str__(self):
        return self.ten_danh_muc

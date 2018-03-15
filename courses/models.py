from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class KhoaHoc(models.Model):
    tac_gia = models.ForeignKey("auth.User", on_delete= models.CASCADE)
    ten_khoa_hoc = models.CharField(max_length = 255)
    anh_cover = models.FileField()
    ngay_tao = models.DateTimeField()
    mieu_ta = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.tac_gia

class Video(models.Model):
    khoa_hoc = models.ForeignKey(KhoaHoc, related_name= "Course", on_delete= models.CASCADE)
    link_video = models.URLField()

class Category(models.Model):
    ten_danh_muc = models.CharField(max_length = 255)
    khoa_hoc = models.ManyToManyField(KhoaHoc)

    def __str__(self):
        return self.ten_danh_muc

from django.db import models
from taggit.managers import TaggableManager
import datetime
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils import timezone
from .tools import pre_upload_cover_course, pre_upload_avatar_image

# Create your models here.

class Course(models.Model):
    ten_khoa_hoc = models.CharField(max_length = 255)
    anh_cover = models.FileField(upload_to = "cover/")
    cover_link = models.CharField(default = "Link is empty", max_length = 1024, blank = True)
    ngay_tao = models.DateTimeField(default = timezone.now)
    mieu_ta = models.TextField()
    tags = TaggableManager()
    students = models.ManyToManyField("auth.User", related_name='course', blank = True)
    views = models.IntegerField(default = 0)
    LANGUAGE_CHOICES = (
        ("Tiếng Việt", "VN"),
        ("Tiếng Anh", "EN")
    )
    language = models.CharField(
        max_length=64, choices=LANGUAGE_CHOICES, default=LANGUAGE_CHOICES[0])
    LEVEL_CHOICES = (
        ('Tất cả', "All"),
        ('Mới học','Beginner'),
        ('Nâng cao', 'Junior')
    )
    level = models.CharField(
        max_length=64, choices=LEVEL_CHOICES, default=LEVEL_CHOICES[0])
    def __str__(self):
        return self.ten_khoa_hoc

pre_save.connect(pre_upload_cover_course, sender=Course)


class Video(models.Model):
    khoa_hoc = models.ForeignKey(Course, related_name= "video", on_delete= models.CASCADE)
    video_name = models.CharField(max_length = 255, default = "Noname")
    link_video = models.URLField()
    duration = models.DurationField(default=datetime.timedelta(minutes=10))
    video_id = models.CharField(max_length = 255)

    def __str__(self):
        return self.video_name

def save_video_function(sender, instance, *args, **kwargs):
        import youtube_dl
        print("Begin save...")
        url = instance.link_video
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                url, download=False)
        duration = int(meta['duration'])
        instance.duration = datetime.timedelta(seconds = duration)
        instance.video_id = meta['id']
        print("Complete")
pre_save.connect(save_video_function, sender=Video)

class Category(models.Model):
    ten_danh_muc = models.CharField(max_length = 255)
    khoa_hoc = models.ManyToManyField(Course, blank = True, related_name="categories")

    def __str__(self):
        return self.ten_danh_muc

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to="user/", blank = True)
    avatar_link = models.CharField(default = "Link is empty", max_length = 1024, blank = True)
    headline = models.CharField(max_length = 255, blank = True)
    biography = models.TextField(blank = True)

    def __str__(self):
        return self.user.username

pre_save.connect(pre_upload_avatar_image, sender=UserProfile)

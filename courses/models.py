from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length = 255)
    course_image = models.FileField()
    course_author = models.CharField(max_length = 64)
    create_date = models.DateTimeField()
    course_description = models.TextField()
    course_language = models.CharField(max_length = 255)

class Video(models.Model):
    course = models.ForeignKey(Course, related_name= "Course", on_delete= models.CASCADE)
    video_url = models.URLField()

from django.contrib import admin
from . import models

# Register your models here.
class VideoInline(admin.TabularInline):
    model = models.Video
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoInline,]


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Video)
admin.site.site_header = "ADMIN SITE"

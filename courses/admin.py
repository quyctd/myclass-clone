from django.contrib import admin
from .models import *

# Register your models here.
class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class CategoryInline(admin.TabularInline):
    model = Category.khoa_hoc.through
    extra = 1
    verbose_name_plural = 'Thêm Danh Mục'
    verbose_name = "Danh Mục"

class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoInline, CategoryInline]


admin.site.register(KhoaHoc, CourseAdmin)
admin.site.register(Video)
admin.site.register(Category)
admin.site.site_header = "ADMIN SITE"

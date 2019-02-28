from django.contrib import admin
from .models import *

# Register your models here.
class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('video_name', 'link_video')

class CategoryInline(admin.TabularInline):
    model = Category.khoa_hoc.through
    extra = 1
    verbose_name_plural = 'Thêm Danh Mục'
    verbose_name = "Danh Mục"
    max_num = 1
    # exclude =("khoa_hoc",)

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ("ten_danh_muc",)

class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoInline, CategoryInline]
    list_display = ("ten_khoa_hoc", "ngay_tao")
    list_filter = ("ten_khoa_hoc", "ngay_tao")
    search_fields = ( "ten_khoa_hoc",)
    exclude = ('views','students',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.site_header = "ADMIN SITE"

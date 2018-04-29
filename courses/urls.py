from courses import views as crs_views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', crs_views.CourseDetailView.as_view(), name = "course-detail"),
    url(r'^', crs_views.courses_list, name = "courses"),
    url(r'^categories/(?P<pk>\d+)/$', crs_views.categories, name = "categories")
]

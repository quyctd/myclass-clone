from courses import views as crs_views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', crs_views.courses_detail, name = "course-detail"),
    url(r'^(?P<pk>\d+)/enroll/$', crs_views.courses_detail_enroll, name="course-enroll"),
    url(r'^(?P<pk>\d+)/enroll/learn/$', crs_views.courses_learn, name="courses-learn"),    
    url(r'^$', crs_views.courses_list, name = "courses"),
    url(r'^categories/(?P<pk>\d+)/$', crs_views.categories, name = "categories"),
]

from apps import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index, name = "home"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/$', views.setting, name = "setting"),
    url(r'^mycourses/$', views.my_course, name='my_course'),
    url(r'^course/$', views.courses_list, name = "courses"),
    url(r'^(?P<pk>\d+)/$', views.courses_detail, name = "course-detail"),
    url(r'^(?P<pk>\d+)/enroll/$', views.courses_detail_enroll, name="course-enroll"),
    url(r'^(?P<pk>\d+)/enroll/learn/$', views.courses_learn, name="courses-learn"),    
    url(r'^categories/(?P<pk>\d+)/$', views.categories, name = "categories"),
]

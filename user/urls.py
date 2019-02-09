from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$', views.index, name = "home"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/$', views.setting, name = "setting"),
    url(r'^mycourses/$', views.my_course, name='my_course')

]

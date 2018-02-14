from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$', views.index, name = "home"),
]

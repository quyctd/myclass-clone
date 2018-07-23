"""myclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from courses import views as crs_views

admin.autodiscover()

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),

    url(r'^login/$', 
        auth_views.login, 
        {'template_name': 'registration/login.html'}, 
        name='login'
    ),
    
    url(r'^logout/$', 
        auth_views.logout, 
        {'next_page': 'home'},
        name='logout'
    ),
    url(r'^search/$', crs_views.search, name="search"),
    url(r'^', include("user.urls")),
    url(r'^course/', include("courses.urls")),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <-- Can't remove?
]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

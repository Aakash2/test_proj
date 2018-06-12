"""map_user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import manage_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
"""    url(r'^user_templates/(?P<path>.*)$', static.serve,  {'document_root': '/opt/test_proj/map_user/manage_user/templates/html'}),
    url(r'^register',manage_user.views.register),
    url(r'^login',manage_user.views.user_login),"""
    
]

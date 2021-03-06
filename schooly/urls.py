"""schooly URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from schooly_app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index), # root
    url(r'^class/(?P<classid>.+)$', class_view), # login
    url(r'^createclass$', create_class), # create a new class
    url(r'^makeclass$',make_class), #make a class
    url(r'^joinclass$', join_class), # join a new class
    url(r'^login$', login_view), # login
    url(r'^logout$', logout_view), # logout
    url(r'^signup$', signup), # signup
]

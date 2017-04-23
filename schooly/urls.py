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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'schooly_app.views.index'), # root
    url(r'^class/(?P<classid>.+)$', 'schooly_app.views.login_view'), # login
    url(r'^createclass$', 'schooly_app.views.create_class'), # create a new class
    url(r'^joinclass$', 'schooly_app.views.join_class'), # join a new class
    url(r'^login$', 'schooly_app.views.login_view'), # login
    url(r'^logout$', 'schooly_app.views.logout_view'), # logout
    url(r'^signup$', 'schooly_app.views.signup'), # signup
]

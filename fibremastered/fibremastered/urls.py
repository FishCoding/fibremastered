"""fibremastered URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from .views import look_into_db, index
from .views import RedirectView, ContentView, ContentEditView, ContentDeleteView, ContentDownloadView, ContentFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #re_path(r'^((?:[\w\-]+/)*)$', look_into_db),
    re_path(r'^$', RedirectView.as_view(), name='redirect_landing'),
  #  re_path(r'^(?P<slug>[-\w]*form[-\w]*)/$', ContentFormView.as_view(), name='form_view'), # allowing first layer form views
    re_path(r'^(?P<slug>[-\w]+)/$', ContentView.as_view(), name='content_view'), # always have the contentview last because its catchall
    # every other layer
    re_path(r'^(?P<rest_url>([-\w]+\/)*)(?P<slug>editor)/(?P<id>\d+)/$', ContentEditView.as_view(), name='editor_view'),
    re_path(r'^(?P<rest_url>([-\w]+\/)*)(?P<slug>delete)/(?P<id>\d+)/$', ContentDeleteView.as_view(), name='delete_view'),
    re_path(r'^(?P<rest_url>([-\w]+\/)*)(?P<slug>download)/(?P<id>\d+)/$', ContentDownloadView.as_view(), name='download_view'),
    re_path(r'^(?P<rest_url>([-\w]+\/)*)(?P<slug>[-\w]*form[-\w]*)/$', ContentFormView.as_view(), name='form_view'),
    re_path(r'^(?P<rest_url>([-\w]+\/)*)(?P<slug>[-\w]+)/$', ContentView.as_view(), name='content_view'),
]

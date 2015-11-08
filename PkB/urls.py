"""PkB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'distilerie.views.home', name='home'),
    url(r'^home/', 'distilerie.views.home', name='home'),
    url(r'^directions/', 'distilerie.views.directions', name='directions'),
    url(r'^directions2/', 'distilerie.views.directions2', name='directions2'),
    url(r'^info/', 'distilerie.views.info', name='info'),

    url(r'^info2/', 'distilerie.views.info2', name='info2'),
    url(r'^nearest/', 'distilerie.views.nearest', name='nearest'),
    url(r'^nearest2/', 'distilerie.views.nearest2', name='nearest2'),
    url(r'^review/', 'distilerie.views.review', name='review'),
    url(r'^review2/', 'distilerie.views.review2', name='review2'),

    url(r'^review3/', 'distilerie.views.review3', name='review3'),
    url(r'^about/', 'distilerie.views.about', name='about'),
                       # keep the next 2 lines uncommented to enable admin

                       url(r'^admin/doc/',
                           include('django.contrib.admindocs.urls')),

                       url(r'^admin/', include(admin.site.urls)),
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

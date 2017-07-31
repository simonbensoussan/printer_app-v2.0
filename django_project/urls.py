# -*- coding: utf-8 -*-
"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
 Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))


"""
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
#   url('r^catalog/',views.Home, name='Home'), de base on appelle la app_nom.classe.fonction
    url(r'^catalog/', include('catalog.urls')),
    url(r'^api/', include('landing.urls')),
    url(r'^admin/', admin.site.urls),
   # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),  # ADD THIS URL
    url(r'^$', RedirectView.as_view(url ='/catalog/', permanent =False))  #si c'est l'unique app utilisé
]
if settings.DEBUG is True :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) developemment uniquement

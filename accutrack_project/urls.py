"""
URL configuration for accutrack_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path  # Import include and re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True)),
    path('apple-touch-icon.png', RedirectView.as_view(url=settings.STATIC_URL + 'images/apple-touch-icon.png', permanent=True)),
    path('apple-touch-icon-precomposed.png', RedirectView.as_view(url=settings.STATIC_URL + 'images/apple-touch-icon.png', permanent=True)),
    path('site.webmanifest', RedirectView.as_view(url=settings.STATIC_URL + 'site.webmanifest', permanent=True)),
    path('admin/', admin.site.urls),
    path('', include('accutrack_app.urls')),  # Include URLs from the 'accutrack_app' app
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
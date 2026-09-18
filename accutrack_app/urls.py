from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('about/', views.about),
    path('services', views.services, name='services'),
    path('services/', views.services),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/', views.gallery),
    path('contact', views.contact, name='contact'),
    path('contact/', views.contact),
]
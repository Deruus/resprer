from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('restaurantes/', views.restaurantes, name='restaurantes'),
    path('reservar/', views.reservar, name='reservar'),
    path('login/', views.login, name='login'),
    path('contacto/', views.contacto, name='contacto'),

]
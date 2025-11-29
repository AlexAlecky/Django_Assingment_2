from django.urls import path
from . import views

urlpatterns = [
    path('', views.ourFirstApp, name='ourFirstApp'),
    path('home/', views.home, name='home'),         
    path('create-animal/', views.createAnimal, name='create-animal'),
    path('animals/', views.fetchAllAnimals, name='fetchAll'),
]


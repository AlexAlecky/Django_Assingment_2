from django.urls import path
from . import views

urlpatterns = [
    path('', views.ourFirstApp, name='ourFirstApp'),
    path('home/', views.home, name='home'),         
    path('create-animals/', views.createAnimals, name='create-animals'),

   
    # Animals CRUD
    path('animals/', views.fetchAllAnimals, name='fetchAll'),
    path('animals/<int:pk>/', views.Animals_detail, name='animals-detail'),
    path('animals/<int:pk>/edit/', views.updateAnimals, name='update-animals'),
    path('animals/<int:pk>/delete/', views.deleteAnimals, name='delete-animals'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('les-cours', views.cours, name='cours'),
    path('Emplois-du-temps', views.emplois, name='emplois'),
    
]

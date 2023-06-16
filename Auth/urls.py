from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login'), name='home'),  # Redirige vers la page de connexion par défaut
    path('login/', views.login, name='login'),  # URL pour la vue de connexion
    path('register/', views.register, name='register'),  # URL pour la vue d'inscription
    path('forgot-password/', views.forgot_password, name='password.forgot'),  # URL pour la vue de mot de passe oublié
    path('new-password/', views.new_password, name='password.new'),  # URL pour la vue de nouveau mot de passe
]

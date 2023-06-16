from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige vers la page du tableau de bord après la connexion
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Créer l'utilisateur
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Autres étapes de traitement si nécessaire
        
        messages.success(request, 'Votre compte a été créé avec succès. Veuillez vous connecter.')
        return redirect('login')  # Redirige vers la page de connexion après l'inscription
    
    return render(request, 'auth/register.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Vérifier si l'e-mail existe dans la base de données
        user = User.objects.filter(email=email).first()
        
        if user:
            # Logique de traitement pour l'envoi d'un e-mail de réinitialisation du mot de passe
            # ...
            
            messages.success(request, 'Un e-mail de réinitialisation du mot de passe a été envoyé.')
            return redirect('login')
        else:
            messages.error(request, 'Aucun utilisateur avec cet e-mail n\'a été trouvé.')
    
    return render(request, 'auth/forgot-password.html')

def new_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            # Logique de traitement pour la réinitialisation du mot de passe
            # ...
            
            messages.success(request, 'Votre mot de passe a été réinitialisé avec succès. Veuillez vous connecter.')
            return redirect('login')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
    
    return render(request, 'auth/new-password.html')

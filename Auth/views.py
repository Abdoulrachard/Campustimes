from django.shortcuts import render , redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login , logout 





def login(request):
    error = False
    message = ""
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.POST.get('email')
        password = request.POST.get('password')
        user  = User.objects.filter(email=email).first()
        if user:
            user_auth = authenticate(username=user.username, password=password)
            if user_auth:
                auth_login(request , user_auth )
                return redirect('default')
            else:
               error = True
               message = "Mot de passe incorrect !"
        else:
            error = True
            message = "Cet utilisateur n'existe pas !"
        
            
    context = {
        'error': error,
        'message': message
    }
    
    return render(request, 'auth/login.html', context)

def register(request):
    error = False
    message = ""
    if request.method == 'POST':
        # Récupérer les données du formulaire
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        newpassword = request.POST.get('newpassword')
        try:
           validate_email(email) == False
        except :
            error = True
            message = 'Entrez un email valide ! '
        
        if error == False:
            if password != newpassword:
                 error = True
                 message = 'Les deux mots de passe ne correspondent pas ! ' 
        
        user = User.objects.filter(email=email).first()
        if user:
            error = True
            message = f"Un utilisateur avec l'email {email} existe déja !" 
        if error == False:
            user = User(
                 username = fullname , 
                email = email ,
            )
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()  
            return redirect('login') 
    context = {
        'error': error,
        'message': message
    }
    
    return render(request, 'auth/register.html', context)

def forgot_password(request):
    
    context = {}
    
    return render(request, 'auth/forgot-password.html', context)

def new_password(request):
    
    context = {}
    
    return render(request, 'auth/new-password.html', context)

def log_out(request):
    logout(request)
    return redirect('login')




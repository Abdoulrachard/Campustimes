from base64 import urlsafe_b64decode
import pdb
from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.core.validators import validate_email
from django.contrib.auth import authenticate , login as auth_login , logout 
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from Auth.mail import send_html_email
from .models import MyUser as User, Level



def login(request):
    error = False
    message = ""

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        
        if user:
            user_auth = authenticate(email=user.email, password=password)
            
            if user_auth:
                auth_login(request, user_auth)
                
                if user.is_superuser or user.is_staff:
                    return redirect('default') 
                else:
                    return redirect('etudiant')  
                
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
     
        last_name, first_name = request.POST.get('fullname').split(' ')
        email = request.POST.get('email')
        password = request.POST.get('password')
        newpassword = request.POST.get('newpassword')
        level_id = request.POST.get('level_id')
        
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
                email = email ,
                first_name = first_name,
                last_name = last_name,
                level=Level.objects.get(id=level_id)
            )
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()
            return redirect('login') 
    context = {
        'error': error,
        'message': message,
        'levels': Level.objects.all(),
    }
    
    return render(request, 'auth/register.html', context)

def forgot_password(request):
    error = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
       
        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = request.build_absolute_uri(f'reset-password/{uid}/{token}')
            send_html_email('Réinitialisation de mot de passe','mail/forgot-password.html', {
                'user': user,
                'reset_link': reset_link,
            }, [email])

            return redirect('password_reset_done')
        else:
            error = True
            message = "Aucun utilisateur avec cet email"
            
    context = {
        'error': error,
        'message': message
    }
    
    return render(request, 'auth/forgot-password.html', context)

def new_password(request, uidb64, token):
    
    try:
        uid = urlsafe_b64decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                user.set_password(password)
                user.save()
                return redirect('password_reset_complete')
            else:
               
                error = True
                message = "Les mots de passe ne correspondent pas."
        else:
            error = False
            message = ""
    else:
       
        error = True
        message = "Le lien de réinitialisation du mot de passe est invalide."

    context = {
        'error': error,
        'message': message
    }
    return render(request, 'auth/new-password.html', context)


def log_out(request):
    logout(request)
    return redirect('login')

def password_reset_done(request):
    return render(request, 'auth/password_reset_done.html')




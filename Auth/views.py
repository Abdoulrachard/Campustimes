from django.shortcuts import render , redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login , logout 
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

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
        last_name, first_name = request.POST.get('fullname').split(' ')
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
                 username = email , 
                email = email ,
                first_name = first_name,
                last_name = last_name
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
    # error = False
    # message = ""
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     user = User.objects.filter(email=email).first()

    #     if user:
    #         token = default_token_generator.make_token(user)
    #         uid = urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8')

    #         reset_link = request.build_absolute_uri(f'reset-password/{uid}/{token}')

    #         subject = 'Réinitialisation de mot de passe'
    #         message = render_to_string('auth/reset_password_email.html', {
    #             'user': user,
    #             'reset_link': reset_link,
    #         })
    #         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    #         return redirect('password_reset_done')
    #     else:
    #         error = True
    #         message = "Aucun utilisateur avec cet email"
    #         # return redirect('password_reset_failed')
    # context = {
    #     'error': error,
    #     'message': message
    # }
    
    return render(request, 'auth/forgot-password.html', context)

def new_password(request):
    # if request.method == 'POST':
    #     password = request.POST.get('password')
    #     user_id = request.POST.get('user_id')

    #     user = User.objects.filter(pk=user_id).first()
    #     if user:
    #         user.set_password(password)
    #         user.save()

    #         return redirect('login')
    context = {}
    
    return render(request, 'auth/new-password.html', context)

# def password_reset_done(request):
#     return render(request, 'auth/password_reset_done.html')


def log_out(request):
    logout(request)
    return redirect('login')




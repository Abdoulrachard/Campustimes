from django.urls import path
from django.shortcuts import redirect
from . import views as custom_views


urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login', custom_views.login, name='login'),
    path('register', custom_views.register, name='register'),
    path('forgot-password', custom_views.forgot_password, name='forgot-password'),
    path('new-password', custom_views.new_password, name='new-password'),
    path('logout', custom_views.log_out, name='log_out'),
    path('password-reset/done/', custom_views.password_reset_done, name='password_reset_done'),
    path('reset-password/<str:uidb64>/<str:token>/', custom_views.new_password, name='new-password'),
    # path('', custom_views.password_reset_done, name='password_reset_done'),
    

    
]


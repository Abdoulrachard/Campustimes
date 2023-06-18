from django.urls import path
from django.shortcuts import redirect
from . import views as custom_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login', custom_views.login, name='login'),
    path('register', custom_views.register, name='register'),
    path('forgot-password', custom_views.forgot_password, name='forgot-password'),
    path('new-password', custom_views.new_password, name='new-password'),
    path('logout', custom_views.log_out, name='log_out'),

    # Utilisation des vues de django.contrib.auth
    # path('forgot-password', auth_views.PasswordResetView.as_view(template_name='forgot-password.html'), name='forgot-password'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    # path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='new-password.html'), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
]


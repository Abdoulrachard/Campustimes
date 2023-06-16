from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('Dashbord', views.dashbord, name='dashbord'),
]

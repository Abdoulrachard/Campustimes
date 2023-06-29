from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('Emplois-du-temps', views.emplois, name='emplois'),
    path('Matiere', views.matiere, name='matiere'),
    path('level', views.level, name='level'),
    path('Proffesseur', views.proffesseur, name='proffesseur'),
    path('Salle', views.salle, name='salle'),
    path('Etudiant', views.etudiant, name='etudiant'),
    path('Notification', views.notification, name='notification'),
    path('Emplois_Etudiants', views.emplois_etudiants, name='emplois_etudiants'),
    path('Aides', views.aides, name='aides'),
]

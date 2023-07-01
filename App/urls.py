from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('Emplois-du-temps', views.emplois, name='_emplois'),
    path('Matiere', views.matiere, name='matiere'),
    path('level', views.level, name='level'),
    path('Proffesseur', views.proffesseur, name='proffesseur'),
    path('Salle', views.salle, name='salle'),
    path('Etudiant', views.etudiant, name='etudiant'),
    path('Notification', views.notification, name='notification'),
    path('Emplois_Etudiants', views.emplois_etudiants, name='emplois_etudiants'),
    path('Aides', views.aides, name='aides'),
    path('emploi-du-temps/<int:pk>', views.final_emplois, name='emplois'),
    path('students/emploi-du-temps', views.emploi_student, name='emploi_student'),
    path('emploi-du-temps', views.final_emplois, name='__emplois'),
    path('emploi-du-temps-test/<int:pk>', views.test, name='test'),
    path('emploi-du-temps-destroy/<int:pk>', views.destroy_shedule, name='destroy_shedule'),
   
]


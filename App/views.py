import json
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Subject, Classroom, Timestable, Level
from Auth.models import MyUser as User, Level
import uuid
from django.db.models import Q
from datetime import datetime, timedelta
from App.models import Timestable


import locale
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

@login_required()
def default(request):

    context = {}

    return render(request, 'app/default.html', context)


@login_required()
def emplois(request):
    proffesseurs = User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
    classrooms = Classroom.objects.all()
    matieres = Subject.objects.all()
    emplois = Timestable.objects.all()
    levels = Level.objects.all()

    error, success = None, None

    if request.method == 'POST':
        matiere_id = request.POST.get('label_id')
        prof_id = request.POST.get('prof_id')
        salle_id = request.POST.get('salle_label')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        level_id = request.POST.get('level_id')

        action = request.POST.get('action')

        if matiere_id and prof_id and salle_id and start_time and end_time:
            try:
                if action == 'POST':
                    start = datetime.strptime(start_time, "%Y-%m-%dT%H:%M")
                    week_number = start.isocalendar()[1]

                    Timestable.objects.create(
                        subject=Subject.objects.get(id=matiere_id),
                        user=User.objects.get(id=prof_id),
                        classroom=Classroom.objects.get(id=salle_id),
                        start_time=start_time,
                        end_time=end_time,
                        week=week_number,
                        level=Level.objects.get(id=level_id),

                    )
                    success = "L'emploi a bien été créé"
                elif action == 'PATCH':
                    emploi_id = request.POST.get('emploi_id')
                    emploi = Timestable.objects.get(id=emploi_id)
                    emploi.subject = Subject.objects.get(id=matiere_id)
                    emploi.user = User.objects.get(id=prof_id)
                    emploi.classroom = Classroom.objects.get(id=salle_id)
                    emploi.start_time = start_time
                    emploi.end_time = end_time
                    emploi.level = Level.objects.get(id=level_id)

                    emploi.save()
                    success = "L'emploi a bien été mis à jour"

            except:
                error = "Erreur lors de la création/édition de l'emploi"
        else:
            error = "Veuillez remplir tous les champs obligatoires"

        if action == 'DELETE':
            emploi_id = request.POST.get('emploi_id')
            try:
                emploi = Timestable.objects.get(id=emploi_id)
                emploi.delete()
                success = "L'emploi a bien été supprimé"
                error = None
            except:
                error = "Erreur lors de la suppression de l'emploi !"

    context = {
        'emplois': emplois,
        'matieres': matieres,
        'proffesseurs': proffesseurs,
        'classrooms': classrooms,

        'levels': levels,
        'state': {
            'success': success,
            'error': error,
        },

    }

    return render(request, 'app/emplois.html', context)


@login_required()
def administ(request):

    context = {}

    return render(request, 'app/administ.html', context)


@login_required()
def matiere(request):

    error, success = None, None

    if request.method == 'POST':

        level_id = request.POST.get('level_id')
        subject_id = request.POST.get('subject_id')
        label = request.POST.get('label')
        bgColor = request.POST.get('bgColor')
        total_times = request.POST.get('total_times')
        code = request.POST.get('code')
        action = request.POST.get('action')

        if level_id and label and total_times:
            try:
                if action == 'POST':
                    Subject.objects.create(
                        label=label,
                        code=code,
                        total_times=total_times,
                        bgColor=bgColor,
                        level=Level.objects.get(id=level_id)
                    )
                elif action == 'PATCH':
                    subject = Subject.objects.get(id=subject_id)
                    subject.label = label
                    subject.code = code
                    subject.bgColor = bgColor
                    subject.total_times = total_times
                    subject.level = Level.objects.get(id=level_id)

                    subject.save()
                success = f"{label} a bien été créer/éditer"

            except:
                error = "Erreur lors de la création/édition d'une matiere"
        else:
            error = "Veuillez remplir tout les champs marqués obligatoires"

        if action == 'DELETE':
            try:
                Subject.objects.get(id=subject_id).delete()
                success = f"une matière a bien été supprimer"
                error = None
            except:
                error = "Erreur lors de la suppression d'une matiere"

    context = {
        'matiers': Subject.objects.all(),
        'levels': Level.objects.all(),
        'state': {
            'success': success,
            'error': error,
        },
    }

    return render(request, 'app/matiere.html', context)


@login_required()
def level(request):

    error, success = None, None

    if request.method == 'POST':
        capacity = request.POST.get('capacity')
        label = request.POST.get('label')
        action = request.POST.get('action')
        level_id = request.POST.get('level_id')

        if label:
            try:
                if action == 'POST':
                    Level.objects.create(
                        label=label,
                        capacity=capacity,
                    )
                elif action == 'PATCH':
                    level = Level.objects.get(id=level_id)
                    level.label = label
                    level.capacity = capacity
                    level.save()
                success = f"{label} de capacité {capacity} a bien été créer/éditer"

                if action == 'DELETE':
                    Level.objects.get(id=level_id).delete()
                    success = f"{label} de capacité {capacity} a bien été supprimer"
            except:
                error = "Erreur lors de la création/édition d'un niveau"
        else:
            error = "Veuillez remplir tout les champs marqués obligatoires"
    levels = Level.objects.all()
    capacity_values = [level.capacity / 20 for level in levels]
    capacity_values_json = json.dumps(capacity_values)
    
    context = {
        "levels": Level.objects.all(),
       "capacity_values_json":capacity_values_json,
        'state': {
            'success': success,
            'error': error,
        },
    }

    return render(request, 'app/level.html', context)

def get_capacity_data(request):
    levels = Level.objects.all()
    capacity_values = [level.capacity / 20 for level in levels]
    level_categories = [level.label for level in levels]

    data = {
        'capacity_values': capacity_values,
        'level_categories': level_categories,
    }

    return JsonResponse(data)

@login_required()
def proffesseur(request):

    error, success = None, None

    if request.method == 'POST':

        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        is_staff = request.POST.get('is_staff')
        is_superuser = request.POST.get('is_superuser')

        action = request.POST.get('action')

        if first_name and last_name and email:
            try:
                password = f"IFRI-{uuid.uuid4().hex}"

                if action == 'POST':
                    if not User.objects.filter(email=email).first():
                        user = User.objects.create(
                            email=email,
                            first_name=first_name,
                            last_name=last_name,
                            is_staff=bool(is_staff),
                            is_superuser=bool(is_superuser),
                        )

                        user.set_password(password)
                        user.save()
                    else:
                        error = "Un Enseignant/Collaborateur existe déjà avec ce email."
                        success = False
                elif action == 'PATCH':
                    user = User.objects.get(id=user_id)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.set_password(password)
                    user.save()
                if success is None:
                    success = f"{email} a bien été créer/éditer avec le mot de passe <span class='fs-3 my-2 text-danger fw-bold d-block text-center'>{password}</span>"

            except:
                error = "Erreur lors de la création/édition d'un enseignant/collaborateur"
        else:
            error = "Veuillez remplir tout les champs marqués obligatoires"

        if action == 'DELETE':
            try:
                User.objects.get(id=user_id).delete()
                success = f"Un enseignant/collaborateur de cours a bien été supprimer"
                error = None
            except:
                error = "Erreur lors de la suppression d'un enseignant/collaborateur"

    context = {
        'teachers': User.objects.filter(Q(is_staff=True) | Q(is_superuser=True)),
        'state': {
            'success': success,
            'error': error,
        },
    }

    return render(request, 'app/proffesseur.html', context)


@login_required()
def salle(request):

    error, success = None, None

    if request.method == 'POST':

        salle_id = request.POST.get('salle_id')
        label = request.POST.get('label')
        desc = request.POST.get('desc')
        action = request.POST.get('action')

        if label:
            try:
                if action == 'POST':
                    Classroom.objects.create(
                        label=label,
                        desc=desc,
                    )
                elif action == 'PATCH':
                    cl = Classroom.objects.get(id=salle_id)
                    cl.label = label
                    cl.desc = desc

                    cl.save()
                success = f"{label} a bien été créer/éditer"

            except:
                error = "Erreur lors de la création/édition d'une salle de cours"
        else:
            error = "Veuillez remplir tout les champs marqués obligatoires"

        if action == 'DELETE':
            try:
                Classroom.objects.get(id=salle_id).delete()
                success = f"Une salle de cours a bien été supprimer"
                error = None
            except:
                error = "Erreur lors de la suppression d'une salle de cours"

    context = {
        'salles': Classroom.objects.all(),
        'state': {
            'success': success,
            'error': error,
        },
    }

    return render(request, 'app/salle.html', context)


@login_required()
def etudiant(request):

    context = {}

    return render(request, 'app/dashbord_etudiant.html', context)


@login_required()
def notification(request):

    context = {}

    return render(request, 'app/notification.html', context)


@login_required()
def emplois_etudiants(request):

    data = get_timetable_data(request.user.level.id, False, 26)
    context = {
        'data': data

    }

    return render(request, 'app/emplois_etudiants.html', context)


@login_required()
def aides(request):

    context = {}

    return render(request, 'app/aide.html', context)


def page_not_found(request, exception):
    return render(request, 'error/404.html', status=404)


def permission_denied(request, exception):
    return render(request, 'error/403.html', status=403)


def get_week_num(date):
    date = datetime.fromisoformat(date)
    return date.isocalendar()[1]


def get_hour_range(time):
    hour = time.hour

    if 0 <= hour < 10:
        return 1
    elif 10 <= hour < 13:
        return 2
    elif 13 <= hour < 16:
        return 3
    elif 16 <= hour < 24:
        return 4


def get_timetable_data(niveau_id, week=26):

    timetable_entries = Timestable.objects.filter(
            level_id=niveau_id, week_num=week)
    
    timetable_all = Timestable.objects.filter(
            level_id=niveau_id)

    all_week = []

    for entry in timetable_all:
        week_number = entry.start_time.isocalendar()[1]

        if week_number not in all_week:
            all_week.append(week_number)
    
    grouped_timetable = {}

    for entry in timetable_entries:
        week_number = entry.start_time.isocalendar()[1]
        day_name = entry.start_time.strftime('%A')

        if week_number not in grouped_timetable:
            grouped_timetable[week_number] = {}

        if day_name not in grouped_timetable[week_number]:
            grouped_timetable[week_number][day_name] = {
                1: [],  # 07-10h
                2: [],  # 10h-13h
                3: [],  # 13h-16h
                4: [],  # 16h-19h
            }

        hour_range = get_hour_range(entry.start_time.time())

        grouped_timetable[week_number][day_name][hour_range].append({
            'id': entry.id,
            'subject': entry.subject.serialize(),
            'teacher': entry.teacher.serialize(),
            'niveau': entry.level.serialize(),
            'classroom': entry.classroom.serialize(),
            'start_time': str(entry.start_time.strftime("%d/%m/%Y, %H:%M")),
            'end_time': str(entry.end_time.strftime("%d/%m/%Y, %H:%M")),
        })

    timetable_data = []

    days_of_week = ['lundi', 'mardi', 'mercredi',
                    'jeudi', 'vendredi', 'samedi', 'dimanche']

    current_day_index = datetime.now().weekday()

    for i in range(7):
        day_index = (current_day_index + i) % 7
        day_name = days_of_week[day_index]
        day_data = {
            'day_name': day_name.capitalize(),
            'time_slots': {},
        }

        for hour_range in range(1, 5):
            hour_range_data = grouped_timetable.get(
                week, {}).get(day_name, {}).get(hour_range, [])
            day_data['time_slots'][hour_range] = hour_range_data

        timetable_data.append(day_data)

    return [timetable_data, all_week]


def test(request, pk):
    return JsonResponse(get_timetable_data(pk), safe=False)


@login_required
def final_emplois(request, pk):
    
    if not request.user.is_superuser:
        return redirect('emploi_student')
    
    try:
        niveaux = Level.objects.get(id=pk)
    except:
        niveaux = Level.objects.first()
        pk = niveaux.id

    errors = []
    success = ""
    teachers = User.objects.filter(is_staff=True)
    matieres = Subject.objects.filter(level_id=pk)

    current_week = datetime.now().isocalendar()[1]
    current_week = int(request.GET.get('week', current_week))

    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        subject_id = request.POST.get('subject_id')
        classroom_id = request.POST.get('classroom_id')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        if teacher_id and subject_id and pk and start_time and end_time and classroom_id:
            weekNum = get_week_num(start_time)

            try:
                Timestable.objects.create(
                    teacher=User.objects.get(id=teacher_id),
                    subject=Subject.objects.get(id=subject_id),
                    classroom=Classroom.objects.get(id=classroom_id),
                    level=Level.objects.get(id=pk),
                    start_time=start_time,
                    end_time=end_time,
                    week_num=weekNum,
                )
            except:
                errors.append(
                    "Erreur lors de la création de l'emploi du temps")

            success = "Votre emploi du temps a été bien enregistré"
        else:
            errors.append("Veuillez bien remplir tout les champs")

    timetable_data = get_timetable_data(pk, current_week)

    context = {
        'niveaux': Level.objects.all(),
        'classrooms': Classroom.objects.all(),
        'level': niveaux,
        'teachers': teachers,
        'matieres': matieres,
        'errors': errors,
        'success': success,
        'timetable_data': timetable_data[0],
        'all_week': timetable_data[1],
        'current_week': current_week,
    }

    return render(request, 'app/emploi_du_temps.html', context)

@login_required
def destroy_shedule(request, pk):
    next = request.GET.get('next')

    if not request.user.is_staff or not request.user.is_superuser:
        return redirect(next)

    Timestable.objects.get(id=pk).delete()

    return redirect(next)

@login_required
def emploi_student(request):
    current_week = datetime.now().isocalendar()[1]
    current_week = int(request.GET.get('week', current_week))
    timetable_data = get_timetable_data(
        request.user.level.id, current_week)

    context = {
        'timetable_data': timetable_data[0],
        'all_week': timetable_data[1],
        'current_week': current_week,
        'level': request.user.level,
    }

    return render(request, 'app/emploi_du_temps.html', context)
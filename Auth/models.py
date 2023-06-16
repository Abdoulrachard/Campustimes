from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    # Autres champs spécifiques à l'étudiant

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Autres champs spécifiques à l'enseignant

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    # Autres champs spécifiques au cours

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    # Autres champs spécifiques à la salle de classe

    def __str__(self):
        return self.name

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Autres champs spécifiques à l'horaire

    def __str__(self):
        return f"{self.course} - {self.start_time} to {self.end_time}"


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    label = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.label

class Level(models.Model):
    label = models.CharField(max_length=100)
    capacity = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.label

class Subject(models.Model):
    label = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    total_times = models.IntegerField()
    level = models.ForeignKey(Level,on_delete=models.SET_DEFAULT, default=1)
    
    def __str__(self)->str:
        return self.label

class Classroom(models.Model):
    label = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.label
    
class Timestable(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    

    

    
from django.db import models
from Auth.models import MyUser as User, Level


class Subject(models.Model):
    label = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    bgColor = models.CharField(max_length=255, blank=True, default="#FFA5FF")
    total_times = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.SET_DEFAULT, default=1)
    
    def __str__(self)->str:
        return self.label
    
    def serialize(self):
        return {
            'id': self.id,
            'label': self.label,
            'code': self.code,
            'total_times': self.total_times,
            'bgColor': self.bgColor,
            'level': self.level.serialize(),
        }

class Classroom(models.Model):
    label = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.label
    
    def serialize(self):
        return {
            'id': self.id,
            'label': self.label,
            'desc': self.desc,
        }

class Timestable(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'teacher': self.teacher.serialize(),
            'subject': self.subject.serialize(),
            'classroom': self.classroom.serialize(),
            'level': self.level.serialize(),
            'start_time': self.start_time,
            'end_time': self.end_time,
            'week_num': self.week,
        }
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Classroom)
admin.site.register(models.Subject)
admin.site.register(models.Timestable)
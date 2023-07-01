from django.contrib import admin
from .models import MyUser as User, Level

admin.site.register(User)
admin.site.register(Level)
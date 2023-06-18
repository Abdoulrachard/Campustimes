from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="auth/login")
def default(request):
    
    context = {}
    
    return render(request, 'app/default.html', context)
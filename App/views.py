from django.shortcuts import render


def default(request):
    
    context = {}
    
    return render(request, 'app/default.html', context)
def dashbord(request):
    
    context = {}
    
    return render(request, 'app/dashbord.html', context)
from django.shortcuts import render
from .models import Platform

# Create your views here.
def home(request):
    plataform = Platform.objects.all()
    return render(request, 'plataform.html', {'plataform': plataform})

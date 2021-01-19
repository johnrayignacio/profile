from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def home(request):
    return render(request, 'portfolio1/index.html')

def works(request):
    works = Works.objects.all().order_by('-id')

    context = {
        'works': works
    }
    return render(request, 'portfolio1/works.html', context)

def experience(request):
    return render(request, 'portfolio1/experience.html')

# Create your views here.

from urllib import request
from django.shortcuts import render

# Create your views here.

def ir_inicio (request):
    return render(request, 'index.html')
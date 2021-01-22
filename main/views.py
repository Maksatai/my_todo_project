from django.shortcuts import render,HttpResponse
from .models import Books

def homepage(request):
    return render(request, 'books.html')
    

from django.shortcuts import render,HttpResponse
from .models import Books

def homepage(request):
    todo_list=Books.objects.all()
    return render(request, 'books.html',{"todo_list":todo_list})
       


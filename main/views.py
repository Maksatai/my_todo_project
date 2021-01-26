from django.shortcuts import render,HttpResponse,redirect
from .models import Books

def homepage(request):
    todo_list=Books.objects.all()
    return render(request, 'books.html',{"todo_list":todo_list})
       

def add_todo(request):
    form=request.POST
    text=form["title"]
    text1=form["subtitle"]
    text2=form["description"]
    text3=form["price"]
    text4=form["genre"]
    text5=form["author"]
    text6=form["year"]
    todo=Books(title=text,subtitle=text1,description=text2,price=text3,genre=text4,author=text5,year=text6)
    todo.save()
    return redirect(homepage)

def delete_todo(request,id):
    todo=Books.objects.get(id=id)
    todo.delete()
    return redirect(homepage)


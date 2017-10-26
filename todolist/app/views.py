# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

# Create your views here.
def index(request):
    # Get data from Model
    todos = Todo.objects.all()[:10]

    # return HttpResponse('Hello World') ==> static response
    data = {
        'todos' : todos
    }
    return render(request, 'index.html', data)

def details(request, id):
    todo = Todo.objects.get(id=id)
    data = {
        'todo' : todo
    }
    return render(request, 'details.html', data)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        #saving data
        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/app')
    else:
        return render(request, 'add.html')
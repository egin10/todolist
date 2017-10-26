# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello World') ==> static response
    data = {
        'name' : 'Egin10'
    }
    return render(request, 'index.html', data)

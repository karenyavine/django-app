from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404

def index(request):

    name = 'Karen'
    template = loader.get_template('hello/index.html')
    context = {
        'name': name,
    }
    return render(request, 'hello/index.html', context)

def detail(request, name):
    return render(request, 'hello/name.html', {'name': 'karen'})

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
from .models import Names

def index(request):

    name = 'all'
    template = loader.get_template('hello/index.html')
    context = {
        'name': name,
    }
    return render(request, 'hello/index.html', context)

def detail(request, name):
    names_list = Names.objects.order_by('-pub_date')[:5]
    template = loader.get_template('hello/name.html')
    context = {
        'names_list': names_list,
    }
    return render(request, 'hello/name.html', context)

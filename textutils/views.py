# I have created this file - Vishal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Vishal', 'place':'Mars'}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("Hello About")
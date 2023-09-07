# I have created this file - Vishal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name':'Vishal', 'place':'Mars'}
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello About")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(djtext)
    print(removepunc)
    if removepunc=='on':
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose':'Remove punctuation',
                'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Please write a sentence')


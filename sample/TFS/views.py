# I have created this file
from typing import Dict

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Pass variable in templates.
    # params = {'name':'Divya','month':'1992'}
    return render(request, 'index.html')
    #return HttpResponse('''<h1> Hello!! This is my first site </h1> <a href="http://127.0.0.1:8000/about"> About src </a>''')

def about(request):
    aboutText = request.GET.get('text','default')
    print(aboutText)
    return HttpResponse('about us')

def signIn(request):
    signInText = request.GET.get('text', 'default')
    print(signInText)
    return HttpResponse('sign In')
from django.shortcuts import render
from django.http import HttpRequest

def test(request):
    return render(request, 'index.html')

def index(request):
    return HttpRequest('<h1>It works</h1>')

def third(request):
    return HttpRequest('<h1>It works</h1>')
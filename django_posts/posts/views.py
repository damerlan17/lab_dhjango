from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', context={"person": Person("Jon")})

class Person:

    def __init__(self, name):
        self.name = name
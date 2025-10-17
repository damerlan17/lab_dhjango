from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {"header": "helo world", "message": "urea in django"}
    return render(request, 'index.html', context=data)

# Create your views here.

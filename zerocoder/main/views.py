from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def second(request):
    return render(request, 'main/second.html')

def third(request):
    return render(request, 'main/third.html')


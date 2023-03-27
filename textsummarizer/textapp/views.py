from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    print(request.POST)
    return render(request, 'index.html')


def post(request):
    print(request.POST)
    return render(request, 'index.html')

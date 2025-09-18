from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def functionWorld(request) :
    return render(request,'hello.html')

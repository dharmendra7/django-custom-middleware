from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class DemoException(Exception):
    pass

def demoForProcessViewMiddleware(request):
    return HttpResponse("Demo procees view")

def demoForProcessExceptionMiddleware(request):
    
    raise DemoException('This is demo process exception')

    return HttpResponse("This is demo process exception view")
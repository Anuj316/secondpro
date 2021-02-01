from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def square(request):
    date=datetime.datetime.now()
    msg='<h1>Hello everyone! If you are seeing this that means I have deployed this seccessfully...</h1>'+str(date)
    return HttpResponse(msg)

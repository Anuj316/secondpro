from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def square(request):
    date=datetime.datetime.now()
    msg='<h1>square of 2 is 4</h1>'+str(date)
    return HttpResponse(msg)

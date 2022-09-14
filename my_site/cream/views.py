from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def unit(Request):
    return HttpResponse("Hey there, dont mess this app. Its worth it")

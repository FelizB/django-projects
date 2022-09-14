from urllib.request import HTTPPasswordMgr
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create(Request):
    return render(Request, 'first_app/example.html')

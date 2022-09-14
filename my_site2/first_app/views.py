from urllib.request import HTTPPasswordMgr
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create(Request):
    return HttpResponse("success is the factor")

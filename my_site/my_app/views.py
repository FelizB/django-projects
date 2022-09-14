from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hELLO THIS IS YOUR NIGGA Feliz, View inside my app")

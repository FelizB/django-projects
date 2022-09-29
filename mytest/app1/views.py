from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def simple(request):
    return render(request,'first_app/app.html')
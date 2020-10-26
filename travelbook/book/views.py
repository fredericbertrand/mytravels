from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    trips = Trip.objects.all()
    context = {"trips": trips}
    return render(request, "book/index.html", context)


def destination(request):
    context = {}
    return render(request, "book/destination.html", context)

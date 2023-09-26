from os import path, name
from django.shortcuts import render
def index(request):
     return render(request, "index.html")

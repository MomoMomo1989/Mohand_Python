from os import path, name
from django.shortcuts import render
def index1(request):
     return render(request, "Me.html")

from django.shortcuts import render

# Create your views here.
def conatct(request):
    return render(request, "contact.html")
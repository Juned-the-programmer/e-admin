from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, "pages/home.html", {'genres': Genre.objects.all()})    

def dashboard(request):
    return render(request,'pages/dashboard.html')

def order(request):
    return render(request,'pages/orders.html')

def nothing(request):
    return render(request, "pages/nothing.html", {'genres': Genre.objects.all()})
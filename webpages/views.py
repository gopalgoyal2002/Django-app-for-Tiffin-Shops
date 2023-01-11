from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def index(request):
    products=Products.objects.all()
    data={
        'products':products,
    }
    return render(request,'pages/home.html',data)

def services(request):
    products=Products.objects.all()
    data={
        'products':products,
    }
    return render(request,'pages/services.html',data)
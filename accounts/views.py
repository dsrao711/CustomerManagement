from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Homepage')
def customers(request):
    return HttpResponse('Customers')
def products (request):
    return HttpResponse('Products')

# Create your views here.
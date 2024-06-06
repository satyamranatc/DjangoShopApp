from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def ProductPage(request):
    return render(request, 'Product.html')

def ProductList(request):
    data = list(Product.objects.values()) 
    return JsonResponse({"List": data})

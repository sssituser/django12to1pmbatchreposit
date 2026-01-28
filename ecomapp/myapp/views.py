
from django.shortcuts import render
from django.views.generic import *
from myapp.models import Product

class ProductList(ListView):
    model = Product
    

class AddProduct(CreateView):
    model = Product
    fields='__all__'

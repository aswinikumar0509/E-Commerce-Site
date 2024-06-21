from django.shortcuts import render,HttpResponse
from . models import Product

# Create your views here.

def index(request):
    Product_object = Product.objects.all()
    return render(request , 'shop/index.html',context={'product_object':Product_object})

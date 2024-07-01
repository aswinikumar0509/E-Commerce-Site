from django.shortcuts import render,HttpResponse
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_object = Product.objects.all()

    # Search Functionality
    item_name = request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_object = product_object.filter(title__icontains=item_name)
    

    paginator = Paginator(product_object,4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    
    return render(request , 'shop/index.html',context={'product_object':product_object})


def detail(request,id):

    product_object = Product.objects.get(id=id)
    return render(request , 'shop/detail.html' ,context={'product_object':product_object})

def checkout(request):

    return render(request , 'shop/checkout.html')


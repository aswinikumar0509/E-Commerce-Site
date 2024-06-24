from django.shortcuts import render,HttpResponse
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    Product_object = Product.objects.all()

    # Search Functionality
    item_name = request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        Product_object = Product_object.filter(title__icontains=item_name)
    

    paginator = Paginator(Product_object,4)
    page = request.GET.get('page')
    Product_object = paginator.get_page(page)
    
    return render(request , 'shop/index.html',context={'product_object':Product_object})

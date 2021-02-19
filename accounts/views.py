from django.shortcuts import render
from django .http import HttpResponse

from . models import *



def home(request):
    orders = Orders .objects . all()
    customers = Customer.objects. all()
    return render (request , 'accounts/Dashboard.html', context)

    context = {'customers':customers , 'orders':orders}

def products(request):
    products = Product.objects.all()
    return render (request ,'accounts/products.html', {'products': products}) 

  


def customer(request):
    return render (request , 'accounts/customer.html')      

from django.shortcuts import render
from django .http import HttpResponse
from . models import *



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()

    delivered = Orders.filter(status='Delivered')
    # similar_actions = Action.objects.filter(created__gte=last_minute, user_id=user.id, verb=verb)

    pending = orders.filter(status='Pending').count()

    context = {'customers':customers , 'orders':orders,
    'total_orders':total_orders,'delivered':delivered, 'pending':pending }
    return render (request , 'accounts/Dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render (request ,'accounts/products.html', {'products': products}) 

  


def customer(request):
    return render (request , 'accounts/customer.html')      

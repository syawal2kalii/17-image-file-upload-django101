from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')

def dashboard(request):
    customers = Customer.objects.all()
    total_customer = customers.count()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'total_customer': total_customer,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)
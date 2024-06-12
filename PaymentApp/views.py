from django.shortcuts import render
from ProductsApp.models import Product

from django.conf import settings
import uuid
from django.urls import reverse

def paypal(request):
    return render(request, 'paypal.html')


def CheckOut(request, product_id):

    product = Product.objects.get(id=product_id)


    context = {
        'product': product,

    }

    return render(request, 'checkout.html', context)

def PaymentSuccessful(request, product_id):

    product = Product.objects.get(id=product_id)

    return render(request, 'payment-success.html', {'product': product})

def paymentFailed(request, product_id):

    product = Product.objects.get(id=product_id)

    return render(request, 'payment-failed.html', {'product': product})
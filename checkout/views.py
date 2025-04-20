from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
@csrf_exempt

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RCSZkBCvEtEjVCmxVBHXC2TrfQhqhAefC1jNYwHRbYe5YgbuRHVdgzUgv559ghcdQEgXheRW4fYgizx95WgI5EI00vyiXph76',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
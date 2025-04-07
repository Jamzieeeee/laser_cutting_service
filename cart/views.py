from django.shortcuts import render, redirect

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id, material_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        materials_cart = cart[item_id]
        if material_id in list(materials_cart.keys()):
            cart[item_id][material_id] += quantity
        else:
            cart[item_id][material_id] = quantity
    else:
        cart[item_id] = {}
        cart[item_id][material_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
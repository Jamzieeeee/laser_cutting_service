from django.shortcuts import render, redirect

# Create your views here.
def cart(request):
    if request.method=="POST":
        params = request.POST
        cart = request.session.get('cart', {})


        for field in params:
            field_parts = field.split("-")
            print(field)

            if field_parts[0]=="quantity":
                base_id = field_parts[1]
                material_id = field_parts[2]
                quantity = int(params[field])
                if quantity == 0:
                    del cart[base_id][material_id]
                else:
                    cart[base_id][material_id] = quantity
                
                request.session['cart'] = cart


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
    return redirect(redirect_url)
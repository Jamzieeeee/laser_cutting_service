from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
import math
from products.models import Base, Material


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for base_id, base_data in cart.items():
        for material_id, quantity in base_data.items():
            base = get_object_or_404(Base, pk=base_id)
            material = get_object_or_404(Material, pk=material_id)
            single_price = (math.ceil(material.cost_per_sheet / base.number_per_sheet)) / 100
            price = quantity * single_price
            total += price
            product_count += quantity
            cart_items.append({
                'base': base,
                'material': material,
                'single_price': single_price,
                'quantity': quantity,
                'price': price,
                'total': total,
            })
    
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD / 100 - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
from django.shortcuts import render
from .models import Base

# Create your views here.
def bases(request):
    products = Base.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/bases.html', context)

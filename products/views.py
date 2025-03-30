from django.shortcuts import render, get_object_or_404
from .models import Base, Material

# Create your views here.
def bases(request):
    products = Base.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/bases.html', context)


def base_detail(request, base_id):
    base = get_object_or_404(Base, pk=base_id)

    context = {
        'base': base,
    }

    return render(request, 'products/base_detail.html', context)


def materials(request):
    materials = Material.objects.all()

    context = {
        'products': materials,
    }

    return render(request, 'products/materials.html', context)
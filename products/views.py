from django.shortcuts import render, get_object_or_404
from .models import Base, Material
from .forms import MaterialForm
import math

# Create your views here.
def bases(request):
    products = Base.objects.all()
    materials = Material.objects.all()

    context = {
        'products': products,
        'materials': materials,
    }

    return render(request, 'products/bases.html', context)


def base_detail(request, base_id, material_id):
    base = get_object_or_404(Base, pk=base_id)
    material = get_object_or_404(Material, pk=material_id)

    price = (math.ceil(material.cost_per_sheet / base.number_per_sheet)) / 100

    form = MaterialForm()

    context = {
        'base': base,
        'material': material,
        'price': price,
        'form': form,
    }

    return render(request, 'products/base_detail.html', context)


def materials(request):
    materials = Material.objects.all()

    context = {
        'products': materials,
    }

    return render(request, 'products/materials.html', context)
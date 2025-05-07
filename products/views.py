from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Shape, Base, Material
from .forms import BaseForm, BaseDetailForm
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

    form = BaseDetailForm()

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


def product_admin(request):
    shapes = Shape.objects.all()
    bases = Base.objects.all()
    materials = Material.objects.all()

    context = {
        'shapes': shapes,
        'bases': bases,
        'materials': materials,
    }

    return render(request, 'products/product_admin.html', context)


def add_base(request):
    if request.method == 'POST':
        form = BaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added base!')
            return redirect(reverse('add_base'))
        else:
            messages.error(request, 'Failed to add base. Please ensure the form is valid.')
    else:
        form = BaseForm()

    template = 'products/add_base.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
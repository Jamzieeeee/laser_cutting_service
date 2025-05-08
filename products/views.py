from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Shape, Base, Material
from .forms import ShapeForm, BaseForm, MaterialForm, BaseDetailForm
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


@login_required
def product_admin(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    shapes = Shape.objects.all()
    bases = Base.objects.all()
    materials = Material.objects.all()

    context = {
        'shapes': shapes,
        'bases': bases,
        'materials': materials,
    }

    return render(request, 'products/product_admin.html', context)


# Shapes
@login_required
def add_shape(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ShapeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added shape!')
            return redirect(reverse('product_admin'))
        else:
            messages.error(request, 'Failed to add shape. Please ensure the form is valid.')
    else:
        form = ShapeForm()

    template = 'products/add_shape.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_shape(request, shape_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    shape = get_object_or_404(Shape, pk=shape_id)
    if request.method == 'POST':
        form = ShapeForm(request.POST, request.FILES, instance=shape)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated shape ID {shape_id}!')
            return redirect(reverse('product_admin'))
        else:
            messages.error(request, 'Failed to update shape. Please ensure the form is valid.')
    else:
        form = ShapeForm(instance=shape)

    template = 'products/edit_shape.html'
    context = {
        'form': form,
        'shape': shape,
    }

    return render(request, template, context)


@login_required
def delete_shape(request, shape_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    shape = get_object_or_404(Shape, pk=shape_id)
    shape.delete()
    messages.success(request, f'Successfully deleted shape ID {shape_id}!')
    return redirect(reverse('product_admin'))


# Bases
@login_required
def add_base(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added base!')
            return redirect(reverse('product_admin'))
        else:
            messages.error(request, 'Failed to add base. Please ensure the form is valid.')
    else:
        form = BaseForm()

    template = 'products/add_base.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_base(request, base_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    base = get_object_or_404(Base, pk=base_id)
    if request.method == 'POST':
        form = BaseForm(request.POST, request.FILES, instance=base)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated base ID {base_id}!')
            return redirect(reverse('product_admin'))
        else:
            messages.error(request, 'Failed to update base. Please ensure the form is valid.')
    else:
        form = BaseForm(instance=base)

    template = 'products/edit_base.html'
    context = {
        'form': form,
        'base': base,
    }

    return render(request, template, context)


@login_required
def delete_base(request, base_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    base = get_object_or_404(Base, pk=base_id)
    base.delete()
    messages.success(request, f'Successfully deleted base ID {base_id}!')
    return redirect(reverse('product_admin'))


# Materials
@login_required
def add_material(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added material!')
            return redirect(reverse('product_admin'))
        else:
            messages.error(request, 'Failed to add material. Please ensure the form is valid.')
    else:
        form = MaterialForm()

    template = 'products/add_material.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_material(request, material_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated material ID {material_id}!')
            return redirect(reverse('product_admin'))
        else:
            messages.error(request, 'Failed to update material. Please ensure the form is valid.')
    else:
        form = MaterialForm(instance=material)

    template = 'products/edit_material.html'
    context = {
        'form': form,
        'material': material,
    }

    return render(request, template, context)


@login_required
def delete_material(request, material_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    material = get_object_or_404(Material, pk=material_id)
    material.delete()
    messages.success(request, f'Successfully deleted material ID {material_id}!')
    return redirect(reverse('product_admin'))


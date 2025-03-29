from django.contrib import admin
from .models import Shape, Base, Material

# Register your models here.
class ShapeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',)


class BaseAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'shape',
        'number_per_sheet',
        'image',
    )

    ordering = ('shape', 'size',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost_per_sheet',
    )

    ordering = ('name',)


admin.site.register(Shape, ShapeAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Material, MaterialAdmin)

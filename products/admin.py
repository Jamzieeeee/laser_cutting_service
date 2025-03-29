from django.contrib import admin
from .models import Base, Material

# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'number_per_sheet',
    )


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost_per_sheet',
    )


admin.site.register(Base, BaseAdmin)
admin.site.register(Material, MaterialAdmin)

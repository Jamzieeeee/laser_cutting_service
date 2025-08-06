from django.urls import path
from . import views


urlpatterns = [
    path('bases/', views.bases, name='bases'),
    path('bases/<base_id>/<material_id>/', views.base_detail, name='base_detail'),
    path('materials/', views.materials, name='materials'),
    path('product_admin/', views.product_admin, name='product_admin'),
    path('add_shape/', views.add_shape, name='add_shape'),
    path('edit_shape/<shape_id>', views.edit_shape, name='edit_shape'),
    path('delete_shape/<shape_id>/', views.delete_shape, name='delete_shape'),
    path('add_base/', views.add_base, name='add_base'),
    path('edit_base/<base_id>', views.edit_base, name='edit_base'),
    path('delete_base/<base_id>/', views.delete_base, name='delete_base'),
    path('add_material/', views.add_material, name='add_material'),
    path('edit_material/<material_id>', views.edit_material, name='edit_material'),
    path('delete_material/<material_id>/', views.delete_material, name='delete_material'),
]

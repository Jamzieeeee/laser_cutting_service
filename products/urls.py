from django.urls import path
from . import views

urlpatterns = [
    path('bases/', views.bases, name='bases'),
    path('bases/<base_id>/<material_id>/', views.base_detail, name='base_detail'),
    path('materials/', views.materials, name='materials'),
    path('product_admin/', views.product_admin, name='product_admin'),
    path('add_base/', views.add_base, name='add_base'),
]

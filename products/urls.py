from django.urls import path
from . import views

urlpatterns = [
    path('bases/', views.bases, name='bases'),
    path('bases/<base_id>', views.base_detail, name='base_detail'),
    path('materials/', views.materials, name='materials'),
]

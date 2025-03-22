from django.db import models

# Create your models here.


class Base(models.Model):
    size = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    number_per_sheet = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)


class Material(models.Model):
    name = models.CharField(max_length=255)
    cost_per_sheet = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

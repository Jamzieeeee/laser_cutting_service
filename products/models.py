from django.db import models

# Create your models here.
class Shape(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Base(models.Model):
    shape = models.ForeignKey('Shape', null=True, blank=True, on_delete=models.SET_NULL)
    size = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    number_per_sheet = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(null=True, blank=True)


class Material(models.Model):
    name = models.CharField(max_length=255)
    cost_per_sheet = models.DecimalField(max_digits=5, decimal_places=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

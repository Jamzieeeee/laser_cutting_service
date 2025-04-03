from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material

        fields = []

    material = forms.ModelChoiceField(queryset=Material.objects.all(), to_field_name="id")

    quantity = forms.IntegerField(label="Quantity")
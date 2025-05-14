from django import forms
from .models import Shape, Base, Material


class BaseDetailForm(forms.ModelForm):
    class Meta:
        model = Material

        fields = []

    quantity = forms.IntegerField(
        label="Quantity",
        min_value=1,
        max_value=999,
        )


class ShapeForm(forms.ModelForm):

    class Meta:
        model = Shape
        fields = '__all__'


class BaseForm(forms.ModelForm):

    class Meta:
        model = Base
        fields = '__all__'

    number_per_sheet = forms.DecimalField(min_value=1, max_value=999)


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = '__all__'

    cost_per_sheet = forms.DecimalField(min_value=1, max_value=9999)

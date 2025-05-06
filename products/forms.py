from django import forms
from .models import Shape, Base, Material


class BaseDetailForm(forms.ModelForm):
    class Meta:
        model = Material

        fields = []

    quantity = forms.IntegerField(label="Quantity")


class BaseForm(forms.ModelForm):

    class Meta:
        model = Base
        fields = '__all__'
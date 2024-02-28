from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'city']
        labels = {
            'address': '',
            'city': '',
        }
        widgets = {
            'address': forms.TextInput(attrs={"class": "form-control text-end", "placeholder": "введите адрес"}),
            'city': forms.TextInput(attrs={"class": "form-control text-end", "placeholder": "введите город"}),
        }

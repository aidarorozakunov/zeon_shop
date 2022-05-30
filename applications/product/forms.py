from django.forms import ModelForm
from django.forms.widgets import TextInput

from applications.product.models import Product


class FooForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
                   'color': TextInput(attrs={'type': 'color'}),
                   }
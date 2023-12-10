from django import forms
from django.forms import ModelForm
from products.models import Product, Category

class ProductForm(ModelForm):
  class Meta :
    model = Product
    fields = '__all__'

    widgets = {
      'product_name': forms.TextInput(attrs={'class': 'form-control '}),
      'price': forms.NumberInput(attrs={'class': 'form-control'}),
      'category_id': forms.Select(attrs={'class': 'form-control'}),
      'status_id': forms.Select(attrs={'class': 'form-control'}),
    }
  
  def clean_product_name(self):
        # Change the product_name value to uppercase
        return self.cleaned_data['product_name'].upper()
  

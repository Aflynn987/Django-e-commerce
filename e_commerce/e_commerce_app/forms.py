from django import forms

from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['text']
        labels = {'text': ''}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
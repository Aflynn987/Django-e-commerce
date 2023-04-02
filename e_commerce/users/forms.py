from django import forms

from .models import User


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'date_of_birth', 'phone_number', 'address1', 'address2', 'city', 'state', 'zip_code', 'card_name', 'card_number', 'card_expiry', 'card_cvv']

    # Add form fields for the new User model fields here
    full_name = forms.CharField(label='Full name', max_length=255)
    date_of_birth = forms.DateField(label='Date of birth', widget=forms.TextInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(label='Phone number', max_length=20, required=False)
from django import forms
from .models import STATES_CHOICES, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address','address_complement','city','states','country')
        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'address_complement':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'states':forms.Select(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'})
        }
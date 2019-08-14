from django import forms
from supplier.models import Supplier

class AddCustomerDetailsForm(forms.ModelForm):
    class Meta:
        model   =   Supplier
        fields  =   ('name','address','mobile','phone')
        
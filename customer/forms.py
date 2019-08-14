from django import forms
from customer.models import Customer

class AddCustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','address','mobile','phone')
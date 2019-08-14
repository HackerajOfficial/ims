from django import forms
from stock.models import StockDetails


class AddStockDetailsForm(forms.ModelForm):
    
    class Meta:
        model = StockDetails
        fields = ("product_name","category","buying_rate","selling_rate","suplier","expire_date")

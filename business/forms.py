from django import forms
from .models import Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('ID','Name', 'Product Type', 'Supplier ID','Supplier', 'Quantity','Cost Price', 'Selling Price')

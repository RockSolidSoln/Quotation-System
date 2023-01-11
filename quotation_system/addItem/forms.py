from django import forms
from project.models import Quotation, QuotationItems

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['quotation_id', 
                'pr_id', 'salesman_id', 
                'manager_id', 'total_price',
                'date', 'status']

class QuotationItemsForm(forms.ModelForm):
    class Meta:
        model = QuotationItems
        fields = ['quotation_id',
                  'q_item_name','q_item_quantity'
                  ,'q_item_price']

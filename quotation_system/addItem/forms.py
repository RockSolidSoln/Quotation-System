from django import forms
from project.models import Quotation, QuotationItems

class QuotationForm(forms.ModelForm):
    total_price = forms.FloatField(label='Total Price')
    manager_id = forms.CharField(required=False)

    class Meta:
        model = Quotation
        fields = ['quotation_id', 
                'pr_id', 'salesman_id', 'customer_id',
                'manager_id', 'total_price',
                'date', 'status', 'number_of_items']

class QuotationItemsForm(forms.ModelForm):
    class Meta:
        model = QuotationItems
        fields = ['quotation_id',
                  'q_item_name','q_item_quantity'
                  ,'q_item_price']

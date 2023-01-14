from django import forms
from project.models import Quotation, PurchaseOrder, PurchaseRequisition

class PRForm(forms.ModelForm):

    class Meta:
        model = PurchaseRequisition
        fields = ['pr_id',
                  'customer_id',
                  'date', 'number_of_items']


class QuotationForm(forms.ModelForm):
    total_price = forms.FloatField(label='Total Price')
    manager_id = forms.CharField(required=False)

    class Meta:
        model = Quotation
        fields = ['quotation_id', 
                'pr_id', 'salesman_id', 'customer_id',
                'manager_id', 'total_price',
                'date', 'status', 'number_of_items']


class POForm(forms.ModelForm):

    class Meta:
        model = PurchaseOrder
        fields = ['po_id', 'quotation_id',
                  'customer_id', 'salesman_id',
                  'finance_officer_id', 'total_price'
                  , 'date', 'number_of_items']

"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control form-control-lg',
                                   'style': 'width: 100%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'style': 'width: 100%; padding: 12px 20px; margin: 8px 0; display: inline-block; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box;',
                                   'placeholder': 'Password'}))


class UserTypeForm(forms.Form):
    USER_TYPE_CHOICES = [
        ('PurchaseRequisitions', 'Customer'),
        ('Quotation', 'Salesman'),
        ('manager', 'Manager'),
        ('finance_officer', 'FinanceOfficer'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

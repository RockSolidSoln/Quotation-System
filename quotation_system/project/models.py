"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

#sharing entity
class Salesman(models.Model):
    salesman_id = models.CharField(primary_key=True, max_length=10)
    salesman_password = models.CharField(max_length=25, null=True)
    salesman_email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.salesman_id)

class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=10)
    customer_name = models.CharField(max_length=20, null=True)
    customer_email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.customer_id)

class Manager(models.Model):
    manager_id = models.CharField(primary_key=True, max_length=10)
    manager_name = models.CharField(max_length=20, null=True)
    manager_email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.manager_id)

class FinanceOfficer(models.Model):
    finance_officer_id = models.CharField(primary_key=True, max_length=10)
    finance_officer_name = models.CharField(max_length=20, null=True)
    finance_officer_email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.finance_officer)


class PurchaseRequisition(models.Model):
    pr_id = models.CharField(primary_key=True, max_length=10)
    customer_id = models.ForeignKey(Customer,default=None, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.product_id)

class Quotation(models.Model):
    quotation_id = models.CharField(primary_key=True, max_length=10)
    pr_id = models.ForeignKey(PurchaseRequisition,default=None, on_delete=models.CASCADE)
    salesman_id = models.ForeignKey(Salesman,default=None, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,default=None, on_delete=models.CASCADE)
    manager_id = models.ForeignKey(Manager,default=None, on_delete=models.CASCADE)
    total_price = models.FloatField(default=None, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.quotation_id)

class PurchaseOrder(models.Model):
    po_id = models.CharField(primary_key=True, max_length=10)
    quotation_id = models.ForeignKey(Quotation,default=None, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,default=None, on_delete=models.CASCADE)
    salesman_id = models.ForeignKey(Salesman,default=None, on_delete=models.CASCADE)
    finance_officer_id = models.ForeignKey(FinanceOfficer,default=None, on_delete=models.CASCADE)
    total_price = models.FloatField(default=None, null=True)
    date = models.DateField()
    
    def __str__(self):
        return str(self.po_id)

class PRItems(models.Model):
    pr_item_id = models.CharField(primary_key=True, max_length=10)
    pr_id = models.ForeignKey(PurchaseRequisition, default=None, on_delete=models.CASCADE)
    pr_item_name = models.CharField(max_length=40, null=True)
    pr_item_quantity = models.PositiveIntegerField(default=None, null=True)

    def __str__(self):
        return str(self.pr_item_id)

class QuotationItems(models.Model):
    q_item_id = models.CharField(primary_key=True, max_length=10)
    quotation_id = models.ForeignKey(Quotation, default=None, on_delete=models.CASCADE)
    q_item_name = models.CharField(max_length=40, null=True)
    q_item_quantity = models.PositiveIntegerField(default=None, null=True)
    q_item_price = models.FloatField(default=None, null=True)

    def __str__(self):
        return str(self.q_item_id)

class POItems(models.Model):
    po_item_id = models.CharField(primary_key=True, max_length=10)
    po_id = models.ForeignKey(PurchaseOrder,default=None, on_delete=models.CASCADE)
    po_item_name = models.CharField(max_length=40, null=True)
    po_item_quantity = models.PositiveIntegerField(default=None, null=True)
    po_item_price = models.FloatField(default=None, null=True)

    def __str__(self):
        return str(self.po_item_id)

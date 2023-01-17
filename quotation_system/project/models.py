"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User


# sharing entity

class Home(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Salesman(models.Model):
    salesman_id = models.CharField(primary_key=True, max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.salesman_id:
            # generate a custom id here
            self.salesman_id = "Quotation{:02d}".format(self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.salesman_id)


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            # generate a custom id here
            self.customer_id = "PurchaseRequisition{:02d}".format(self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.customer_id)


class Manager(models.Model):
    manager_id = models.CharField(primary_key=True, max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.manager_id:
            # generate a custom id here
            self.manager_id = "manager{:02d}".format(self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.manager_id)


class FinanceOfficer(models.Model):
    finance_officer_id = models.CharField(primary_key=True, max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.finance_officer_id:
            # generate a custom id here
            self.finance_officer_id = "finance_officer{:02d}".format(self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.finance_officer_id)


class PurchaseRequisition(models.Model):
    pr_id = models.CharField(primary_key=True, max_length=10)
    customer_id = models.ForeignKey(Customer, default=None, on_delete=models.PROTECT)
    date = models.DateField()
    number_of_items = models.PositiveIntegerField(default=None, null=True)

    def __str__(self):
        return str(self.pr_id)


class Quotation(models.Model):
    status_option = (
        ('Uncleared', 'Uncleared'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
    )
    quotation_id = models.CharField(primary_key=True, max_length=10)
    pr_id = models.ForeignKey(PurchaseRequisition, default=None, on_delete=models.CASCADE)
    salesman_id = models.ForeignKey(Salesman, default=None, on_delete=models.PROTECT)
    customer_id = models.ForeignKey(Customer, default=None, on_delete=models.PROTECT)
    manager_id = models.ForeignKey(Manager, default="MAN0001", on_delete=models.PROTECT)
    total_price = models.FloatField(default=None, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=status_option, default='Uncleared')
    number_of_items = models.PositiveIntegerField(default=None, null=True)

    def price_display(self):
        return "${:,.2f}".format(self.total_price)

    def __str__(self):
        return str(self.quotation_id)

    def update_status(self):
        if self.status == 'Approved':
            self.status = 'Approved'
        elif self.status == 'Declined':
            self.status = 'Declined'
        self.save()


class PurchaseOrder(models.Model):
    po_id = models.CharField(primary_key=True, max_length=10)
    quotation_id = models.ForeignKey(Quotation, default=None, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, default=None, on_delete=models.PROTECT)
    salesman_id = models.ForeignKey(Salesman, default=None, on_delete=models.PROTECT)
    finance_officer_id = models.ForeignKey(FinanceOfficer, default=None, on_delete=models.PROTECT)
    total_price = models.FloatField(default=None, null=True)
    date = models.DateField()
    number_of_items = models.PositiveIntegerField(default=None, null=True)

    def price_display(self):
        return "${:,.2f}".format(self.total_price)

    def __str__(self):
        return str(self.po_id)


class PRItems(models.Model):
    pr_item_id = models.AutoField(primary_key=True)
    pr_id = models.ForeignKey(PurchaseRequisition, default=None, on_delete=models.CASCADE)
    pr_item_name = models.CharField(max_length=40, null=True)
    pr_item_quantity = models.PositiveIntegerField(default=None, null=True)

    def __str__(self):
        return str(self.pr_item_id)


class QuotationItems(models.Model):
    q_item_id = models.AutoField(primary_key=True)
    quotation_id = models.ForeignKey(Quotation, default=None, on_delete=models.CASCADE)
    q_item_name = models.CharField(max_length=40, null=True)
    q_item_quantity = models.PositiveIntegerField(default=None, null=True)
    q_item_price = models.FloatField(default=None, null=True)

    def __str__(self):
        return str(self.q_item_id)


class POItems(models.Model):
    po_item_id = models.AutoField(primary_key=True)
    po_id = models.ForeignKey(PurchaseOrder, default=None, on_delete=models.CASCADE)
    po_item_name = models.CharField(max_length=40, null=True)
    po_item_quantity = models.PositiveIntegerField(default=None, null=True)
    po_item_price = models.FloatField(default=None, null=True)

    def __str__(self):
        return str(self.po_item_id)

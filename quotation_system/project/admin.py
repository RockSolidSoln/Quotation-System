from django.contrib import admin
from project.models import Salesman, Customer, Manager, FinanceOfficer, PurchaseOrder, PurchaseRequisition, Quotation, PRItems, POItems, QuotationItems

admin.site.register(Salesman)
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(FinanceOfficer)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseRequisition)
admin.site.register(Quotation)
admin.site.register(POItems)
admin.site.register(PRItems)
admin.site.register(QuotationItems)


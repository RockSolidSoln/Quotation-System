from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from project.models import PurchaseRequisition, PurchaseOrder, Quotation, PRItems, POItems, QuotationItems, Salesman
from .forms import QuotationForm, QuotationItemsForm

# Create your views here.

@login_required
def add_quotation(request):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id

    context = {
            'salesman_id': salesman_id,
            'year': datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'addItem/addQuotation.html',context)

def add_quotation_form(request):
    
    return render(request,'addItem/addQuotation.html',context)

def show_quotation(request):
    new_quotation_id = request.POST['quotation_id']
    new_pr_id= request.POST['pr_id']
    new_salesman_id = request.POST['salesman_id']
    new_customer_id = request.POST['customer_id']
    new_manager_id = request.POST['manager_id']
    new_price = request.POST['total_price']
    new_date = request.POST['date']
    new_status = request.POST['status']

    salesman = Salesman.objects.get(pk=salesman_id)
    manager = Manager.objects.get(pk=manager_id)
    customer = Customer.objects.get(pk=customer_id)
    pr = PurchaseRequistion.objects.get(pk=pr_id)
    
    newEntry = Quotation(quotation_id = new_quotation_id, pr_id = new_pr_id, 
                salesman_id= new_salesman_id, customer_id = new_customer_id, 
                manager_id = new_manager, total_price = new_price,
                date = new_date, status = new_status)
    newEntry.save()

    context = {
        'quotation_id': new_quotation_id,
        'pr_id': new_pr_id,
        'salesman_id': newitem_description,
        'customer_id': vendor,
        'manager_id': newitem_quantity,
        'total_price': newitem_price,
        'date' : new_date,
        'status' : new_status
    }
    return render(request,'additem/addQuotation.html',context)

   
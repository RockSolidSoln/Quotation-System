from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from project.models import PurchaseRequisition, PurchaseOrder, Quotation, PRItems, POItems, QuotationItems, Salesman, Manager, Customer, FinanceOfficer
from .forms import QuotationForm, QuotationItemsForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.

@login_required
def add_quotation(request):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id
    pr_id = list(PurchaseRequisition.objects.values_list('pr_id', flat=True))

    context = {
            'salesman_id': salesman_id,
            'pr_id': pr_id,
            'year': datetime.now().year,
        }
    context['user'] = request.user

    if request.method == 'POST':
        form = QuotationForm(request.POST)

        if form.is_valid():
            quotation = form.save()
            item_count = quotation.number_of_items
            for i in range(item_count):
                q_item_name = request.POST.get(f'q_item_name')
                print(q_item_name)
                q_item_quantity = request.POST.get(f'q_item_quantity')
                q_item_price = request.POST.get(f'q_item_price')
                QuotationItems.objects.create(q_item_name=q_item_name, 
                                q_item_quantity=q_item_quantity, 
                                q_item_price=q_item_price, 
                                quotation_id=quotation)
                print("Successfully created Quotation")
        else:
            print(form.errors)
            print("Error creating Quotation")
            return render(request, 'addItem/addQuotation.html', context)

    return render(request,'addItem/addQuotation.html',context)

def get_customer_id(request):
    pr_id = request.GET.get('pr_id')
    try:
        pr = PurchaseRequisition.objects.get(pr_id=pr_id)
        customer = pr.customer_id
        print(customer)
        customer_dict = model_to_dict(customer)
        return JsonResponse(customer_dict, safe=False)
    except PurchaseRequisition.DoesNotExist:
        print("Error in getting Customer Id")
        return JsonResponse({'error': 'Invalid Purchase Requisition ID'}, status=400)


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
    pr = PurchaseRequisition.objects.get(pk=pr_id)
    
    newEntry = Quotation(quotation_id = new_quotation_id, pr_id = new_pr_id, 
                salesman_id= new_salesman_id, customer_id = new_customer_id, 
                manager_id = new_manager_id, total_price = new_price,
                date = new_date, status = new_status)
    newEntry.save()

    context = {
        'quotation_id': new_quotation_id,
        'pr_id': new_pr_id,
        'salesman_id': new_salesman_id,
        'customer_id': new_customer_id,
        'manager_id': new_manager_id,
        'total_price': new_price,
        'date' : new_date,
        'status' : new_status
    }
    return render(request,'additem/addQuotation.html',context)

   
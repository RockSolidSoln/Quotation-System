from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from project.models import PurchaseRequisition, PurchaseOrder, Quotation, PRItems, POItems, QuotationItems, Salesman,  Manager, Customer, FinanceOfficer
from .forms import QuotationForm, POForm, PRForm
from django.http import JsonResponse
from django.forms.models import model_to_dict


# Create your views here.

def add_PR(request):
    customer_id = Customer.objects.get(user=request.user).customer_id
    context = {'customer_id': customer_id, 'user': request.user}

    if request.method == 'POST':
        form = PRForm(request.POST)

        if form.is_valid():
            pr = form.save()
            messages.success(request, 'Data was successfully entered in the database.')

            item_count = pr.number_of_items

            print(item_count)
            pr_item_name_list = request.POST.getlist('pr_item_name')
            pr_item_quantity_list = request.POST.getlist('pr_item_quantity')

            for i in range(item_count):
                pr_item_name = pr_item_name_list[i]
                print(pr_item_name)
                pr_item_quantity = pr_item_quantity_list[i]
                PRItems.objects.create(pr_item_name=pr_item_name,
                                       pr_item_quantity=pr_item_quantity,
                                       pr_id=pr)
                print("Successfully created Quotation")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/addPR.html', context)

    return render(request, 'addItem/addPR.html', context)


def add_quotation(request):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id
    pr_id = list(PurchaseRequisition.objects.values_list('pr_id', flat=True))

    context = {'salesman_id': salesman_id, 'pr_id': pr_id, 'year': datetime.now().year, 'user': request.user}

    if request.method == 'POST':
        form = QuotationForm(request.POST)

        if form.is_valid():
            quotation = form.save()
            messages.success(request, 'Data was successfully entered in the database.')
            item_count = quotation.number_of_items
            q_item_name_list = request.POST.getlist('q_item_name')
            q_item_quantity_list = request.POST.getlist('q_item_quantity')
            q_item_price_list = request.POST.getlist('q_item_price')
            for i in range(item_count):
                q_item_name = q_item_name_list[i]
                print(q_item_name)
                q_item_quantity = q_item_quantity_list[i]
                q_item_price = q_item_price_list[i]
                QuotationItems.objects.create(q_item_name=q_item_name,
                                              q_item_quantity=q_item_quantity,
                                              q_item_price=q_item_price,
                                              quotation_id=quotation)
                print("Successfully created Quotation")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/addQuotation.html', context)

    return render(request, 'addItem/addQuotation.html', context)


def add_PO(request):
    finance_officer_id = FinanceOfficer.objects.get(user=request.user).finance_officer_id
    quotation_id = list(Quotation.objects.values_list('quotation_id', flat=True).filter(status__in=["Accepted"]))
    # Quotations = Quotation.objects.filter(status__in=['Uncleared', 'Rejected', 'Approved']).values()

    context = {
        'finance_officer_id': finance_officer_id,
        'quotation_id': quotation_id,
        'user': request.user}

    if request.method == 'POST':
        form = POForm(request.POST)
        if form.is_valid():
            PO = form.save()

            messages.success(request, 'Data was successfully entered in the database.')
            item_count = PO.number_of_items

            po_item_name_list = request.POST.getlist('po_item_name')
            po_item_quantity_list = request.POST.getlist('po_item_quantity')
            po_item_price_list = request.POST.getlist('po_item_price')
            for i in range(item_count):
                po_item_name = po_item_name_list[i]
                print(po_item_name)
                po_item_quantity = po_item_quantity_list[i]
                po_item_price = po_item_price_list[i]
                POItems.objects.create(po_item_name=po_item_name,
                                       po_item_quantity=po_item_quantity,
                                       po_item_price=po_item_price,
                                       po_id=PO)
                print("Successfully created Quotation")
        else:
            print(form.errors)
            messages.error(request, 'Data was not entered in the database')
            return render(request, 'addItem/addPO.html', context)

    return render(request, 'addItem/addPO.html', context)


def customer_id(request):
    quotation_id = request.GET.get('quotation_id')

    try:
        q = Quotation.objects.get(quotation_id=quotation_id)
        print(q)
        customer = q.customer_id
        print(customer)
        customer_dict = model_to_dict(customer)
        return JsonResponse(customer_dict, safe=False)

    except Quotation.DoesNotExist:
        print("Error in getting Customer Id")
        return JsonResponse({'error': 'Invalid Quotation ID'}, status=400)


def salesman_id(request):
    quotation_id = request.GET.get('quotation_id')

    try:
        q = Quotation.objects.get(quotation_id=quotation_id)
        print(q)
        salesman = q.salesman_id
        print(salesman)
        customer_dict = model_to_dict(salesman)
        return JsonResponse(customer_dict, safe=False)

    except Quotation.DoesNotExist:
        print("Error in getting Salesman Id")
        return JsonResponse({'error': 'Invalid Quotation ID'}, status=400)


def get_customer_id(request):
    pr_id = request.GET.get('pr_id')
    print(pr_id)
    try:
        pr = PurchaseRequisition.objects.get(pr_id=pr_id)
        customer = pr.customer_id
        print(customer)
        customer_dict = model_to_dict(customer)
        return JsonResponse(customer_dict, safe=False)
    except PurchaseRequisition.DoesNotExist:
        print("Error in getting Customer Id")
        return JsonResponse({'error': 'Invalid Purchase Requisition ID'}, status=400)

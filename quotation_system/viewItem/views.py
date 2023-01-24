from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from project.models import QuotationItems, Quotation, Salesman, Customer, FinanceOfficer, PurchaseOrder, POItems, PurchaseRequisition, PRItems
from addItem.forms import QuotationForm
from django.views.decorators.csrf import csrf_exempt


def view_purchase_requisition(request):
    Pr = PurchaseRequisition.objects.all()
    Pr_item = PRItems.objects.all()

    context = {
        'Pr': Pr,
        'Pr_item': Pr_item
    }
    return render(request, 'PurchaseRequisitions/viewAllPR.html', context)


def view_PR(request):
    customer_id = Customer.objects.get(user=request.user).customer_id

    PR = PurchaseRequisition.objects.filter(customer_id=customer_id)
    PR_item = PRItems.objects.all().values()

    print(PR_item)
    context = {
        'Pr': PR,
        'Pr_item': PR_item
    }

    return render(request, 'PurchaseRequisitions/viewCustomerPR.html', context)


def view_one_PR(request, pr_id):
    select_pr_id = PurchaseRequisition.objects.get(pr_id=pr_id)

    is_salesman = request.user.groups.filter(name='Salesman').exists()
    is_customer = request.user.groups.filter(name='Customer').exists()

    Pr_item = PRItems.objects.filter(pr_id=select_pr_id)

    print(Pr_item)
    context = {
        'selected_pr': select_pr_id,
        'Pr_item': Pr_item,
        'salesman': is_salesman,
        'customer': is_customer,
    }
    return render(request, 'PurchaseRequisitions/viewOnePR.html', context)


def purchase_requisition_view_sort(request, sort_by=None):
    Pr = PurchaseRequisition.objects.all()
    Pr_item = PRItems.objects.all()
    if sort_by:
        if sort_by == 'number_of_items':
            Pr = Pr.order_by('number_of_items')
        elif sort_by == '-number_of_items':
            Pr = Pr.order_by('-number_of_items')
        elif sort_by == 'date':
            Pr = Pr.order_by('date')
        elif sort_by == '-date':
            Pr = Pr.order_by('-date')

    context = {
        'Pr': Pr,
        'Pr_item': Pr_item
    }
    return render(request, 'PurchaseRequisitions/viewCustomerPR.html', context)


# manager can view all the quotation
# customer only the active one
def view_all_quotation(request):
    is_customer = request.user.groups.filter(name='Customer').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()

    if (is_customer):
        Quotations = Quotation.objects.filter(status__in=['Accepted', 'Rejected', 'Approved']).values()
    else:
        Quotations = Quotation.objects.all().values()

    Quotation_item = QuotationItems.objects.all().values()

    print(Quotation)
    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item,
        'customer': is_customer,
        'manager': is_manager,
    }

    return render(request, 'Quotation/viewAllQuotation.html', context)

# salesman view quotation for himself only
def view_quotation(request):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id

    Quotations = Quotation.objects.filter(salesman_id=salesman_id)
    Quotation_item = QuotationItems.objects.all().values()

    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item
    }

    return render(request, 'Quotation/viewSalesmanQuotation.html', context)

def quotations_view_sort(request,sort_by=None):
    Quotations = Quotation.objects.all()
    Quotation_item = QuotationItems.objects.all().values()

    if sort_by:
        if sort_by == 'total_price':
            Quotations = Quotations.order_by('total_price')
        elif sort_by == '-total_price':
            Quotations = Quotations.order_by('-total_price')
        elif sort_by == 'date':
            Quotations = Quotations.order_by('date')
        elif sort_by == '-date':
            Quotations = Quotations.order_by('-date')
        elif sort_by == 'customer_id':
            Quotations = Quotations.order_by('customer_id')
        elif sort_by == '-customer_id':
            Quotations = Quotations.order_by('-customer_id')
        elif sort_by == 'salesman_id':
            Quotations = Quotations.order_by('salesman_id')
        elif sort_by == '-salesman_id':
            Quotations = Quotations.order_by('-salesman_id')

    is_manager = request.user.groups.filter(name='Manager').exists()
    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item,
        'manager': is_manager
    }
    if(request.user.groups.filter(name='Salesman').exists()):
        return render(request, 'Quotation/viewSalesmanQuotation.html', context)
    else:
        return render(request, 'Quotation/viewAllQuotation.html', context)

# function for manager to view and update quotation
def view_active_quotation(request):
    Quotations = Quotation.objects.all().values()
    Quotation_item = QuotationItems.objects.all().values()

    Quotations = Quotation.objects.filter(status__in=['Uncleared', 'Rejected', 'Approved']).values()

    print(Quotation_item)
    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item
    }

    return render(request, 'Quotation/viewManagerQuotation.html', context)

# function to view one quotation
def view_one_quotation(request, quotation_id):
    select_q_id = Quotation.objects.get(quotation_id=quotation_id)

    is_salesman = request.user.groups.filter(name='Salesman').exists()
    is_customer = request.user.groups.filter(name='Customer').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()

    current_status = Quotation.objects.get(quotation_id=quotation_id).status

    Quotation_item = QuotationItems.objects.filter(quotation_id=select_q_id)
    is_approved = False
    if current_status == 'Approved':
        is_approved = True
        print(is_approved)
    else:
        is_approved = False
    print(current_status)
    context = {
        'selected_quotation': select_q_id,
        'Quotation_item': Quotation_item,
        'salesman': is_salesman,
        'customer': is_customer,
        'is_approved': is_approved,
        'manager': is_manager,
    }
    return render(request, 'Quotation/viewOneQuotation.html', context)


@csrf_exempt
def update_quotation(request):
    if request.method == 'POST':
        quotation_id = request.POST.get('quotation_id')
        status_type = request.POST.get('status_type')

        print(quotation_id + "," + status_type)
        if status_type == 'Accepted':
            Quotation.objects.filter(quotation_id=quotation_id).update(status='Accepted')
        elif status_type == 'Approved':
            Quotation.objects.filter(quotation_id=quotation_id).update(status='Approved')
        elif status_type == 'Declined':
            Quotation.objects.filter(quotation_id=quotation_id).update(status='Declined')
        elif status_type == 'Rejected':
            Quotation.objects.filter(quotation_id=quotation_id).update(status='Rejected')
        return JsonResponse("Status saved", safe=False)
    else:
        return HttpResponseBadRequest("Invalid request method")


def view_PO(request):
    fo_id = FinanceOfficer.objects.get(user=request.user).finance_officer_id

    PO = PurchaseOrder.objects.filter(finance_officer_id=fo_id)
    Po_item = POItems.objects.all().values()

    print(Po_item)
    context = {
        'PO': PO,
        'PO_item': Po_item
    }

    return render(request, 'PurchaseOrder/viewPO.html', context)


def view_one_PO(request, po_id):
    select_po_id = PurchaseOrder.objects.get(po_id=po_id)

    PO_item = POItems.objects.filter(po_id=select_po_id)

    print(PO_item)
    context = {
        'selected_po': select_po_id,
        'PO_item': PO_item
    }
    return render(request, 'PurchaseOrder/viewOnePO.html', context)


def purchase_order_view_sort(request, sort_by=None):
    PO = PurchaseOrder.objects.all()
    PO_item = POItems.objects.all()

    if sort_by:
        if sort_by == 'total_price':
            PO = PO.order_by('total_price')
        elif sort_by == '-total_price':
            PO = PO.order_by('-total_price')
        elif sort_by == 'date':
            PO = PO.order_by('date')
        elif sort_by == '-date':
            PO = PO.order_by('-date')
        elif sort_by == 'salesman_id':
            PO = PO.order_by('salesman_id')
        elif sort_by == '-salesman_id':
            PO = PO.order_by('-salesman_id')

    context = {
        'PO': PO,
        'PO_item': PO_item
    }
    return render(request, 'PurchaseOrder/viewPO.html', context)

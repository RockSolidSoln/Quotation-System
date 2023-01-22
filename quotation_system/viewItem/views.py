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


def view_all_quotation(request):
    is_customer = request.user.groups.filter(name='Customer').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()
    if (is_customer):
        Quotations = Quotation.objects.filter(status__in=['Accepted', 'Rejected', 'Approved']).values()
    else:
        Quotations = Quotation.objects.all().values()

    Quotation_item = QuotationItems.objects.all().values()

    print(Quotation_item)
    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item,
        'customer': is_customer,
        'manager': is_manager,
    }

    return render(request, 'Quotation/viewAllQuotation.html', context)


def view_quotation(request):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id

    Quotations = Quotation.objects.filter(salesman_id=salesman_id)
    Quotation_item = QuotationItems.objects.all().values()

    print(Quotation_item)
    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item
    }

    return render(request, 'Quotation/viewSalesmanQuotation.html', context)


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

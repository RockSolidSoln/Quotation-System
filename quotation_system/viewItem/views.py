from django.shortcuts import render
from project.models import QuotationItems, Quotation, Salesman, Customer, FinanceOfficer, PurchaseOrder, POItems, \
    PurchaseRequisition, PRItems


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
    Quotations = Quotation.objects.all().values()
    Quotation_item = QuotationItems.objects.all().values()

    is_customer = request.user.groups.filter(name='Customer').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()
    if(is_manager):
        Quotations = Quotation.objects.all().values()
        Quotation_item = QuotationItems.objects.all().values()
    elif(is_customer):
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

    Quotation_item = QuotationItems.objects.filter(quotation_id=select_q_id)

    print(Quotation_item)
    context = {
        'selected_quotation': select_q_id,
        'Quotation_item': Quotation_item,
        'salesman': is_salesman,
        'customer': is_customer,
        'manager': is_manager,
    }
    return render(request, 'Quotation/viewOneQuotation.html', context)


def update_quotation(request, quotation_id):
    select_q_id = Quotation.objects.get(quotation_id=quotation_id)

    print("I'm here"+select_q_id)
    context = {
        'quotation_id': select_q_id,
    }

    status = "approved"
    select_q_id.status = status
    select_q_id.save()


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

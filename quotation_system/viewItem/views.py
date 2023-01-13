from django.shortcuts import render
from project.models import PurchaseRequisition, PRItems, QuotationItems, Quotation, Salesman


# Create your views here.

def view_purchase_requisition(request):
    Pr = PurchaseRequisition.objects.all()
    Pr_item = PRItems.objects.all()

    context = {
        'Pr': Pr,
        'Pr_item': Pr_item
    }
    return render(request, 'salesman/viewPR.html', context)


def view_one_PR(request):
    return render(request, 'salesman/viewOnePR.html')


def view_quotation(request):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id

    Quotations = Quotation.objects.filter(salesman_id=salesman_id)
    Quotation_item = QuotationItems.objects.all().values()

    print(Quotation_item)
    context = {
        'Quotations': Quotations,
        'Quotation_item': Quotation_item
    }

    return render(request, 'salesman/viewQuotation.html', context)


def view_one_quotation(request, quotation_id):
    salesman_id = Salesman.objects.get(user=request.user).salesman_id
    select_q_id = Quotation.objects.get(quotation_id=quotation_id)

    Quotation_item = QuotationItems.objects.filter(quotation_id=select_q_id)

    print(Quotation_item)
    context = {
        'selected_quotation': select_q_id,
        'Quotation_item': Quotation_item
    }
    return render(request, 'salesman/viewOneQuotation.html', context)


def view_PO(request):
    return render(request, 'finance officer/viewPO.html')


def view_one_PO(request):
    return render(request, 'finance officer/viewOnePO.html')

"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import PurchaseRequisition, PRItems

from .models import Customer, FinanceOfficer, Manager, Salesman
from .forms import UserTypeForm

from django.contrib.auth.decorators import login_required

def create_user(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            if user_type == 'customer':
                customer = Customer(user=request.user)
                customer.save()
            elif user_type == 'salesman':
                salesman = Salesman(user=request.user)
                salesman.save()
            elif user_type == 'manager':
                manager = Manager(user=request.user)
                manager.save()
            elif user_type == 'finance_officer':
                finance_officer = FinanceOfficer(user=request.user)
                finance_officer.save()
            return redirect('users_list')
    else:
        form = UserTypeForm()
    return render(request, 'users/create.html', {'form': form})

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/dashboard'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

@login_required

def dashboard(request):
    role = request.user.groups.get()
    print(role)

    mydata= Salesman.objects.all().values()

    print(mydata)
    is_salesman = request.user.groups.filter(name='Salesman').exists()
    is_customer = request.user.groups.filter(name='Customer').exists()
    if(is_salesman == True):
        mydata = Salesman.objects.values_list('salesman_id')
    if(request.user.groups.filter(name='Customer').exists() == True):
        mydata = Customer.objects.values_list('customer_id')
    if(request.user.groups.filter(name='Manager').exists() == True):
        mydata = Manager.objects.values_list('manager_id')
    if(request.user.groups.filter(name='FinanceOfficer').exists() == True):
        mydata = FinanceOfficer.objects.values_list('finance_officer_id')  
    
    print(mydata)

    context = {
            'sys_id': mydata,
            'salesman': is_salesman,
            'customer': is_customer,
            'role': request.user.groups.get(),
            'year':datetime.now().year,
        }
    context['user'] = request.user
    print(context)

    return render(request,'app/dashboard.html',context)    

"""
Customer pages
"""

def apr(request):
    return render(request, 'customer/APR.html')

def vspr(request):
    Pr = PurchaseRequisition.objects.all()
    Pr_item = PRItems.objects.all()
    return render(request, 'customer/VSPR.html', {'Pr' : Pr, 'Pr_item' : Pr_item})

def vq(request):
    return render(request, 'customer/VQ.html')

"""
Salesman pages
"""

def add_quotation(request):
    return render(request, 'salesman/addQuotation.html')

def view_purchase_requisition(request):
    return render(request, 'salesman/viewPR.html')

def view_one_PR(request):
    return render(request, 'salesman/viewOnePR.html')

def view_quotation(request):
    return render(request, 'salesman/viewQuotation.html')

def view_one_quotation(request):
    return render(request, 'salesman/viewOneQuotation.html')


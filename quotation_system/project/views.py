"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from .models import Customer, FinanceOfficer, Manager, Salesman
from .forms import UserTypeForm
from django.views.generic import ListView
from view_breadcrumbs import ListBreadcrumbMixin

from django.contrib.auth.decorators import login_required

def create_user(request):
    if request.method == 'POST':
        form = UserTypeForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            if user_type == 'PurchaseRequisitions':
                customer = Customer(user=request.user)
                customer.save()
            elif user_type == 'Quotation':
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

    is_salesman = request.user.groups.filter(name='Salesman').exists()
    is_customer = request.user.groups.filter(name='Customer').exists()
    is_finance_officer = request.user.groups.filter(name='Finance Officer').exists()
    is_manager = request.user.groups.filter(name='Manager').exists()

    if(is_salesman == True):
        mydata = Salesman.objects.get(user=request.user).salesman_id
    if(is_customer == True):
        mydata = Customer.objects.get(user=request.user).customer_id
    if(is_manager == True):
        mydata = Manager.objects.get(user=request.user).manager_id
    if(is_finance_officer == True):
        mydata = FinanceOfficer.objects.get(user=request.user).finance_officer_id  
    
    print(mydata)
    context = {
            'sys_id': mydata,
            'salesman': is_salesman,
            'customer': is_customer,
            'finance_officer': is_finance_officer,
            'manager': is_manager,
            'role': role,
        }
    # context['user'] = request.user
    print(context)

    return render(request, 'app/dashboard.html',context)

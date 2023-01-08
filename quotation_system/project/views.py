"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
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
        return(redirect('/menu'))
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
def menu(request):
    role = request.user.groups.get()

    print(role)
    
    check_employee = request.user.groups.filter(name='Salesman').exists()
    
    context = {
            # 'title':'Main Menu',
            'role': check_employee,
            'year':datetime.now().year,
        }

    print(context)

    context['user'] = request.user

    if(request.user.groups.filter(name='Salesman').exists()):
        return render(request,'salesman/index.html',context)
    
    elif(request.user.groups.filter(name='Customer').exists()):
        return render(request,'customer/index.html',context)
    
    elif(request.user.groups.filter(name='Manager').exists()):
        return render(request,'manager/index.html',context)
    
    elif(request.user.groups.filter(name='Finance Officer').exists()):
        return render(request,'finance officer/index.html',context)
        
    else:
        return render(request,'app/menu.html',context)    

"""
Customer pages
"""

def apr(request):
    return render(request, 'customer/APR.html')

def vspr(request):
    return render(request, 'customer/VSPR.html')

def vq(request):
    return render(request, 'customer/VQ.html')

def index(request):
    return render(request, 'customer/index.html')

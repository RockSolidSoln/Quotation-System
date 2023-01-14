"""myproject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from project import views, forms
from addItem import views as additem_views
from viewItem import views as view_items
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

admin.autodiscover()



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^login/$',
            LoginView.as_view(template_name='registration/login.html'),
            name='login'),
    re_path(r'^logout$',
            LogoutView.as_view(template_name='app/index.html'),
            name='logout'),
    re_path(r'^dashboard$', views.dashboard, name='dashboard'),

    # View urls
    path('view_purchase_requisition/', view_items.view_purchase_requisition, name='view_purchase_requisition'),
    path('view_PR/', view_items.view_PR, name='view_PR'),
    path('view_one_PR/', view_items.view_one_PR, name='view_one_PR'),
    path('view_one_PR/<str:pr_id>/', view_items.view_one_PR, name='view_one_PR'),

    path('view_quotation/', view_items.view_quotation, name='view_quotation'),
    path('view_one_quotation/', view_items.view_one_quotation, name='view_one_quotation'),
    path('view_quotation/<str:quotation_id>/', view_items.view_one_quotation, name='view_one_quotation'),
    path('view_all_quotation/', view_items.view_all_quotation, name='view_all_quotation'),

    path('view_PO/', view_items.view_PO, name='view_PO'),
    path('view_one_PO/', view_items.view_one_PO, name='view_one_PO'),
    path('view_one_PO/<str:po_id>', view_items.view_one_PO, name='view_one_PO'),


    # Add Item urls
    path('add_quotation/', additem_views.add_quotation, name='add_quotation'),
    path('add_PO/', additem_views.add_PO, name='add_PO'),
    path('add_PR/', additem_views.add_PR, name='add_PR'),

    path('customer_id/', additem_views.customer_id, name='customer_id'),
    path('salesman_id/', additem_views.salesman_id, name='salesman_id'),
    path('get_customer_id/', additem_views.get_customer_id, name='get_customer_id'),

]

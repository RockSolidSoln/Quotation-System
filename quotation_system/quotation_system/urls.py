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
from django.urls import path, re_path
from project import views, forms
from addItem import views as additem_views
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'registration/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^dashboard$', views.dashboard, name='dashboard'),
    re_path(r'^apr$', views.apr, name='apr'),
    re_path(r'^vspr$', views.vspr, name='vspr'),
    re_path(r'^vq$', views.vq, name='vq'),
    path('view-purchase-requisition/', views.view_purchase_requisition, name='view_purchase_requisition'),
    path('view_quotation/', views.view_quotation, name='view_quotation'),
    path('add_quotation/', additem_views.add_quotation, name='add_quotation'),
    path('view_one_quotation/', views.view_one_quotation, name='view_one_quotation'),
    path('view_one_PR/', views.view_one_PR, name='view_one_PR'),
]
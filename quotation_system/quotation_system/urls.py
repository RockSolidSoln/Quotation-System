"""
Definition of urls for django_project1.
"""

from datetime import datetime
from django.urls import re_path as url 
import django.contrib.auth.views

import project.forms
import project.views

import addItem.views

# Uncomment the next lines to enable the admin:
from django.urls import include, path
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', project.views.home, name='home'),
    url(r'^contact$', project.views.contact, name='contact'),
    url(r'^about$', project.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.LoginView.as_view(),
        {
            'template_name': 'project/login.html',
            'authentication_form': project.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.LogoutView.as_view(),
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),

    url(r'^menu$', project.views.menu, name='menu'),

    ## module 1 urls
    url(r'^additemform$', addItem.views.additemform, name="additem_form"),
    url(r'^additemconfirmation', addItem.views.additemconfirmation, name="confirm_additem"),
]

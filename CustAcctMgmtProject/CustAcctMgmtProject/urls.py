"""
URL configuration for CustAcctMgmtProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from CustAcctMgmtApp import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.details, name='home'),
    path('', RedirectView.as_view(url='/home')),
    path('createCustomer', views.CreateCustomerView.as_view(), name='create'),
    path('editCustomer/<int:id>/', views.EditCustomerView.as_view(), name='edit'),
    path('add_account/<int:fk>/', views.AddAccountView.as_view(), name='add_account'),
    path('edit_account/<int:id>/', views.EditAccountView.as_view(), name='edit_account'),
    path('addTransaction/<int:fk>/', views.AddTransaction, name='add_trans'),
    # Assignment 5
    path('view_home_list/', views.CustomerListView.as_view(), name='view_home_list'),
    path('listCustomerJSON/', views.CustomerListCreate.as_view(), name='list_customer_json'),
    path('listAccountJSON/<int:id>', views.AccountListCreate.as_view(), name='list_account_json'),
    path('updateCustomerJSON/<int:id>', views.CustomerUpdateView.as_view(), name='update_customer_json'),
    path('updateAccountJSON/<int:id>', views.AccountUpdateView.as_view(), name='update_account_json'),
    path('listTransactionJSON/<int:id>', views.TransactionListCreateViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='list_transaction_json'),
]

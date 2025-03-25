from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer, Account, Transaction
from django.core.exceptions import ValidationError
from .Serializers import CustomerSerializer, AccountSerializer, TransactionSerializer

from datetime import date
from django.http import HttpRequest
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .customerForms import TransactionForm, TransactionModelForm, AccountModelForm, CustomerModelForm
from django.contrib import messages
# Create your views here.

def details(request):
    # We will retrieve all customers, accounts, and transactions from the underlying database and display them
    customers = Customer.objects.all()
    accounts = Account.objects.all()
    transactions = Transaction.objects.all()

    paginator = Paginator(accounts, 5)  # Show 2 addresses per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html',
                  {'page_obj': page_obj, 'customers': customers, 'accounts': accounts,
                   'transactions': transactions})


class CreateCustomerView(CreateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print(" id = " + str(kwargs.get("id")))

        if id > 0:
            # This is an Edit customer
            customer = Customer.objects.get(id=kwargs.get("id"))
        else:
            customer = Customer()

        form = CustomerModelForm(instance=customer)
        return render(request, 'create_customer.html', {'form': form})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print(" id = " + str(kwargs.get("id")))

        if id > 0:
            # this is an edit customer
            customer = Customer.objects.get(id=kwargs.get("id"))
        else:
            # this is a new customer
            customer = Customer()

        form = CustomerModelForm(request.POST, instance=customer);
        if form.is_valid():
            customer.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'create_customer.html', {'form': form})


class AddAccountView(CreateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print(" id = " + str(kwargs.get("id")))

        if id > 0:
            # This is a Edit
            account = Account.objects.get(id=kwargs.get("id"))
        else:
            account = Account()

        form = AccountModelForm(instance=account)
        return render(request, 'create_account.html', {'form': form})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print(" id = " + str(kwargs.get("id")))

        if id > 0:
            # this is an edit Account
            account = Account.objects.get(id=kwargs.get("id"))
        else:
            # this is a new Account
            account = Account()

        form = AccountModelForm(request.POST, instance=account)
        if form.is_valid():
            customer = Customer.objects.get(id=kwargs.get("fk"))
            account.customer = customer
            account.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'create_account.html', {'form': form})

def AddTransaction(request, fk):
    transactions = Transaction.objects.all()
    paginator = Paginator(transactions, 4)  # Show 2 addresses per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = TransactionForm(request.POST, {'page_obj': page_obj, 'transactions': transactions})
        if form.is_valid():
            account = Account.objects.get(id=fk)
            cd = form.cleaned_data
            # further subject cd to data validation
            transaction = Transaction(transaction_type=cd['transactionType'], transaction_amount=cd['transactionAmount'],
                                      initiated_date=cd['initiatedDate'], posted_date=cd['postedDate'],
                                      status=cd['status'])
            if transaction.transaction_type == 'C':
                account.balance += transaction.transaction_amount
            else:
                account.balance -= transaction.transaction_amount

            print('Account Balance', account.balance)

            if account.balance >= 0:
                form.cleaned_data
                # This sets up the link between Account and transaction
                transaction.account = account
                transaction.save()
                account.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request, 'Account Balance cannot be less than zero.')
                #print(form.errors)
                # raise ValidationError("Account Balance cannot be less than zero.")
                return render(request, 'create_transaction.html', {'page_obj': page_obj,
                                                                   'transactions': transactions, 'form': form})
        else:
            return render(request, 'create_transaction.html', {'page_obj': page_obj,
                                                               'transactions': transactions, 'form': form})
    else:
        form = TransactionForm()
        return render(request, 'create_transaction.html', {'page_obj': page_obj,
                                                           'transactions': transactions, 'form': form})


class EditCustomerView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print(" id = " + str(kwargs.get("id")))

        if id > 0:
            # This is an Edit customer
            customer = Customer.objects.get(id=kwargs.get("id"))
        else:
            customer = Customer()

        form = CustomerModelForm(instance=customer)
        return render(request, 'create_customer.html', {'form': form})

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = 0 if id is None else id
        print(" id = " + str(kwargs.get("id")))

        if id > 0:
            # this is an edit customer
            customer = Customer.objects.get(id=kwargs.get("id"))
        else:
            # this is a new customer
            customer = Customer()

        form = CustomerModelForm(request.POST, instance=customer);
        if form.is_valid():
            customer.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'create_customer.html', {'form': form})


class EditAccountView(View):
    def validate(self):
        # implement contact validation code
        print("Validate method called")

    def get(self, request, *args, **kwargs):
        print(" id = " + str (kwargs.get("id")))

        account = Account.objects.get(id=kwargs.get("id"))

        form = AccountModelForm(instance=account)
        return render(request, 'create_account.html', {'form': form})

    def post(self, request, *args, **kwargs):
        print(" id = " + str (kwargs.get("id")))

        account = Account.objects.get(id=kwargs.get("id"))

        form = AccountModelForm(request.POST, instance=account)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'create_account.html', {'form': form})

################
# Assignment 5 #
################

class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'home_listview.html'
    def get_queryset(self):
        return Customer.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CustomerListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        accounts = Account.objects.all()

        #add pagination to the contact list.
        paginator = Paginator(accounts, 3)  # Show 5 contacts per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj

        return context


class CustomerListCreate(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.create(serializer.validated_data)
            return Response({"Success": "Customer '{}' created successfully".format(CustomerSerializer(customer).data)})


class AccountListCreate(ListCreateAPIView):
    serializer_class = AccountSerializer
    # queryset = Account.objects.all().filter(customer_id=id)

    def list(self, request, *args, **kwargs):
        cus = self.kwargs.get('id')
        self.queryset = Account.objects.all().filter(customer_id=cus)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.create(serializer.validated_data)
            return Response({"Success": "Account '{}' created successfully".format(AccountSerializer(account).data)})


class CustomerUpdateView(APIView):
    def get(self, request, id):
        customers = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)

    def put(self, request, id):
        customer_data = request.data
        customer = get_object_or_404(Customer.objects.all(), pk=customer_data.get('id'))
        serializer = CustomerSerializer(instance=customer, data=customer_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            customer_saved = serializer.save()
        return Response({"Success": "Customer '{}' updated successfully".format(CustomerSerializer(customer).data)})


class AccountUpdateView(APIView):
    def get(self, request, id):
        accounts = Account.objects.get(id=id)
        serializer = AccountSerializer(accounts)
        return Response(serializer.data)

    def put(self, request, id):
        account_data = request.data
        account = get_object_or_404(Account.objects.all(), pk=account_data.get('id'))
        serializer = AccountSerializer(instance=account, data=account_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            account_saved = serializer.save()
        return Response({"Success": "Account '{}' updated successfully".format(AccountSerializer(account).data)})


class TransactionListCreateViewSet(viewsets.ViewSet):
    serializer_class = TransactionSerializer

    def list(self, request, id):
        queryset = Transaction.objects.all().filter(account_id=id)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, id):
        serializer = TransactionSerializer(data=request.data)
        act = id
        account = Account.objects.get(id=act)
        transactions = request.POST

        tran_type = transactions.get("transaction_type")
        if tran_type.upper() == "C".upper():
            account.balance += float(transactions.get("transaction_amount"))
        else:
            account.balance -= float(transactions.get("transaction_amount"))
        account.save()

        if serializer.is_valid(raise_exception=True):
            transaction = serializer.create(serializer.validated_data)
            return Response({"Success": "Transaction '{}' created successfully".format(TransactionSerializer(transaction).data)})

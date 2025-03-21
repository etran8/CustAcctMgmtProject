import readonly
from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxInput, HiddenInput
from django.urls import resolve
from .models import Customer, Account, Transaction
from .validators import validate_balance, validate_amount


class CustomerForm(forms.Form):
    # id = forms.IntegerField(widget=forms.HiddenInput)
    PREFERRED_CUSTOMER = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    STATE_CHOICES = [
        ('SC', 'South Carolina'),
        ('NC', 'North Carolina'),
        ('GA', 'Georgia'),
        ('VA', 'Virginia'),
        ('MD', 'Maryland'),
        ('PA', 'Pennsylvania'),
        ('NJ', 'New Jersey'),
        ('DE', 'Delaware'),
        ('NY', 'New York'),
        ('CT', 'Connecticut')
    ]

    current_url = ""
    firstName = forms.CharField(max_length=25, label='Enter First Name', required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'What is your Name'}))
    lastName = forms.CharField(max_length=25, label='Enter Last Name', required=True)
    ssn = forms.CharField(max_length=11, required=True, label='Enter SSN')
    preferredCustomer = forms.ChoiceField(label='Select Customer Status', required=True, choices=PREFERRED_CUSTOMER)
    customerSince = forms.DateField(label='Enter Customer Since', required=True, widget=forms.DateInput)
    street = forms.CharField(required=True, label='Enter Street name')
    city = forms.CharField(required=True, label='Enter City')
    state = forms.ChoiceField(required=True, label='Enter State', choices=STATE_CHOICES)
    zip = forms.CharField(required=True, label='Enter Zipcode')

    def clean_premium_customer(self):
        print("Clean Preferred Customer method called")
        preferredCustomer = self.cleaned_data["preferredCustomer"]
        print("Preferred Customer = " + preferredCustomer)
        # very important to return the data access from the cleaned_data dict
        return preferredCustomer


class AccountForm(forms.Form):
    PAPER_STATEMENT = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    ACCOUNT_CHOICES = [
        ('C', 'Checking'),
        ('S', 'Saving'),
        ('I', 'Investment')
    ]

    accountNumber = forms.IntegerField(required=True, label='Enter Account Number')
    accountType = forms.ChoiceField(required=True, label='Enter Account Type', choices=ACCOUNT_CHOICES)
    PaperStatement = forms.ChoiceField(label='Select Paper test Statement', required=True, choices=PAPER_STATEMENT)
    password = forms.CharField(required=True, label='Enter test Password', widget=forms.PasswordInput())
    balance = forms.FloatField(required=True, label='Enter Account Balance', initial=1000.00, disabled=True,
                               validators=[validate_balance])
    agreement = forms.CharField(required=True, label='Enter Account Agreement')
    widgets = {
        'agreement': forms.Textarea(attrs={'rows': 4, 'cols': 25}),
        'password': forms.PasswordInput(),
        }


class TransactionForm(forms.Form):
    TRANSACTION_CHOICES = [
        ('D', 'Debit'),
        ('C', 'Credit'),
    ]

    STATUS_CHOICES = [
        ('C', 'Completed'),
        ('P', 'Pending'),
    ]

    transactionType = forms.ChoiceField(required=True, label='Select Transaction Type', choices=TRANSACTION_CHOICES)
    transactionAmount = forms.FloatField(required=True, label='Enter Transaction Amount', validators=[validate_amount])
    initiatedDate = forms.DateField(label='Enter Initiated Date', required=True, widget=forms.DateInput)
    postedDate = forms.DateField(label='Enter Posted Date', required=True, widget=forms.DateInput)
    status = forms.ChoiceField(required=True, label='Select Status', choices=STATUS_CHOICES)
    balance = forms.FloatField(required=False, widget=HiddenInput(), validators=[validate_balance])

    widgets = {
        "transactionAmount": forms.FloatField(required=True, validators=[validate_amount]),
        "balance": forms.FloatField(required=False, validators=[validate_balance]),
        "balance": forms.Field.hidden_widget()
    }

class AccountModelForm(forms.ModelForm):
    class Meta:
        ACCOUNT_CHOICES = [
            ('C', 'Checking'),
            ('S', 'Saving'),
            ('I', 'Investment')
        ]
        PAPER_STATEMENT = [
            ('Y', 'Yes'),
            ('N', 'No')
        ]
        model = Account
        model.balance = 1000.00
        exclude = ("customer",)
        labels = {
            "paper_statement": "Paper Statement",
            "account_number": "Account Number",
            "account_type": "Account Type",
            "password": "Password",
            "balance": "Account Balance",
            "agreement": "Account Agreement",
        }

        widgets = {
            "account_type": forms.Select(choices=ACCOUNT_CHOICES),
            'agreement': forms.Textarea(attrs={'rows': 4, 'cols': 25}),
            'paper_statement': CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'password': forms.PasswordInput(render_value=True),
            'balance': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'balance': forms.FloatField(validators=[validate_balance])
        }

class TransactionModelForm(forms.ModelForm):
    class Meta:
        TRANSACTION_CHOICES = [
            ('D', 'Debit'),
            ('C', 'Credit'),
        ]

        STATUS_CHOICES = [
            ('C', 'Completed'),
            ('P', 'Pending'),
        ]

        model = Transaction
        exclude = ("account",)
        labels = {
            "transaction_type": "Transaction Type",
            "transaction_amount": "Transaction Amount",
            "initiated_date": "Transaction Initiated Date",
            "posted_date": "Transaction Posted Date",
            "status": "Account Status",
        }
        widgets = {
            "transaction_type": forms.Select(choices=TRANSACTION_CHOICES),
            "status": forms.Select(choices=STATUS_CHOICES),
        }


class CustomerModelForm(forms.ModelForm):
    class Meta:
        PREFERRED_CUSTOMER = [
            ('Y', 'Yes'),
            ('N', 'No')
        ]
        STATE_CHOICES = [
            ('SC', 'South Carolina'),
            ('NC', 'North Carolina'),
            ('GA', 'Georgia'),
            ('VA', 'Virginia'),
            ('MD', 'Maryland'),
            ('PA', 'Pennsylvania'),
            ('NJ', 'New Jersey'),
            ('DE', 'Delaware'),
            ('NY', 'New York'),
            ('CT', 'Connecticut')
        ]

        model = Customer
        exclude = {}
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "ssn": "Social Security Number",
            "customer_since": "Customer Since",
            "preferred_customer": "Preferred Customer",
            "street": "Street",
            "city": "City",
            "state": "State",
            "zip": "Zip Code"
        }
        widgets = {
            "preferred_customer": forms.Select(choices=PREFERRED_CUSTOMER),
            "state": forms.Select(choices=STATE_CHOICES),
            "customer_since": forms.DateInput()
        }


from datetime import date

from django.test import TestCase
from .models import Customer, Account, Transaction

# Account Types: Expenses, Asset, Bank, Equity, Income, Liability, Saving, Cash
# transaction types: purchases, sales, payments, and receipts


# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        joe = Customer.objects.create(first_name='Joe', last_name='Smith', ssn='111-11-1111',
                                      customer_since=date.today(), preferred_customer='Y', street='123 Main Street',
                                      city='Falls Church', state='Virginia', zip='22043')
        acct = Account.objects.create(account_number=111, account_type='E', balance=111.11,
                                      agreement='Agreement Notes', customer=joe)
        Transaction.objects.create(transaction_type='S', transaction_amount=222.22, initiated_date=date.today(),
                                   posted_date=date.today(), status='C', account=acct)

    # Test Model Creation
    def test_create_customer(self):
        print("Customer Creating")
        Customer.objects.create(first_name='Jane', last_name='Johnson', ssn='222-22-2222', customer_since=date.today(),
                                preferred_customer='N',street='222 Second Street', city='Arlington', state='Virginia',
                                zip='22043')
        print("Customer Created")
        print("============================================")

    def test_create_account(self):
        print("Account Creating")
        joe = Customer.objects.get(first_name="Joe")
        Account.objects.create(account_number=222, account_type='A', balance=333.33,
                               agreement='Agreement Description', customer=joe)
        print("Account Created")
        print("============================================")

    def test_create_transaction(self):
        print("Transaction Creating")
        acct = Account.objects.get(account_number=111)
        Transaction.objects.create(transaction_type='P', transaction_amount=444.44, initiated_date=date.today(),
                                   posted_date=date.today(), account=acct)
        print("Transaction Created")
        print("============================================")

    # Test Model Read
    def test_customer_exists(self):
        print('Retrieving existing Customer')
        joe = Customer.objects.get(first_name="Joe")
        print(" Customer First Name = ", joe.first_name)
        print(" Customer Last Name = ", joe.last_name)
        print(" Customer SSN = ", joe.ssn)
        print(" Customer Customer Since = ", joe.customer_since)
        print(" Customer Preferred Customer = ", joe.preferred_customer)
        print(" Customer Street = ", joe.street)
        print(" Customer City = ", joe.city)
        print(" Customer State = ", joe.state)
        print(" Customer Zip = ", joe.zip)
        self.assertEqual(joe.first_name, 'Joe')
        self.assertEqual(joe.last_name, 'Smith')
        print("============================================")

    def test_retrieve_existing_customer(self):
        print('Retrieving existing Customer')
        joe = Customer.objects.get(first_name="Joe")
        print("Existing Customer retrieved ", joe)
        print("============================================")

    def test_account_exists(self):
        print('Retrieving existing Account')
        account = Account.objects.get(account_number=111)
        print(" Account Account Number = ", account.account_number)
        print(" Account Account Type = ", account.account_type)
        print(" Account Balance = ", account.balance)
        print(" Account Agreement = ", account.agreement)
        print("============================================")

    def test_retrieve_existing_account(self):
        print('Retrieving existing Account')
        account = Account.objects.get(account_number=111)
        print("Existing Account retrieved ", account)
        print("============================================")

    def test_transaction_exists(self):
        print('Retrieving existing Transaction')
        transaction = Transaction.objects.get(transaction_type='S')
        print(" Transaction Type = ", transaction.transaction_type)
        print(" Transaction Amount = ", transaction.transaction_amount)
        print(" Transaction Initiated Date = ", transaction.initiated_date)
        print(" Transaction Posted Date = ", transaction.posted_date)
        print("============================================")

    def test_retrieve_existing_transaction(self):
        print('Retrieving existing Transaction')
        transaction = Transaction.objects.get(transaction_type='S')
        print("Existing Transaction retrieved ", transaction)
        print("============================================")

    # Test Model Update
    def test_customer_update(self):
        print('Updating SSN in Customer')
        joe = Customer.objects.get(first_name="Joe")
        print(" Customer First Name = ", joe.first_name)
        print(" Customer Last Name = ", joe.last_name)
        print(" Customer SSN = ", joe.ssn)
        print(" Customer Since = ", joe.customer_since)
        joe.ssn = '111-11-1212'
        joe.save()
        print('Updated Cell Phone in Customer')
        print(" Customer First Name = ", joe.first_name)
        print(" Customer Last Name = ", joe.last_name)
        print(" Customer SSN = ", joe.ssn)
        print(" Customer Since = ", joe.customer_since)
        print("============================================")

    def test_account_update(self):
        print('Updating Balance in Account')
        account = Account.objects.get(account_number=111)
        print(" Account Account Number = ", account.account_number)
        print(" Account Account Type = ", account.account_type)
        print(" Account Balance = ", account.balance)
        print(" Account Agreement = ", account.agreement)
        account.balance = 222.22
        account.save()
        print('Updated Balance in Account')
        print(" Account Account Number = ", account.account_number)
        print(" Account Account Type = ", account.account_type)
        print(" Account Balance = ", account.balance)
        print(" Account Agreement = ", account.agreement)
        print("============================================")

    def test_transaction_update(self):
        print('Updating Quantity in transaction')
        transaction = Transaction.objects.get(transaction_type='S')
        print(" Transaction Type = ", transaction.transaction_type)
        print(" Transaction Amount = ", transaction.transaction_amount)
        print(" Transaction Initiated Date = ", transaction.initiated_date)
        print(" Transaction Posted Date = ", transaction.posted_date)
        transaction.transaction_type = 'P'
        transaction.save()
        print('Updated Quantity in Transaction')
        print(" Transaction Type = ", transaction.transaction_type)
        print(" Transaction Amount = ", transaction.transaction_amount)
        print(" Transaction Initiated Date = ", transaction.initiated_date)
        print(" Transaction Posted Date = ", transaction.posted_date)
        print("============================================")

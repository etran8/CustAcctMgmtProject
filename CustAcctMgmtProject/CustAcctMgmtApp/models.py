from django.core.validators import MinValueValidator
from django.db import models
from datetime import date

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=25, default='', null=False)
    last_name = models.CharField(max_length=25, default='', null=False)
    ssn = models.CharField(max_length=11, default='111-11-1111', null=False)
    customer_since = models.DateField(default=date.today(), null=False)
    preferred_customer = models.CharField(max_length=1, null=False)
    street = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=20, null=False)
    zip = models.CharField(max_length=11, null=False)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class Account(models.Model):
    account_number = models.IntegerField(null=False)
    account_type = models.CharField(max_length=1, null=False)
    paper_statement = models.BooleanField(default=False, null=False)
    password = models.CharField(max_length=25, default='', null=False)
    balance = models.FloatField(default=1000.00,  null=False, validators=[MinValueValidator(0)])
    agreement = models.CharField(max_length=100, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        ordering = ['account_number']

    def __str__(self):
        return str(self.account_number)


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=1, null=False)
    # transaction_amount = models.FloatField(default=0, null=False)
    transaction_amount = models.FloatField(default=0, null=False, validators=[MinValueValidator(0)])
    initiated_date = models.DateField(default=date.today(), null=False)
    posted_date = models.DateField(default=date.today(), null=False)
    status = models.CharField(max_length=1, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')

    class Meta:
        ordering = ['account_id']

    def __str__(self):
        return str(self.account_id)


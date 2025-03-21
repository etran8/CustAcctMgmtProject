from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Customer, Account, Transaction

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transaction)

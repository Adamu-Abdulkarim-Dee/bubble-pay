from django.contrib import admin
from .models import Wallet, Account, Transaction

admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)

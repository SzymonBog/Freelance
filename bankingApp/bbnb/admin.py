from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Deposit)
admin.site.register(Account)
admin.site.register(SavedAccounts)
admin.site.register(Transfer)
admin.site.register(Loan)

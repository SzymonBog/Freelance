from django.db import models
from bbnb.models import Account
from django.apps import apps
# Create your models here.


class StocksAccount(models.Model):
    i = models.IntegerField()
    connectedBankingAccount = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='banking_account')


class StocksCompany(models.Model):
    companyName = models.CharField(max_length=50)
    date = models.DateField()
    sharePrice = models.FloatField()

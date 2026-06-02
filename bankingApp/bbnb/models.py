from django.db import models

# Create your models here.


class Deposit(models.Model):
    money = models.FloatField()
    percent = models.FloatField()
    startDate = models.DateField()
    endDate = models.DateField()
    duration = models.IntegerField()  # months
    account = models.ForeignKey('Account', on_delete=models.CASCADE, null=True)


class Account(models.Model):
    accountNumber = models.CharField(max_length=39)  # 32
    savingsAccountNumber = models.CharField(max_length=39)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    userId = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    balance = models.FloatField()
    loggedIn = models.IntegerField(default=0)

    def get_user_id(self):
        return self.userId

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNumber

    """
    def get_deposits(self):
        return Deposit.objects.filter(account=self)
    """


class SavedAccounts(models.Model):
    yourAccount = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='owner_account')
    savedAccount = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='saved_account')

    def get_your_account(self):
        return self.yourAccount

    def get_saved_account(self):
        return self.savedAccount


class Transfer(models.Model):
    fromAccount = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='from_account')
    toAccount = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='to_account')
    amount = models.FloatField()
    description = models.CharField(max_length=1000)
    deposit = models.IntegerField(default=0)  # if from deposit(1) if to deposit(2) if not (0)


class Loan(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='account')
    amount = models.FloatField()
    percent = models.FloatField()
    duration = models.IntegerField()
    installment = models.FloatField()  # rata
    startDate = models.DateField()
    endDate = models.DateField()
    """
    If not paid in time:
    - Interest rate increases(1%)
    - Fixed penalty amounts
    
    If paid in time:
    - no penalty, no benefits
    
    If overpaid in time:
    - lower payments needed
    """

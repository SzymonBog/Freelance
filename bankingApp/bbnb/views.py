from django.shortcuts import render, redirect
from .models import *
from random import randint
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse
from django.template import loader
# from flask import Flask, render_template


# Create your views here.
# https://www.youtube.com/watch?v=1Ve3KB2Jxgg


# app = Flask(__name__)


# @app.route('/')
"""
def main_page(request):
    template = loader.get_template("main_page.html")
    return HttpResponse(template.render())
"""


def create_account_number():
    s = ""
    for i in range(39):
        if i != 4 and i != 9 and i != 14 and i != 19 and i != 24 and i != 29 and i != 34:
            s = s + str(randint(0, 9))
        else:
            s = s + " "

    return s


def main_page(request):
    # sign in variables
    signin_result = None
    inserted_id = None
    inserted_password = None

    # sign up variables
    signup_result = None
    name = None
    surname = None
    email = None
    user_id = None
    password = None
    balance = None

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')

        # get credentials
        inserted_id = str(request.POST.get('id'))
        inserted_password = str(request.POST.get('password'))

        if operation == 'sign in':
            accounts = Account.objects.all()

            if accounts.count() > 0:

                for a in accounts:
                    if inserted_id == a.userId:
                        if inserted_password == a.password:
                            a.loggedIn = 1
                            a.save()
                            return redirect(f'http://127.0.0.1:8000/bbnb/account/{a.userId}/accounts')
                        else:
                            return render(request, 'main_page.html', {
                                'signin_result': 'Incorrect ID and/or password'
                            })

            return render(request, 'main_page.html', {
                'signin_result': 'Incorrect ID and/or password'
            })

        # get info
        name = str(request.POST.get('name'))
        surname = str(request.POST.get('surname'))
        email = str(request.POST.get('email'))
        user_id = str(request.POST.get('userId'))
        password = str(request.POST.get('accountPassword'))
        balance = float(request.POST.get('balance'))

        if operation == 'sign up':
            accounts = Account.objects.all()

            if accounts.count() == 0:

                account = Account.objects.create(
                    accountNumber=create_account_number(),
                    savingsAccountNumber=create_account_number(),
                    name=name,
                    surname=surname,
                    email=email,
                    userId=user_id,
                    password=password,
                    balance=balance
                )
                return render(request, 'main_page.html', {
                    'signup_result': 'Account created successfully'
                })

            else:
                # print(password, user_id)
                if Account.objects.filter(userId=user_id).exists():
                    error = "Could not create account\n(this user id is already\nused by other account)"
                    return render(request, 'main_page.html', {
                        'signup_result': error
                    })
                else:
                    ok = False
                    while not ok:
                        number = create_account_number()

                        if not Account.objects.filter(accountNumber=number).exists():
                            ok = True

                    ok = False
                    while not ok:
                        savings_number = create_account_number()

                        if not Account.objects.filter(savingsAccountNumber=savings_number).exists():
                            ok = True

                    account = Account.objects.create(
                        accountNumber=number,
                        savingsAccountNumber=savings_number,
                        name=name,
                        surname=surname,
                        email=email,
                        userId=user_id,
                        password=password,
                        balance=balance
                    )
                    return render(request, 'main_page.html', {
                        'signup_result': 'Account created successfully'
                    })

    return render(request, 'main_page.html')


def user_account(request, user_id):
    account = Account.objects.get(userId=user_id)
    name = account.get_name()
    balance = account.get_balance()
    deposit = 0

    user_deposits = Deposit.objects.filter(account=account)

    for i in user_deposits:
        deposit = deposit + i.money

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

    return render(request, 'user_account.html', {
        'name': name,
        'balance': balance,
        'deposit': deposit,
        'user_id': user_id
    })


def money_transfer_make_transfer(request, user_id):
    account = Account.objects.get(userId=user_id)
    name = account.get_name()
    balance = account.get_balance()
    number = account.get_account_number()
    deposit = 0

    all_saved_accounts = SavedAccounts.objects.all()
    saved_accounts = []
    account_numbers = []
    saved_account_numbers = []
    saved_account_names = []
    saved_account_surnames = []

    for i in range(len(all_saved_accounts)):
        if number == all_saved_accounts[i].yourAccount.get_account_number():
            # saved_accounts.append(all_saved_accounts[i])
            account_numbers.append(all_saved_accounts[i].savedAccount)

    for i in account_numbers:
        a = Account.objects.get(accountNumber=i.get_account_number())

        if not saved_account_numbers.__contains__(a.get_account_number()):
            saved_account_names.append(a.get_name())
            saved_account_surnames.append(a.get_surname())
            saved_account_numbers.append(a.get_account_number())

    saved_accounts = zip(saved_account_names, saved_account_surnames, saved_account_numbers)
    # print(saved_account_numbers[0].get_account_number())
    # print(saved_account_numbers[0].get_account_number(), saved_account_numbers[1].get_account_number())

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')
        transfer = request.POST.get('transfer')
        page = request.POST.get('page')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if transfer == "send":
            from_account = str(number)  # for now
            to_account = str(request.POST.get('saved_accounts'))
            amount = float(request.POST.get('amount'))
            description = str(request.POST.get('description'))

            if amount <= account.get_balance():

                recipient = Account.objects.get(accountNumber=to_account)

                Transfer.objects.create(
                    fromAccount=account,
                    toAccount=recipient,
                    amount=amount,
                    description=description
                )

                account.balance = account.get_balance() - amount
                recipient.balance = recipient.get_balance() + amount

                account.save()
                recipient.save()

                return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

            else:
                # for now send everything
                recipient = Account.objects.get(accountNumber=to_account)

                Transfer.objects.create(
                    fromAccount=account,  # for now
                    toAccount=recipient,
                    amount=account.get_balance(),
                    description=description
                )

                account.balance = 0
                recipient.balance = recipient.get_balance() + account.get_balance()

                account.save()
                recipient.save()

                return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if transfer == "cancel":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if page == "transfer_activity":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if page == "make_transfer":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/make_transfer')

        if page == "add_accounts_recipients":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/add_recipient')

    return render(request, 'money_transfer_make_transfer.html', {
        'name': name,
        'balance': balance,
        'deposit': deposit,
        'saved_accounts': saved_accounts,
        'user_id': user_id,
        'account': number
    })


def money_transfer_transfer_activity(request, user_id):
    account = Account.objects.get(userId=user_id)
    name = account.get_name()
    balance = account.get_balance()
    number = account.get_account_number()
    deposit = 0

    all_transfers = Transfer.objects.all()
    recipient_name = []
    recipient_surname = []
    sender_name = []
    sender_surname = []
    from_account = []
    to_account = []
    transferred_amount = []
    description = []
    received = []

    for i in range(len(all_transfers)):
        if number == all_transfers[i].fromAccount.get_account_number() or number == all_transfers[i].toAccount.get_account_number():
            # saved_accounts.append(all_saved_accounts[i])

            if all_transfers[i].deposit == 0:
                if number == all_transfers[i].toAccount.get_account_number():
                    received.append(True)
                else:
                    received.append(False)
            else:
                if all_transfers[i].deposit == 1:
                    received.append(True)
                else:
                    received.append(False)

            if all_transfers[i].deposit != 0:
                if received[i]:
                    from_account.append(account.savingsAccountNumber)
                    to_account.append(account.get_account_number())
                    recipient_name.append(all_transfers[i].fromAccount.get_name())
                    recipient_surname.append(all_transfers[i].fromAccount.get_surname())
                    sender_name.append("Simple Savings - 8183")
                    sender_surname.append("")
                else:
                    from_account.append(account.get_account_number())
                    to_account.append(account.savingsAccountNumber)
                    recipient_name.append("Simple Savings - 8183")
                    recipient_surname.append("")
                    sender_name.append(all_transfers[i].fromAccount.get_name())
                    sender_surname.append(all_transfers[i].fromAccount.get_surname())
            else:
                from_account.append(all_transfers[i].fromAccount.get_account_number())
                to_account.append(all_transfers[i].toAccount.get_account_number())
                recipient_name.append(all_transfers[i].toAccount.get_name())
                recipient_surname.append(all_transfers[i].toAccount.get_surname())
                sender_name.append(all_transfers[i].fromAccount.get_name())
                sender_surname.append(all_transfers[i].fromAccount.get_surname())

            transferred_amount.append(all_transfers[i].amount)
            description.append(all_transfers[i].description)

    # print(saved_account_numbers[0].get_account_number())
    # print(transferred_amount[0], recipient_name[0], recipient_surname[0])
    # print(transfers)

    if len(from_account) > 50:
        dif = len(from_account) - 50
        from_account = from_account[dif:]
        to_account = to_account[dif:]
        transferred_amount = transferred_amount[dif:]
        description = description[dif:]
        recipient_name = recipient_name[dif:]
        recipient_surname = recipient_surname[dif:]
        sender_name = sender_name[dif:]
        sender_surname = sender_surname[dif:]
        received = received[dif:]

    from_account.reverse()
    to_account.reverse()
    transferred_amount.reverse()
    description.reverse()
    recipient_name.reverse()
    recipient_surname.reverse()
    received.reverse()
    sender_name.reverse()
    sender_surname.reverse()

    transfers = zip(recipient_name, recipient_surname, from_account, to_account, received, transferred_amount, description, sender_name, sender_surname)

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')
        page = request.POST.get('page')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if page == "transfer_activity":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if page == "make_transfer":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/make_transfer')

        if page == "add_accounts_recipients":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/add_recipient')

    return render(request, 'money_transfer_transfer_activity.html', {
        'name': name,
        'balance': balance,
        'deposit': deposit,
        'transfers': transfers,
        'user_id': user_id,
        'account': number
    })


def money_transfer_add_recipient(request, user_id):
    account = Account.objects.get(userId=user_id)
    account_number = None
    result = None
    saved_account = None
    # name = None
    # surname = None

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')
        page = request.POST.get('page')
        add = request.POST.get('add')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if page == "transfer_activity":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if page == "make_transfer":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/make_transfer')

        if page == "add_accounts_recipients":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/add_recipient')

        if add == "canceled":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/add_recipient')

        if add == "approved":
            account_number = request.POST.get('account_number')

            if len(str(account_number)) != 39 or str(account_number[4]) != " " or str(account_number[9]) != " " \
                    or str(account_number[14]) != " " or str(account_number[19]) != " " or str(account_number[24]) != \
                    " " or str(account_number[29]) != " " or str(account_number[34]) != " ":
                result = 'Incorrect account number or account number format()'
            else:
                if Account.objects.filter(accountNumber=account_number).exists():

                    saved_account = Account.objects.get(accountNumber=account_number)

                    if not SavedAccounts.objects.filter(yourAccount=account, savedAccount=saved_account).exists():

                        if saved_account != account:
                            SavedAccounts.objects.create(
                                yourAccount=account,
                                savedAccount=saved_account
                            )

                            result = 'Added new recipient'

                        else:
                            result = 'Cannot add your own account'

                    else:
                        result = 'Cannot add recipient. Recipient already exists'

    return render(request, 'money_transfer_add_recipient.html', {
        'result': result
    })


def investments(request, user_id):  # add starting up a deposit and transferring money(add savings account)
    account = Account.objects.get(userId=user_id)
    name = account.get_name()
    balance = account.get_balance()

    money_d = None
    percent_d = None
    start_date_d = None
    end_date_d = None
    duration_d = None

    all_deposits = Deposit.objects.all()
    start = []
    end = []
    duration = []
    amount = []
    percent = []

    start_delete = []
    end_delete = []
    duration_delete = []
    amount_delete = []
    percent_delete = []

    deposit_offers = []
    deposit45 = [4.5, 1, f"http://127.0.0.1:8000/bbnb/account/{user_id}/investments/deposit/{1}/{45}"]  # percent, months, link
    deposit55 = [5.5, 3, f"http://127.0.0.1:8000/bbnb/account/{user_id}/investments/deposit/{3}/{55}"]  # percent, months, link

    deposit_offers.append(deposit45)
    deposit_offers.append(deposit55)

    for i in all_deposits:
        if i.account == account:

            current_date = datetime.now().date()
            end_date = i.endDate

            if current_date >= end_date:
                start_delete.append(i.startDate)
                end_delete.append(i.endDate)
                duration_delete.append(i.duration)
                amount_delete.append(i.money)
                percent_delete.append(i.percent)

                Transfer.objects.create(
                    fromAccount=account,
                    toAccount=account,
                    amount=i.money * (1 + ((i.percent / 100) * (i.duration / 12))),  # (1 + (i.percent / 100)),
                    description="Deposit ended",
                    deposit=1
                )

                account.balance = account.balance + i.money * (1 + ((i.percent / 100) * (i.duration / 12)))
                account.save()

            else:
                start.append(i.startDate)
                end.append(i.endDate)
                duration.append(i.duration)
                amount.append(i.money)
                percent.append(i.percent)

    for j in range(len(amount_delete)):
        dp = Deposit.objects.filter(account=account, money=amount_delete[j], percent=percent_delete[j], startDate=start_delete[j], endDate=end_delete[j], duration=duration_delete[j]).first()
        dp.delete()

    deposits = zip(start, end, duration, amount, percent)

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')
        remove = request.POST.get('break')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if remove == "break":
            money_d = request.POST.get('amount')
            percent_d = request.POST.get('percent')

            start_date_d = request.POST.get('start')
            start_date_d = datetime.strptime(start_date_d, "%b. %d, %Y")
            start_date_d = start_date_d.strftime("%Y-%m-%d")

            end_date_d = request.POST.get('end')
            end_date_d = datetime.strptime(end_date_d, "%b. %d, %Y")
            end_date_d = end_date_d.strftime("%Y-%m-%d")

            duration_d = request.POST.get('duration')

            depo = Deposit.objects.filter(money=money_d, percent=percent_d, startDate=start_date_d, endDate=end_date_d, duration=duration_d, account=account).first()

            if depo:
                depo.delete()

                Transfer.objects.create(
                    fromAccount=account,
                    toAccount=account,
                    amount=i.money,  # change it later(not realistic)
                    description="Deposit withdrawn/broken",
                    deposit=1
                )

                account.balance = account.balance + i.money
                account.save()

            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

    return render(request, 'investments.html', {
        'user_id': user_id,
        'deposits': deposits,
        'deposit_offers': deposit_offers
    })


def investment_45(request, user_id):
    account = Account.objects.get(userId=user_id)

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')
        button = request.POST.get('button')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if button == "cancel":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if button == "send":
            amount = float(request.POST.get('money'))
            percent = 4.5
            duration = 1
            start_date = datetime.now().date()
            end_date = start_date + relativedelta(months=duration)

            if amount <= account.get_balance():
                Deposit.objects.create(
                    money=amount,
                    percent=percent,
                    startDate=start_date,
                    endDate=end_date,
                    duration=duration,
                    account=account
                )

                Transfer.objects.create(
                    fromAccount=account,
                    toAccount=account,
                    amount=amount,
                    description="Opened a deposit",
                    deposit=2
                )

                account.balance = account.balance - amount
                account.save()

            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

    return render(request, 'investments_deposit_45.html', {
        'user_id': user_id
    })  # delete


def investment_details(request, user_id, duration, percent):
    account = Account.objects.get(userId=user_id)

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')
        button = request.POST.get('button')

        if operation == "logout":
            account.loggedIn = 0
            account.save()
            return redirect(f'http://127.0.0.1:8000/bbnb/')

        if operation == "accounts":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/accounts')

        if operation == "transfers":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/transfers/transfer_activity')

        if operation == "investments":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if button == "cancel":
            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

        if button == "send":
            amount = float(request.POST.get('money'))
            percent = float(percent)
            percent = percent/10
            duration = int(duration)
            start_date = datetime.now().date()
            end_date = start_date + relativedelta(months=duration)

            if amount <= account.get_balance():
                Deposit.objects.create(
                    money=amount,
                    percent=percent,
                    startDate=start_date,
                    endDate=end_date,
                    duration=duration,
                    account=account
                )

                Transfer.objects.create(
                    fromAccount=account,
                    toAccount=account,
                    amount=amount,
                    description="Opened a deposit",
                    deposit=2
                )

                account.balance = account.balance - amount
                account.save()

            return redirect(f'http://127.0.0.1:8000/bbnb/account/{user_id}/investments')

    return render(request, 'investments_deposit.html', {
        'user_id': user_id,
        'percent': percent/10,
        'months': duration,
    })


def loans(request, user_id):
    account = Account.objects.get(userId=user_id)

    all_loans = Loan.objects.all()
    loans_taken = []
    start = []
    end = []
    duration = []
    amount = []
    percent = []

    for i in all_loans:

        if i.account == account:
            start.append(i.startDate)
            end.append(i.endDate)
            duration.append(i.duration)
            amount.append(i.amount)
            percent.append(i.percent)

    loans_taken = zip(start, end, duration, amount, percent)

    loan20_30000 = [20, 1, 30000, f"http://127.0.0.1:8000/bbnb/account/{user_id}/loans/loan/{1}/{20}"]
    loan_offers = [loan20_30000]

    return render(request, 'loans.html', {
        'user_id': user_id,
        'loans': loans_taken,
        'loan_offers': loan_offers
    })


def test_page(request, user_id):
    # initialize all results to None
    multiply_result = None
    add_result = None
    divide_result = None

    if request.method == 'POST':
        # check which operation was requested
        operation = request.POST.get('operation')  # get name

        # get numbers for operations
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))

        # handle each operation separately
        if operation == 'multiply':
            multiply_result = num1 * num2
        elif operation == 'add':
            add_result = num1 + num2
        elif operation == 'divide':
            if num2 != 0:
                divide_result = num1/num2
            else:
                return render(request, 'user_account.html', {
                    'divide_result': 'Error! Cannot divde by zero!'
                })

    # template = loader.get_template("main_page.html")
    # return HttpResponse(template.render())
    return render(request, 'user_account.html', {
        'multiply_result': multiply_result,
        'add_result': add_result,
        'divide_result': divide_result
    })


def v(request):
    template = loader.get_template("try.html")
    return HttpResponse(template.render())

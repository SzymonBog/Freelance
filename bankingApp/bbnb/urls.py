from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_page, name="main page"),
    path("account/<str:user_id>/accounts", views.user_account, name="account details"),
    path("account/<str:user_id>/transfers/make_transfer", views.money_transfer_make_transfer, name="make transfer"),
    path("account/<str:user_id>/transfers/transfer_activity", views.money_transfer_transfer_activity, name="transfer activity"),
    path("account/<str:user_id>/transfers/add_recipient", views.money_transfer_add_recipient, name="add recipient"),
    path("account/<str:user_id>/investments", views.investments, name="investments"),
    path("account/<str:user_id>/investments/deposit/<int:duration>/<int:percent>", views.investment_details, name="investment details"),
    path("account/<str:user_id>/loans", views.loans, name="loans"),
    # path("el/", views.v, name="index1"),
]

# http://127.0.0.1:8000/bbnb/

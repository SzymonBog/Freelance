from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="main page"),
    # path("el/", views.v, name="index1"),
]
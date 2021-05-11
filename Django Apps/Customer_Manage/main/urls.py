from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),

    # Dinamik url yaptık. cust_id views den geliyor.
    path("customer/<str:cust_id>", views.customer, name="customer"),
    path("product/", views.product, name="product"),
]

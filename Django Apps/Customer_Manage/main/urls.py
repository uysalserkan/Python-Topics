from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("customer/", views.customer),
    path("product/", views.product),
]

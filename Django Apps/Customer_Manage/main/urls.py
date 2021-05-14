from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    # Dinamik url yaptık. cust_id views den geliyor.
    path("customer/<str:cust_id>", views.customer, name="customer"),
    path("product/", views.product, name="product"),
    path("create-order/<str:customer_id>",
         views.createOrder, name="create-order"),
    path("update-order/<str:order_id>", views.updateOrder, name="update-order"),
    path("delete-order/<str:order_id>", views.deleteOrder, name="delete-order"),
    path("user/", views.userPage, name="user"),
]

from django.urls import path
from django.contrib.auth import views as auth_views
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
    path("settings/", views.accountSettings, name="user_settings"),

    # Reset Password sections..
    path(
        "reset_password",
        auth_views.PasswordResetView.as_view(
            # buraya custom html dosyaları gelebilir, eğer gelmezse default olarak eklenen sayfa gelecektir.
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent",
        auth_views.PasswordResetDoneView.as_view(
            # buraya custom html dosyaları gelebilir, eğer gelmezse default olarak eklenen sayfa gelecektir.
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            # buraya custom html dosyaları gelebilir, eğer gelmezse default olarak eklenen sayfa gelecektir.
        ),
        name="passowrd_reset_confirm",
    ),
    path(
        "complete",
        auth_views.PasswordResetCompleteView.as_view(
            # buraya custom html dosyaları gelebilir, eğer gelmezse default olarak eklenen sayfa gelecektir.
        ),
        name="password_reset_complete",
    ),
]

# ! settings.py dosyasındaki STMP configuration kısmını düzenleyip kullanabiliriz.

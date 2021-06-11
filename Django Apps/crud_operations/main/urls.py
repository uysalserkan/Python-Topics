from main.views import employee_form, employee_list
from django.urls import path
from .models import *

urlpatterns = [
    path('', employee_form),
    path('list/', employee_list),
    path('form/', employee_form),
]

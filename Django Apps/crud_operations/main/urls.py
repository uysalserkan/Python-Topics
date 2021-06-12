from main.views import employee_delete, employee_form, employee_list
from django.urls import path
from .models import *

urlpatterns = [
    path('', employee_form, name='home'),
    path('list/', employee_list, name='list'),
    path('form/', employee_form, name="form"),
    path('update/<int:id>', employee_form, name='update'),
    path('delete/<int:id>', employee_delete, name='delete'),
]

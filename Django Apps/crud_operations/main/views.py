from django.shortcuts import render, HttpResponse
from .forms import EmployeeForm

# Create your views here.


def employee_list(request):
    return render(
        request=request,
        template_name='src/emp_list.html',
        context={

        }
    )


def employee_form(request):
    form = EmployeeForm

    return render(
        request=request,
        template_name='src/emp_form.html',
        context={
            'form': form,
        }
    )


def employee_delete(request):
    pass

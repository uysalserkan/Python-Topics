from django.shortcuts import redirect, render, HttpResponse
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

    if request.method == 'GET':
        form = EmployeeForm

        return render(
            request=request,
            template_name='src/emp_form.html',
            context={
                'form': form,
            }
        )

    else:
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()

        return redirect('list/')


def employee_delete(request):
    pass

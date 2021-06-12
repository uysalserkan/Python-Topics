from django.shortcuts import redirect, render, HttpResponse
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def employee_list(request):
    return render(
        request=request,
        template_name='src/emp_list.html',
        context={
            'employees': Employee.objects.all(),
        }
    )


def employee_form(request, id=0):

    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)

        return render(
            request=request,
            template_name='src/emp_form.html',
            context={
                'form': form,
            }
        )

    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid:
            form.save()

        return redirect('/list/')


def employee_delete(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/list/')

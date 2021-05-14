from django.http import HttpResponse
from django.shortcuts import redirect


def unauth_user(view_funct):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_funct(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_groups=[]):
    def decorator(view_funct):
        def wrapper_func(request, *args, **kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_groups:
                return view_funct(request, * args, **kwargs)
            else:
                return HttpResponse("You are not allowed to show this page.\nPlease contact to admin..")

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None

        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "customer":
            return redirect('user')

        elif group == 'admin':
            return view_func(request, * args, **kwargs)

        else:
            return redirect('login')

    return wrapper_func

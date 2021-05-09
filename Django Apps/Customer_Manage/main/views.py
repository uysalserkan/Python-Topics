from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(
        request=request,
        template_name="src/dashboard.html"
    )


def customer(request):
    return render(
        request, "src/customer.html"
    )


def product(request):
    return render(
        request, "src/product.html"
    )

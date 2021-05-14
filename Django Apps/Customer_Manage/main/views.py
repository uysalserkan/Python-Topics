from django.db.models import fields
from main.models import Product
from main.models import Order
from main.models import Customer
from django.shortcuts import render
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from .models import Order
from .forms import OrderForm
from .filters import OrderFilter
# from django.http import HttpResponse

# Create your views here.


def homepage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='DELIVERED').count()
    pending = orders.filter(status='PENDING').count()

    return render(
        request=request,
        template_name="src/dashboard.html",
        context={
            "orders": orders,
            "customers": customers,
            "total_customers": total_customers,
            "total_orders": total_orders,
            "delivered": delivered,
            "pending": pending,
        },
    )


def customer(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    orders = customer.order_set.all()
    orders_count = orders.count()

    filters = OrderFilter(request.GET, queryset=orders)

    orders = filters.qs    

    return render(
        request=request,
        template_name="src/customer.html",
        context={
            "customer": customer,
            "orders": orders,
            "orders_count": orders_count,
            "filters": filters,
        },
    )


def product(request):
    products = Product.objects.all()
    return render(
        request=request,
        template_name="src/product.html",
        context={"products": products}
    )


def createOrder(request, customer_id):

    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=['product', 'status'], extra=10,
    )
    customer = Customer.objects.get(id=customer_id)

    # form_set ile Customer ile Order sınıflarını bir ele aldıktan sonra yukarıdaki elde ettiğimiz spesifik customer bilgilerini elde ederiz.
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    return render(
        request=request,
        template_name="src/order_form.html",
        context={'form': formset, 'customer_name': customer.name},
    )


def updateOrder(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')

    return render(
        request=request,
        template_name="src/order_form.html",
        context={'form': form},
    )


def deleteOrder(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    return render(
        request=request,
        template_name="src/delete.html",
        context={'order': order},
    )

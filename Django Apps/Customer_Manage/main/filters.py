import django_filters
# from django_filters import DateFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    # böylece dinamik arama yapabiliriz.
    # end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        # Böylelikle customer filtresini kaldırıyoruz. Zaten tek customer üzerinde arama yaptığımız için buna gerek duymuyoruz..
        exclude = ['customer']

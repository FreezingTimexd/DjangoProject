import django_filters
from django.db.models import Q
from django_filters import OrderingFilter

from .models import Product


class ProductFilter(django_filters.FilterSet):
    s = django_filters.CharFilter(method='my_custom_search', label="Search")

    o = OrderingFilter(
        fields=(
            ('price', 'price'),
        ),
        field_labels={
            'price': 'по возрастанию',
            '-price': 'по убыванию',
        }
    )

    o2 = OrderingFilter(
        fields=(
            ('name', 'name'),
        ),
        field_labels={
            'name': 'от А до Я',
            '-name': 'от Я до А',
        }
    )

    class Meta:
        model = Product
        fields = ['category', 'brand']

    def my_custom_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value) |
            Q(category__name__icontains=value) |
            Q(brand__name__icontains=value)
        )

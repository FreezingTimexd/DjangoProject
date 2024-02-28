from django.db.models import Q, CharField, Value
from django.db.models.functions import Concat
from django.views.generic import TemplateView
from django.views.generic.list import ListView

import orders.models
from .models import Customer, Order


class HomePageView(TemplateView):
    template_name = 'home.html'


class CustomersListView(ListView):
    template_name = "customers.html"
    model = Customer
    context_object_name = "list_of_all_customers"


class OrdersListView(ListView):
    template_name = "orders.html"
    model = orders.models.OrderItem
    queryset = model.objects.all()

    context_object_name = "list_of_all_orders"




class SearchView(ListView):
    template_name = "search.html"
    model = orders.models.OrderItem
    context_object_name = "list_of_all_orders"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return orders.models.OrderItem.objects.filter(
            Q(order__user__username__icontains=query)).order_by('price').reverse()


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from orders.models import Order
from orders.models import OrderItem

from .forms import UpdateUserForm, UpdateProfileForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'информация успешно обновлена')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    order_history = Order.objects.filter(user=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        "order_history": order_history,
    }

    return render(request, 'profile.html', context)


def order_history_items(request, id):
    order = Order.objects.get(id=id)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        "order_history_items": order_items,
        "order": order,
    }
    return render(request, 'profile_history_detail.html', context)


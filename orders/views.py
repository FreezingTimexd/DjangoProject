from django.shortcuts import render

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST,
                               initial={'city': request.user.profile.city,
                                        'address': request.user.profile.address})
        if form.is_valid():
            order = form.save(commit=False)
            if cart.promocode:
                order.promocode = cart.promocode
                order.discount = cart.promocode.discount
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            # запуск асинхронной задачи
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm(initial={'city': request.user.profile.city,
                                        'address': request.user.profile.address})
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})

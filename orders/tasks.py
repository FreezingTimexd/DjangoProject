from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order
from myShop import settings


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Уважаемый {order.user.first_name},' \
              f'Вы успешно сделали заказ в нашем магазине. ' \
              f'Номер вашего заказа {order.id}.'
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.user.email])
    return mail_sent
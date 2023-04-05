from threading import Thread

from django.core.mail import send_mail


def order_created(order):
    """Task to send an e-mail when an order is successfully created"""
    subject = f'Order N{order.id}'
    message = f'Dear {order.first_name}!' \
              f'You have successfully placed an order.' \
              f'Order`s number is {order.id}'
    Thread(target=send_mail, args=(subject, message, 'admin@myshop.com', [order.email])).start()

import json

from django.shortcuts import render
from apps.order.models import Order, ShippingAddress
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

import datetime


@login_required(login_url='loginUser')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': True}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


@login_required(login_url='loginUser')
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                country=data['shipping']['country'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zip=data['shipping']['zip'],

            )

    else:
        print('User is not logged in')
    return JsonResponse('Payment complete', safe=False)

from django.shortcuts import render, get_object_or_404

from .models import Product
from apps.order.models import Order


def productslist(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    products_new = Product.objects.filter(is_new=True)

    context = {
        'products': products,
        'products_new': products_new,
        'cartItems': cartItems
    }

    return render(request, 'productslist.html', context)


def productdetail(request, id):
    product = Product.objects.get(id=id)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': True}
        cartItems = order['get_cart_items']

    context = {
        'product': product, 'items': items, 'order': order, 'cartItems': cartItems
    }
    return render(request, 'productdetail.html', context)


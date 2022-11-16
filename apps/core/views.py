from django.shortcuts import render
from apps.store.models import Product
from apps.core.models import Contact


def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name, email, subject, message)
        ins = Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
        print('The data has been written to db')
    return render(request, 'contact.html')

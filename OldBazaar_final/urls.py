"""OldBazaar_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.core.views import contact, home
from apps.store.views import productslist, productdetail
from apps.cart.views import cart, update_item
from apps.order.views import checkout, processOrder
from apps.loginRegister.views import loginUser, myAccount, logoutUser, registerUser

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', productslist, name='productlist'),
    path('products/<int:id>/', productdetail, name='productdetail'),
    path('admin/', admin.site.urls),
    path('cart/', cart, name='cart'),
    path('update_item/', update_item, name='update_item'),
    path('checkout/', checkout, name='checkout'),
    path('processOrder/', processOrder, name='processOrder'),
    path('login/', loginUser, name='loginUser'),
    path('account/', myAccount, name='myAccount'),
    path('logout/', logoutUser, name='logoutUser'),
    path('register/', registerUser, name='registerUser')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""laundry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from address.views import customer_address_view
from pages.views import home_view, order_view, price_view
from rateboard.views import show_rate_board
from registration.views import customer_login_view, customer_logingin_view, customer_registration_view
from request.views import item_counting_view, request_view, request_completing_view, requesting_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('address/', customer_address_view, name = "customer_address"),
    path('admin/', admin.site.urls),
    path('customer_logingin/', customer_logingin_view, name = "customer_logingin"),
    path('customer_login/', customer_login_view, name = "customer_login"),
    path('customer_registration/', customer_registration_view, name = "customer_registration"),
    path('item_counting/<int:request_value>/', item_counting_view, name = "item_counting"),
    path('price/', show_rate_board, name = "price"),
    path('requesting/', requesting_view, name = "requesting"),
    path('request_completing/<int:request_value>/', request_completing_view, name = "request_completing"),
    path('request/', request_view, name = "request"),
    path('', home_view, name = "home"), 
]

urlpatterns += staticfiles_urlpatterns()

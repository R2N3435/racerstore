"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from .models import games

urlpatterns = [
    url(r'^games/$', views.shop, name='shop'),
    url(r'^mouse/$', views.mouses, name='mouses'),
    url(r'^games/(?P<games_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^mouse/(?P<mouse_id>[0-9]+)/$', views.detail_mouse, name='detail_mouse'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^add1/(\d+)',views.add_to_cart, name='add_to_cart'),
    url(r'^remove1/(\d+)',views.remove_from_cart, name='remove_from_cart'),
    url(r'^add2/(\d+)',views.add_to_cart_mouse, name='add_to_cart_mouse'),
    url(r'^remove2/(\d+)',views.remove_from_cart_mouse, name='remove_from_cart_mouse'),
    url(r'^search/$', views.search_titles, name='search'),
    url(r'^clear', views.clear, name='clear')
]

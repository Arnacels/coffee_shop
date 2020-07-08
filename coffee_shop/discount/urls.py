from django.conf.urls import url
from .views import CoffeeListView, BoughtCoffeeListView, CreateBoughtCoffeeView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^coffeelist/$', CoffeeListView.as_view(), name='coffee-list'),
    url(r'^bouthcoffeelist/$', BoughtCoffeeListView.as_view(), name='check-list'),
    url(r'^createbuy/$', CreateBoughtCoffeeView.as_view(), name='check-create')
]

urlpatterns = format_suffix_patterns(urlpatterns)
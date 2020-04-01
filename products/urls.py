# import our base url pattern
from django.conf.urls import url, include
# import all_machinery function to be used in our url pattern
from .views import all_products, search

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', search, name='search'),
]
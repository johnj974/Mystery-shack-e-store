# import our base url pattern
from django.conf.urls import url, include
# import all_machinery function to be used in our url pattern
from .views import all_products, createProduct, updateProduct

urlpatterns = [
    url('^$', all_products, name='products'),
    url("^create_product/$", createProduct, name='create_product'),
    url(r"^update_product/(?P<id>\d+)", updateProduct, name='update_product'),
]


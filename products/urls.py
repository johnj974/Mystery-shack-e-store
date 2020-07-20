# import our base url pattern
from django.conf.urls import url
# import all_machinery function to be used in our url pattern
from .views import all_products, createProduct, updateProduct, deleteProduct

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r"^create_product/$", createProduct, name='create_product'),
    url(r"^update_product/(?P<id>\d+)", updateProduct, name='update_product'),
    url(r"^delete_product/(?P<id>\d+)", deleteProduct, name='delete_product'),
]


# import our base url pattern
from django.conf.urls import url
# import all_machinery function to be used in our url pattern
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]
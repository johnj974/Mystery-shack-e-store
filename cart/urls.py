# import our base url pattern
from django.conf.urls import url, include
# import all_machinery function to be used in our url pattern
from .views import cart

urlpatterns = [
    url('^cart$', cart, name='cart')
]
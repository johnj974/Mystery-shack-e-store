# import our base url pattern
from django.conf.urls import url
# import all_machinery function to be used in our url pattern
from .views import rare_items

urlpatterns = [
    url(r'^$', rare_items, name='rare'),
]
# import our base url pattern
from django.conf.urls import url, include
# import all_machinery function to be used in our url pattern
from .views import search

urlpatterns = [
    url(r'^$', search, name='search'),
]
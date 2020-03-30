# import our base url pattern
from django.conf.urls import url, include
# import all_machinery function to be used in our url pattern
from .views import all_machinery, search

urlpatterns = [
    url('^$', all_machinery, name='machinery'),
    url(r'^$', search, name='search'),
]
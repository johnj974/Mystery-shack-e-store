# import our base url pattern
from django.conf.urls import url, include
# import all_machinery function to be used in our url pattern
from .views import all_machinery

urlpatterns = [
    url('^$', all_machinery, name='machinery')
]
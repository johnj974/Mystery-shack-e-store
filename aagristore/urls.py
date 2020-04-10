"""aagristore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# static files
from django.views import static
# imported functions from account app
from accounts.views import index
# imported urls from products app
from products import urls as urls_products
# import the media root from settings
from .settings import MEDIA_ROOT
# import cart functions
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from accounts import urls as urls_accounts
from search import urls as urls_search
from rare_items import urls as urls_rare


urlpatterns = [
    url(r'^admin/', admin.site.urls,),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^rare/', include(urls_rare)),
]

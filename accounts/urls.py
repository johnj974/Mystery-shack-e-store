from django.conf.urls import url, include
from .views import index, logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url("^$", index, name="index"),
    url("^logout/$", logout, name="logout"),
    url("^login/$", login, name="login"),
    url("^registration/$", registration, name="registration"),
    url("^user_profile/$", user_profile, name="user_profile"),
    url(r'^password-reset/', include(url_reset)),
]

   
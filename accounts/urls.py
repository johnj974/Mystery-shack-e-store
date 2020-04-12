from django.conf.urls import url, include
from .views import index, logout, login, registration, user_profile
from accounts import url_reset
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    url("^$", index, name="index"),
    url("^logout/$", logout, name="logout"),
    url("^login/$", login, name="login"),
    url("^registration/$", registration, name="registration"),
    url("^user_profile/$", user_profile, name="user_profile"),
    url(r'^password-reset/', include(url_reset)),
]

   
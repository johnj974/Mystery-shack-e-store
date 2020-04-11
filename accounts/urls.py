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
    url(r"^reset_password/$", password_reset, name= "reset_password"),
    url(r'^reset_password/done/$', password_reset_done, name= "password_reset_done"),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name= "password_reset_confirm"),
    url(r'^reset_password/complete/$', password_reset_complete, name= "password_reset_complete"),
]

    #url('^reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    #url('^reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #url('^reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #url('^reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
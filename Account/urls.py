from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", handleLogin, name="login"),
    path("signup/", handleSignup, name="signup"),
    path("logout/", handleLogout, name="logout"),
    path("token/", token, name="token"),
    path("verify/<auth_token>", verify, name="verify"),
    path("error/", error, name="error"),
    path("search/", search, name="search"),
    path("user", user, name="user"),
    path("profile/", profile, name="profile"),
    path("terms/", terms_and_conditions, name="terms"),
    path("edit_profile", edit_profile, name="edit_profile"),
    path("change_safe_mode", change_safe_mode, name="change_safe_mode"),
]

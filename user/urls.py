from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("profile/", views.UserProfile.as_view(), name="profile"),
    path("password/", views.UserPWChange.as_view(), name="password"),
]

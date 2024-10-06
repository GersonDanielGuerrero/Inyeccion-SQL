from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("user_info/", views.user_info, name="user_info"),
    path("productos/", views.products_view, name="productos"),
]

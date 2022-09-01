from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup", views.UserSignUpView.as_view(), name="signup"),
    path("user/<pk>/details", views.DetailView.as_view(), name="user-details"),
]
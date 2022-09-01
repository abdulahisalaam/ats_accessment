from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.detail import DetailView
from django.views.generic import ListView



from .models import CustomUser
from .forms import UserForm

# Create your views here.
class UserSignUpView(CreateView):
    form_class = UserForm
    template_name = "accounts/create_user.html"
    success_url = 'home'
    success_message = "Your Registration is Successful!!!"
    success_url = reverse_lazy('login')


class UserUpdate(UpdateView):
    form_class = UserForm
    template_name = "accounts/update_user.html"


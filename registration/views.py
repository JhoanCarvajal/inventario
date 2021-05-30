from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here.

class UserCreateView(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserForm
    success_url = reverse_lazy('login')
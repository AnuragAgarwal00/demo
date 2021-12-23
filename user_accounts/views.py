from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"


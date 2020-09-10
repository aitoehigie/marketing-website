from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy



class SignUpView(CreateView):
    model = CustomUser
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from accounts.models import User
from accounts.forms import SignUpForm

# Create your views here.

class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login_url")
    template_name = "accounts/signup.html"

    #def get_success_url(self):
    #    return reverse('login/')

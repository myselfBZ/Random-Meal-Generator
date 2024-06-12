from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def root(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('log-in')


@login_required
def log_out(request):
    logout(request)
    return redirect('log-in')    

class Home(generic.TemplateView):
    template_name = 'home.html'

class SignUp(generic.CreateView):
    template_name = 'sign-up.html'
    success_url = reverse_lazy('home')
    model = User
    form_class = UserCreationForm


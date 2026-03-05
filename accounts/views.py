from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = 'core:home'


@login_required
def account_view(request):
    """User account/profile page."""
    return render(request, 'account.html', {'user': request.user})

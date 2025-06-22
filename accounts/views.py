from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomLoginForm, CustomRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            print("✅ Login berhasil")
            login(request, form.get_user())
            return redirect('chat_view')
        else:
            print("❌ Login gagal:", form.errors)
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'your account creation has been successful')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def Logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('home')
    else:
        return redirect('dashboard')

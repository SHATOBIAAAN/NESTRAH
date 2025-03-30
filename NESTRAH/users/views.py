from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def profile(request):
    return render(request, 'users/profile.j2')

def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Автоматический вход после регистрации (если нужно)
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            
            return redirect('profile')


    else:
        form = UserCreationForm()
    
    return render(request, 'users/login.j2', {'form': form})

def register(request):
    return render(request, 'users/register.j2')

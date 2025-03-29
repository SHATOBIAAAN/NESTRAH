from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'users/profile.j2')

def login_view(request):
    return render(request, 'users/login.j2')

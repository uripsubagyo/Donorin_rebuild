from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('signin:login_user')
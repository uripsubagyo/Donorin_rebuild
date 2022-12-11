from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import FormSignUp


def register_user_view(request):
    form = UserCreationForm()
    context = {'form':form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('signin:login_users')
        else:
            messages.success(request, 'input anda salah, akun tidak dapat dibuat!')
            return()
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', context)

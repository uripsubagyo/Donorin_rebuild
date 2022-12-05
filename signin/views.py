from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login_user(request):
    users = request.user
    if request.user.is_authenticated:
        return redirect("information_user:information_user")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            information = InformationUser.objects.filter(user=user).count()
            if information == 0:
                return redirect('information_user:information_user')
            else:
                return redirect('information_user:information_user')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'signin.html', context)
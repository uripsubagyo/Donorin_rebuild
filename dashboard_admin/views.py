from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from information_user.models import InformationUser

# @login_required(login_url='login/')
def dashboard_admin(request):
    context = {}
    usersa = InformationUser.objects.filter(user=request.user, is_admin_user=True)

    if usersa != 0:
        return render(request, 'dashboard_admin.html', context)
    else:
        return redirect('dashboard:dashboard_relawan')

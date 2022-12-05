from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from information_user.models import InformationUser

# @login_required(login_url='login/')
def dashboard_admin(request):
    context = {}
    users = InformationUser.objects.filter(user = request.user)
    usersa = InformationUser.objects.filter(user=request.user, is_admin_user=True).count()
    usersr = InformationUser.objects.filter(user=request.user, is_admin_user=False).count()

    if users != 0:
        if usersa != 0:
            return render(request, 'dashboard_admin.html', context)
        else:
            return redirect('dashboard_user:dashboard_relawan')
    else:
        return redirect('information_user:information_user')

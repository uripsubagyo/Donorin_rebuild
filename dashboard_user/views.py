from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from information_user.models import InformationUser

@login_required(login_url='login/')
def dashboard_relawan(request):
        context = {}
        users = InformationUser.objects.filter(user = request.user).count()
        userA = InformationUser.objects.filter(user = request.user, is_admin_user=True).count()
        userR = InformationUser.objects.filter(user=request.user, is_admin_user=False).count()


        if users != 0:
            if(userA != 0):
                return redirect('dashboard_admin:dashboard_admin') 
            else:
                return render(request, 'dashboard_relawan.html', context)
        else:
            return redirect('information_user:information_user') 
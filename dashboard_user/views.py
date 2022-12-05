from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from information_user.models import InformationUser

# @login_required(login_url='login/')
def dashboard_relawan(request):
        context = {}
        userCount = InformationUser.objects.filter(user=request.user, is_admin_user=False).count()
        userInfomation = InformationUser.objects.filter(user = request.user)

        if userCount != 0:
            # Todo Condition user is admin handle:
            # ....
            return render(request, 'dashboard_relawan.html', context)
        else:
            return redirect('information_user:information_user') 
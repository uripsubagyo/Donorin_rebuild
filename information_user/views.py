from django.shortcuts import render

from multiprocessing import context
from multiprocessing.util import info
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InformationUser
from django.http import HttpResponse
import json


@login_required(login_url='login/')
def information_user(request):
    username_user = request.user.username

    # check user sudah pernah isi atau tidak:
    information_default = InformationUser.objects.filter(user = request.user).count()
    is_admin = InformationUser.objects.filter(user = request.user, is_admin_user = True).count()
    if request.method == "POST":
        print(request)
        full_name = request.POST.get("full_name")
        blood_group = request.POST.get('blood_group')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        province = request.POST.get('province')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        information = InformationUser(user = request.user, 
                    full_name = full_name, 
                    blood_group=blood_group, 
                    phone_number = phone_number, 
                    birth_date = birth_date, 
                    province = province, 
                    city = city, 
                    gender = gender,
                    is_admin_user = False,
                    )
        information.save()
        data = {}
        data['success'] = True
        return HttpResponse(json.dumps(data), content_type='application/json')

    context = {'username': username_user}

    if information_default == 0:
        return render(request, 'build_information_user.html', context)
    else:
        # direct dashboard information

        usersa = InformationUser.objects.filter(user=request.user, is_admin_user=False).count()
        if usersa !=0 & is_admin != 0:
            return redirect('dashboard_user:dashboard_relawan')
        else:
            return redirect('dashboard_user:dashboard_relawan')


@login_required(login_url='login/')
def information_admin(request):
    username_user = request.user.username

    # check user sudah pernah isi atau tidak:
    information_default = InformationUser.objects.filter(user = request.user).count()

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        blood_group = request.POST.get('blood_group')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        province = request.POST.get('province')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        information = InformationUser(user = request.user, 
                    full_name = full_name, 
                    blood_group=blood_group, 
                    phone_number = phone_number, 
                    birth_date = birth_date, 
                    province = province, 
                    city = city, 
                    gender = gender,
                    is_validate = True,
                    is_admin_user = True,
                    )
        information.save()

    context = {'username': username_user}
    #direct ke dashboard

    if information_default == 0:
        #kondosi belum isi
        render(request, 'build_information_admin.html', context)
    else:
        usersa = InformationUser.objects.filter(user=request.user, is_admin_user=True)
        if usersa != 0:
            return redirect('dashboard:dashboard_admin')
        else:
            return redirect('dashboard:dashboard_relawan')


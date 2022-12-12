from django.shortcuts import render

from multiprocessing import context
from multiprocessing.util import info
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InformationUser
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='login/')
def information_user(request):
    username_user = request.user.username

    # check user sudah pernah isi atau tidak:
    user_atp = InformationUser.objects.filter(user = request.user).count()
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

    if user_atp == 0:
        return render(request, 'build_information_user.html', context)
    else:
        is_admin = InformationUser.objects.filter(user = request.user, is_admin_user = True).count()
        if(is_admin != 0):
            return redirect('dashboard_admin:dashboard_admin')
        else:
            return redirect('dashboard_user:dashboard_relawan')


@login_required(login_url='login/')
def information_admin(request):
    username_user = request.user.username

    # check user sudah pernah isi atau tidak:
    useratp = InformationUser.objects.filter(user = request.user).count()
 
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

    if useratp == 0:
        #kondosi belum isi
        render(request, 'build_information_admin.html', context)
    else:
        is_admin = InformationUser.objects.filter(user = request.user, is_admin_user = True).count()
        if is_admin != 0:
            return redirect('dashboard_admin:dashboard_admin')
        else:
            return redirect('dashboard_user:dashboard_relawan')


@csrf_exempt
def information_user_flutter(request):
    print(request.method)
    if request.method == "POST":

        username = request.POST['username']
        full_name = request.POST['full_name']
        blood_group = request.POST['blood_group']
        phone_number = request.POST['phone_number']
        birth_date = request.POST['birth_date']
        province = request.POST['province']
        city = 'Jakarta'
        gender = 'Man'

        user = User.objects.get(username=username)

        info = InformationUser(
            user = user, 
            full_name = full_name, 
            blood_group=blood_group, 
            phone_number = phone_number, 
            birth_date = birth_date, 
            province = province, 
            city = city, 
            gender = gender,
            is_admin_user = False,
        )

        try:
            info.save()
        except Exception as e:
            print(e)
        # users_information.save()
        return JsonResponse({
                "status": True,
                "message": "Successfully Submit identity",
                }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)


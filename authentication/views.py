from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from information_user.models import InformationUser

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            user_atp = InformationUser.objects.filter(user = user).count()

            if(user_atp != 0):
                user_data = InformationUser.objects.filter(user = user)
                return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "data_field" : True,
                "data_user" : user_data
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
            else:
                return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "data_field" : False,
                "data_user" : []
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
                
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)
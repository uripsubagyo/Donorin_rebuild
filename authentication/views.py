from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from information_user.models import InformationUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            user_atp = InformationUser.objects.filter(user = user).count()
            user_id = User.objects.get(username=username).pk

            print(user_atp)
            if(user_atp != 0):
                return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "user_name" : username,
                "data_field" : True,
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
            else:
                return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!",
                "user_name" : username,
                "data_field" : False,
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

@csrf_exempt
def register_flutter(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse(
        {
            "status": True,
            "message": "Registration success!",
        }, status = 200)
    else:
        return JsonResponse(
        {
            "status": False,
            "message": "Registration failed!",
            "details": form.errors
        }, status = 400)

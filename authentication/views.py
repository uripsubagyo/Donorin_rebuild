# from django.shortcuts import render
# from django.contrib.auth import authenticate, login as auth_login
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from information_user.models import InformationUser

# @csrf_exempt
# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             auth_login(request, user)
#             # Redirect to a success page.
#             user_atp = InformationUser.objects.filter(user = user).count()

#             if(user_atp != 0):
#                 user_data = InformationUser.objects.filter(user = user)
#                 return JsonResponse({
#                 "status": True,
#                 "message": "Successfully Logged In!",
#                 "data_field" : True,
#                 "data_user" : user_data
#                 # Insert any extra data if you want to pass data to Flutter
#                 }, status=200)
#             else:
#                 return JsonResponse({
#                 "status": True,
#                 "message": "Successfully Logged In!",
#                 "data_field" : False,
#                 "data_user" : []
#                 # Insert any extra data if you want to pass data to Flutter
#                 }, status=200)

#         else:
#             return JsonResponse({
#             "status": False,
#             "message": "Failed to Login, Account Disabled."
#             }, status=401)

#     else:
#         return JsonResponse({
#         "status": False,
#         "message": "Failed to Login, check your email/password."
#         }, status=401)

# # @csrf_exempt
# # def signup_flutter(request):
# #     if request.method == 'POST':
# # 		data = json.loads(request.body)
# # 		email = data['email']
# # 		username = data['username']
# # 		password = data['password']
# # 		nama = data['nama']
# # 		jenis_kelamin = data['jenis_kelamin']
# # 		institusi = data['institusi']
# # 		kontak = data['kontak']
		
# # 		try:
# # 			new_user = User.objects.create_user(email, username, password)
# # 			new_user.nama = nama
# # 			new_user.jenis_kelamin = jenis_kelamin
# # 			new_user.institusi = institusi
# # 			new_user.kontak = kontak
# # 			new_user.save()
# # 			return JsonResponse({"instance": "user Dibuat"}, status=200)
# # 		except:
# # 			return JsonResponse({"instance": "gagal Dibuat"}, status=400)

# #     else:
# # 	    return JsonResponse({"instance": "gagal Dibuat"}, status=400)

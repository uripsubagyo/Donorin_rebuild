from django.urls import path
from .views import login_flutter, register_flutter
from information_user.views import information_user_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login_flutter, name='login_flutter'),
    path('register/', register_flutter, name='register_flutter'),
    path('information-user/', information_user_flutter, name='information_user_flutter'),
]
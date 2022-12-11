from django.urls import path
from .views import login_flutter, register_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login_flutter, name='login_flutter'),
    path('register/', register_flutter, name='register_flutter'),
]
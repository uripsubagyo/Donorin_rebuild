
from django.urls import path

from .views import information_user

app_name = 'information_user'


urlpatterns  = [
        path('', information_user, name='information_user'),
        ]

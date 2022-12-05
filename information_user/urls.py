
from django.urls import path

from .views import information_user, information_admin

app_name = 'information_user'


urlpatterns  = [
        path('', information_user, name='information_user'),
        path('admin', information_admin, name='information_admin'),
        ]

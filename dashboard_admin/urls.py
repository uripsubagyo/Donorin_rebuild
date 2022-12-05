
from django.urls import path

from .views import dashboard_admin

app_name = 'dashboard_admin'


urlpatterns  = [
        path('', dashboard_admin, name='dashboard_admin'),
]